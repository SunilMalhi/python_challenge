#import packages
import os
import csv

#set path
election_data_csv = os.path.join('Resources', 'election_data.csv')

#Open csvfile
with open(election_data_csv, 'r') as csvfile:
          
    csvreader = csv.reader(csvfile, delimiter = ',')
          
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

      #Set Variables
    Count = 0
    Vote = []
    Percent = []
    TotalCandidate = []
    Candidate = []

    for row in csvreader:
    
      Count = Count + 1
        
      TotalCandidate.append(row[2])

    for name in set(TotalCandidate):
      Candidate.append(name)

      TotalVoteCandidate = TotalCandidate.count(name)
      Vote.append(TotalVoteCandidate)

      TotalVotePercent = (TotalVoteCandidate/Count)*100
      Percent.append(TotalVotePercent)

      WinningCount = max(Vote)
      WinningCandidate = TotalCandidate[Vote.index(WinningCount)]
    
    election_results = os.path.join('analysis', 'election_results.txt')
      
    with open(election_results, 'w') as text:
            text.write(f"Financial Analysis\n"
                       f"---------------------\n"
                       f"Total Votes : {Count}\n"
                       f"---------------------\n"
                       f"{Candidate} {Percent} {Vote} \n"
                       f"---------------------\n"
                       f"Winner: {WinningCandidate}\n")