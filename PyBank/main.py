import os
import csv

filepath = os.path.join('Input', 'budget_data.csv')

total_months = 0
total_net = 0
change_list = []
greatest_inc = [" ", 0]
greatest_dec = [" ", 999999999]


with open(filepath, 'r') as csvfile:
	reader = csv.reader(csvfile, delimiter = ',')
	header = next(reader)
	first_row = next(reader)

	total_months = 1
	total_net = int(first_row[1])
	current_row_pl = int(first_row[1])

	for row in reader:
		total_months += 1
		total_net += int(row[1])
		net_change = int(row[1]) - current_row_pl
		change_list.append(net_change)
		if (net_change > greatest_inc[1]):
			greatest_inc[0] = row[0]
			greatest_inc[1] = net_change

		if (net_change < greatest_dec[1]):
			greatest_dec[0] = row[0]
			greatest_dec[1] = net_change

		current_row_pl = int(row[1])


average_change = sum(change_list)/len(change_list)

result = (
		f"Financial Analysis \n"
		f"___________________________\n"
		f"\nTotal Months: {total_months} \n"
		f"Net Total Profit/Loss: ${total_net} \n"
		f"Average Change in Profit/Loss : ${round(average_change,2)}\n"
		f"Greatest Increase in Profits: {greatest_inc[0]} (${greatest_inc[1]})\n"
		f"Greatest Decrease in Profits: {greatest_dec[0]} (${greatest_dec[1]})\n")

print(result)

output_path = os.path.join('Output', 'analysis.txt')
with open(output_path, "w") as txt_file:
	txt_file.write(result)





