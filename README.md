

# 🧾 Automated Invoice Processing System

##🚀 Project Summary

Automating invoice processing reduces human error, saves time, and streamlines business operations. This Python-based solution scans PDF invoices from a folder or email inbox, extracts relevant data using OCR and regex logic, and stores it in a structured, accessible format like CSV or SQLite. The tool optionally features a user-friendly GUI built using `tkinter`.

 ## 💼  Real-World Problem Statement

Companies receive hundreds or even thousands of invoices through digital channels. Manually opening each PDF, identifying invoice details (like amount, vendor, invoice number), and copying them into Excel or databases is repetitive and error-prone. This project provides a smart automation solution.

---

## 📚 Key Functionalities

- ✅ **Automated PDF Invoice Reading**
- ✅ **Regex-based Field Extraction**
- ✅ **Store data in Excel/CSV and SQLite DB**
- ✅ **Error Handling & Logging**
- ✅ **Simple User Interface using `tkinter`**
- ✅ **Duplicate Validation**
- ✅ **Summary Report Generation**

---

## 🧑‍💻 Technologies and Libraries Used

| Area                  | Tools / Libraries                          |
|-----------------------|---------------------------------------------|
| Language              | Python                                      |
| PDF Reading           | `pdfplumber`, `PyPDF2`                      |
| Text Extraction       | `re` (Regex)                                |
| Data Manipulation     | `pandas`, `openpyxl`                        |
| GUI                   | `tkinter`, `filedialog`                     |
| Database (optional)   | `SQLite3`                                   |
| Logging               | `logging`, `os`                             |
| File I/O              | `csv`, `pathlib`, `os`                      |

---

## 🧾 Invoice Fields Extracted

- 📄 **Invoice Number**
- 📅 **Invoice Date**
- 💰 **Total Amount**
- 🏢 **Vendor Name**
- 🆔 **Invoice ID / Reference Code (if applicable)**

---

## 🧱 Project Directory Overview

```
attachments/
├── all_files/
│   ├── books.py #homework
│   ├── email_read #Possibly handles invoice reading from email
│   ├── extracted_data.csv #Final data output file with   extracted invoice details.
│   ├── log.py #For logging and debugging purposes.
│   ├── pets.py #homework
│   ├── regex.py #handle sample inputs, regex logic
│   ├── sql_connection.py #handle sample inputs and database connections.
│   └── test_class.db #SQLite database
├── dist/                   # Compiled app (PyInstaller output)
├── testdir/                # Temporary/test output
├── sample.ipynb            # Notebook version for dev/testing
├── ORDER_INVOICE_RD...pdf  # Sample invoice files
├── ui.py                   # GUI interface using tkinter
├── README.md               # Project documentation
```

---

## 📆 Development Roadmap

### 🗓️ Week 1: Invoice Reading & Text Extraction
- Folder watcher setup using `os`
- Read and extract text from PDFs with `pdfplumber`
- Apply `regex` to extract relevant fields

### 🗓️ Week 2: Data Handling & Storage
- Convert parsed data to structured `DataFrame` (via `pandas`)
- Store output in `CSV` or export to Excel using `openpyxl`
- Optional: Save to `SQLite` using `sql_connection.py`

### 🗓️ Week 3: GUI & Input Validation
- Build basic GUI using `tkinter`
- Implement upload button and form display
- Add validations for duplicate entries, missing data

### 🗓️ Week 4: Logging, Testing, and Reporting
- Implement `logging` for errors and activity tracking
- Generate reports (monthly summary, vendor-wise)
- Final testing and deployment with `.spec` and `dist/`

---

## 🖥️ How to Run This Project

### 1️⃣ Command Line Mode

```bash
python attachments/all_files/email_read.py
```

### 2️⃣ Graphical User Interface (GUI)

```bash
python ui.py
```

---

## 📁 Output Files

| File Name             | Description                                |
|-----------------------|--------------------------------------------|
| `extracted_data.csv`  | Final extracted invoice data               |
| `invoice_app.log`     | Log file with timestamps & errors          |
| `test_class.db`       | Optional SQLite database file              |
| `test.log`            | Debug/test logs                            |

---

## 📊 Example Use Case Scenarios

- A small business owner uploads all monthly invoices at once
- A finance team member wants automated Excel tracking
- Developers integrate the engine with email scraping for real-time processing

---

## 🛠️ Future Improvements

- 📧 Auto-read invoices directly from Gmail/Outlook inbox
- 🌐 Web dashboard using Flask or Django
- 📷 Add OCR support for scanned image-based invoices (via Tesseract)
- 📈 Advanced reporting using visualizations (matplotlib/seaborn)
- ☁️ Cloud deployment for team-wide access

---

## 👨‍💻 Developed By

**Vishwa Vardhini**  
B.Tech in Computer Science, SR University  
📧 [vishwavardhinidumpeti@gmail.com](mailto:vishwavardhinidumpeti@gmail.com)

---
