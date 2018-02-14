import os
import csv

csv_path = os.path.join("election_data_1.csv")

Candidates=[]

with open(csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
 
    next(csv_reader, None)

    # Loop through rows
    for row in csv_reader:
        Candidates.append(row[2])

total_votes = len(Candidates)
candidate_list = set(Candidates)
candidate_list = [i for i in candidate_list]
counts = [Candidates.count(i) for i in candidate_list]
percent = [((Candidates.count(i)/total_votes)*100) for i in candidate_list]
percent = [round(i,3) for i in percent]
maxed = max(counts)
mx,idx = max( (counts[i],i) for i in range(len(counts)) )
wins=candidate_list[idx]

print('Election Results')
print("***************")
print('Total Votes: ' + str(total_votes))
print("***************")
candidate_num=0
for i in candidate_list:
    print(i + ': ' + str(percent[candidate_num])+'% '+ '(' + str(counts[candidate_num]) + ')' )
    candidate_num+=1
print('Winner: ' + str(wins)) 