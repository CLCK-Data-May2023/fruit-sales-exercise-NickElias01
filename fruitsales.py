#Fetch library
import pandas as pd

#Create dataframe
Fruit_Sales = pd.DataFrame({"Apples":[35,41], "Bananas":[21,34]}, index =  ["2017 Sales","2018 Sales"])

#Create csv file
Fruit_Sales.to_csv("fruit.csv")

print(Fruit_Sales)