# Assessment
PyLS is a command-line utility developed as part of an assessment. It lists files and directories based on a JSON file structure, offering features similar to the Unix ls command with additional capabilities such as nested directory navigation, filtering, sorting, and displaying detailed file information.
Depending on the arguments provided, PyLS can perform various tasks:
1. List Top-Level Files and Directories: **`python -m pyls`**
2. Show All Files (including hidden files): **`python -m pyls -A`**
3. Detailed Information: **`python -m pyls -l`**
4. Human-Readable Sizes (along with detailed information): **`python -m pyls -l -h`**
5. Sort by Time (oldest files first): **`python -m pyls -t`**
6. Filter by Type by dir: **`python -m pyls --filter=dir`**
7. Filter by Type by file: **`python -m pyls --filter=file`**

# Features
Basic Listing: Lists top-level files and directories.
Show All Files: Includes hidden files (files starting with a dot).
Detailed Information: Shows permissions, size, and modification time.
Human-Readable Sizes: Converts sizes into KB, MB, GB, etc.
Sort by Time: Orders files and directories by modification time.
Filter by Type: Filters results to show only files or directories.
Path Navigation: Lists contents of specific paths or files.

# Installation
1. Clone the repository: git clone https://github.com/akashpaira/pyls.git
2. Install dependencies (if any): pip install -r requirements.txt

# Usage

To use Project Title, follow these steps:
1. Open the project in your favorite code editor.
2. Modify the source code to fit your needs.
3. Build the project: **`npm run build`**
4. Start the project: **`npm start`**
5. Use the project as desired.

# JSON Structure
The JSON file should be named file_structure.json and have this format:

{
    "name": "interpreter",
    "size": 4096,
    "time_modified": 1699957865,
    "permissions": "-rw-r--r--",
    "contents": [
        {
            "name": ".gitignore",
            "size": 8911,
            "time_modified": 1699941437,
            "permissions": "drwxr-xr-x"
        },
        {
            "name": "LICENSE",
            "size": 1071,
            "time_modified": 1699941437,
            "permissions": "drwxr-xr-x"
        }
        // Additional files and directories...
    ]
}

# License
This project is licensed under the MIT License. See the LICENSE file for details.

# Contact
For questions or issues, email akashpaira123@gmail.com.



