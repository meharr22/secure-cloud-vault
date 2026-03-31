# ☁️ Secure Cloud Vault (AWS + Flask)

## 📌 Overview
Secure Cloud Vault is a **cloud-based file management system** built using **Flask and AWS S3**.  
It allows users to securely upload, download, and manage files with support for **versioning and access control**.

---

## 🚀 Features
- 🔐 User Authentication (Login system)
- 📤 Upload files to AWS S3
- 📥 Download files
- 📂 View uploaded files
- 🔄 File Versioning (V1, V2, V3…)
- ☁️ Cloud storage using AWS S3
- 🔓 Session-based access control

---

## 🏗️ Tech Stack
- **Backend:** Flask (Python)
- **Cloud:** AWS S3
- **SDK:** Boto3
- **Frontend:** HTML (basic forms)

---

## 📂 Project Structure
```
secure-cloud-vault/
│
├── app.py
├── requirements.txt
├── report.pdf
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

### 2️⃣ Configure AWS
- Create an S3 bucket  
- Replace bucket name in `app.py`:
```python
BUCKET = "your-bucket-name"
```

- Configure AWS credentials:
```bash
aws configure
```

---

### 3️⃣ Run the App
```bash
python app.py
```

---

### 4️⃣ Open in Browser
```
http://localhost:5000
```

---

## 🔐 Login Credentials
```
Username: admin
Password: admin123
```

---

## 🧪 How to Use
1. Login using credentials  
2. Upload file  
3. View files  
4. Check versions  
5. Download files  

---

## 📚 Learning Outcomes
- Working with AWS S3 using Boto3  
- Building web apps using Flask  
- Implementing file upload/download systems  
- Understanding cloud storage & versioning  

---

## 🔮 Future Improvements
- Multi-user authentication  
- File encryption  
- Better UI (React/Bootstrap)  
- Activity logs  

---

## 👩‍💻 Author
**Mehar Arora**  
 

---

## ⭐ Note
This project demonstrates a real-world implementation of a cloud-based file storage system using AWS.
