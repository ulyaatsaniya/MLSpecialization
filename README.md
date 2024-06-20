**Google Cloud End-to-End Machine Learning Using Black Friday Dataset to Predict Customer Purchase**

**Abstract**

Machine learning (ML) has become incredibly important over the past ten years. ML teaches computers to learn from data, allowing them to make better decisions on their own. This progress has led to incredible advancements – think of how good computers are at recognizing faces, or even understanding our regular speech! Businesses are using ML to predict what might happen in the future, especially with their customers. In this project, the goal is to figure out what individual customers are likely to buy on Black Friday, based on things we know about them. This model would be a huge help for businesses trying to boost their sales during the busiest shopping day of the year. We tested out several ML techniques, but the best one for this job seems to be a method called XGBoost regression.

**Table of Contents**
Introduction
System Architecture
Dataset
Exploratory Data Analysis
Univariate Analysis
Bivariate Analysis
Multivariate Analysis
Data Preprocessing
Model Implementation
Evaluation and Analysis
Conclusion
Installation
Usage
Features
Contributing
License
Contact Information

**Introduction**
In the realm of retail, Black Friday stands as a pivotal moment, attracting customers with its enticing deals and discounts. To capitalize on this lucrative opportunity, businesses strive to anticipate consumer behavior and tailor their strategies accordingly. Machine learning (ML) offers a powerful tool in this regard, enabling businesses to leverage data to make informed decisions. In this project, a Black Friday dataset was analyzed using ML classification models, with the aim of predicting individual customer purchases. Among the various models tested, XGBoost regression emerged as the most effective in identifying likely purchases. This model holds significant promise for businesses looking to optimize their sales strategies during the busiest shopping day of the year.

**System Architecture**
The system architecture involves machine learning techniques applied to the Black Friday dataset to predict purchase amounts using various regression models. The evaluation metrics used are root mean squared error (RMSE) and R-squared. Data preprocessing steps include handling missing values, converting categorical features to numerical features, and normalizing numerical features. Models are trained and evaluated on the training set, and the best model is deployed to a production environment.

**Dataset**
The Black Friday dataset is a publicly available dataset that contains information about customer purchases made on Black Friday. The dataset includes information such as customer ID, gender, age, occupation, city category, marital status, product category, and purchase amount. It has over 550,000 rows of data and is well-structured and relatively clean.

**Exploratory Data Analysis**
Univariate Analysis
Univariate analysis examines one variable at a time to describe the data, summarizing it and finding patterns using visual tools like bar graphs, pie charts, and histograms.

Distribution of Purchase Amount
Distribution of Gender
Distribution of Age
Distribution of Category
Distribution of Occupation
Distribution of Current City
Bivariate Analysis
Bivariate analysis examines the relationship between two variables to identify correlations, trends, patterns, and make predictions.

Distribution of Purchase amount vs Occupation
Distribution of Purchase amount vs Age
Distribution of Purchase amount vs Gender
Distribution of Purchase amount vs City Category
Distribution of Purchase amount vs Product Category
Distribution of Purchase amount vs Marital Status
Multivariate Analysis
Multivariate analysis is used to analyze the relationships between multiple variables and includes techniques like regression analysis, factor analysis, cluster analysis, and discriminant analysis.

Pairplot of All Features
Heatmap of All Features
Data Preprocessing
Data preprocessing involves preparing the dataset for training:

Handling missing values by imputing them with the median.
Converting categorical features to numerical features using one-hot encoding.
Normalizing numerical features using MinMaxScaler.
Splitting the dataset into training and test sets.
Model Implementation
Four machine learning models were trained and evaluated on the dataset to predict customer purchase amounts:

Linear Regression
Decision Tree Regression
Random Forest Regression
XGBoost Regression

**Evaluation and Analysis**
The XGBoost regression model achieved the highest accuracy with an RMSE of 2931.73 and an R-squared of 0.6589, making it the best-suited model for the Black Friday dataset.

**Conclusion**
The project explored four machine learning models to predict customer purchase amounts on Black Friday using the Black Friday dataset. The XGBoost regression model achieved the best performance, demonstrating the potential of ML models to aid businesses in targeting marketing campaigns and improving sales strategies.

Contact Information
For questions or support, please contact Ulya Tsaniya at ulyaatsaniya@gmail.com.

