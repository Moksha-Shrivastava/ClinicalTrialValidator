import pandas as pd

def report(query, records, output): #generates a csv file listing all the queries 
	a = pd.DataFrame(query)
	a.to_csv(output + "/query.csv")
	summary = a["Error"].value_counts()
	print(summary)
	print(a["Error"].value_counts()[:5])
	print(round(len(a) / records * 100, 2))
