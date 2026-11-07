from datetime import datetime
import os


# This function converts Fahrenheit temperatures to Celsius.
def convertData(data):
    convertedValue = (data - 32) * 5 / 9
    return convertedValue


# This function inserts comma-separated data into a CSV file.
def insertData(filePath, data):
    try:
        with open(filePath, "a") as file:
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


# Sets the file path for ZooData.csv.
filePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ZooData.csv")


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
    else:
        print("Error: The chosen functionality is not implemented yet")
else:
    print("Error: Invalid choice selected.")
