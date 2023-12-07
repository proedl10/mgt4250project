# The Impact of Income Inquality - The class project of MGT 4250 Fall 2023 at Elon University



## Project Questions
- Q1: What are the key drivers for income inequality?
- Q2: How does race affect the median income of everyday people?
- Q3: What is the impact of Education on income levels? 

## Why we Picked These Questions
- Income Inequality has a significant societal and economic impact, and it is important that we understand the factors that lead to inequality for greater economic development.
- When comparing median incomes, it is important to factor in race as the data could highlight challenges that certain racial groups go through.
- This data could provide insight into the role of education, and show the importance of equal opportunity. 

  
## Data Description and Access Instructions
- To access data, the first step is to click on the link to the streamlit app. Once in the app, you will be able to access our visualizations. 
- First Visualization
    -  Our first visualization is 
- Second Visualization
    - 



## Interpreting Visualizations
<img width="500" alt=![image](https://github.com/proedl10/mgt4250project/assets/152214737/6afa4d27-d8a1-45b8-a006-243d1d1e483f)>




## Discussion & Summary
- Explain how and why these visualizations answer your question


 

- Include figures for your most up-to-date three visualizations with descriptions



Technological Impact:
- Bar chart illustrating the distribution of income across different industries.
- X-axis: Industries, Y-axis: Hourly Earnings.
- Highlight industries with a significant technological impact. 
- This data explains how the industry you work in affects income levels, and how gender also has a serious input.
- By visualizing income distribution across industries, you can identify sectors where technological advancements may be contributing to income disparities. We can see which industries are most frequent in which locations, and see how this can impact income inequality.


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

## Section 2: Data Description & Upload 
To find and download publicly available datasets for our project, we looked for sources regarding median income by a variety of characteristics inculding race, gender, and education. We were able to find an abundance of datasets on census.gov that met our needs but in order to visualize the data we had to re-organize them into a more user friendly format as there were several cells containing text as opposed to numbers. To do this, we selected a certain characteristic and the data that represented it, and moved it into a seperate spreadsheet. For example, in the uploaded files of this repository there are 4 excel spreadsheets containing the data found on census.gov regarding median income and race. Each spreadsheet contains data about a different race in order to make vizualizing the data on python simple and fluid. 

To download the datasets we used and explored, click the census.gov link below, scroll down to the "Tables" section, and downlaod the desired spreadsheet. The data used for our visualizations can be found in the dataset labeled "A-1" under the "Tables" section. This spreadsheet containes data about a variety of races that we had to split up into their own spreadsheet in order to compare against one another.

Another source of our data was from statista.com, where we found data regarding median income in USD by level of education. This spreadsheet only contained the processed means of the original dataset so it did not need much processing. That being said, we had to clean up the spreadsheet and format it in a python analysis/visualization friendly way. It can be found on the right under "Download" at the top of the page, the link can be found below. The data types in the original spreadsheet did not need to be modified as all numbers were pre-processed into their means and the only other column was the name/title of the level of education. If we had the original data before the means were calculated, we could have used label encoding or OneHotEncoding to encode the level of education and produce a machine learning model to deepen our understanding of the data through statistics and visualizations. 

https://www.statista.com/statistics/233301/median-household-income-in-the-united-states-by-education/#:~:text=U.S.%20median%20household%20income%202022%2C%20by%20education%20of%20householder&text=U.S.%20citizens%20with%20a%20professional,money%2C%20at%2033%2C830%20U.S.%20dollars.

https://www.census.gov/library/publications/2023/demo/p60-279.html
