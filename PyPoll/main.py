import os
import csv

# total_votes will count the total number of votes
total_votes = 0

# candidate_list is a dictionary to store name of candidate as key 
# and votes candidate won as value
candidate_list = {}


# Reading csv file using DictReader
filepath = os.path.join('Input', 'election_data.csv')
with open(filepath, 'r') as csvfile:
	reader = csv.DictReader(csvfile)
	
	for row in reader:
		
		total_votes += 1
		
		# if candidate name not in candidate_list dictionary,
		# add candidate name as key and set value = 1
		if row['Candidate'] not in candidate_list:
			candidate_list[row['Candidate']] = 1
		# else if candidate name is there as key in dictionary,
		# increment the value by 1
		else:
			candidate_list[row['Candidate']] += 1

# max_votes stores the maximum votes received by any candidate
max_votes = 0
winner = " "

# voter_count is a string to display the candidate name along 
# with his vote result
voting_result = ""

for candidate, votes in candidate_list.items():
	if votes > max_votes:
		max_votes = votes
		winner = candidate

	percent_votes = (float(votes)/ float(total_votes) * 100)

	# Changing value of candidate_list dictionary
	
	# For candidate name as key, value is a dictionary with win votes and 
	# percent of votes 
	
	candidate_list[candidate] = {"votes" : votes, "win_percent" : percent_votes}
	
	voting_result += (
		f"{candidate}: {candidate_list[candidate]['win_percent']:.3f}% "
		f"({candidate_list[candidate]['votes']})\n")


result = (
		f"\nElection Results\n"
		f"-------------------------\n"
		f"Total Votes: {total_votes}\n"
		f"-------------------------\n"
		f"{voting_result}"
		f"-------------------------\n"
		f"Winner: {winner}\n"
		f"-------------------------\n")


print(result)

# Exporting result to a text file
output_path = os.path.join('Output', 'election_result.txt')
with open(output_path, "w") as txt_file:
	txt_file.write(result)  

