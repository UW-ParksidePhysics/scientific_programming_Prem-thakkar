n_years = 3
p_interest_nom3yr = 3.55 #Febuary 11th 2026
initial_investment = 1000 #A

future_value = initial_investment*(1+(p_interest_nom3yr/100))**n_years
gain = future_value - initial_investment

print(f'Initial Investment: ${initial_investment:.2f}')
print(f'Interest rate Nominal 3 years: {p_interest_nom3yr:.2f}%')
print(f'Future Value = ${future_value:.2f}')
print(f'Gain: ${future_value:.2f} - ${initial_investment:.2f} = ${gain:.2f}')