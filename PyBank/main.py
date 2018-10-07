#modules
import os
import csv


print("Financial Analysis")
print("--------------------------")

count = 0
total = 0

bddate = []
profitloss = []

#set path for file
csvpath = os.path.join("..", 'budget_data.csv')

#Total months
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        count += 1
print("Total Months: " + str(count))

#Total Profit/Loss
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)   
    for row in csvreader:
       total += int(row[1]) 
    print("Total: " + "$" + str(total))

#find average change, increase and decrease
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)  
    #append lists
    for row in csvreader:
        bddate.append(row[0])
        profitloss.append(int(row[1]))

greatestincrease = profitloss[1]-profitloss[0]
greatestdecrease = greatestincrease
total = profitloss[0]

#loop for figuring greatest increase & decrease
for r in range(1, len(profitloss)):
    if profitloss[r] - profitloss[r-1] >= greatestincrease:
        greatestincrease = profitloss[r] - profitloss[r-1]
        greatincreasedate = bddate[r]
    elif profitloss[r] - profitloss[r-1] <= greatestdecrease:
        greatestdecrease = profitloss[r] - profitloss[r-1]
        greatdecreasedate = bddate[r]
    total += profitloss[r]
    
#finding average change
averagechnge = round((profitloss[len(profitloss)-1] - profitloss[0])/(len(profitloss)-1), 2)

print("Average Change $" + str(averagechnge))
print("Greatest Increase " + greatincreasedate + ' ($' + str(greatestincrease) + ')')
print("Greatest Decrease " + greatdecreasedate + ' ($' + str(greatestdecrease) + ')') 
