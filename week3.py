from datetime import datetime


def convertData(data):
    convertedValue = (data - 32) * 5 / 9
    return convertedValue


def getInput():
    numberOfEntries = int(input("How many entries are you inputting? "))

    for entry in range(numberOfEntries):
        date = input("Enter a date: ")
        value = float(input("Enter the highest temp for the inputted date: "))

        # Calls convertData, requires the numerical value as an argument, and returns the converted value.
        convertedValue = convertData(value)

        print("The following was saved at", datetime.now(), ":")
        print(f"{date},{value},{convertedValue}")


print("KERKUH7439 Spreadsheet Automation Menu")
print("Choose a number from the following options")

menuOptions = ["Input Data", "View Current Data", "Generate Report"]
validOptions = ["1", "2", "3"]

# menuOption represents each option in the menu list
for menuOption in menuOptions:
    print(menuOptions.index(menuOption) + 1, menuOption)

# The next line retrieves the inputted option and stores into the variable called option.
option = input()

if option in validOptions:
    print("You selected", option, "at", datetime.now())

    if option == "1":
        getInput()
    else:
        print("Error: The chosen functionality is not implemented yet")
else:
    print("Error: Invalid choice selected.")
