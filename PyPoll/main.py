#Voter ID, County, Candidate
#import os and csv
import os
import csv

#print title
print("Election Results")
print("------------------------------")

count = 0
candidates = []
votes = []


#set path for file
csvpath = os.path.join("..", 'election_data.csv')

#open file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#skip header    
    csv_header = next(csvreader)
#count votes total  
    for row in csvreader:
       count = count + 1
       candidate = row[2]
       
       if candidate in candidates:
           candidate_index = candidates.index(candidate)
           votes[candidate_index] = votes[candidate_index] + 1 
    else:
        candidates.append(candidate)
        votes.append(1)

percentages = []
max_votes = votes[0]
max_index = 0

for line in range(len(candidates)):
    vote_percentage = votes[line]/count * 100
    percentages.append(vote_percentage)
    if votes[line] > max_votes:
        max_votes = votes[line]
        print(max_votes)
        max_index = count
winner = candidates[max_index]
#print
print("Total Votes " + str(count))
print("------------------------------")
for x in range(len(candidates)):
    print(f"{candidates[x]}: {percentages[x]}% ({votes[x]})")
print("------------------------------")
print(f"Winner: {winner}")
print("------------------------------")