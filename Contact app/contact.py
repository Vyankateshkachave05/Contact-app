## your code here

contacts = [
   {"name":"Shayash","number":"8504215201","email" :"shayash@gmail.com"},
    {"name": "Vyankatesh","number": "8504215202","email" : "vyankatesh@gmail.com"},
    {"name": "Sujeeth","number": "8504215205","email" : "sujeeth@gmail.com"}

]
def show_contacts(contacts):
    for i in contacts:
      print(i)
      
def add_contact(contacts):
  name = input("Enter Name")
  number = input("Enter Mobile no.")
  email = input("Enter a Emial id ")
  new_contact= {"name":name,"number":number,"email":email}
  contacts.append(new_contact)

def delete_contact(contacts):
  name = input("Enter a name")
  for name1 in contacts:
    if name1["name"] == name:
      contacts.remove(name1)

def update_contact(contacts):
    name = input("Enter a name").strip().lower()
    for contact in contacts:
        if contact["name"].lower() == name:
            print(f"\nUpdating contact for {contact['name']}...")

            new_name = input("Enter new name: ").strip()
            new_number = input("Enter new mobile number: ").strip()
            new_email = input("Enter new email ID: ").strip()

            contact["name"] = new_name
            contact["number"] = new_number
            contact["email"] = new_email

            print("\nContact updated successfully!")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['number']}")
            print(f"Email: {contact['email']}")
            return

    print("Contact not found!")


def open_contact(contacts,name):
    name = name.strip().lower()
    for contact in contacts:
      if contact["name"].lower() == name:
        print("\ncontact found")
        print(f"name:{contact['name']}")
        print(f"number:{contact['number']}")
        print(f"email:{contact['email']}")
        return

    print("no match found")
    
    
while True:

    action = input("Press 'a' - add contact, 'o' - open contact,'d'-delete contact'u'-update contact 's' - show contact, 'q' - quit")
    if action == 'a':
        ## add contact
        add_contact(contacts)

    elif action == 'o':
        name = input("Enter name of the contact you want to open. ")
        ## open contact
        open_contact(contacts,name)

    elif action == 's':
       ## show all contacts
      show_contacts(contacts)

    elif action == 'q':
        ## break
        break
    elif action== 'u':
      update_contact(contacts)
    elif action == 'd':
      delete_contact(contacts)

    else:
        ## print incorrect choice
        print("incorrect choice")