import pandas as pd
import numpy as np

file = pd.read_excel(r"C:\Users\ifladmin\Desktop\Python Class\Mini_Project\Facilitator Updates.xlsx")

columns = [
    "S_No",
    "Date",
    "Year",
    "PR_No",
    "Client",
    "Client_Location",
    "Department",
    "Project_Title",
    "Workshop_Status",
    "Study",
    "Facilitator",
    "Scribe",
    "Session_Date",
    "WO_Number",
    "Amount",
    "Unused",
    "Payment_Status"
]

file.columns = columns
file = file.iloc[2:].copy()

project_columns = [
    "S_No",
    "Date",
    "Year",
    "PR_No",
    "Client",
    "Client_Location",
    "Department",
    "Project_Title"
]



file[project_columns] = file[project_columns].ffill()

print(file["Workshop_Status"].value_counts())