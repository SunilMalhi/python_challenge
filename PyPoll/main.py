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
    TotalProfit = 0
    TotalChangeProfit = 0
    InitialProfit = 0
    MonthChange = []
    Date = []

    for row in csvreader:
      #Count how many rows there are for the number of months
      Count = Count + 1
      
      #So greatest increase and decrease date can be located
      Date.append(row[0])
      
      #Calulate Profit
      TotalProfit = TotalProfit + int(row[1])
      
      #Calculate monthly change
      OverallProfit = int(row[1])
      MonthChangeProfit = OverallProfit - InitialProfit
      
      #Place into list
      MonthChange.append(MonthChangeProfit)
      
      #Calculate overall profit
      TotalChangeProfit = TotalChangeProfit + MonthChangeProfit
      InitialProfit = OverallProfit
      
      #Calculate average
      AverageChangeProfit = (TotalChangeProfit/Count)
      
      #Get greatest increase
      Increase = max(MonthChange)
      IncreaseMonth = Date[MonthChange.index(Increase)]

      print(f'Greatest Increase in Profits: {IncreaseMonth} ({Increase})')
      
      #Get greatest descrease
      Decrease = min(MonthChange)
      DecreaseMonth = Date[MonthChange.index(Decrease)]

      print(f'Greatest Decrease in Profits: {DecreaseMonth} ({Decrease})')
      
      #Set path for file to be written
      financial_analysis = os.path.join('analysis', 'financial_analysis.txt')
      
      with open(financial_analysis, 'w') as text:
            text.write(f"Financial Analysis\n"
                       f"---------------------\n"
                       f"Total Month : {Count}\n"
                       f"Total: ${TotalProfit}\n"
                       f"Average Change: ${AverageChangeProfit:.2f}\n"
                       f"Greatest Increase in Profits: {IncreaseMonth} (${Increase})\n"
                       f"Greatest Decrease in Profits: {DecreaseMonth} (${Decrease})\n")