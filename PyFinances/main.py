import os
import csv

budget_path = os.path.join('_RiceDataAnalytics','Homework','python-challenge','PyFinances','Budget.csv')

total = 0
mos_count = 0
profit_list = []
profit_diff = []
date_list = []

with open(budget_path,newline='',encoding='utf-8') as csvfile:
    budget_reader = csv.reader(csvfile,delimiter = ',')
    csv_header = next(budget_reader)
   
   #This counts the months, sums the profits and stores the profit and dates into lists
    for row in budget_reader:
        mos_count += 1
        total = total + int(row[0])
        profit_list.append(row[0])
        date_list.append(row[1])
    
    #The gets the diffenential change between two dates and stores it into a new list
    x = 1
    for y in range(mos_count):
        if x < mos_count:
            profit_diff.append(int(profit_list[x])-int(profit_list[y]))
            x = x + 1
        else:
            continue
    
    #These functions get the average change and the max and min from the list
    avg_change = int(sum(profit_diff))/int(mos_count-1)
    max_diff = max(profit_diff)
    min_diff = min(profit_diff)

    #This indexes the place where the highest and lowest differentials occured
    #it then looks up that indexed location in the date list and gets the date of this event
    max_date_get = profit_diff.index(int(max_diff))
    max_date_return = date_list[int(max_date_get+1)]
    min_date_get = profit_diff.index(int(min_diff))
    min_date_return = date_list[int(min_date_get+1)]
            
    print("\nFinancial Analysis")
    print("-------------------------")
    print(f'Total Months: {mos_count}')
    print(f'Total: ${total}')
    print(f'Average Change: ${format(avg_change,".2f")}')
    print(f'Greatest increase in Profit: {max_date_return} $({max_diff})')
    print(f'Greatest decrease in Profit: {min_date_return} $({min_diff})')
