# Assessment
This repository is for demo only

# Features
Basic Listing: Lists top-level files and directories.
Show All Files: Includes hidden files (files starting with a dot).
Detailed Information: Shows permissions, size, and modification time.
Human-Readable Sizes: Converts sizes into KB, MB, GB, etc.
Sort by Time: Orders files and directories by modification time.
Filter by Type: Filters results to show only files or directories.
Path Navigation: Lists contents of specific paths or files.

# Installation
1. Clone the repository: git clone https://github.com/yourusername/zuru_.git
2. Install dependencies (if any): pip install -r requirements.txt

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



