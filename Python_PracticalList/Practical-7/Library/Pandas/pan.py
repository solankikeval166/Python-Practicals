import pandas as pd
import matplotlib.pyplot as plt

data = {"calories": [420, 380, 390], "duration": [50, 40, 45]}

# load data into a DataFrame object:
df = pd.DataFrame(data)

print(df, end="\n\n")

# reading csv file
data = pd.read_csv(
    "D:\Sem 4\Python\Python_PracticalList\Practical-7\Library\Pandas\data.csv"
)
print(data,end='\n\n')

data2 = {"year": [2001, 2002, 2003, 2004], "student": [50, 75, 80, 100]}
data2 = pd.DataFrame(data2)
print(data2,end="\n\n")

