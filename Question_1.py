#import modules
import pandas as pd
import matplotlib.pyplot as plt

#Loading the dataset
#copy file path from folder directory
df = pd.read_csv("Enter path to data file: ")
print(df.head())

#1.	How many countries had no recorded population data (0)
# for the year 2000? List these countries along with their continent

# Filter rows where year is 2000 and population is 0
no_pop_2000 = df[(df['year'] == 2000) & (df['population'] == 0)]

# Select unique countries with their continent
countries_no_pop_2000 = no_pop_2000[['country name', 'continent']].drop_duplicates()

# Count how many such countries
num_countries = countries_no_pop_2000.shape[0]

print("Number of countries with population = 0 in 2000:", num_countries)
print("List of countries and their continents:")
print(countries_no_pop_2000)

