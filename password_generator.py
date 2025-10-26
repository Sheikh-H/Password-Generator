#A password generator that uses 3 memorable words to create a password for each app/website you have then allowing you to store that information in a JSON file in the same folder as this script. You can also view all the stored passwords, change your memorable words and update a password for a website/app. With this script you can generate 432 unique passwords with just 3 memorable words.

import os
import random #This is needed for generating and shuffling the words / characters
import sys
import json #This is needed to help read and write to a file in JSON format
#The above is where I have imported the necessary modules / libraries for this script to work
password_file = 'passwords.json' #This is the name of the JSON file that you will create to store your data in
# Get folder of the current script
script_dir = os.path.dirname(os.path.abspath(__file__)) #This get the current directory of this script
# JSON file path in the same folder
password_file = os.path.join(script_dir, "passwords.json") #This places the JSON file in the same directory as the script

# Load JSON data
def load_data():
    if not os.path.exists(password_file):
        with open(password_file, 'w') as f:
            json.dump({"memorable_words": [], "apps": []}, f, indent=4)
    with open(password_file, 'r') as f:
        return json.load(f)
#^The above function is what loads the JSON data from the file and into the script, it particularly checks if the file exists and if it doesn't it creates on with the right structure and 'table / column' names.

# Save JSON data
def save_data(data):
    with open(password_file, 'w') as f:
        json.dump(data, f, indent=4)
#^This function saves the data from the script into the JSON file.

def startup(data):
    if len(data["memorable_words"]) == 0: #This line checks if the memorable words list is empty by checking its length, data is the variable that holds the data from the JSON file.
        print("Hey! Welcome to your password generator! This is your first set up, so we'll need to take 3 memorable words from your to begin")
        for i in range(3): #Originally I had listed this outside a for loop and when using AI to help me, it arranged my code in a shorter for loop which is more efficient.
            word = input(f"Enter memorable word #{i+1}: ").capitalize() #This is what takes the input, converts the first letter to uppercase and then stores it in the variable
            data["memorable_words"].append(word)#This is now what appends the words to the list in the JSON file structure
        save_data(data)#This then saves that data into the json file
        print(f"Your memorable words: {data['memorable_words']}")#This now prints out your memorable word, not from the variable but from the JSON file itself.
    else:
        print("Welcome back! Let's get you in the application")

#^This function checks if the user has already set their memorable words, if not it prompts them to enter 3 words and saves these to the JSON file. 

# Generate a new password
def generate_password(data):
    #This had more than 20 lines of code when I first wrote it, again with AI I was able to create something more efficient. This is the function that takes your memorable words, create a permutation of it, adds a random number and special character and then appends that onto the JSON file under those details. I could have created an incremental ID for each password or entry but I felt it wasn't required for this application.
    app_name = input("App/Website name: ").capitalize() 
    app_username = input("Username/email: ").lower()
    notes = input("Notes (Enter to skip): ")

    # Check if app exists
    for app in data["apps"]:
        if app["app_name"] == app_name:
            print("Password already exists for this app. Consider updating instead.")
            return
#Before generating a password, the script has to check if there is a password for the app/website already. If there is, then you would be asked to create a unique name or update the existing password.
    random.shuffle(data["memorable_words"])
    #This is where the memorable words are shuffled to create a different arrangement of your memorable words.
    temp_password = ''.join(data["memorable_words"])
    #This joins the shuffled words back together without any spaces/separators.
    randnum = str(random.randint(0,9))
    #This now gathers a random number between 0 and 9 and converts that to a string which is treated as text to be stored later.
    randspecial = random.choice(['!', '@', '#', '$', '%', '^', '&', '*'])
    #This selects a random character out of the list above.
    generated_password = temp_password + randnum + randspecial + app_name
    #This now concatonates all the elements together to create your password.

    # Save details
    data["apps"].append({
        "app_name": app_name,
        "username": app_username,
        "notes": notes,
        "password": generated_password
    })
    #This now creates the structure of entering the details into the JSON file under 'apps'
    save_data(data) # This now pushes the data to the file which is stored and saved

    print(f"Generated password: {generated_password}") #This prints out what your password now is.

