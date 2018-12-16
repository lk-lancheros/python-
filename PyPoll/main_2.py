import os
import csv

election_csv_path = os.path.join("..","resources", "election_data.csv")
file_to_output = "PyPoll_output.txt"

Total_Votes = 0
Summary_Cand_list = []
Summary_Votes_by_Cand = {}
winning_candidate = ""
winning_count = 0

# Open and read csv
with open(election_csv_path, newline="") as election_csvfile:
    electionreader = csv.reader(election_csvfile, delimiter=",")

    # Read the header row first 
    csv_header = next(electionreader)
    
    #loop through csv data where 1 row = 1 vote
    for row in electionreader:
        #create counter for all votes equal to number of rows minus header
        Total_Votes= Total_Votes+1
        #bring in the third column of data, candidate name in a list called U_voted_this_name
        U_voted_this_name = row[2]
    
        #if the candidate name in this row is NOT on my summary list of cand add
        if U_voted_this_name not in Summary_Cand_list:
            Summary_Cand_list.append(U_voted_this_name)
            #Fill a new dictionary with unique candidate name and count it as a vote
            Summary_Votes_by_Cand[U_voted_this_name]=0
          
        #Summary_Votes_by_Cand
        Summary_Votes_by_Cand[U_voted_this_name]=Summary_Votes_by_Cand[U_voted_this_name]+1

#start to print
with open(file_to_output, "w") as txt_file:

    election_results = (
        f"\n\nElection results\n"
        f"-----------------------------\n"
        f"Total votes: {Total_Votes}\n"
        f"-----------------------------\n") 

    print (election_results, end="")
    txt_file.write(election_results)

    # Determine the winner by looping through the counts

    for candidate in Summary_Votes_by_Cand:
    # Retrieve vote count and percentage
        votes = Summary_Votes_by_Cand.get(candidate)
        vote_percentage = (float(votes) / float(Total_Votes) * 100)

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
        
        # print the results
        voter_output = f"{candidate}: {vote_percentage:.1f}% ({votes})\n"
        print(voter_output, end="")
        txt_file.write(voter_output)

    winner = (
        f"-----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-----------------------------\n") 

    print(winner)

    txt_file.write(winner)
