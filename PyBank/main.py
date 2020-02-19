import os
import csv

csvpath = os.path.join('.', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
      
    # Read the header row first
    csv_header = next(csvreader)
    
    total_amount = 0
    total_months = 0
    total_change = 0
    average_change = 0
    profit_loss = []
    months = []
    profit_loss_change = []
     
    # Read each row of data after the header and extract all the columns into separate lists
    for row in csvreader:
        months.append(row[0])
        profit_loss.append(row[1])
    
    #Calculate the total number of months included in the dataset
    total_months = int(len(months))
    
    #Loop thru the items in the list, calcuate the changes between the list items and create a new list with changes
    for item in range(0,len(profit_loss)):
        current_elem = int(profit_loss[item])
        next_item = int(item) + 1
        
        # Check if the end of the list is reached, if not..
        if (next_item < total_months):
            next_elem = int(profit_loss[next_item])
            change = next_elem - current_elem
            profit_loss_change.append(change)
            
        #Calculate the net total amount of "Profit/Losses" over the entire period
        total_amount = total_amount + int(profit_loss[item]) 
        
    #Calculate the greatest increase and decrease in the Profit/Loss changes
    great_increase = int(max(profit_loss_change))
    great_decrease = int(min(profit_loss_change))
    
    #Loop thru the newly created changes list and calculate the average of the changes in "Profit/Losses" over the entire period
    for item in range(0,len(profit_loss_change)):
        current_change = int(profit_loss_change[item])
        if (current_change == great_increase):
            increase_index = item
        elif (current_change == great_decrease):
            decrease_index = item
        total_change = total_change + int(profit_loss_change[item])
    average_change = total_change / int(len(profit_loss_change))
    average_change = round(average_change,2)
    
    #Loop thru the months list and determing the months in which the  greatest increase and decrease of Profit/Losses occured
    for item in range(0, total_months): 
        great_inc_month = months[increase_index + 1]
        great_dec_month = months[decrease_index + 1]
        
    #Open a text file to write output data to it and the terminal 
    file = open("pybank_analysis.txt","w")
    output_data = """ Financial Analysis
----------------------------------------"""
    print(output_data)   
    file.write(output_data) 
    file.write('\n')
    t_month= "Total Months: " + str(total_months)
    print(t_month)
    file.write(t_month) 
    file.write('\n')
    t_amount = "Total: $" + str(total_amount)
    print(t_amount)
    file.write(t_amount) 
    file.write('\n')
    a_change = "Average Change: $" + str(average_change)
    print(a_change)
    file.write(a_change) 
    file.write('\n')
    g_inc_month = "Greatest Increase In Profits: " + str(great_inc_month) + " ($" + str(great_increase) + ")"
    print(g_inc_month)
    file.write(g_inc_month) 
    file.write('\n')
    g_dec_month = "Greatest Decrease In Profits: " + str(great_dec_month) + " ($" + str(great_decrease) + ")"
    print(g_dec_month)
    file.write(g_dec_month)
    #Close the text file
    file.close()