# View all passwords
def view_all_passwords(data): #This function is what calls 'data' which we created earlier which is to read the JSON file and hold that data in the script while it is running.
    if len(data["apps"]) == 0:#This does the same as with the memorable words to check if there are entries to display
        print("No passwords stored yet.")
        return #This is similar to a break statement to exit a loop but this exits the whole function.
    for app in data["apps"]:
        print(f"PASSWORDS \n Site: {app['app_name']} |\n Username: {app['username']} |\n Password: {app['password']} |\n Notes: {app['notes']}")
        print("----------------------------------------------------------------------------")
        #This loops through each entry in the 'apps' list in 'data' which is the JSON file and print out the details in a list format.

def change_memorable_words(data):
    print("You can change your memorable words here.")
    data["memorable_words"].clear() #this clears the current list of memorable wors inside the JSON file.
    for i in range(3): # This does the same loop 3 times to collate 3 new words from the user. 
        word = input(f"Enter new memorable word #{i+1}: ").capitalize() #This is what takes the input and the 'i+1' is what makes the number increment each time a word is entered.
        data["memorable_words"].append(word)#This now appends those details to the file
    save_data(data)
    print("Memorable words updated to: ", data["memorable_words"])

def update_password(data):
    app_name = input("Enter the name of the app you would like to update the password for: ").capitalize()#Here you enter the name of the app/website you want to update the password for.
    for app in data["apps"]:#This now loops through each entry in the data (password file) and checks if there is a match.
        if app["app_name"] == app_name: #if there is a match, it does the following == means exact match
            random.shuffle(data["memorable_words"]) #This shuffles the new memorable words
            temp_password = ''.join(data["memorable_words"])#This again creates a permutation of the shuffled memorable words
            randnum = str(random.randint(0,9))
            randspecial = random.choice(['!', '@', '#', '$', '%', '^', '&', '*'])
            new_password = temp_password + randnum + randspecial + app_name
            app["password"] = new_password
            save_data(data)
            print(f"Password for {app_name} updated to: {new_password}")
            return
        else:
            print("App not found, please use the exact name.")
            return

def delete_data(data):
    app_name = input("Enter the name of the website/app you would like to delete the password for: ").capitalize()
    for i, app in enumerate(data["apps"]):#As opposed to just searching through the list, you can see here that it also uses the index as an ID to help find and delete the right entry. Essentially 'i' is the index number and 'app' is the actual entry.
        if app["app_name"] == app_name:
            del data["apps"][i] #This is what deletes the whole entry from the list using the index number temporarily assined to look for the exact app name. 
            save_data(data) #This then saves the file or data back.
            print(f"Password for {app_name} deleted.")
            return
        else:
            print("App not found, try again.")
            return
#^This function allows you to delete an entry from the JSON file by specifying the app/website name. Again, I didn't create an ID field for each entry but that could be a future improvement.

# Main menu loop
def main_menu(data):
    while True:
        option = input("\n1. Generate password\n2. View all passwords\n3. Change memorable words\n4. Update a password\n5. Delete a password\n6. Exit\nType Option: ")
        if option == "1":
            generate_password(data)
        elif option == "2":
            view_all_passwords(data)
        elif option == "3":
            change_memorable_words(data)
        elif option == "4":
            update_password(data)
        elif option == "5":
            delete_data(data)
        elif option == "6":
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid option.")

data = load_data()
startup(data)
main_menu(data)

#I could go on to explain the code in more detail but this should give you an idea of what I am able to create myself with some help of AI. I am still learning and this is a small project but it does what I could expect it to do. The improvements I could make to this would be to add an ID field for each entry which would make CRUD operations/functions easier. I could also add some validations to the password it generates to ensure that it meets a certain criteria like character length, upperlower case, and etc. I think it would be important to also create an encryption function to encrypt the passwords in the JSON file so it would be stored in plain text. All of these updates I will be working on hopefully within the next few weeks.




