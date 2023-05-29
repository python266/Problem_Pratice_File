import os

def os_function():
    drive_folder = input("Write full path: ")  # Get path
    if os.path.exists(drive_folder):  # Check if the path exists
        print("Your Drive and Folder is found.")
        print("Do you want to modify this folder")
        choice = input("Y for Yes or N for No: ")
        if choice == "Y":
            print("\nYou have chosen 'Y': ")
            print("We are just changing your file names to capitalize the first letter.")
            # Changing file names
            for filenames in os.listdir(drive_folder):
                if os.path.isfile(os.path.join(drive_folder, filenames)):
                    new_file_name = filenames.capitalize()[0]
                    os.rename(os.path.join(drive_folder, filenames), os.path.join(drive_folder, new_file_name))
                    print(f"File '{filenames}' renamed to '{new_file_name}'")

        elif choice == "N":
            print("You have chosen 'N'.")
            print("\nThank you for using our program.")
            exit()
    else:
        raise FileNotFoundError("Sorry! The specified path does not exist. Please try again!")

if __name__ == '__main__':
    os_function()
