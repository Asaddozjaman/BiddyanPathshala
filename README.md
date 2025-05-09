# 📘 Biddyan Pathshala – Playwright Automation Suite

A beginner-friendly, powerful automation test project using **Python + Playwright** to simulate real user activity on the [Biddyan Pathshala](https://biddyanpathshala.com) educational platform.

---

## 🚀 Features Covered

- 🔐 Student & Teacher Login (valid/invalid)
- 📥 APK download verification
- 🧑‍🏫 Academic members view
- 🗓 Routine opening/closing
- 📄 Note Sheet view and download
- 🧪 Online Exam & Quiz functionality

---

## 🛠 Prerequisites

Before you begin, make sure you have the following installed:

- [Python 3.8+](https://www.python.org/downloads/)
- [Node.js (for Playwright install)](https://nodejs.org/)
- [Git](https://git-scm.com/)

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Asaddozjaman/BiddyanPathshala.git
cd BiddyanPathshala


2. Set Up Virtual Environment (optional but recommended)
python -m venv venv
venv\Scripts\activate  # On Windows


3. Install Python Dependencies
pip install playwright


4. Install Playwright Browsers
playwright install


▶️ Running the Tests
Each feature has a separate Python file. You can run them one by one:
python login_test.py
python apk_download.py
python teacher_login_test.py
python student_login_test.py
python routine_test.py
python quiz_test.py
python note_sheet_test.py
python online_exam_test.py


📁 Project Structure
BiddyanPathshala/
├── login_test.py
├── teacher_login_test.py
├── student_login_test.py
├── apk_download.py
├── quiz_test.py
├── note_sheet_test.py
├── routine_test.py
├── online_exam_test.py
├── requirements.txt
└── README.md


💡 Tips for Beginners
You can view logs printed in your terminal to follow each step.
Each test includes print() statements and timeouts for easy debugging.
Run scripts with headless=False to watch the browser actions live.


🤝 Contributing
Feel free to fork the repo, improve the tests, and make pull requests. All contributions are welcome!


📜 License
This project is for educational and testing purposes only.


🙋‍♂️ Maintained by
Md. Asaddozjaman
Student ID: 212902042
Dept. of CSE, GUB
