import os
import csv
import numpy

budget_csv = os.path.join("../PyPoll", "election_data.csv")
poll_txt = os.path.join("../PyPoll","poll_txt.txt")
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")
    csv_header = next(csvfile)

    data = list(csvreader)
    print('Election Results')
    print('---------------------------------')

    #Total Votes 
    totalVotes = len(data)
    print(f'Total Votes: {totalVotes}')
    print('---------------------------------')
       
    names = []

    for row in data:
        names.append(row[2])

    candidates = list(set(names))
 
    tallyVotes = []
    for candidate in candidates:
        candidateCount = sum(x.count(candidate) for x in data)
        candidatePercent = round(candidateCount/totalVotes,3)
        print(f'{candidate}: {"{:.3%}".format(candidatePercent)} ({candidateCount})')
        tallyVotes.append(candidateCount)

    print('---------------------------------')
    
    candidateDict = {}
    for key in candidates:
        for value in tallyVotes:
            candidateDict[key] = value
            tallyVotes.remove(value)
            break

    #Winner         
    winner = max(candidateDict, key=candidateDict.get)
    print(f'Winner: {winner}')

    with open(poll_txt, "a") as text:
        text.write(
        f'Election Results\n'
        f'---------------------------------\n'
        f'Total Votes: {totalVotes}\n'
        f'---------------------------------\n'
        )

        for candidate in candidates:
            text.write(f'{candidate}: {"{:.3%}".format(candidatePercent)} ({candidateCount})\n')

        text.write(
            f'---------------------------------\n'
            f'Winner: {winner}'
        )
    



