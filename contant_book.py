Contact = {}

def ShowFunction():
    print(Contact.items())
    print("Name \t Contact")
    
    for key in Contact:
        print('{} \t {}'.format(key,Contact.get(key)))

while True:
    choice = int(input("1. Add new Contact \n "
                   "2. Search the Contact \n"
                   "3. View Contact \n"
                   "4. Edit Contact \n"
                   "5. Delete Contact \n"
                   "6. Exit"
                   "Please choice the number 1-6: "))
    if choice == 1:
        name = input("Please add your conact name : ")
        phone = input("Please add your phone number : ")
        Contact[name] = phone
        
    elif choice == 2:
        search = input("Search the Contact: ")
        if search in Contact:
            print(search, "Contact number is ", Contact[search])
        
        else:
            print("Contact not found ")
            
    elif choice == 3:
        if not Contact:
            print("Contact book is empty")
            
        else:
            ShowFunction()
            
    elif choice == 4:
        EditContact = input("Edit your Contact : ")
        if EditContact in Contact:
            phone = input('change your number: ')
            Contact[EditContact] = phone
            print('Contact updated successfully ')
            ShowFunction()
            
        else:
            print("Name is not found")
            
    elif choice == 5:
        del_Contact = input("Which Contact do you want to delete :")
        if del_Contact in Contact:
            del_confirm = input('Do you want to delete this Contact y/n')
            if del_confirm == "y" or del_confirm == "Y":
                Contact.pop(del_Contact)
            ShowFunction()
            
        else:
            print("The name is not found in the Contact")
            
            
    else:
        break