Crop Price Predictor

Abstract

The contemporary challenges of predicting crop prices accurately and reliably in agricultural economics are significant, with direct implications on farmers’ economic security, traders in market decisions and governments in making policy decisions. The objective of this project is to provide an Automated Machine Learning Based System for use in predicting future crop prices for many agricultural commodity types based on historical market data collected over a two-year period ending in calendar year 2025 and 2026. Regression Models along with Linear regression models, as well as HTML Language will be used to train the models and to evaluate them against a set of real-life data from past crop markets and will include various features, including: Crop Type, State, Commodity Code, Modal Price, Minimum Price, Maximum Price.
The proposed system includes extensive data preprocessing, feature engineering, and modelling and selection in order to enhance prediction accuracy through multiple measures of evaluation which include Root Mean Square Error (RMSE), Mean Absolute Error (MAE) and R squared (R²) . Through benchmarking against these metrics, models can be compared based upon performance.
The findings of our research demonstrate the ability of machine learning to provide new insights into agricultural price forecasting which will allow stakeholders to make data-driven decisions before prices change. In this report we provide a comprehensive overview of the entire process, from data collection and exploratory analysis through to model training, validation and result interpretation; thus providing a replicable methodology that can be applied to other crops and areas of the world.

Introduction

Agricultural exports continue to be one of the main sources for developing countries in the world today. One particular example is in India, where approximately 58% of the rural population relies upon agriculture as their main means of making a living. The fluctuation of crop prices has major implications on all aspects of life for these people. For instance, a sudden decrease in market price can result in farmers going into debt while unexpected increases in market price can create food insecurity for millions of people. Therefore, closing the gap between production and achieving a fair market return will serve as an important means of stabilising both the economy as well as improving social welfare for these nations.
Historically, estimating crop prices has been accomplished through agricultural officer expertise, with gardeners typically conducting annual manual surveys, relying on commodity exchange reports, or utilizing other local information sources. However, most methods are more retrospective than predictive in order to allow both farmers and policy makers to better prepare for farm production in the future. Estimating future crop prices can be made more difficult due to the dependence on numerous factors that are connected. Examples of these types of factors include: the changing climate and weather conditions, soil characteristics, the effects of geopolitical actions, import/export policies, the cost of equipment and transportation, and the resulting changes in consumer demand for food.
The rapid advancement of Artificial Intelligence (AI) and Machine Learning (ML) has opened transformative possibilities in the domain of agricultural analytics. By training models on large historical datasets, ML algorithms are capable of identifying non-linear relationships and temporal patterns that are invisible to conventional statistical methods. These models can learn from past market behavior across two or more years of data and generate forward-looking price forecasts with measurable accuracy.
A multi-crop price prediction system based on Regression-based Machine Learning Techniques Project (MLTP) is proposed for predicting prices and developing a tool for data-driven decision making in the agricultural sector. This project is based on a consolidated dataset containing the last two years of agricultural market data, combined with key data points for economic and nature-related variables.
This project will accomplish three major objectives:
(1) To develop and execute an end-to-end ML pipeline for predicting the prices of various crops;
(2) To determine the comparative performance of the various Regression algorithms in this domain and
(3) To identify opportunities for helping farmers, agri-businesses and decision-makers within their respective sectors in making informed choices about the future development of agricultural production.

Problem Statement

Even with countless pieces of information regarding agriculture (past prices, yields produced, seasonal tendencies and patterns, meteorological historical data and government buying records) there is an absolute lack of actionable (real time) and predictive (forward-thinking) pricing intelligence for multiple crops at once. Forecasting systems today are all siloed, tend to be specific to individual crops and lack the scalability and accuracy needed to provide value across a larger application base.

2.1 Core Problem

The central problem addressed in this project is: Given a comprehensive dataset of historical crop market data spanning at least two years, can a machine learning regression model accurately forecast future crop prices across multiple agricultural commodities, providing reliable predictions that account for seasonal, economic, and environmental variability?

2.2 Specific Challenges

