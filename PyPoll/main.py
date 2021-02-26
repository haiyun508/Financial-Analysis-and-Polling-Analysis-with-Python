# Modules
import os
import csv
# set Path to collect data from the Resources folder
current_directory = os.path.dirname(os.path.abspath(__file__))
election_data=os.path.join("Resources","election_data.csv")
# Read in the CSV file
with open(election_data,"r") as csvfile:
    # Split the data on commas
    csvreader=csv.reader(csvfile,delimiter=",")
    #read the header row first(skip this if there is no header)
    header=next(csvreader)
    # Lists to store data
    Votes_Nums=0
    Candidate_List=[]
    Unique_Candidate_List=[]
    Percentage_list=[]
    # Loop through looking for the values
    for row in csvreader:
        # Add numbers of votes
        Votes_Nums+=1
        Candidate_List.append(row[2])
        # Loop through getting the unique value of candidates
        if row[2] not in Unique_Candidate_List:
            Unique_Candidate_List.append(row[2])
    # print out total number of votes
    print(f"Election Results\n"
            f"------------------------\n"
            f"Total Votes: {Votes_Nums}\n"
            f"------------------------")
    # Loop thrugh the candidate list getting values for each candidate
    for i in range(len(Unique_Candidate_List)):
        Unique_Candidate_Votes=Candidate_List.count(Unique_Candidate_List[i])
        Unique_Candidate_Percentage=round((Unique_Candidate_Votes/Votes_Nums)*100,2) 
        Percentage_list.append(Unique_Candidate_Percentage)
        # Print out values for each candidate
        print(f"{Unique_Candidate_List[i]}: "
          f"{str(Unique_Candidate_Percentage)}% "
           f"({str(Unique_Candidate_Votes)})")
    # Looking for the candidate winning the maximum percentage of votes
    # Get the index of the maximum percentage
    Max_index=Percentage_list.index(max(Percentage_list))
    winner=Unique_Candidate_List[Max_index]
    # Print out the winner
    print(f"------------------------\n"
        f"Winner: {winner}\n"
        f"------------------------")