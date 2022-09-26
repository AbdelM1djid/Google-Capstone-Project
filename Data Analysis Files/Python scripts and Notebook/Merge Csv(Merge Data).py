import pandas as pd 
import os 

Full_Data = pd.DataFrame()

for file in os.listdir(os.getcwd()) : 
	if file.endswith('.csv') : 
		Full_Data = Full_Data.append(pd.read_csv(file))

print("Done Joining ")
Full_Data.to_csv("Full Data.csv",index=False)

print("Done Combining !!!!!!!!!!!!")