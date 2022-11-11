import matplotlib.pyplot as plt
import pandas as pd

#creat new data frame with data from the file
data = pd.read_csv('rubiksdata.csv', index_col = 0)
# print(data)
sorted_data = data.sort_values(by=["Time"], ascending=True)
print(sorted_data)

#.head() shows top rows in data
# data.plot()
plt.title('Speedcuber Times Graph 3x3 and 4x4')
# plt.show()