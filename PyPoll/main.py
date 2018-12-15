import os
import csv

election_csv_path = os.path.join("..","resources", "election_data.csv")

# Open and read csv
with open(election_csv_path, newline="") as election_csvfile:
    electionreader = csv.reader(election_csvfile, delimiter=",")

    # Read the header row first 
    csv_header = next(election_csvfile)
    
    Total_Votes = 0
    Candidate_name =[]
    Candidate_list = []
    Candidate_votes = {}
    winning_candidate = ""
    winning_count = 0
    
    #loop through csv data where 1 row = 1 vote
    for row in electionreader:
        #create counter for all votes equal to number of rows minus header
        Total_Votes= Total_Votes+1
        #bring in the third column of data, candidate name in a list called candidate list
        Candidate_name = row[2]
    
    #     #if the candidate name in this row is NOT on my new list called candidate list add it
        if Candidate_name not in Candidate_list:
            Candidate_list.append(Candidate_name)
            
            #Create a dictionary with four rows of data - candidate name and total votes
            Candidate_votes[Candidate_name]=0
        Candidate_votes[Candidate_name]=Candidate_votes[Candidate_name]+1

# print the results
print("Election results")
print("--------------------------------------------------------------------------")
print("Total votes: " + str(Total_Votes))
print("----------------------------------------------------------------------------") 

# Determine the winner by looping through the counts
    for candidate in Candidate_votes:

        # Retrieve vote count and percentage
        votes = Candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(Total_Votes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
        # Print each candidate's voter count and percentage (to terminal)
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

print("----------------------------------------------------------------------------------------")
      
print("Winner:" + winning_candidate)
