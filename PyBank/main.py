# Modules
import os
import csv
# set Path to collect data from the Resources folder
current_directory = os.path.dirname(os.path.abspath(__file__))
budget_data=os.path.join("Resources","budget_data.csv")
# Read in the CSV file
with open(budget_data,"r") as csvfile:
    # Split the data on commas
    csvreader=csv.reader(csvfile,delimiter=",")
    #read the header row first(skip this if there is no header)
    header=next(csvreader)
    # Lists to store data
    Months_Nums=0
    Total=0
    Month_List=[]
    ProLoss_List=[]
    # Loop through looking for the values
    for row in csvreader:
        # Add numbers of months
        Months_Nums+=1
        # Add total amount of "Profit/Losses"
        Total=Total+int(row[1])
        # Add Month to the list of Month
        Month_List.append(row[0])
        # Add float values to the list of Profit/Losses
        ProLoss_List.append(float(row[1]))
    #list to store the changes in "Profit/Losses" 
    ProLoss_change_List=[]
    #loop through the list of Profit/Losses
    for i in range(len(ProLoss_List)-1):
        #get the value of changes in Profit/Losses
        ProLoss_change=ProLoss_List[i+1]-ProLoss_List[i]
        # add to the list of Profit/Losses changes
        ProLoss_change_List.append(ProLoss_change)
    # Calculate the total of the changes in Profit/Losses
    ProLoss_changeTotal=sum(ProLoss_change_List)
    # Calculate the average of the changes in Profit/Losses
    ProLoss_changeAverage=round(ProLoss_changeTotal/len(ProLoss_change_List),2)
    # Get the greatest increase in profits
    Greatest_increase=max(ProLoss_change_List)
    # Get the greatest decrease in profits
    Greatest_decrease=min(ProLoss_change_List)
    # Get the indext of greatest increase in the list of Profit/Losses changes
    MaxIndex=ProLoss_change_List.index(Greatest_increase)
    # Get the indext of greatest decrease in the list of Profit/Losses changes
    MinIndex=ProLoss_change_List.index(Greatest_decrease)
    # The month corresponding to the greatest increase
    Month_Max=Month_List[MaxIndex+1]
    # The month corresponding to the greatest decrease
    Month_Min=Month_List[MinIndex+1]
# Print all the values needed
print(f"Financial Analysis\n"   
    f"----------------\n"
    f"Total Months: {Months_Nums}\n"
    f"Total: ${Total}\n"
    f"Average Change: ${ProLoss_changeAverage}\n"
    f"Greatesd Increase in Profits: {Month_Max} (${Greatest_increase})\n"
    f"Greatest Decrease: {Month_Min} (${Greatest_decrease})")
       