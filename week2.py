from datetime import datetime

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
else:
    print("Error: Invalid choice selected.")
