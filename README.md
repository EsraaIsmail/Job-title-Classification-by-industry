## 0- INTRODUCTION: 
The problem is a supervised text classification problem, using an imbalanced dataset to train the model, The Dataset has two variables (Job title & Industry), our goal is:
    • Clean the data and preparing for the model,
    • Solve the Imbalance data issue.	
    • Chose the Appropriate model for our problem


## 1- Cleaning the data:
        1.1- Remove duplicates data:
I noticed that more than half of the available data are duplicated so there is no need to use a duplicate data in the model training it is lead to a false accuracy, thus I removed duplicate data.
Removing duplicate data helped partially to solve the problem of imbalanced data.
Data classes distribution before removing duplicates

        1.2- Removing words less than 2 char 
        1.3- Removing numbers 
        1.4- Removing stop words
        1.5- Use lowercase
        1.6- Convert a collection of text documents to a matrix of token counts.
        1.7- Transform a count matrix to a normalized tf-idf representation.



## 2- THE CLASSIFIER: 
We tried different algorithms and techniques, to interpret text data we tried 3 types of models:
    • LinearSVC
    • Multi Nominal NB
    • Logistic Regression
the 3 models could contribute well with text data, but finally, I choose my final model to be the highest in measure F1-score, LinearSVC is the highest F1-score, This model implements  L2 regularization with stochastic gradient descent  .
    3 Dealing with Data Imbalance:
        3.1- Frist approach:
Adding class weights into consideration when training, using compute_sample_weight in sklearn.utils to estimate sample weights by class for unbalanced datasets.
        3.2- Second approach:
Sampling technique Oversampling followed by under-sampling, the combination of over-sampling and under-sampling, using the SMOTE and Tomek links techniques.
    4 Extend the model to have better performance:
        4.1- Add more data 
Train the model with extra data.
        4.2- Algorithm Tuning
Using grid search to tune the model but it could cause overfitting, thus I prefer manual-tuning parameter.
 


## 5- Model Evaluation:
Imbalance classes provide to mislead classification accuracy, Evaluation of a classification algorithm performance is measured by the 
        5.1 F1-score:
It is calculated from the precision and recall of the test, Precision is a positive predictive value, and recall is as sensitivity.
        5.2 Confusion Matrix:
contaisns information about the actual and the predicted class.
## 6- Limitations:
The limitation in this problem is about the data, first of all, the data size is relatively small after removing duplicate data we lose more than half of the original data.
I tried to handle class imbalance with sample weights and sampling technique the combination of over-sampling and under-sampling, but misclassifying for classes with lower relative samples still occurs, thus this problem requires a lot of data.
## 7- Flask API:
    1. Run the server by commend : python3 app.py
    2. Running on http://127.0.0.1:5000/ 

