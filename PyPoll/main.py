# importing necessary modules
import os
import csv

# declaring necessary lists
total_votes = []
charles_casper_stockham = []
diana_degette = []
raymon_anthony_doane = []

# recieving file path
file_path = os.path.join("PyPoll","Recources","election_data.csv")

# opening and reading file
with open(file_path) as election_data:
    csvreader = csv.reader(election_data, delimiter=",")

    # header
    header = next(csvreader)

    # looping through the rows
    for row in csvreader:
        total_votes.append(row)
        if row[2] == "Charles Casper Stockham":
            charles_casper_stockham.append(row)
        if row[2] == "Diana DeGette":
            diana_degette.append(row)
        if row[2] == "Raymon Anthony Doane":
            raymon_anthony_doane.append(row)

    # printing analysis header
    print("Election Results")
    print("-------------------------")

    # printing total number of votes
    print(f'Total Votes: {len(total_votes)}')
    print("-------------------------")

    # charles casper stockham total votes, and vote percentage
    charles_vote_percentage = format((len(charles_casper_stockham)/len(total_votes)), ".3%")
    print(f'Charles Casper Stocham: {charles_vote_percentage} ({len(charles_casper_stockham)})')

    # Diana DeGette total votes, and vote percentage
    diana_vote_percentage = format((len(diana_degette)/len(total_votes)), ".3%")
    print(f'Diana DeGette: {diana_vote_percentage} ({len(diana_degette)})')

    # Raymon Anthony Doane total votes, and vote percentage
    raymon_vote_percentage = format((len(raymon_anthony_doane)/len(total_votes)), ".3%")
    print(f'Raymon Anthony Doane: {raymon_vote_percentage} ({len(raymon_anthony_doane)})')
    print("-------------------------")

    # winner
    if len(diana_degette) > len(raymon_anthony_doane) and len(charles_casper_stockham):
        print("Winner: Diana DeGette")
    elif len(raymon_anthony_doane) > len(diana_degette) and len(charles_casper_stockham):
        print("Winner: Raymon Anthony Doane")
    elif len(charles_casper_stockham) > len(diana_degette) and len(raymon_anthony_doane):
        print("Winner: Charles Casper Stockam")

    print("-------------------------")

# recieving path for output
output_path = os.path.join("PyPoll","Analysis","PyPoll_analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as csvfile:
        
        # Initialize csv.writer
        csvwriter = csv.writer(csvfile, delimiter=',')

        csvwriter.writerow(['Election Results'])
        
        csvwriter.writerow(['-------------------------'])

        csvwriter.writerow([f'Total Votes: {len(total_votes)}'])
        
        csvwriter.writerow(["-------------------------"])

        csvwriter.writerow([f'Charles Casper Stocham: {charles_vote_percentage} ({len(charles_casper_stockham)})'])

        csvwriter.writerow([f'Diana DeGette: {diana_vote_percentage} ({len(diana_degette)})'])

        csvwriter.writerow([f'Raymon Anthony Doane: {raymon_vote_percentage} ({len(raymon_anthony_doane)})'])
        
        csvwriter.writerow(['-------------------------'])

        csvwriter.writerow(['Winner: Diana DeGette'])
        
        csvwriter.writerow(['-------------------------'])