import pandas as pd
import matplotlib.pyplot as plt
#Loading the dataset
#copy file path from folder directory
df = pd.read_csv("Enter path to data file: ")
print(df.head())
#3.	Determine the average population of countries in South America 
# for the year 2000. Highlight countries with populations above 
# and below this average. Include the lists in your analysis.

#Filtering for countries in SA for the year 2000
south_america_2000 = df[(df['continent'] == 'South America') 
                        & (df['year'] == 2000)]
# Remove countries with population = 0 (missing data)
south_america_2000 = south_america_2000[south_america_2000
                                        ['population'] > 0]
#Finding the average for those countries 
average_pop = south_america_2000['population'].mean()
print("Average population (South America, 2000):", average_pop)
#Using more than and less than to filter again compared to the average
above_avg = south_america_2000[south_america_2000['population'] 
                               > average_pop]
below_avg = south_america_2000[south_america_2000['population'] 
                               <= average_pop]

#Showing the countries above the average, name and population
print("Countries ABOVE average:")
print(above_avg[['country name', 'population']])
#Showing the countries below the average, name and population
print("Countries BELOW average:")
print(below_avg[['country name', 'population']])

#average result was 24.5 and the blow and above will be shown in word