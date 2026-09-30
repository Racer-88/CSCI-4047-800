import pandas as pd
import scipy.stats as stats

# Load the contingency table from the CSV file
df = pd.read_csv('overwatch_contingency_table.csv')

print(df.head())
wait = input('')

# Pivot the data to create a contingency table
contingency_table = df.pivot(index='Role', columns='Favorite_Hero', values='Observed')
print(contingency_table)
wait = input('')

# Perform Chi-square test
chi2, p, dof, expected = stats.chi2_contingency(contingency_table)

# Display results
print(f"Chi-square statistic: {chi2}")
print(f"p-value: {p}")
print(f"Degrees of freedom: {dof}")

# may be used -- meh
print("Expected frequencies:")
print(expected)
