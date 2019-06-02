import csv
input= "Resources/PyPoll.csv"
votes=[]
candidates={}
t = open("PyPoll.txt","w") #create file in write mode.
with open(input ,"r") as f:
	reader = csv.reader(f)
	next(reader, None) #skip the header
	for x in reader:
		votes.append(int(x[0]))
		if x[2] in candidates: ### If existing candidate increment vote count
			candidates[x[2]]+=1
		else:
			### If the new candidate - add candidate Name and 1 vote to the candidate
			candidates[x[2]]=1
		
n=len(votes)
print(f"Total Votes: {n}",file=t)
print(f"Total Votes: {n}")
for k in candidates.keys():
	m=candidates.get(k)
	p=float("%0.3f" % ((m/n)*100))
	print(f"{k} {p}% ({m})",file=t)
	print(f"{k} {p}% ({m})")
print(f"The winner:{max(candidates, key=candidates.get)}",file=t)
print(f"The winner:{max(candidates, key=candidates.get)}")
t.close() #closing file object.
