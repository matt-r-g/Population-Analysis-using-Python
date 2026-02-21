#import modules
import pandas as pd
import matplotlib.pyplot as plt

#Loading the dataset
#copy file path from folder directory
df = pd.read_csv("Enter path to data file: ")
print(df.head())

#5.	Calculate the total population growth in Europe between 2000 and
# 2010. Identify the top 5 European countries by population growth 
# during this period and create a line plot showing the population
#  changes of these countries from 2000 to 2010.

#Filter the data for Europe only
europe = df[df['continent'] == 'Europe']
#Create a pivot table for countries
pivot = europe.pivot_table(
    index='country name',
    columns='year',
    values='population'
)

#Calculate total population growth in Europe (2010 - 2000)
total_growth = pivot[2010].sum() - pivot[2000].sum()
#Show the result of calculation
print("Total population growth in Europe (2000-2010):", total_growth)

#Calculate growth for each country
pivot['growth'] = pivot[2010] - pivot[2000]

#Identify and display the top 5 countries by population growth
top5 = pivot.sort_values(by='growth', ascending=False).head(5)

print("\nTop 5 European countries by population growth (2000-2010):")
print(top5['growth'])

#Get the list of top 5 countries
top5_countries = top5.index.tolist()

#Filter the original Europe data for these top 5 countries 
#and years 2000-2010
top5_data = europe[
    (europe['country name'].isin(top5_countries)) &
    (europe['year'].between(2000, 2010))
]

#Plot line chart showing population changes from 2000 to 2010
plt.figure(figsize=(12, 6))

for country in top5_countries:
    # Filter data for each country
    country_data = top5_data[top5_data['country name'] == country]
    
    # Plot line for each country
    plt.plot(
        country_data['year'],
        country_data['population'],
        marker='o',
        label=country
    )
#Adding titles and lables to the graph
plt.title('Top 5 European Countries by Population Growth (2000-2010)')
plt.xlabel('Year')
plt.ylabel('Population')
plt.legend()
plt.show()

#answer shown as a line graph/chart in word 