The development of an effective crop price prediction system is constrained by several interrelated challenges:
Data Heterogeneity: Agricultural datasets are often sourced from multiple agencies (APMC markets, government portals, weather stations), each with differing formats, frequencies, and quality standards. Merging and harmonizing such data requires extensive preprocessing.
High Price Volatility: Crop prices are subject to sudden and extreme fluctuations driven by events such as drought, pest outbreaks, policy changes, or global supply chain disruptions. This volatility increases the difficulty of building stable and generalizable models.
Feature Complexity: Crop prices are influenced by a large number of variables including sowing season, state/region, minimum support price, rainfall, procurement volumes, and cold storage availability — many of which exhibit complex, non-linear interdependencies.
Temporal Dependencies: Price trends exhibit strong seasonality and lag effects, meaning that current prices are often influenced by conditions from previous weeks or months. Capturing these temporal relationships accurately requires thoughtful feature engineering.
Model Generalizability: A model trained on data for one crop or region may not transfer well to another. Building a system that generalises across multiple crop types and geographic markets without overfitting remains a significant technical challenge.

2.3 Motivation

The motivation for this project stems from the real-world consequences of crop price uncertainty. Farmers frequently lack access to reliable price forecasts at the time of sowing, the stage at which they commit to a specific crop, leading to market gluts or shortages that harm producers and consumers alike. Agri-market intermediaries and food processing companies require accurate price signals to plan procurement, logistics, and inventory. Government bodies need reliable forecasts to design timely price support interventions and buffer stock policies.
By building a machine learning-based prediction system trained on two years of multi-crop market data, this project aims to contribute a replicable, scalable, and interpretable tool that can meaningfully improve price transparency in agricultural markets.

Literature Review

Agricultural commodity price prediction has emerged as a significant field of research because of its impact on farmers, traders, and policymakers. Various researchers have attempted to utilise different statistical and machine learning-based models to analyse and forecast crop prices.
Researchers have utilised traditional methods such as Linear Regression to determine the relationship between different price factors such as minimum price, maximum price, and modal price.
Researchers have also attempted to utilise more recent techniques, such as Decision Tree, Random Forest, and Neural Network, to enhance the accuracy of agricultural commodity price prediction.
Considering the Indian agricultural commodity market, researchers have utilised mandi price datasets to determine the trends of agricultural commodity prices across different states, districts, and types of agricultural commodities. Researchers have also identified that different factors, such as location, type of commodity, and seasonal variations, affect agricultural commodity prices.
This project aims to utilise multiple linear regression to determine the relationship between minimum, maximum, and modal prices of crops.

Data Description

This project uses a dataset collected from Kaggle containing daily prices of agricultural commodities in markets throughout India for 2 years, 2025 and 2026, as well as details concerning the changes in price of the various crops throughout various regions and time periods.
The dataset contains important features used to locate the mandi: State, District, Market. It also specifies the type of commodity, type of variety, and grade of commodity related to the agricultural product. Additional features include Arrival_Date, which denotes when the price has been recorded. The three key numeric variables are Min_Price, Max_Price, and Modal_Price, which represent the minimum, maximum, and most common prices for that commodity on a given day.
This dataset is also quite large in size and appears to be well-structured for the use of advanced machine learning techniques (for example, there is enough data for each crop price to perform analysis and prediction accurately using Multiple Linear Regression).

 Model Development Details
The development of this project was managed through a collaborative ecosystem to ensure the coding integrity and seamless integration of a machine learning model with the web interface.

Integrated Development Environment (IDE)

Visual Studio Code was utilised as the primary coding environment for writing Python scripts, the major Crop Price Prediction model training and HTML to develop the Frontend.
 GitHub was used to host the project repository. This allowed us to increase our efficiency through collaborative coding, tracking changes across different versions of regression models and maintaining a centralised codebase.

Development Details 

