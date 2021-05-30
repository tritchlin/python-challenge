# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
# You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:

# As an example, your analysis should look similar to the one below:
# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan
# -------------------------
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# load dependencies
import os
import csv
from types import DynamicClassAttribute

csvpath = os.path.join(".","Resources","election_data.csv")

# set variables
votecount = 0
candidates = dict()

# open CSV, remove headers
with open(csvpath, 'r') as csvfile:
    polling = csv.reader(csvfile)

    csv_header = next(polling)
    # print(csv_header)

    # start for loop
    for row in polling:
        voterID = (row[0])
        county = (row[1])
        candidate = (row[2])
        votecount = votecount + 1

        # identify unique candidates and append to list
        if candidate not in candidates:
            candidates[candidate] = 0

        # Keep running count of votes per candidate
        candidates[candidate] = candidates[candidate] + 1

# Combine data for each candidate, and prep format for summary
def candidate_stats():
    stats = []
    array = "\n"
    for key in candidates:
        ratio = format((candidates[key]/votecount * 100),".2f")
        # print(f'{key}: {ratio}% ({candidates[key]})')
        stats.append(f'{key}: {ratio}% ({candidates[key]})')
    array = array.join(stats)
    return array

winner = max(candidates, key=candidates.get)

# Create and output full summary with formatting
message = f"""
Election Results
-------------------------
Total Votes: {votecount}
-------------------------
{candidate_stats()}
-------------------------
Winner: {winner}
-------------------------
"""
print(message)

# Create and write summary to text file in Analysis folder
output_path = os.path.join("Analysis","output.txt")

f = open(output_path,"w")
f.write(message)
f.close()
