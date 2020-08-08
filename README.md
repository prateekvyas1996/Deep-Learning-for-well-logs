# Deep-Learning-for-well-logs

There are 2 jupyter notebook in the repository
1. [well_log_data_preparation.ipynb](https://github.com/prateekvyas1996/Deep-Learning-for-well-logs/blob/master/well_log_data_preparation.ipynb)
2. [log_data_prep_nonsacrifised.ipynb](https://github.com/prateekvyas1996/Deep-Learning-for-well-logs/blob/master/log_data_prep_nonsacrifised.ipynb)

* well_log_data_preparation is used to create clean data set from the las files inside folder 2017_kansas_log_data. You have to put all your las files in this folder. When you run the notebook it automatically scan the files and clean it and finally save it to new file called well_log_data_prepared.csv.

* The well_log_data_prepared.csv already contain 200 wells of data which are taken from kansas geological survey [website](http://www.kgs.ku.edu/Magellan/Logs/index.html)

* log_data_prep_nonsacrifised notebook is used to create big data set when the amount of las files are very less, it can also be used on big data as well. This notebook replaces NA values with zeros which actually increase our dataset for deep learning training purpose.

My recommendations are to use nonsacrifised notebook, if it does not give good results than use 1st one.

## Prequisite

Before running the notebook you must have following

1. numpy installed
2. pandas installed
3. lasio installed

* Run the below command to install all

`pip install numpy`

`pip install pandas`

`pip install lasio`