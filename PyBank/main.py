# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
previous_profit = None
changes = []
dates = []
# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)


    # Process each row of data
    for row in reader:
        date = row[0]
        profit = int(row[1])


        # Track the total
        total_months += 1
        total_net += profit
        

        # Track the net change
        if previous_profit is not None:
            change = profit - previous_profit
            changes.append(change)
            dates.append(date)

        previous_profit = profit
        # Calculate the greatest increase in profits (month and amount)
greatest_increase = max(changes) if changes else 0
greatest_increase_date = dates[changes.index(greatest_increase)] if changes else "N/A"


        # Calculate the greatest decrease in losses (month and amount)
greatest_decrease = min(changes) if changes else 0
greatest_decrease_date = dates[changes.index(greatest_decrease)] if changes else "N/A"


# Calculate the average net change across the months
average_change = sum(changes) / len(changes) if changes else 0 


# Generate the output summary
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"

)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
