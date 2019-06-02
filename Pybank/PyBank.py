import csv
input= "Resources/PyBank.csv"
values=[]
months=[]
t = open("PyBank.txt","w") #create file in write mode.
with open(input ,"r") as f:
	reader = csv.reader(f)
	next(reader, None) #skip the header
	for x in reader:
		months.append(str(x[0]))
		values.append(float(x[1]))
	net_change = [values[i+1] -values[i] for i in range(len(values)-1)]# to find change in corresponding values
	number_of_values = len(net_change)
	print(f"Total months : {len(values)}",file=t) #to count rows so as to find total months
	print(f"Total months : {len(values)}")
	print(f"Total: {sum(values)}",file=t) # to find sum of profit and losses
	print(f"Total: {sum(values)}")
	sum_net_change = sum(net_change)
	avg_change = sum_net_change / number_of_values # finding average change
	print (f"Average Change: {avg_change}", file=t)
	print (f"Average Change: {avg_change}")
	maxnum = max(net_change) # to find greatest increase in profit
	maxpos=net_change.index(maxnum) # to find index of greatest increase in profit
	print(f"Greatest increase in profits:  {months[maxpos+1]} (${(maxnum)})",file=t)
	print(f"Greatest increase in profits:  {months[maxpos+1]} (${(maxnum)})")
	minnum= min(net_change)# to find greatest decrease in profit
	minpos=net_change.index(minnum) # to find index of greatest decrease in profit
	print(f"Greatest decrease in profits :{months[minpos+1]} (${(minnum)})",file=t)
	print(f"Greatest decrease in profits :{months[minpos+1]} (${(minnum)})")
