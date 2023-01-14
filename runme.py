import os, subprocess, webbrowser

while True:
    try:
        print("Welcome to SKOOL3D, made by bcodog")

        print("\n Type !suggest for cmd commands. If the screen shows no output or error message, press Ctrl + C to get out. This happens if you type in commands with no direct output.")
        command = input("\n Type in your command: ")
        print("\n")
        
        if command == "!suggest":
            print("\n Opening...")
            webbrowser.open("https://ss64.com/nt/netsh.html")
            input("Press any key to clear...")
            os.system('cls')
        else:
            returned_text = subprocess.check_output(command, shell=True, universal_newlines=True)
            print("\n " + returned_text)
            input("\n Press enter to clear...")
            os.system("cls")
    except:
        print("\n There was an error. \n")
        input("\n Press enter to clear...")
        os.system("cls")
