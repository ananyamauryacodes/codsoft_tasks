# =====================================
# PERSONAL CONTACT MANAGER 
# =====================================

contact_book = []


# -------------------------------------
# Add New Contact
# -------------------------------------
def create_contact():

    print("\n----- Add New Contact -----")

    full_name = input("Enter Full Name: ").strip()
    mobile = input("Enter Mobile Number: ").strip()
    mail_id = input("Enter Email ID: ").strip()
    location = input("Enter Address: ").strip()


    if full_name == "" or mobile == "" or mail_id == "" or location == "":
        print("Please fill all contact details!")
        return


    person = {
        "full_name": full_name,
        "mobile": mobile,
        "mail_id": mail_id,
        "location": location
    }


    contact_book.append(person)

    print("\nNew contact saved successfully!")


# -------------------------------------
# Display Contact List
# -------------------------------------
def display_contacts():

    print("\n----- Saved Contacts -----")


    if len(contact_book) == 0:
        print("Your contact list is empty.")
        return


    for number, person in enumerate(contact_book, start=1):

        print("\nContact Number:", number)
        print("----------------------")
        print("Name  :", person["full_name"])
        print("Phone :", person["mobile"])

        # Extra Feature 1:
        # Show number of stored details
        print("Stored Details:", len(person), "fields")


    print("\nTotal saved contacts:", len(contact_book))


# -------------------------------------
# Find Contact
# -------------------------------------
def find_contact():

    print("\n----- Search Contact -----")

    keyword = input("Enter name or mobile to search: ").strip()


    # Extra Feature 2:
    # Empty search handling
    if keyword == "":
        print("Please enter something to search.")
        return


    found = False


    for person in contact_book:


        # Extra Feature 3:
        # Case insensitive search

        if (person["full_name"].lower() == keyword.lower()
                or person["mobile"] == keyword):


            print("\nContact Found")
            print("----------------------")
            print("Name    :", person["full_name"])
            print("Mobile  :", person["mobile"])
            print("Email   :", person["mail_id"])
            print("Address :", person["location"])

            found = True
            break


    if found == False:
        print("No matching contact found.")



# -------------------------------------
# Modify Contact
# -------------------------------------
def modify_contact():

    print("\n----- Update Contact -----")


    keyword = input("Enter name or mobile: ").strip()


    for person in contact_book:


        if (person["full_name"].lower() == keyword.lower()
                or person["mobile"] == keyword):


            print("\nEnter updated information")


            updated_name = input("New Name: ").strip()
            updated_mobile = input("New Mobile: ").strip()
            updated_mail = input("New Email: ").strip()
            updated_address = input("New Address: ").strip()


            if updated_name == "" or updated_mobile == "" or updated_mail == "" or updated_address == "":
                print("Details cannot be empty!")
                return


            person["full_name"] = updated_name
            person["mobile"] = updated_mobile
            person["mail_id"] = updated_mail
            person["location"] = updated_address


            print("\nContact updated successfully!")
            return


    print("Contact does not exist.")



# -------------------------------------
# Remove Contact
# -------------------------------------
def remove_contact():

    print("\n----- Delete Contact -----")


    keyword = input("Enter name or mobile: ").strip()


    for person in contact_book:


        if (person["full_name"].lower() == keyword.lower()
                or person["mobile"] == keyword):


            contact_book.remove(person)

            print("\nContact removed successfully!")
            return


    print("Contact not found.")



# -------------------------------------
# Main Menu
# -------------------------------------

while True:


    print("\n" + "=" * 40)
    print("       PERSONAL CONTACT MANAGER")
    print("=" * 40)

    print("1. Create Contact")
    print("2. Display Contact List")
    print("3. Find Contact")
    print("4. Modify Contact")
    print("5. Remove Contact")
    print("6. Close Program")

    print("=" * 40)


    option = input("Select an option: ").strip()


    if option == "1":
        create_contact()


    elif option == "2":
        display_contacts()


    elif option == "3":
        find_contact()


    elif option == "4":
        modify_contact()


    elif option == "5":
        remove_contact()


    elif option == "6":
        print("\nClosing Contact Manager. Goodbye!")
        break


    else:
        print("\nInvalid option. Try again.")
