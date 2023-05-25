# Modules
import AppOpener
import pyttsx3
import winsound
from functools import lru_cache
# function
@lru_cache(600000)
def app_open():
    # user-name
    name = input("Enter your name: ")
    welcome_txt = f"Welcome! {name}"
    welcome_voice = pyttsx3.speak(welcome_txt)
    print(welcome_voice)
    print(welcome_txt)
    pyttsx3.speak("How Can I Help You?\nI can open any app from your PC")
    # choice for continue and exit
    print("Continue for C and Exit for E")
    input1 = input("--> ")
    # statements
    # if user choice C
    if input1 == "C":
        print("\nOk! This program has been started;")
        k = "I can able to open; Microsoft-edge\nThis Pc\nCode editor\nMicrosoft store\nCommand prompt\nMail"
        pyttsx3.speak(k)
        print(k)
        # True loop
        while True:
            print("\n\tFor closing app Type 'E'")
            user_input22 = input("What app you want to open: ")
            # Microsoft-edge
            if user_input22 == "Edge" or user_input22 == "browser":
                pyttsx3.speak("It's opening.")
                edge = AppOpener.open("microsoft edge")
                print(edge)
                winsound.PlaySound("App opening",winsound.MB_OK)
                # if user want to exit from the app
                if user_input22 == "E":
                    print("Thank you for using our app")
                    pyttsx3.speak("Thank you for using our app.")
                    break
            # This statement for this pc or file explorer
            elif user_input22 == "file explorer" or user_input22 == "This pc":
                pyttsx3.speak("This pc is opening..")
                file = AppOpener.open("File Explorer")
                print(file)
                winsound.PlaySound("App opening", winsound.MB_OK)
                # This statement for this pc or file explorer
                if user_input22 == "E":
                    print("Thank you for using our app")
                    pyttsx3.speak("Thank you for using our app.")
                    break
            elif user_input22 == "Code editor" or user_input22 == "Pycharm":
                pyttsx3.speak("Pycharm is starting")
                pycharm = AppOpener.open("Pycharm")
                print(pycharm)
                winsound.PlaySound("App opening", winsound.MB_OK)
                if user_input22 == "E":
                    print("Thank you for using our app")
                    pyttsx3.speak("Thank you for using our app.")
                    break
            elif user_input22 == "Microsoft store" or user_input22 == "store":
                pyttsx3.speak("Microsoft store")
                micro = AppOpener.open("microsoft store")
                print(micro)
                winsound.PlaySound("App opening", winsound.MB_OK)
                if user_input22 == "E":
                    print("Thank you for using our app")
                    pyttsx3.speak("Thank you for using our app.")
                    break
            elif user_input22 == "cmd" or user_input22 == "Command prompt":
                pyttsx3.speak("CMD is opening...")
                cmd = AppOpener.open("cmd")
                print(cmd)
                winsound.PlaySound("App opening", winsound.MB_OK)
                if user_input22 == "E":
                    pyttsx3.speak("Thank you for using our product")
                    print("Thank you")
                    break
            elif user_input22 == "Mail" or user_input22=="mail":
                pyttsx3.speak("Mail is opening...")
                mail = AppOpener.open("mail")
                print(mail)
                winsound.PlaySound("App opening", winsound.MB_OK)
                if user_input22 == "E":
                    pyttsx3.speak("Thank you for using our product")
                    print("Thank you for using our product")
                    break
    # Exit
    elif input1 == "E":
        print("Thank you for using our app")
        pyttsx3.speak("Thank you for using our app.")
        exit()
    else:
        pyttsx3.speak("Invalid... Please Try again")
        return app_open()
#driver code
if __name__ == '__main__':
    try:
        app_open()
    except:
        raise Exception("Sorry something went wrong.")