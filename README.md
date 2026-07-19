# 🚀 Codeforces Terminal Profile Statistics Viewer

A lightweight command-line tool that fetches real-time Codeforces user statistics and displays a clean, formatted profile card directly in the terminal.


## 🛠️ Tech Stack-
* **Language:** Python 3.14
* **Library:** `requests` (for HTTP GET Requests)
* **API:** Codeforces Public API to fetch user data


## 🧠 Concepts Learned-
* **REST API Integration:** Sending `GET` requests to a public server and receiving data.
* **JSON Parsing:** Decoding raw internet data into usable Python Dictionaries (`response.json()`) making it easier to code.
* **Defensive Programming:** Using Python's `.get()` method to safely extract data, preventing `KeyError` crashes when certain API fields (like organization or name) are missing.
* **Exception Handling:** Using `try-except` blocks to handle network issues without crashing the program.
* **CLI UI Design:** Using f-strings and emojis to make plain terminal text look structured and appealing.


## ⚙️ How to Run-
1. Install the required library:
   ```bash
   pip install requests

2. Run the script:
   ```bash
   python main.py
