import json
import os
import sys

def list_top_level(directory):
    # Define the path to the JSON file
    #json_file_path = os.path.join(directory, 'file_structure.json')
    json_file_path = directory
    
    # Read and parse the JSON file
    try:
        with open(json_file_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: The file {json_file_path} does not exist.")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: The file is not a valid JSON.")
        sys.exit(1)
    top_level_contents = data.get('contents', [])
    return top_level_contents
    
def Task(directory):
    # Extract top-level contents    
    res = list_top_level(directory)   
    # Filter and collect names of files and directories
    names = [item['name'] for item in res]
    
    # Print names separated by space
    print(' '.join(names))

if __name__ == '__main__':
    # Get the directory path from command-line arguments or default to current directory
    #directory = os.path.dirname(os.path.abspath(__file__))
    directory = "file_structure.json"
    Task(directory)
