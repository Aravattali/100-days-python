# 📬 Mail Merge Project – Day 24 of #100DaysOfCode

This is a simple **Mail Merge** automation project built with Python. It reads a list of names from a text file, inserts each name into a letter template, and generates personalized invitation letters.

## 🛠 What It Does

✅ Reads names from a file  
✅ Replaces a placeholder (`[name]`) in a letter template  
✅ Writes a personalized letter for each person into the `Output/ReadyToSend` folder  

## 📂 Project Structure

MailMergeProject/
├── main.py # Main script that performs the mail merge
├── Input/
│ ├── Names/
│ │ └── invited_names.txt # List of names to invite
│ └── Letters/
│ └── starting_letter.txt # Template letter with [name] placeholder
├── Output/
│ └── ReadyToSend/
│ └── letter_for_Name.txt # Generated personalized letters
└── README.md # You're here!

makefile
Copy
Edit

## 📜 Example Template

**starting_letter.txt:**

Dear [name],

You are invited to my birthday this Saturday.

Hope you can make it!

Angela

markdown
Copy
Edit

## 🧠 Concepts Practiced

- File handling with `open()`, `.readlines()`, and `.write()`
- String manipulation and `.replace()`
- Using `for` loops and `.strip()` to clean up data
- Working with file paths and output folders

## 🚀 How to Run

1. Make sure you have Python 3 installed.
2. Put your names in `Input/Names/invited_names.txt`, one per line.
3. Customize `Input/Letters/starting_letter.txt` as needed.
4. Run the program:

```bash
python3 main.py