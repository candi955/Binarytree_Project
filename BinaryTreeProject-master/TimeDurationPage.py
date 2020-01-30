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




# Creating a variable for data being pulled from the TimeDurationComparison.xlsx file and placed into array format
book = xlrd.open_workbook('TimeDurationComparison.xlsx')
sheets = book.sheets()
for sheet in sheets:
    data = np.array([[sheet.cell_value(r, c) for c in range(sheet.ncols)] for r in range(sheet.nrows)])

# Creating a variable for data to be transformed into excel file format
timeduration_df = pd.read_excel(book, index_col=None,
                                na_values=['NA'])

class Regression():
    def _showTable_(self):

        # Showing the data that was pulled from TimeDurationComparison.xlsx in array form
        print("\n\nData pulled from the excel file:\n\n", data, "\n\n")

        # Obtaining the shape of the data
        print("Data shape: ", data.shape, "\n\n")
        # Data shape:  (9, 4)

        # Showing the data that was pulled from TimeDurationComparison.xlsx in excel form
        print("Data put into excel format:\n\n", timeduration_df, "\n\n")

    def _showPlot_(self):

        # Attempting to create a table and plot chart of the dataframe TimeDurationComparison.xlsx
        # using iloc (row and column slicing) for python, references:
        # https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
        # https://datacarpentry.org/python-ecology-lesson/03-index-slice-subset/
        # Rows 0-7 (0:8), and columns 1-3 (to take out column 0, shows as 1:4 in iloc) to show the main data in the
        # dataframe
        data = timeduration_df.iloc[0:8, 1:4]
        print("------- Splitting the dataframe into sections -------\n\nThe data of the dataframe:\n\n", data, "\n")

        # This is the iloc to show the entire first column, the row labels, of the dataframe, for the label column
        rowLabels_ForData = timeduration_df.iloc[:, 0]
        print("The column of the dataframe:\n\n", rowLabels_ForData, "\n")

        # This is to pull the top label for the data only, with the variable data.head calling the pandas function
        # head, with the index 0.  You can change the index to show more rows.
        columnLabels = data.head(0)
        print("Showing the header labels only:\n\n", columnLabels, "\n\n")

        # Creating values for the graph
        # Creating the values variable as increments 0.125 apart, between 0 and 1.625, so that the top level value
        # shows as 1.5
        # using np.arange(bottom level #, just above top level #, increment)
        # reference: https://appdividend.com/2019/01/31/numpy-arange-tutorial-with-example-python-numpy-functions/
        values = np.arange(0, 1.625, 0.125)
        print('\n\n', values)
        valueIncrement = 0.125

        fig, ax = plt.subplots()
        ax.plot(columnLabels, data, labels=('This is the Label'))

        ax.legend()
        plt.show()


Regression()

show = Regression()

# Calling methods
show._showTable_()
show._showPlot_()