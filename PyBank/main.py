# Import the necessary dependencies for os.path.join() 
import os 
import csv 

# Read in a .csv file 
csv_file = os.path.join("../","budget_data.csv") 

# Lists to store data
date = []
prof_loss = []

with open(budget_data.csv, newline="") as csvfile:
    read_budget = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        # Add title
        title.append(row[1])
        date.append(row[2])
        prof_loss.append(row[3])
 
return date
return prof_loss
            