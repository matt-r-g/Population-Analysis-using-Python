# 🐍 Global Population Analysis – Python (Pandas & Matplotlib)

This project was completed as part of a **technical case study for a Data Analyst role at GlobalTech**.  
The objective was to analyse global population data using **Python, Pandas, and Matplotlib** to answer business-focused questions and present clear analytical outputs.

The project demonstrates:
- Data cleaning and filtering with Pandas  
- Aggregations and statistical analysis  
- Data visualisation with Matplotlib  
- Communicating insights in a structured, stakeholder-friendly format  

---

# 🎯 Scenario

As a Data Analyst applicant at **GlobalTech**, I was provided with population statistics and asked to:

- Manipulate and analyse the data using **Pandas**  
- Create visualisations using **Matplotlib** where appropriate  
- Present findings as clear analytical deliverables  

---

# 🧰 Tools & Libraries Used
- 🐍 Python  
- 🐼 Pandas  
- 📊 Matplotlib  
- Jupyter Notebook  

---

# ❓ Analysis Questions & Deliverables

---

## 1️⃣ How many countries had a recorded population of zero for the year 2000?

📸 **Output:**  

<img width="808" height="490" alt="Screenshot 2026-02-14 211606" src="https://github.com/user-attachments/assets/ee09fa5b-c02c-4cec-8957-f80eefdc5ac4" />


📝 **Result:**  
The answer to this question was 59 and above is a screenshot of part of the list of countries that were output from the python code, it could be beneficial going forward to remove these countries during analysis as they may make results inaccurate. If we do not include these values we can come up with better insights especially for visualisations. 

---

## 2️⃣ Total Population of Africa in 2010

📸 **Output:**  

<img width="1294" height="673" alt="Screenshot 2026-02-14 211649" src="https://github.com/user-attachments/assets/3b0cd0a0-717c-4da4-a781-df2cfc3ac003" />

📝 **Result:**  
My original graph had the results sorted from A-Z by default for country name, I felt that there was a better way to display this so I sorted it by Population from highest to lowest. This way we can easily see that Nigeria is the highest populated country by at least 60 million people. We can also see that there are countries that are not populated in 2010 such as Seychelles for example. Upon further analysis these countries are not populated throughout the years and may need to be removed from the graph to provide better insights going forward. 



---

## 3️⃣ Average Population of South America in 2000

📸 **Output:**  

<img width="598" height="539" alt="Screenshot 2026-02-14 211732" src="https://github.com/user-attachments/assets/c2160fde-9cb0-42b9-aecd-bb70782668ac" />

📝 **Result:**  

The average was 24.5 The countries BELOW and ABOVE average are listed in the screenshot. Some contain an average of 0.0 and may need to be updated/removed from the results. Below is an updated result set, so that the 0.0 is removed and it is not so misleading in terms of population averages. 

<img width="894" height="643" alt="Screenshot 2026-02-14 211746" src="https://github.com/user-attachments/assets/a1e6ad66-db58-4b3a-aa95-7d86502bac43" />



---

## 4️⃣ Countries with Population > 1000 Million in 2007

📸 **Output:**  
I felt there is a much better way to show this data, by limiting it to the top 20 countries, it still shows the threshold along with the top countries. This way its much more readable and clearer to see, this is a better way to display the data in my opinion as you can actually read the graph and understand what it is showing. The updated graph is shown below. I used ascending and head 20 to gather the top 20 countries 

📝 **Result:**  

<img width="1173" height="639" alt="Screenshot 2026-02-14 211812" src="https://github.com/user-attachments/assets/4872cc25-601f-443c-8bb1-d58a06b75d7a" />



---

## 5️⃣ Population Growth in Europe (2000–2010)

📸 **Output:**  
Upon looking into the dataset more closely, I found there are many other countries that have higher population than Ireland, however this is a graph showing the Growth rather that the sum. Leading the way are Italy, UK and France for highest population growth from 2000-2010. 

📝 **Results:**  

<img width="1091" height="625" alt="Screenshot 2026-02-14 211840" src="https://github.com/user-attachments/assets/a5b726bd-8fb7-40ae-a97b-9f35c9abd418" />


---

# 📊 Key Insights

- Zero population values may indicate **missing or incomplete data** rather than true population counts  
- Africa shows **significant population concentration** in a small number of countries  
- South America has a **clear population imbalance**, with a few countries above the continental average  
- Only a small number of countries exceed **1 billion population**, highlighting global demographic concentration  
- European population growth is **uneven**, driven by a subset of countries  

---
# 📌 Limitations and Assumptions

- Many countries show population as 0 for some years. These likely represent missing data, not actual population values. ✅ 
- The dataset covers 2000–2010, so there is no data before 2000 or after 2010. 📅
- While trends within this period can be analysed, long-term trends and their impacts are missing.
(Example: A country might begin declining in population around 2009–2010, but we cannot see what happens afterward without additional data)
- The dataset does not include COVID-19 impacts, which occurred after 2010. 🦠 (This limits our ability to see recent demographic changes)

---
# 🔍 Suggestions for Further Exploration

- Compare regions by continent 🌍, not just individual countries.
- Analyze population growth trends beyond Europe, including factors like:
- Life expectancy 🏥
- Migration rates ✈️
- Countries with highest or lowest growth 📈📉

If patterns emerge, action should be considered:
- Lowest growth may indicate high emigration, low birth rates, or poor healthcare.
- Highest growth may result in resource shortages, high housing demands, and environmental impacts. 🏘️🌱

---

# 💡 Recommendations

- Treat zero values as **data quality flags** and validate before analysis  
- Focus policy and trade strategy on **high-population countries** within each continent  
- Monitor **regional growth leaders** to anticipate future economic influence  
- Use **visual analytics** to communicate demographic shifts to non-technical stakeholders  

---

# 🧠 Skills Demonstrated

- Data cleaning and filtering in Pandas  
- GroupBy aggregations and statistical calculations  
- Data visualisation with Matplotlib  
- Identifying and handling data quality issues  
- Translating analysis into business insights  

---


---
