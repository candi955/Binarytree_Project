# Time Duration Page

# Comparing time durations of the BST functions insertion and deletion using the binarytree python library in chart
# form.  These numbers will be compared to similar numbers with previous projects concerning arrays and linked lists.
# The time durations of a hundred, thousand, ten-thousand, and hundred-thousand random numbers will be compared.

# references:
# https://matplotlib.org/api/table_api.html?highlight=table#module-matplotlib.table
# https://matplotlib.org/gallery/index.html
# https://matplotlib.org/gallery/misc/table_demo.html#sphx-glr-gallery-misc-table-demo-py

import numpy as np
import xlrd
import pandas as pd
import matplotlib.pyplot as plt
#from numpy.polynomial.polynomial import polyfit
#import statsmodels.api as sm
#import tensorflow as tf

# Creating a variable for data being pulled from the TimeDurationComparison.xlsx file and placed into array format
book = xlrd.open_workbook('TimeDurationComparison.xlsx')
sheets = book.sheets()
for sheet in sheets:
    data = np.array([[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])

# Creating a variable for data to be transformed into excel file format
timeduration_df = pd.read_excel(book, index_col=None,
                                na_values=['NA'])

class Regression():
    def _duration_(self):

        # Showing the data that was pulled from TimeDurationComparison.xlsx in array form
        print("Data pulled from the excel file:\n\n", data, "\n")

        # Obtaining the shape of the data
        print("Data shape: ", data.shape, "\n")
        # Data shape:  (9, 4)

        # Showing the data that was pulled from TimeDurationComparison.xlsx in excel form
        print("Data put into excel format:\n\n", timeduration_df, "\n")

    def _tableAndPlot_(self):
        pass
        # Attempting to create a table and plot chart of the dataframe TimeDurationComparison.xlsx
        #data =


Regression()

show = Regression()

# Calling methods
show._duration_()