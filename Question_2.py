import pandas as pd
import matplotlib.pyplot as plt

#Loading the dataset
#copy file path from folder directory
df = pd.read_csv("Enter path to data file: ")
print(df.head())

#2.	Calculate the total population for all African countries in 2010.
# Create a bar chart showing the population distribution across African
# countries in 2010.

africa_2010 = df[
    (df['continent'] == 'Africa') &
    (df['year'] == 2010)
]
#remove countries with 0 population
africa_2010 = africa_2010[africa_2010['population'] > 0]
#sorting values from highest to lowest for the chart
africa_2010 = africa_2010.sort_values(by='population', ascending=False)
#using sum to add total populations
total_population_africa_2010 = africa_2010['population'].sum()
print("Total population of African countries in 2010:", 
      total_population_africa_2010)
#Plotting the bar chart with the country x population
plt.bar(
    africa_2010['country name'],
    africa_2010['population']
)
#Bar chart title
plt.title('Population Distribution Across African Countries (2010)')
#X Axis title
plt.xlabel('Country')
#Y Axis title
plt.ylabel('Population')
#Rotate country names so they all fit, as there are many in the chart
#helping readability
#could also use barh for horizontal bar chart to fit in countries
plt.xticks(rotation=90)
#adjust bin size for readability
plt.tight_layout()
plt.show()


#answer shown in a chart in word with Nigeria being the highest pop