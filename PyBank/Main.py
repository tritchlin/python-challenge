import os
import csv
import locale

# Set number and currency formatting
locale.setlocale(locale.LC_ALL,'en_US')
locale._override_localeconv = {"n_sign_posn": 3}

# Locate and open CSV file
csvpath = os.path.join(".","Resources","budget_data.csv")

# Create lists and variables
month = []
data = []
total = 0
count = 0
date = []
change = []
collate = {}

# Open CSV file
with open(csvpath,'r') as csvfile:
    budget = csv.reader(csvfile)

    csv_header = next(budget)
    
    # Begin for loop
    for row in budget:
        month = str(row[0])
        data = int(row[1])
        
        # If/else to create list of profit/loss deltas and corresponding months
        if count == 0:
            firstvalue = int(row[1])
        elif count == 1:
            current_value = int(row[1])
            delta = current_value - firstvalue
            change.append(delta)
            date.append(str(row[0]))
            previous_value = int(row[1])
        else:
            current_value = int(row[1])
            delta = current_value - previous_value
            change.append(delta)
            date.append(str(row[0]))
            previous_value = int(row[1])
        
        # Tracking running totals for number of months, total from P&L column
        total = total + data
        count = count + 1

# Create dictionary with deltas and months for calculations
collate = dict(zip(date, change))
maxdate = max(collate, key = collate.get)
mindate = min(collate, key = collate.get)

# Additional maths and finalized formatting
totalprofit = locale.currency(total, grouping = True)
deltaaverage = locale.currency((sum(change) / len(change)), grouping = True)
minprofit = locale.currency(int(min(change)), grouping = True)
maxprofit = locale.currency(int(max(change)), grouping = True)

# Set complete message, with formatting, including top and bottom spacing
message = f"""
 
Financial Analysis
-------------------
Total Months: {count}
Total: {totalprofit}
Average Change: {deltaaverage}
Greatest Increase in Profits: {maxdate} ({maxprofit})
Greatest Decrease in Profits: {mindate} ({minprofit})

"""
print(message)

# Create and write results to text file in Analysis folder
output_path = os.path.join("Analysis","output.txt")

f = open(output_path,"w")
f.write(message)
f.close()
