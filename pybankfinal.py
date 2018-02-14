import os
import csv

csv_path = os.path.join("budget_data_1.csv")

month=[]
rev=[]

with open(csv_path, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    next(csv_reader, None)

    for row in csv_reader:

        month.append(row[0])
        rev.append(int(row[1]))
val= rev[0] 
Change=[]  
for i in rev:
    Diff = i-val
    Change.append(Diff)
    val=i

max_index=[i for i, j in enumerate(Change) if j == (max(Change))][0] 
min_index=[i for i, j in enumerate(Change) if j == (min(Change))][0]

total_mon=len(rev)
total_rev=sum(rev) 
avg_rev=((sum(Change))/(len(Change)-1))
greatest_mon=month[max_index] 
greatest_inc=max(Change)
lowest_mon=month[min_index]
lowest_inc=min(Change)
print('Financial Analysis')
print('----------------------------')
print('Total Months: ' + str(total_mon)) 
print('Total Revenue: $' + str(total_rev))
print('Average Revenue Change: $' + str(avg_rev))
print('Greatest Increase in Revenue:' + greatest_mon +" $"+ str(greatest_inc))
print('Greatest Decrease in Revenue:' + lowest_mon +" $"+ str(lowest_inc))