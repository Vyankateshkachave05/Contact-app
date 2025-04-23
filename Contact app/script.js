let contacts = [
    { name: "Shayash", number: "8504215201", email: "shayash@gmail.com" },
    { name: "Vyankatesh", number: "8504215202", email: "vyankatesh@gmail.com" },
    { name: "Sujeeth", number: "8504215205", email: "sujeeth@gmail.com" },
  ];
  
  const contactList = document.getElementById("contactList");
  const contactForm = document.getElementById("contactForm");
  
  function renderContacts() {
    contactList.innerHTML = "";
    contacts.forEach((contact, index) => {
      const li = document.createElement("li");
      li.innerHTML = `
        <span>
          <strong>${contact.name}</strong><br>
          📞 ${contact.number}<br>
          📧 ${contact.email}
        </span>
        <span class="actions">
          <button onclick="editContact(${index})">Edit</button>
          <button onclick="deleteContact(${index})">Delete</button>
        </span>
      `;
      contactList.appendChild(li);
    });
  }
  
  function addContact(e) {
    e.preventDefault();
    const name = document.getElementById("name").value.trim();
    const number = document.getElementById("number").value.trim();
    const email = document.getElementById("email").value.trim();
  
    contacts.push({ name, number, email });
    contactForm.reset();
    renderContacts();
  }
  
  function deleteContact(index) {
    if (confirm("Are you sure you want to delete this contact?")) {
      contacts.splice(index, 1);
      renderContacts();
    }
  }
  
  function editContact(index) {
    const contact = contacts[index];
    const newName = prompt("Enter new name", contact.name);
    const newNumber = prompt("Enter new number", contact.number);
    const newEmail = prompt("Enter new email", contact.email);
  
    if (newName && newNumber && newEmail) {
      contacts[index] = {
        name: newName,
        number: newNumber,
        email: newEmail,
      };
      renderContacts();
    }
  }
  
  contactForm.addEventListener("submit", addContact);
  renderContacts();
  