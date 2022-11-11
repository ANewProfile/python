import matplotlib.pyplot as plt
import pandas as pd

#creat new data frame with data from the file
data = pd.read_csv('rubiksdata.csv', index_col = 0)

d1 = pd.DataFrame(
    {
        'Name':['Feliks', 'Max', 'Rowe', 'Katie'],
        'Time':[5.53,5.59,7.63,6]
    }
)
# print(d1)
d1.sort_values(by='Time',ascending=True)
print(d1)