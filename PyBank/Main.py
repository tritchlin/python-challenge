import os
import csv
import locale

# import currency formatting settings
from numpy.lib.function_base import select
from numpy.lib.histograms import _histogram_dispatcher
locale.setlocale(locale.LC_ALL,'en_US')


# Locate and open CSV file
csvpath = os.path.join("Resources","budget_data.csv")
csvfile = open(csvpath,'r')
budget = csv.reader(csvfile)

#remove headers
csv_header = next(budget)

# create lists and variables
month = []
data = []
total = 0
count = 0
maxrow = None
minrow = None

#start for loop
for row in budget:
    month = str(row[0])
    data = int(row[1])

#identify max and min while iterating
    if maxrow == None:
        maxrow = row
    elif int(maxrow[1]) < data:
        maxrow = row

    if minrow == None:
        minrow = row
    elif int(minrow[1]) > data:
        minrow = row

# running total and count per row
    total = total + data
    count = count + 1

# maths
totalprofit = locale.currency(total, grouping = True)
average = total / count
average_formatted = locale.currency(average, grouping = True)
minprofit = locale.currency(int(minrow[1]), grouping = True)
minname = str(minrow[0])
maxprofit = locale.currency(int(maxrow[1]), grouping = True)
maxname = str(maxrow[0])

#set complete message, with formatting, including top and bottom spacing
message = f"""
 
Financial Analysis
-------------------
Total Months: {count}
Total: {totalprofit}
Average Change: {average_formatted}
Greatest Increase in Profits: {maxname}, {maxprofit}
Greatest Decrease in Profits: {minname}, {minprofit}

"""
print(message)

output_path = os.path.join("Analysis","output.txt")

f = open(output_path,"w")
f.write(message)
f.close()
