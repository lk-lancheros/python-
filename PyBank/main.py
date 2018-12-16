#import library
import os
import csv

#joining path
budget_data_path = os.path.join("..", "Resources", "budget_data.csv")
file_to_output = "PyBank_output.txt"

# open and read csv
with open(budget_data_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    # skip header row
    print(f"Header: {csv_header}")

    # find net amount of profit and loss
    profit = []
    months = []
    profit_prev_row = []
    total_months = 0
    revenue_change = []
    
    #read through each row of data after header
    for row in csvreader:
        profit.append(int(row[1]))
        months.append(row[0])
            
    # find revenue change
    
    for x in range(1, len(profit)):
        revenue_change.append((int(profit[x]) - int(profit[x-1])))
    
    #calculate average revenue change
    revenue_average = round(sum(revenue_change) / len(revenue_change),2)
    
    # calculate total length of months
    total_months = len(months)

    # greatest increase in revenue
    greatest_increase = max(revenue_change)
    # greatest decrease in revenue
    greatest_decrease = min(revenue_change)


with open(file_to_output, "w") as txt_file:
    # Print the final vote count (to terminal)
    financial_results = (
        f"\n\nFinancial Analysis\n"
        f"-------------------------\n"
        f"Total Months:{total_months}\n"
        f"Total: ${sum(profit)}\n"
        f"Average change: $ {revenue_average}\n"
        f"Greatest Increase in Profits: {months[revenue_change.index(max(revenue_change))+1]} ${greatest_increase}\n"
        f"Greatest Decrease in Profits: {months[revenue_change.index(min(revenue_change))+1]} ${greatest_decrease}\n")
        
    print(financial_results, end="")

    # Save the final vote count to the text file
    txt_file.write(financial_results)