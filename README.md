# 🌐 Site Monitor

A Python-based website monitoring tool that continuously checks whether a website is online, measures its response time, and sends email notifications whenever the website changes its status.

This project was developed to practice HTTP requests, automation, monitoring systems, logging, and email notifications.

---

# 🚀 Features

* Monitor a website continuously
* Check website availability (UP / DOWN)
* Measure response time
* Display HTTP status code
* Log every verification
* Detect status changes
* Send email alerts when the website goes offline
* Send email alerts when the website comes back online

---

# 📂 Project Structure

```text
Site-Monitor/
│
├── main.py
├── monitor.py
├── notification.py
├── logger.py
├── .env
├── requirements.txt
└── README.md
```

---

# 📧 Email Notifications

The application automatically sends an email when:

* The website becomes unavailable.
* The website is available again.

This prevents duplicate notifications while the website remains in the same state.

---

# 🔒 Environment Variables

Sensitive information is stored using environment variables.

Example:

```env
EMAIL=your_email@gmail.com
PASSWORD=your_app_password
RECEIVER=user@email.com
```

The `.env` file should **never** be committed to GitHub.

---

# ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/Yuri09-hub/Site-Monitor.git
```

Move into the project directory:

```bash
cd Site-Monitor
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment.

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

---


# 👨‍💻 Author

**Yuri Rodrigues**

GitHub: https://github.com/Yuri09-hub
