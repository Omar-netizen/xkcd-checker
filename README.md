# Did I Miss My XKCD? 🚀

A simple Python command-line tool to fetch and display the latest or a specific XKCD comic. Never miss your daily dose of wit and wisdom!

## ✨ Features

* **Get Latest Comic:** Fetch and display the details of the most recent XKCD comic.
* **Get Specific Comic:** Retrieve any XKCD comic by its unique number.
* **Clear Output:** Presents comic information in an easy-to-read format.
* **Robust Error Handling:** Gracefully handles network issues, invalid comic numbers, and API errors.
* **User-Friendly CLI:** Built with `argparse` for intuitive command-line usage and helpful messages.

## 🛠️ Tech Stack

* **Python 3:** The core programming language.
* **`requests` library:** For making HTTP requests to the XKCD API.
* **`argparse` module:** For handling command-line arguments.
* **`logging` module:** For structured error and informational messages.

## 🚀 Installation & Setup

1.  **Clone the repository (or download the ZIP):**
    ```bash
    git clone [https://github.com/](https://github.com/)[YourGitHubUsername]/xkcd-checker.git
    cd xkcd-checker
    ```
2.  **Create and activate a Python virtual environment:**
    * **macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * **Windows (Command Prompt):**
        ```cmd
        python -m venv venv
        venv\Scripts\activate.bat
        ```
    * **Windows (PowerShell - *this is what you use*):**
        ```powershell
        python -m venv venv
        Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass # Temporary policy bypass
        .\venv\Scripts\Activate.ps1
        ```
        *(Confirm with 'Y' if prompted by `Set-ExecutionPolicy`)*

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 💡 Usage

Make sure your virtual environment is activated (`(venv)` prefix in your terminal).

* **To get the latest XKCD comic:**
    ```bash
    python main.py --latest
    ```

* **To get a specific XKCD comic (e.g., comic number 614 - "Python"):**
    ```bash
    python main.py --comic 614
    ```

* **To see the help message and available options:**
    ```bash
    python main.py --help
    ```

## 📸 Screenshot / Demo
   <img width="1552" height="723" alt="image" src="https://github.com/user-attachments/assets/9d958c77-33e5-4bc6-8c99-f480beb54289" />


## 🤝 Contributing

Feel free to open issues or submit pull requests to improve this tool!

---
*Built with ❤️ by Omar*
