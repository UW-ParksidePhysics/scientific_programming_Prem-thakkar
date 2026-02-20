Q_life_expectancy_baby_seconds = 10**9 # seconds
Seconds_in_one_yr = 1/31536000 
Q_life_expectancy_baby_years = Q_life_expectancy_baby_seconds*Seconds_in_one_yr 

print(f'Question: Can a new born baby in the United States live up to {Q_life_expectancy_baby_seconds} seconds?')
print(f'Converting {Q_life_expectancy_baby_seconds} seconds to years is {Q_life_expectancy_baby_years} years')
CDClife_expectancy_baby_years = 78.4     # years

print(f'{Q_life_expectancy_baby_years} years is < than Center for Disease control:{CDClife_expectancy_baby_years} years, so a baby can live for such time.')