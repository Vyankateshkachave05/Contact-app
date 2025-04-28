
# 📒 Contact Manager

A basic Python-based Contact Manager app that lets you create, view, search, and modify contacts through a command-line interface.

# 🚀 Key Features
➕ Create a new contact  
🔍 View existing contacts  
🔎 Search for a contact (Note: Search functionality still needs implementation)  
✏️ Edit an existing contact  
❌ Exit the application

# 🛠 Tools Used
- Python 3
- IPython Display (optional, used for clearing screen in Jupyter Notebook)

# 💻 How to Execute
1. Ensure Python is installed on your system.
2. Save the provided `.py` file onto your device.
3. Open your terminal or command prompt.
4. Navigate to the folder containing the script.
5. Run the program with the command:
```bash
python contact_manager.py
```

6. Follow the on-screen instructions:
   - Press 'a' to add a new contact
   - Press 'o' to view/open a contact
   - Press 's' to search for a contact
   - Press 'u' to update a contact
   - Press 'q' to quit the application

# 📂 Program Flow
- Runs an infinite loop
- Prompts the user to choose an action
- Based on the input:
    - 'a': Add a new contact
    - 'o': Display an existing contact
    - 's': (Currently not implemented)
    - 'u': Edit a contact
    - 'q': Exit the application
- If an invalid option is entered, it will display "incorrect choice".

# 📢 Important Points
- The `contacts` dictionary must be initialized at the beginning of the program.
- Functions like `add_contact()`, `open_contact()`, `search_contact()`, and `update_contact()` should be created separately.
- Although the search option ('s') is listed, it is not yet implemented in the code.

---

Would you also like me to help you with a polished version that looks even more like a professional project README? 🚀
