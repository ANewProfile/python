import pandas as pd
import matplotlib.pyplot as plt


names = ['Theo', 'Billy', 'Bob', 'Joe', 'William']
ages = [9, 23, 38, 30, 9]
name_table = pd.DataFrame({'Names': names, 'Age': ages})
# city_table.columns = cities2
# city_table.rows = populations
print(name_table)
name_table.plot()

#HOMEWORK:
#Install Seaborn
#Use this link to research problem: https://www.jetbrains.com/help/pycharm/configuring-local-python-interpreters.html