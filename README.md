# The Impact of Income Inequality - The class project of MGT 4250 Fall 2023 at Elon University


## Section 1: Project Description
- Link to Streamlit app: https://mgt4250project-jjluskeraqz6dotpy4h225.streamlit.app/
### Project Questions
- Q1: What are the key drivers for income inequality?
- Q2: How does race affect the median income of everyday people?
- Q3: What is the impact of Education on income levels? 


### Importance of our Questions
- Income Inequality has a significant societal and economic impact, and it is important that we understand the factors that lead to inequality for greater economic development.
- When comparing median incomes, it is important to factor in race as the data could highlight challenges that certain racial groups go through.
- This data could provide insight into the role of education, and show the importance of equal opportunity. 



## Section 2: Data Description & Upload 
To find and download publicly available datasets for our project, we looked for sources regarding median income by a variety of characteristics inculding race, gender, and education. We were able to find an abundance of datasets on census.gov that met our needs but in order to visualize the data we had to re-organize them into a more user friendly format as there were several cells containing text as opposed to numbers. To do this, we selected a certain characteristic and the data that represented it, and moved it into a seperate spreadsheet. For example, in the uploaded files of this repository there are 4 excel spreadsheets containing the data found on census.gov regarding median income and race. Each spreadsheet contains data about a different race in order to make vizualizing the data on python simple and fluid. 

To download the datasets we used and explored, click the census.gov link below, scroll down to the "Tables" section, and downlaod the desired spreadsheet. The data used for our visualizations can be found in the dataset labeled "A-2" under the "Tables" section. This spreadsheet containes data about a variety of races that we had to split up into their own spreadsheet in order to compare against one another.

Another source of our data was from statista.com, where we found data regarding median income in USD by level of education. This spreadsheet only contained the processed means of the original dataset so it did not need much processing. That being said, we had to clean up the spreadsheet and format it in a python analysis/visualization friendly way. It can be found on the right under "Download" at the top of the page, the link can be found below. The data types in the original spreadsheet did not need to be modified as all numbers were pre-processed into their means and the only other column was the name/title of the level of education. If we had the original data before the means were calculated, we could have used label encoding or OneHotEncoding to encode the level of education and produce a machine learning model to deepen our understanding of the data through statistics and visualizations. 


## Section 3 – Interpreting Visualizations
### Race
<img width="967" alt="Screenshot 2023-12-06 at 18 57 25" src="https://github.com/proedl10/mgt4250project/assets/152214737/c0d1b696-2417-4dac-a04d-f1e055383a46">

Interpretation:
- The graph above show the median income between two races in the United States between 1972 and 2001. This data is just a brief part of the data sets we have collected and used in creating visuals and developing an understanding of our topics. 

### Education
<img width="1432" alt="Screenshot 2023-12-06 at 19 02 45" src="https://github.com/proedl10/mgt4250project/assets/152214737/96e8ec85-03a2-472e-b414-d5ab92960698">

Interpretation:
- This Visualization help us understand the relationship between income and education levels, showing that education has a great effect on income. As you can see, there is a linear relationship between income and level of education with the two highest earning levels of education being Doctorate and Professional Degree. The minimum mean income is $33,830(less than 9th grade) while the highest(professional degree) has a mean of $157,800, the difference between the two being $123,970.


## Section 4 – Discussion & Summary
### Summary of Related Article and Link
- Link to article: https://www.investopedia.com/terms/i/income-inequality.asp#:~:text=Income%20inequality%20refers%20to%20how,the%20greater%20the%20income%20inequality. 
- The Article that we chose is called "Income Inequality Definition: Examples and how its Measured", written by Carol M. Kopp, from the website investopedia.com. The article talks about what income inequality means, how it can lead to uneven distribution of wealth, and unfair opportunity for better standards of living and sucess in general. Netx, the article explains the causes of Income Inequality, where it mentions globalization, advances in technology, gender and race bias, education, economic conditions, and taxation. The article realizes that income inequality is an issue, explaining that it can promote potentially destructive social and economic upheaval, amongst many other dangers. Large imbalances in income have been caused and maintained by these factors, and it is important that the world adresses this problem. 


### Chat GPT-4 Responses
- Using our Professors API key, we were able to ask Chat GPT-4 our questions, and these were its responses.
<img width="1005" alt="Screenshot 2023-12-06 at 6 58 07 PM" src="https://github.com/proedl10/mgt4250project/assets/152214864/563bda84-cee6-4ab6-aad4-c224a0c1fcb3">

- When we asked Chat GPT-4 the second question, this was its reponse.
<img width="1000" alt="Screenshot 2023-12-06 at 7 14 21 PM" src="https://github.com/proedl10/mgt4250project/assets/152214864/bbe7c430-3c66-4945-9fb1-8b051b0e69f2">

- When we asked Chat GPT-4 the third question, this was its reponse.
<img width="994" alt="Screenshot 2023-12-06 at 7 16 28 PM" src="https://github.com/proedl10/mgt4250project/assets/152214864/a0a6a8e7-2e0f-4b8a-a267-e6e0872330bd">


### Our Visualizations compared to Article Summary and Chat GPT-4 Response
- Our idea that education and race were factors of Income Inequality was proven right from data recorded from Chat GPT-4 and the found article. The article mentioned that education and race were two of the main reasons for income inequality, as well as Chat GPT-4. Our first visualization, where the graph compares median income by race, backs up the argument that race is a main reason for income inequality because according to the data, black people have a lower income than white people. Our second visualization, where the graph compares median income by education, also supports the argument that education is a main reason for income inequality because the data shows that having a high level of education results in a higher income. While Chat GPT-4 as well as the article had other important information, the knowledge it shared about the effect of income inequality on education and race proved our visualizations correct, showing that a lot of work needs to be done to adress this problem successfully. 

## Instructions
- Include a link to your visualization app
- mention that this repo is for the class project of MGT 4250 Fall 2023 at Elon University
- Project questions are stated
- Their importance are clearly mentioned with valid references
- Instructions about how to access and download your data correctly
- The data types and descriptions of the columns used in visualizations are clearly explained
- For each visualization, interpret a visualization and explain how it contributes to answering your question
- Find an article related to your questions and summarize the article
- Ask your questions to GPT-4 and write your query and GPT-4’s responses (You can use the API key for our course; Ask as many as possible for proper responses; Mention that the response is generated from GPT-4)
- Discuss whether your visualizations align well with the article and GPT-4’s
response



https://www.statista.com/statistics/233301/median-household-income-in-the-united-states-by-education/#:~:text=U.S.%20median%20household%20income%202022%2C%20by%20education%20of%20householder&text=U.S.%20citizens%20with%20a%20professional,money%2C%20at%2033%2C830%20U.S.%20dollars.

https://www.census.gov/library/publications/2023/demo/p60-279.html
