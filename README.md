# Frexco Challenge

### Introduction 
This is a project developed to automate the first step of the comparing market prices process.

#### Goals 

The target here is to get competitor market prices in order to compare Frexco prices, ensuring the prices are competitive. However in this feature the functionalities are: 

- [x] Open Frubana's page;
- [x] Load all the items; 
- [x] Get all products data;
- [x] Create and insert them in a csv file;
- [x] Save in the SqLite database.

### Requirements

To execute this solution, you must have: 
* [Python 3.6+](https://www.python.org/)
* [pip](https://pypi.org/)

After installed those programs, you'll need run pip install:

```pip instal -r requiriments.txt```

```python run.py```

### FAQ

- **Where are the csv files saved?**
  
  Inside the 'challenge_frexco/files'.
  

- **What's the file's name created?** 
  
  It's generated using the current's execution date and hour, following this format:

  "frubana_precos_data_%d_%m_%y_hora_%H_%M.csv"

### Any Suggestions
[creator's email:](vinicius.cavallaro.silva@gmail.com) vinicius.cavallaro.silva@gmail.com