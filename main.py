import matplotlib.pyplot as plt
import pandas as pd
import time
import os

"""Visual representation for the 3N+1 problem"""

start_time = time.time()  # Runtime variable
START = 1  # Start number
END = 1000  # End number
permanent_dict = {}  # Dictionary for the pandas, and xlsx file
temporary_list = []  # Stores the current steps

# Makes the frame of the plot
plt.figure(figsize=(20, 20))
plt.title(f"3N+1 graphs from {START} to {END}", fontsize=40)
plt.xlabel(f"Step number", fontsize=24)
plt.ylabel("Value of the number", fontsize=24)
plt.grid()

for i in range(START, END+1):
    n = i
    while True:  # Loop for each numbers until it reaches 1
        temporary_list.append(n)
        if n == 1:
            break
        if n % 2 == 0:
            n = int(n/2)
        else:
            n = 3*n+1

    permanent_dict[i] = temporary_list

    plt.plot(temporary_list, linewidth=0.1)  # Makes the plot with each number
    temporary_list = []

data = pd.DataFrame.from_dict(permanent_dict, orient="index")  # Dataframe to create excel from it
data.to_excel("Data.xlsx")  # Excel with each number and its steps
plt.savefig("3n+1.pdf")  # Creates a PDF from the plot
os.startfile("3n+1.pdf")  # Opens the created PDF file
os.startfile("Data.xlsx")  # Opens the created Excel file

print(f"Runtime: {time.time() - start_time}")  # Gives the needed runtime
