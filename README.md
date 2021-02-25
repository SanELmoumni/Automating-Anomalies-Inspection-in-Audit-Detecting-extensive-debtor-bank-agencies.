# Automating Anomalies Inspection in Audit : Detecting extensive debtor bank agencies !

## First objective : 

Each day, the BI team sends a daily file containing the balance for each expense center. These debits are in the form of a negative number, hence the first objective is to detect whether each agency has exceeded 5 million DHs per day, if so, calculate the number of occurrence of successive days of this state, and also the number of recurrence of the period of realization of this state, that is to say during all the time, how much period of time each CDF represented this anomaly.

## Second objective : 

The second objective is to detect the agencies representing anomalies, which spend for three successive days or more, a debit greater than three million DHs per day, and again calculating the occurrence and recurrences of this state. 

![Suspicious behaviour, WARNING !](Images/Capture.PNG)

## About the files : 

For confidentiality purposes, the data used in this notebook isn't real, but was generated randomly using a script.

The input file is ```Archive_Soldes_generated.csv``` and is generated randomly, while the output file is ```Reporting Caisse.xlsx```, and contains 4 Excel sheets. Check the notebook for more informations !

Text me if you need more details !