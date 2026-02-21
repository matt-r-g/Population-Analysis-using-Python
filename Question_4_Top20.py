#import modules
import pandas as pd
import matplotlib.pyplot as plt
#Loading the dataset
#copy file path from folder directory
df = pd.read_csv("Enter path to data file: ")
print(df.head())
#4.	Identify the countries with populations exceeding 1000 million in
#  2007. Create a bar chart or scatter plot to display all countries'
#  populations in 2007, marking those above 1000.

# Filter for year 2007
pop_2007 = df[df['year'] == 2007]
# Sort countries by population (ascending for better view)
pop_2007_sorted = pop_2007.sort_values(by='population', ascending=True)
# Colors: red if >1000 million, blue otherwise
colors = ['red' if pop > 1000 else 'blue' for 
          pop in pop_2007_sorted['population']]
# Plotling the graph with bin sizes
plt.figure(figsize=(18, 8))
plt.bar(pop_2007_sorted['country name'], 
        pop_2007_sorted['population'], color=colors)
# Adding a threshold line for 1000 with black colour for readability
plt.axhline(1000, color='black', linestyle='--',
             label='1000 million threshold')

#Adding the titles and labels to the graph
plt.title('Population of All Countries in 2007 (Bar Chart)')
plt.xlabel('Country')
plt.ylabel('Population (millions)')
plt.xticks(rotation=90)

#Printing the graph
plt.legend()
plt.show()

#answer was China and India, the graph for other countries
#will be shown in word doc, with explanations


#The output it way too crowded for readability, so I decided to limit  
#results to top 20 that way its still showing meaningful data
#and is also readable and not crowded

#Filter year 2007, sort descending, take top 20
top20 = df[df['year'] == 2007].sort_values(by='population', 
                                           ascending=False).head(20)

#Create colors for above/below 1000 million
colors = ['red' if pop > 1000 else 'blue' for pop in 
          top20['population']]

#Plot bar chart
plt.figure(figsize=(14, 7))
plt.bar(top20['country name'], top20['population'], color=colors)

#Add threshold line at 1000
plt.axhline(1000, color='black', linestyle='--', 
            label='1000 million threshold')

plt.title('Top 20 Countries by Population in 2007')
plt.xlabel('Country')
plt.ylabel('Population (millions)')
plt.xticks(rotation=45)
plt.legend()
plt.show()


print(top20[['country name', 'population']])

