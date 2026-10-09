import os

clear = lambda: os.system('clear')

applicationActive = True;
todos = []
completedTodos = []

GREEN = "\033[32m"
RESET = "\033[0m"

def menu():
    print("[1] New task\n[2] Show tasks\n\n[3] Import\n[4] Export")

while applicationActive == True:
    clear()
    menu()
    userInput = int(input())
    clear()

    # import todo list
    if userInput == 3:
        with open("todo.txt", "r", encoding="utf-8") as datei:
            fileContent = datei.read()

            todos.clear()
            completedTodos.clear()

            importArray = fileContent.split(";")
            importSteps = (len(importArray) -1) /2

            for x in range(int(importSteps)):

                todos.append(importArray[0])
                importArray.pop(0)

                if importArray[0] == "completed":
                    completedTodos.append(True)
                else:
                    completedTodos.append(False)
                importArray.pop(0)


    # export todo list
    if userInput == 4:
        exportFile = ""
        for x in range(len(todos)):
            exportFile = exportFile + todos[x] + ";"
            if completedTodos[x] == True:
                exportFile = exportFile + "completed;"
            else:
                exportFile = exportFile + "active;"    
        open("todo.txt", "w", encoding="utf-8").write(exportFile)
        currentPath = os.getcwd()
        input(f"successfully exported to " + GREEN + currentPath + "/todo.txt\n" + RESET)

    # add new
    if userInput == 1:
        todos.append(input("New Reminder: "))
        completedTodos.append(False)

    # review
    if userInput == 2:
        for x in range(len(todos)):
            if completedTodos[x] == True:
                print(GREEN+f"{x+1}: {todos[x]}"+RESET)
            else:
                print(f"{x+1}: {todos[x]}")

        if len(todos) > 0:
            print("\n[1] Mark as done\n[2] Remove\n[3] Back")
            userInput = int(input())

            if userInput == 1:
                completedTodos[int(input("Mark as complete: "))-1] = True

            if userInput == 2:
                userInput = int(input("Delete: "))
                completedTodos.pop(userInput-1)
                todos.pop(userInput-1)
        else:
            print("No reminders yet")
            input()
