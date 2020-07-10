import pandas as pd
import matplotlib.pyplot as plt
import numpy as nd
from pandas import DataFrame

df = DataFrame({'Chips': ['Simba', 'Lays', 0],
                'Cooldrink': ['Coke', 'Fanta', 0],
                'Chocolates': ['Cadbury', 'Tex', 0],
                'Pies': ['Pepper steak', 'Chicken', 0],
                'Fruit': ['Pear', 'Apple', 'Orange'],
                'Cupcakes': ['vanilla', 'chocolate', 0],
                'Veggies': ['Spinach', 'cabbage', 0]})

the_table = plt.table(cellText=table_vals,
                      colWidths=[0.5]*len(col_labels),
                      rowLabels=row_labels, colLabels=col_labels,
                      cellLoc='center', rowLoc='center')

plt.show()
