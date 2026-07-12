import pandas as pd

def report(query, records, output):
	a = pd.DataFrame(query)
	a.to_csv(output + "/query.csv")
	summary = a["Error"].value_counts()
	print(summary)
	print(a["Error"].value_counts()[:5])
	print(round(len(a) / records * 100, 2))