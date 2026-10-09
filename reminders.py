import os

clear = lambda: os.system('clear')

applicationActive = True;
reminders = []
completedReminders = []

GREEN = "\033[32m"
RESET = "\033[0m"

def menu():
    print("[1] New Reminder\n[2] Show Reminders\n\n[3] Import\n[4] Export")

while applicationActive == True:
    clear()
    menu()
    userInput = int(input())
    clear()

    # import todo list
    if userInput == 3:
        with open("todo.txt", "r", encoding="utf-8") as datei:
            fileContent = datei.read()

            reminders.clear()
            completedReminders.clear()

            importArray = fileContent.split(";")
            input(importArray)

            for x in range(len(importArray)-1):
                
                reminders.append(importArray[0])
                importArray.pop(0)

                if importArray[0] == "completed":
                    completedReminders.append(True)
                elif importArray[0] == "active": 
                    completedReminders.append(False)


    # export todo list
    if userInput == 4:
        exportFile = ""
        for x in range(len(reminders)):
            exportFile = exportFile + reminders[x] + ";"
            if completedReminders[x] == True:
                exportFile = exportFile + "completed;"
            else:
                exportFile = exportFile + "active;"    
        open("todo.txt", "w", encoding="utf-8").write(exportFile)
        currentPath = os.getcwd()
        input(f"successfully exported to " + GREEN + currentPath + "/todo.txt\n" + RESET)

    # add new
    if userInput == 1:
        reminders.append(input("New Reminder: "))
        completedReminders.append(False)

    # review
    if userInput == 2:
        for x in range(len(reminders)):
            if completedReminders[x] == True:
                print(GREEN+f"{x+1}: {reminders[x]}"+RESET)
            else:
                print(f"{x+1}: {reminders[x]}")

        if len(reminders) > 0:
            print("\n[1] Mark as done\n[2] Remove\n[3] Back")
            userInput = int(input())

            if userInput == 1:
                completedReminders[int(input("Mark as complete: "))-1] = True

            if userInput == 2:
                userInput = int(input("Delete: "))
                completedReminders.pop(userInput-1)
                reminders.pop(userInput-1)
        else:
            print("No reminders yet")
            input()
