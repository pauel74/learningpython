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
    if userInput == 3:
        with open("todo.txt", "r", encoding="utf-8") as datei:
            fileContent = datei.read()
        input(fileContent)
    if userInput == 4:
        exportFile = "ToDo("
        for x in range(len(reminders)):
            exportFile = exportFile + "((" + reminders[x] + ")("
            if completedReminders[x] == True:
                exportFile = exportFile + "1))"
            else:
                exportFile = exportFile + "0))"    
        exportFile = exportFile + ")"  
        open("todo.txt", "w", encoding="utf-8").write(exportFile)
        currentPath = os.getcwd()
        input(f"successfully exported at " + GREEN + currentPath + "/todo.txt\n" + RESET)
    if userInput == 1:
        reminders.append(input("New Reminder: "))
        completedReminders.append(False)
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
