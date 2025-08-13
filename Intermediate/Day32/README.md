# Birthday Wisher Email App

This Python app automatically sends birthday emails to people listed in a CSV file using Gmail. It selects a random letter template and replaces placeholders with the recipient's name.

---

## Features

- Reads birthdays from a CSV file (`birthdays.csv`).
- Checks if today matches any birthday.
- Picks a random letter template from `letter_templates/`.
- Sends personalized emails using Gmail SMTP.
- Supports multiple birthdays on the same day.

---

## Requirements

- Python 3.x
- `pandas` library
- Gmail account with **App Password** enabled
- CSV file with the following columns: `name,email,year,month,day`
- Letter templates folder: `letter_templates/letter_1.txt`, `letter_2.txt`, `letter_3.txt`

---

## Installation

1. Clone the repository or download the files.
2. Install dependencies:

```bash
pip install pandas
