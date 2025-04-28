📒 Contact Manager

A simple Python-based Contact Manager that allows you to add, open, search, and update contacts using a command-line interface.

🚀 Features:
➕ Add a new contact
🔍 Open an existing contact
🔎 Search for a contact (Note: search functionality needs to be handled)
✏️ Update a contact
❌ Quit the application

🛠 Technologies Used
Python 3
IPython Display (for clearing outputs, optional in Jupyter Notebook)

💻 How to Run
Make sure you have Python installed.
Copy the project files (.py file) onto your computer.
Open terminal or command prompt.
Run the script:
python contact_manager.py
 
5. Follow on-screen options:

Press 'a' to add a contact
Press 'o' to open/view a contact
Press 's' to search for a contact
Press 'u' to update a contact
Press 'q' to quit the program

📂 Code Flow
- Start an infinite loop
- Ask user for an action
- If user selects:
    - 'a': Add a new contact
    - 'o': Open an existing contact
    - 's': (Not handled yet)
    - 'u': Update contact information
    - 'q': Quit program
- Otherwise, print "incorrect choice"

📢 Notes
contacts dictionary must be initialized at the start.

Functions like add_contact(), open_contact(), update_contact(), and search_contact() must be defined separately.

The search ('s') option is shown in the menu, but its function is not implemented in the code yet.





