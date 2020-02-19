import os
import csv
import decimal
from collections import Counter

csvpath = os.path.join('.', 'election_data.csv')
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
      
    # Read the header row first
    csv_header = next(csvreader)
    
    total_votes = 0
    voter_id = []
    candidate = []

    # Read each row of data after the header and extract the columns into separate lists
    for row in csvreader:
        voter_id.append(row[0])
        candidate.append(row[2])
        
    #Calculate the total number of votes
    total_votes = int(len(voter_id))
    
    #Open a text file to write output data to it and the terminal
    file = open("pypoll_analysis.txt","w")
    result1 = """Election Results
----------------------------
Total Votes: """ + str(total_votes) + """
----------------------------"""
    print(result1)
    file.write(result1)
    file.write('\n')
    
    #Determine all the unique candidates and the total vote count for each of them in the data set. Calculate the percentage of votes each candidate won
    candidate_countr = Counter(candidate)
    for i in candidate_countr:
        percent_votes = candidate_countr[i]/total_votes
        loop_result =  str(i) + ": " + str("{:.3%}".format(percent_votes)) + " (" + str(candidate_countr[i]) + ")"
        print(loop_result)
        file.writelines(loop_result)
        file.write('\n')
        
    #Determine the candidate with the most number of votes.
    winner = candidate_countr.most_common(1)[0][0]
    result2 = """----------------------------
Winner: """ + str(winner) + """
----------------------------"""
    print(result2)
    file.write(result2)
    file.close()
