
from datetime import datetime
import os
import csv
from openpyxl import Workbook
from openpyxl.chart import BarChart, LineChart, Reference


# This function converts Fahrenheit temperatures to Celsius.
def convertData(data):
    convertedValue = (data - 32) * 5 / 9
    return convertedValue


# This function inserts comma-separated data into a CSV file.
def insertData(filePath, data):
    try:
        with open(filePath, "a", newline="") as file:
            file.write(data + "\n")
        return True
    except Exception as error:
        print("Error: Unable to save data.", error)
        return False


# This function displays the file path and contents of a CSV file.
def viewData(filePath):
    try:
        with open(filePath, "r") as file:
            print("The file", filePath)
            print(file.read())
    except Exception as error:
        print("Error: Unable to read file.", error)


# This function collects user input, converts data, and saves it to a CSV file.
def getInput():
    numberOfEntries = int(input("How many entries are you inputting? "))

    for entry in range(numberOfEntries):
        date = input("Enter a date: ")
        value = int(input("Enter the highest temp for the inputted date: "))

        # Calls convertData to convert Fahrenheit to Celsius.
        convertedValue = convertData(value)

        # Creates the comma-separated string to save.
        data = f"{date},{value},{convertedValue}"

        # Attempts to save each entry to the CSV file.
        try:
            if insertData(filePath, data):
                print("The following data was saved at", datetime.now(), ":")
                print(data)
        except Exception as error:
            print("Error: Unable to insert data.", error)


# This function accepts a CSV file path (str) and chart type (str).
# It creates an Excel spreadsheet with a chart and returns nothing.
def createChart(filePath, chartType):
    print("Choose the data source for your chart:")
    print("1 Fahrenheit")
    print("2 Celsius")

    dataChoice = input("Enter your choice: ")

    if dataChoice not in ["1", "2"]:
        print("Error: Invalid data source selected.")
        return

    try:
        # Creates a new Excel workbook and worksheet.
        workbook = Workbook()
        worksheet = workbook.active
        worksheet.title = "Temperature Data"

        # Adds column headings to the spreadsheet.
        worksheet.append(["Date", "Fahrenheit", "Celsius"])

        # Opens the CSV file and reads the saved data.
        with open(filePath, "r", newline="") as file:
            csvData = csv.reader(file)

            for row in csvData:
                if len(row) == 3:
                    date = row[0]
                    fahrenheit = float(row[1])
                    celsius = float(row[2])

                    worksheet.append([date, fahrenheit, celsius])

        if worksheet.max_row == 1:
            print("Error: No data available to create a chart.")
            return

        # Determines which data column to use.
        if dataChoice == "1":
            dataColumn = 2
            yAxisLabel = "Temperature (Fahrenheit)"
        else:
            dataColumn = 3
            yAxisLabel = "Temperature (Celsius)"

        # Creates the selected chart type.
        if chartType == "bar":
            chart = BarChart()
        else:
            chart = LineChart()

        # Adds the student ID and current date as the chart title.
        currentDate = datetime.now().strftime("%m/%d/%Y")
        chart.title = "KERKUH7439 " + currentDate

        # Labels the x-axis and y-axis.
        chart.x_axis.title = "Date"
        chart.y_axis.title = yAxisLabel

        # Selects the temperature values and date labels.
        dataValues = Reference(
            worksheet,
            min_col=dataColumn,
            min_row=1,
            max_row=worksheet.max_row
        )

        dateLabels = Reference(
            worksheet,
            min_col=1,
            min_row=2,
            max_row=worksheet.max_row
        )

        chart.add_data(dataValues, titles_from_data=True)
        chart.set_categories(dateLabels)

        # Adds the chart to the Excel worksheet.
        worksheet.add_chart(chart, "E2")

        # Saves the Excel file in the project folder.
        reportPath = os.path.join(
            os.path.dirname(filePath), "final.xlsx"
        )

        workbook.save(reportPath)

        print("Report successfully generated!")
        print("Excel file saved at:", reportPath)

    except Exception as error:
        print("Error: Unable to create chart.", error)


# This function accepts a CSV file path (str) and returns nothing.
# It asks for a chart type and calls createChart with two string arguments.
def generateReport(filePath):
    print("Choose the type of chart you would like to create:")
    print("1 Line Chart")
    print("2 Bar Chart")

    chartChoice = input("Enter your choice: ")

    if chartChoice == "1":
        createChart(filePath, "line")
    elif chartChoice == "2":
        createChart(filePath, "bar")
    else:
        print("Error: Invalid chart type selected.")


# Sets the file path for ZooData.csv.
filePath = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "ZooData.csv"
)


# Displays the Spreadsheet Automation Menu.
print("KERKUH7439 Spreadsheet Automation Menu")
print("Choose a number from the following options")

menuOptions = ["Input Data", "View Current Data", "Generate Report"]
validOptions = ["1", "2", "3"]

# Loops through the menu options and displays each one.
for menuOption in menuOptions:
    print(menuOptions.index(menuOption) + 1, menuOption)

# Retrieves the user's menu selection.
option = input()

if option in validOptions:
    print("You selected", option, "at", datetime.now())

    if option == "1":
        getInput()
    elif option == "2":
        viewData(filePath)
    elif option == "3":
        generateReport(filePath)
else:
    print("Error: Invalid choice selected.")
