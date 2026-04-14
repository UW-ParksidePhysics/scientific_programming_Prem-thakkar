"""
Seasonal Solar Generation at UW-Parkside: Including Cloud Cover and Soiling Effects

This script is designed to match the content of the presentation slide:
- It defines the four required functions:
  load_clean_data()
  cloud_adjusted_irradiance()
  soiling_factor()
  plot_comparision()
- It includes the two presentation graphs exactly from the slide data.
- It also computes a simple solar-power model using irradiance, cloud cover,
  temperature, and soiling loss.

The code is import-safe and only runs when executed directly.

Model idea used here:
    P = A * eta(T) * I_effective
where
    I_effective = I * (1 - cloud_cover) * soiling_factor(days_since_rain)

Units:
- irradiance in W/m^2
- temperature in deg C
- energy/output in relative units for plotting demonstration
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def load_clean_data(csv_path: Optional[str] = None) -> pd.DataFrame:
    """
    Load and clean solar/weather data.

    If csv_path is provided and the file exists, the function reads that file.
    Otherwise, it creates a built-in demonstration dataset that is guaranteed
    to run and is consistent with the presentation topic.

    Expected columns:
    - day_of_year
    - solar_irradiance
    - high_temperature
    - cloud_cover_fraction
    - rainfall_mm

    Returns
    -------
    pandas.DataFrame
        Cleaned dataframe with the required columns.
    """
    required_columns = [
        "day_of_year",
        "solar_irradiance",
        "high_temperature",
        "cloud_cover_fraction",
        "rainfall_mm",
    ]

    if csv_path is not None and Path(csv_path).exists():
        data = pd.read_csv(csv_path)
        missing = [col for col in required_columns if col not in data.columns]
        if missing:
            raise ValueError(
                f"CSV file is missing required columns: {missing}. "
                f"Required columns are: {required_columns}"
            )
    else:
        # Built-in sample data so the code definitely runs even without an external file.
        day_of_year = np.arange(1, 366)

        # Seasonal irradiance trend for Kenosha-style yearly behavior
        solar_irradiance = 550 + 350 * np.sin(2 * np.pi * (day_of_year - 80) / 365)
        solar_irradiance = np.clip(solar_irradiance, 120, 1000)

        # Seasonal temperature trend in deg C
        high_temperature = 10 + 20 * np.sin(2 * np.pi * (day_of_year - 172) / 365)

        # Cloud cover fraction bounded between 0 and 1
        cloud_cover_fraction = 0.45 + 0.25 * np.sin(2 * np.pi * (day_of_year + 30) / 365)
        cloud_cover_fraction = np.clip(cloud_cover_fraction, 0.0, 1.0)

        # Simple rainfall pattern used to reset dust/soiling
        rainfall_mm = np.where((day_of_year % 17) == 0, 6.0, 0.0)

        data = pd.DataFrame(
            {
                "day_of_year": day_of_year,
                "solar_irradiance": solar_irradiance,
                "high_temperature": high_temperature,
                "cloud_cover_fraction": cloud_cover_fraction,
                "rainfall_mm": rainfall_mm,
            }
        )

    data = data.copy()

    # Numeric conversion + cleaning
    for column in required_columns:
        data[column] = pd.to_numeric(data[column], errors="coerce")

    data = data.dropna(subset=required_columns)

    data["day_of_year"] = data["day_of_year"].clip(1, 365).astype(int)
    data["solar_irradiance"] = data["solar_irradiance"].clip(0, 1000)
    data["high_temperature"] = data["high_temperature"].clip(-20, 40)
    data["cloud_cover_fraction"] = data["cloud_cover_fraction"].clip(0, 1)
    data["rainfall_mm"] = data["rainfall_mm"].clip(lower=0)

    return data.reset_index(drop=True)


def cloud_adjusted_irradiance(
    solar_irradiance: np.ndarray | pd.Series,
    cloud_cover_fraction: np.ndarray | pd.Series,
    cloud_loss_strength: float = 0.85,
) -> np.ndarray:
    """
    Reduce irradiance according to cloud cover.

    Parameters
    ----------
    solar_irradiance : array-like
        Incoming irradiance in W/m^2.
    cloud_cover_fraction : array-like
        Cloud fraction from 0 to 1.
    cloud_loss_strength : float
        Fractional strength of cloud reduction. A value of 0.85 means
        full cloud cover can reduce irradiance by 85%.

    Returns
    -------
    numpy.ndarray
        Cloud-adjusted irradiance in W/m^2.
    """
    solar_irradiance = np.asarray(solar_irradiance, dtype=float)
    cloud_cover_fraction = np.asarray(cloud_cover_fraction, dtype=float)
    return solar_irradiance * (1.0 - cloud_loss_strength * cloud_cover_fraction)


def soiling_factor(days_since_rain: np.ndarray | pd.Series, max_loss: float = 0.10) -> np.ndarray:
    """
    Compute a multiplicative soiling factor.

    A clean panel starts near 1.0. As dust accumulates, the factor gradually
    decreases. Rain resets the dust accumulation.

    Parameters
    ----------
    days_since_rain : array-like
        Number of days since the last rain event.
    max_loss : float
        Maximum fractional loss due to soiling.

    Returns
    -------
    numpy.ndarray
        Factor between (1 - max_loss) and 1.
    """
    days_since_rain = np.asarray(days_since_rain, dtype=float)
    return 1.0 - max_loss * (1.0 - np.exp(-days_since_rain / 14.0))


def compute_days_since_rain(rainfall_mm: np.ndarray | pd.Series) -> np.ndarray:
    """
    Compute days since last rain from a rainfall time series.

    Any rainfall > 0 mm is treated as a cleaning event.
    """
    rainfall_mm = np.asarray(rainfall_mm, dtype=float)
    result = np.zeros_like(rainfall_mm, dtype=float)

    days = 0.0
    for index, rain in enumerate(rainfall_mm):
        if rain > 0:
            days = 0.0
        else:
            if index != 0:
                days += 1.0
        result[index] = days

    return result


def temperature_efficiency_factor(
    high_temperature: np.ndarray | pd.Series,
    reference_temperature: float = 25.0,
    temperature_coefficient: float = 0.004,
) -> np.ndarray:
    """
    Compute a simple PV efficiency correction due to temperature.

    Efficiency decreases as temperature rises above the reference temperature.
    """
    high_temperature = np.asarray(high_temperature, dtype=float)
    factor = 1.0 - temperature_coefficient * (high_temperature - reference_temperature)
    return np.clip(factor, 0.75, 1.08)


def simulate_solar_output(
    data: pd.DataFrame,
    panel_area_m2: float = 1.0,
    reference_efficiency: float = 0.20,
) -> pd.DataFrame:
    """
    Create model outputs for seasonal solar generation.

    Returns a copy of the dataframe with added columns:
    - days_since_rain
    - cloud_adjusted_irradiance
    - soiling_factor
    - temperature_factor
    - modeled_power_watts
    """
    result = data.copy()

    result["days_since_rain"] = compute_days_since_rain(result["rainfall_mm"])
    result["cloud_adjusted_irradiance"] = cloud_adjusted_irradiance(
        result["solar_irradiance"],
        result["cloud_cover_fraction"],
    )
    result["soiling_factor"] = soiling_factor(result["days_since_rain"])
    result["temperature_factor"] = temperature_efficiency_factor(result["high_temperature"])

    # Derivation used in code:
    # P = A * eta(T) * I_effective * soiling_factor
    # where I_effective = cloud_adjusted_irradiance
    result["modeled_power_watts"] = (
        panel_area_m2
        * reference_efficiency
        * result["temperature_factor"]
        * result["cloud_adjusted_irradiance"]
        * result["soiling_factor"]
    )

    return result


def plot_comparision(data: Optional[pd.DataFrame] = None) -> None:
    """
    Plot both graphs required by the presentation.

    Graph 1 from the PPT:
    cloud cover fraction vs solar irradiance
        x = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
        y = [1000, 950, 820, 600, 350, 150]
    (A leading zero point is kept as in the slide data.)

    Graph 2 from the PPT:
    high temperature vs output
        x = [0, 5, 10, 15, 20, 25, 30]
        y = [50, 49, 48, 47, 46, 45, 44]
    """
    # --- Exact graph data from the PowerPoint slide ---
    ppt_cloud_fraction = np.array([0.0, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0], dtype=float)
    ppt_irradiance = np.array([0.0, 1000.0, 950.0, 820.0, 600.0, 350.0, 150.0], dtype=float)

    ppt_temperature = np.array([0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0], dtype=float)
    ppt_output = np.array([50.0, 49.0, 48.0, 47.0, 46.0, 45.0, 44.0], dtype=float)

    # Graph 1
    plt.figure(figsize=(8, 5))
    plt.plot(ppt_cloud_fraction, ppt_irradiance, marker="o")
    plt.title("Cloud Cover Fraction vs Solar Irradiance")
    plt.xlabel("Cloud Cover Fraction")
    plt.ylabel("Solar Irradiance (W/m^2)")
    plt.xlim(0, 1)
    plt.ylim(0, 1050)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    # Graph 2
    plt.figure(figsize=(8, 5))
    plt.plot(ppt_temperature, ppt_output, marker="o")
    plt.title("High Temperature vs Output")
    plt.xlabel("High Temperature (°C)")
    plt.ylabel("Output")
    plt.xlim(0, 30)
    plt.ylim(43.5, 50.5)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    # Optional extra comparison figure using the model
    if data is not None:
        modeled = simulate_solar_output(data)

        plt.figure(figsize=(10, 5))
        plt.plot(modeled["day_of_year"], modeled["modeled_power_watts"], label="Modeled Power")
        plt.plot(
            modeled["day_of_year"],
            modeled["cloud_adjusted_irradiance"] * 0.18,
            label="Cloud-Adjusted Irradiance (scaled)",
        )
        plt.title("Seasonal Solar Generation at UW-Parkside")
        plt.xlabel("Day of Year")
        plt.ylabel("Relative Output / Power")
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()

    plt.show()


def print_derivation_summary() -> None:
    """
    Print a clean derivation summary for presentation use.
    """
    print("Derivation used in the model:")
    print("P = A * eta(T) * I_effective * S")
    print("I_effective = I * (1 - k * cloud_cover_fraction)")
    print("S = soiling_factor(days_since_rain)")
    print()
    print("Where:")
    print("P  = modeled solar power")
    print("A  = panel area")
    print("eta(T) = temperature-dependent efficiency")
    print("I  = solar irradiance")
    print("k  = cloud loss strength")
    print("S  = soiling multiplier")


def main() -> None:
    """
    Run the full solar-generation demonstration.
    """
    data = load_clean_data()
    modeled = simulate_solar_output(data)

    print("First 10 cleaned/model rows:")
    print(modeled.head(10).to_string(index=False))
    print()
    print_derivation_summary()

    plot_comparision(data)


if __name__ == "__main__":
    main()

