# import necessary modules
import os
import csv

# Declaring necessary lists
total_months = []
profit_loss = []
avg_change = []

# get file path
file_path = os.path.join("PyBank" ,"Recources" , "budget_data.csv")

# open and read file
with open(file_path) as budget_data:
    csvreader = csv.reader(budget_data)

    # header
    header = next(csvreader)

    # declaring the first row, and previous net value
    first_row = next(csvreader)
    prev_net = int(first_row[1])

    # adding first values to appropriate lists
    total_months.append(first_row[0])
    profit_loss.append(int(first_row[1]))
    avg_change.append(prev_net)

    # gather necessary values into correlating lists
    for row in csvreader:
        total_months.append(row[0])
        profit_loss.append(int(row[1]))
        
        change = prev_net - int(row[1])
        prev_net = int(row[1])
        avg_change.append(change)

    # removing first value from avg_change (the first 'prev_net' value).
    avg_change.pop(0)

    # header of the data
    print("Financial Analysis")
    print("-------------------------------")
    
    # print total number of months
    print(f'Total Months: {len(total_months)}')

    # summing and printing profit/loss
    total_profit_loss = sum(profit_loss)
    print(f'Total: {total_profit_loss}')        

    # calculating and printing average change
    average_change = (sum(avg_change)/len(avg_change)) * -1
    print(f'Average Change: {average_change}')

    #calculating and printing average increase
    greatest_increase = min(avg_change) * -1
    print(f'Greatest Increase in Profits: {greatest_increase}')

    #calculating and printing average decrease
    greatest_decrease = max(avg_change) * -1
    print(f'Greatest Decrease in Profits: {greatest_decrease}')