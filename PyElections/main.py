import os
import csv
from heapq import nlargest

elect_path = os.path.join('_RiceDataAnalytics','Homework','python-challenge','PyElections','Election.csv')


with open(elect_path,newline='',encoding='utf-8') as csvfile:
    election_reader = csv.reader(csvfile,delimiter = ',')
    csv_header = next(election_reader)

    total_vote = 0
    candidates = []
    candidate_dict = {}
    number = 0
    for row in election_reader:
        total_vote = total_vote +1

        if row[0] not in candidates:
            candidates.append(row[0])
            candidate_dict.update({row[0]:number})
        if row[0] in candidates:
            candidate_dict[row[0]] += 1
        

    #print(candidates)
    print("\nHouston Mayoral Election Results")
    print("---------------------------------")
    print(f'Total Votes Cast: {total_vote}')
    print("---------------------------------")
    
   
    for key,value in sorted(candidate_dict.items(),key=lambda item:item[1], reverse=True):
        print(f'{key}: {format(value/total_vote,".1%")} ({value}) ')
       
    two_highest = nlargest(2,candidate_dict,key = candidate_dict.get)
    print("\n---------------------------------")
    print (f'1st Advancing Candidate: {two_highest[0]}')
    print (f'2nd Advancing Candidate: {two_highest[1]}')
    print("---------------------------------")
