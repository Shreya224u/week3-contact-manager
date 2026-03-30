# 📒 Contact Management System

## 📌 Project Description

The **Contact Management System** is a Python-based application that allows users to efficiently manage their contacts using dictionaries and functions. It supports full CRUD (Create, Read, Update, Delete) operations, search functionality, and persistent data storage using JSON files.

This project demonstrates the practical use of **functions, dictionaries, file handling, and input validation** in Python.

---

## 🎯 Objectives

* Build a real-world CLI-based application
* Understand dictionary-based data storage
* Implement modular programming using functions
* Handle user inputs and errors effectively
* Work with file persistence (JSON & CSV)

---

## 🧠 What I Learned

1. **Functions** – Creating reusable and modular code
2. **Dictionaries** – Efficient key-value data storage
3. **String Methods** – Data cleaning and formatting
4. **File Handling** – Saving and loading JSON data
5. **Input Validation** – Preventing invalid entries
6. **Error Handling** – Using try-except for stability

---

## 🚀 Features

* ✅ Add new contacts with validation
* ✅ Search contacts (partial name matching)
* ✅ Update existing contact details
* ✅ Delete contacts with confirmation
* ✅ Display all contacts in formatted view
* ✅ Save & load contacts using JSON
* ✅ Export contacts to CSV
* ✅ Contact statistics (total, groups, recent updates)
* ✅ Phone number & email validation
* ✅ User-friendly menu-driven interface

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Libraries Used:**

  * `json` – Data storage
  * `re` – Validation (regex)
  * `datetime` – Timestamp tracking
  * `csv` – Export functionality

---

## 📂 Project Structure

```
week3-contact-manager/
│── contacts_manager.py
│── contacts_data.json
│── test_contacts.py
│── README.md
│── requirements.txt
│── .gitignore
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/contact-management-system.git
cd contact-management-system
```

### 2. Run the Program

```bash
python contacts_manager.py
```

---

## ▶️ How to Use

1. Run the program
2. Choose from menu options:

   * Add Contact
   * Search Contact
   * Update Contact
   * Delete Contact
   * View All Contacts
   * Export to CSV
   * View Statistics
   * Exit
3. Enter details as prompted
4. Data is automatically saved

---

## 📊 Sample Output

```
=========== CONTACT MANAGEMENT SYSTEM ===========

MAIN MENU
1. Add New Contact
2. Search Contact
3. Update Contact
4. Delete Contact
5. View All Contacts
6. Export to CSV
7. View Statistics
8. Exit

Enter your choice: 1

Contact added successfully!
```

---

## 🧩 Technical Implementation

### ✔ Requirement Coverage

| Requirement      | Implementation                        |
| ---------------- | ------------------------------------- |
| Dictionaries     | Used to store contacts                |
| Functions        | Separate functions for each operation |
| Input Validation | Regex for phone/email                 |
| CRUD Operations  | Add, Search, Update, Delete           |
| File Handling    | JSON save/load                        |
| Search           | Partial matching implemented          |
| Error Handling   | try-except blocks                     |
| UI               | Menu-driven CLI                       |

---

## ⚠️ Challenges & Solutions

### 🔹 Challenge: Validating phone numbers

**Solution:** Used regex to ensure 10–15 digit format

### 🔹 Challenge: Persistent data storage

**Solution:** Implemented JSON file handling

### 🔹 Challenge: Clean UI output

**Solution:** Used formatted printing and structure

---

## 📸 Screenshots

(Add screenshots here when uploading)

* Menu interface
* Add contact
* Search results
* Statistics display

---

## 🔮 Future Enhancements

* GUI version using Tkinter
* Cloud-based storage
* Contact import/export via Excel
* Authentication system

---

## 🔗 Repository Link

```

```