To perform Exploratory Data Analysis (EDA) and execute machine learning, several specialised Python libraries were utilised. Pandas and NumPy played a significant role in data cleaning and handling of large-scale numerical arrays.
Similarly, for visual exploration of price trends, and implying correlation of two variables etc Matplotlib and Seaborn were employed to generate graphical representations.
The machine learning phase relied heavily on Scikit-learn (Sklearn), which provided the necessary tools for feature scaling, data splitting, and implementing regression algorithms.
Specifically, Sklearn was used to compute the R^2 score to assess the model's reliability and accuracy.

7.Evaluation Results

The performance of the multi-output Linear Regression model was evaluated using the Coefficient of Determination (R2 Score). This metric measures the "goodness of fit" of the model, specifically how well the independent features explain the fluctuations in crop prices.

7.1 Statistical Accuracy (R2 Analysis)

After training on the historical market dataset for 2025 and 2026, the model achieved near-perfect correlation across all three target variables on the test dataset:
Key Insight: An R^2 score of 0.98 for the Modal Price implies that 98% of the variation in the most frequent market prices can be explained by the input features (State, District, Market, and Commodity). This level of accuracy suggests a highly stable and linear relationship within the 2-year dataset.

Technical Implementation Highlights

Efficiency of Label Encoding: The near-perfect R2 scores validate the decision to use Label Encoding for categorical data. It allowed the Linear Regression algorithm to accurately map geographical premiums (different states/markets) to specific price points without losing critical information.
Consistency of the Linear Relationship: The results demonstrate that crop prices during the 2025–2026 period followed a highly linear trend relative to the encoded features, allowing the model to generalize with extreme precision.
Multi-Price Simultaneous Prediction: Through the Gradio Frontend, the model generates all three prices—Min, Max, and Modal—in a single execution. The logic remains consistent with the R2 scores, as the predicted "Min" is consistently lower than the "Max," providing a reliable "price corridor" for stakeholders.

7.4 Discussion of Findings

The high R2 values indicate that the dataset is highly structured and the selected features are the primary drivers of price. For end-users like farmers and traders, this means the model can be used with a high degree of confidence to anticipate market trends. However, it should be noted that while the model is extremely accurate for the 2025–2026 timeframe, real-world external "shocks" (like sudden floods or policy changes) would be required as additional features to maintain this level of accuracy in the long term.

Deployment Details

To facilitate backend development and interaction between the model and the end-user, Gradio was integrated as the primary framework. Gradio served as one of the major sources that allowed Python-based regression. By utilising Gradio’s library, we created an intuitive input layer where users can select categorical variables such as State, Crop Category, etc. 
Three models were built, one for predicting the Modal Price, to know the most frequently occurring price and two others were built for predicting the Maximum and Minimum price. All the models were made using the Gradio interface.
Now, the frontend development was built using HTML for the semantic structure and CSS for background design, ensuring a user-friendly interface. 



Conclusion and Future Scope  

The developed Crop Price Prediction Model successfully demonstrates the significance of Machine learning in various domains including agriculture. As we know, India is an agrarian economy and hence it becomes essential to address issues like information asymmetry in this sector. Utilising historical data including state, district, market and commodity variables, the model provides users with reliable forecasts of Minimum, Maximum and Modal Prices.
Key highlights
The unique approach of using two price points as features to predict the third (e.g., using Min and Max to predict Modal) significantly improved the model's logical consistency and accuracy.
The model successfully captures regional and commodity-specific price trends, helping users make informed decisions on when and where to sell their produce to maximize profit.
1.Future Scope 
a.Supply Chain Expansion
Expanding the model to predict Arrival Quantities alongside prices would help in identifying potential market gluts or shortages, assisting the government and private sectors in better supply chain management.
b.Mobile Application
To make sure this model's utility reaches every corner it could be turned into a Mobile Application, with Multilingual support to diversify usage of the model.
c.External Factor Analysis
Agricultural prices are heavily influenced by external variables. Integrating additional data layers would improve usefulness Incorporating rainfall and temperature data to account for crop yield fluctuations. Factoring in transportation costs which directly impact market prices.

