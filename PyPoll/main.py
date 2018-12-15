import os
import csv

election_csv_path = os.path.join("..","resources", "election_data.csv")

# Open and read csv
with open(election_csv_path, newline="") as election_csvfile:
    electionreader = csv.reader(election_csvfile, delimiter=",")

    # Read the header row first 
    csv_header = next(election_csvfile)
    print(f"Header: {csv_header}")

    Total_Votes = 0
    Candidate_list = []
    Candidate_votes = {}
    #use dictionary
    
    for row in electionreader:
        Total_Votes= Total_Votes+1
        Candidate_name= row[2]
        if Candidate_name not in Candidate_list:
            Candidate_list.append(Candidate_name)
            Candidate_votes[Candidate_name]=0
        Candidate_votes[Candidate_name]=Candidate_votes[Candidate_name]+1
    
    Candidate_votes.values()
    
    
    #winner_vote = max(Candidate_votes{1})
    
    #print(Candidate_votes)

    #print(Candidate_list)

    #candidates_count
    
    #percentage_votes = (candidates_count/total_votes)*100
    # percentage_votes

    # winner = candidates_count.idxmax()
    # winner

# # print the results
# print("Election results")

# print("--------------------------------------------------------------------------")

# print("Total votes: " + str(total_votes))

# print("----------------------------------------------------------------------------")

# print("Khan:" + " " + str(round(percentage_votes[0],3)) + "%" + "("+str(candidates_count[0])+")")
      
# print("Correy:" + " " + str(round(percentage_votes[1],3)) + "%" + "("+str(candidates_count[1])+")")
      
# print("Li:" + " " + str(round(percentage_votes[2],3)) + "%" + "("+str(candidates_count[2])+")")
      
# print("O'Tooley:" + " " + str(round(percentage_votes[3],3)) + "%" + "("+str(candidates_count[3])+")")

# print("----------------------------------------------------------------------------------------")
      
# print("winner: " + winner)
