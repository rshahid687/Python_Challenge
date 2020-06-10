import os
import csv
import numpy

budget_csv = os.path.join("../PyBank", "budget_data.csv")
bank_txt = os.path.join("../PyBank", "bank_txt.csv")

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")
    csv_header = next(csvreader)

    print('Financial Analysis')
    print('---------------------------------')

    #Get Total Months 
    data = list(csvreader)
    totalMonths = len(data)
    print(f'Total Months: {totalMonths}')
    #print(data)

    sum = 0
    dates = []
    for row in data:

        value = int(row[1])
        sum = sum + value 
        dates.append(row[0])
    dates = dates[1:]
    #print(dates)

    #Total    
    print(f'Total: ${sum}')

    #Average Change 
    avgChange = round((int(data[-1][1])- int(data[0][1]))/(totalMonths-1),2)
    print(f'Average Change: ${avgChange}')

    #Greatest Increase/Decrease 
    deltas = []
    for i in range(totalMonths):
        if i + 1 >= totalMonths:
            break
        delta = int(data[i+1][1]) - int(data[i][1])
        deltas.append(delta)

    #print(deltas)
    maxVal = max(deltas)
    minVal = min(deltas)

    changesDict = {}
    for key in dates:
        for value in deltas:
            changesDict[key] = value
            deltas.remove(value)
            break
    
    #print(changesDict)
    greatestInc = max(changesDict, key=changesDict.get)
    greatestDec = min(changesDict, key=changesDict.get)
    print(f'Greatest Increase in Profits: {greatestInc} (${maxVal})')
    print(f'Greatest Decrease in Profits: {greatestDec} (${minVal})')


    output = (
        f'Financial Analysis\n'
        f'---------------------------------\n'
        f'Total Months: {totalMonths}\n'
        f'Total: ${sum}\n'
        f'Average Change: ${avgChange}\n'
        f'Greatest Increase in Profits: {greatestInc} (${maxVal})\n'
        f'Greatest Decrease in Profits: {greatestDec} (${minVal})\n'
    )

    with open(bank_txt, "a") as text:
        text.write(output)





        


