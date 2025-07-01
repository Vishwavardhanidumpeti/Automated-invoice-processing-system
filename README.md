# zaalima
🧾 Automated Invoice Processing System

## 📌 Project Overview

Businesses receive thousands of invoices via email or in shared folders. Manually processing these invoices is time-consuming and error-prone. This project automates the process of reading **PDF invoices**, extracting **key fields** (invoice number, date, amount, vendor), and storing them in a structured format like **CSV** or **SQLite database**. An optional GUI built using `tkinter` allows users to easily upload and track invoice data.

---

## 🛠️ Tech Stack
**Languages & Libraries:**

- **Python**
- `PyPDF2` / `pdfplumber` – PDF parsing
- `re` – Regular expressions for field extraction
- `pandas`, `openpyxl` – Data handling & Excel export
- `SQLite` – Local database (optional)
- `tkinter` – GUI for file uploads and visualization
- `os`, `csv`, `logging` – File system access, CSV writing, error logging

---

## 📂 Project Structure

```
attachments/
├── all_files/
│   ├── books.py
│   ├── email_read
│   ├── extracted_data.csv
│   ├── log.py
│   ├── pets.py
│   ├── regex.py
│   ├── sql_connection.py
│   └── test_class.db
├── build/
├── dist/
├── testdir/
│   ├── details.txt
│   └── extracted_data.csv
├── ORDER_INVOICE_RD...pdf
├── invoice_app.log
├── sample.ipynb
├── test.py
├── ui.py
├── ui.spec
├── README.md
```

---

## 🗓️ Development Timeline (Month 1)

### ✅ Week 1 – PDF Parsing
- Set up invoice folder watcher using `os`
- Read text from PDFs using `pdfplumber`
- Apply `regex` to extract invoice fields

### ✅ Week 2 – Data Storage
- Store extracted data using `pandas` in CSV
- Optionally store in `SQLite` with a proper schema

### ✅ Week 3 – GUI Interface
- Develop a `tkinter` GUI for uploading invoices
- Add input validation and duplicate checks

### ✅ Week 4 – Logging and Reporting
- Add error handling with `logging`
- Generate summary reports (monthly, vendor-wise)
- Prepare documentation and finalize README

---

## ✅ Features

- 📄 Extracts key data from PDF invoices (Number, Date, Amount, Vendor)
- 📥 Uploads PDFs via a GUI (`tkinter`)
- 📊 Stores data in CSV or SQLite DB
- 🛑 Detects duplicates and handles invalid files
- 📑 Logs all events and errors
- 📈 Generates summaries and reports

---

## 🚀 How to Run

### 🖥️ Using Command Line

```bash
python attachments/all_files/email_read.py
```

### 🖼️ Using GUI

```bash
python ui.py
```

---

## 📦 Output

- `extracted_data.csv`: Final structured invoice data
- `invoice_app.log` / `test.log`: Event and error logs
- `test_class.db`: Optional SQLite database file
- GUI window for uploading invoices

---

## 📌 Future Enhancements

- Email integration for invoice reading
- Export to Google Sheets
- Vendor-wise analysis charts
- OCR support for scanned PDF invoices

---

## 👨‍💻 Author

**Vishwa Vardhini**  
B.Tech Computer Science  
SR University  
Email: [vishwavardhinidumpeti@gmail.com](mailto:vishwavardhinidumpeti@gmail.com)
