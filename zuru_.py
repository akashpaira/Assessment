import json
import os
import sys
import argparse
from datetime import datetime

import pdb

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


def format_modification_time(timestamp):
    """
    Format the modification time into a readable string.

    :param timestamp: Unix timestamp.
    :return: Formatted date and time string.
    """
    dt = datetime.fromtimestamp(timestamp)
    return dt.strftime('%b %d %H:%M')

def filter_items(items, filter_option):
    """
    Filter items based on the given filter option.

    :param items: List of dictionaries containing file and directory information.
    :param filter_option: Filter option to show only files or directories.
    :return: Filtered list of items.
    """
    filtered_items = []
    for item in items:
        if filter_option == 'dir' and 'contents' in item:
            filtered_items.append(item)
        elif filter_option == 'file' and 'contents' not in item:
            filtered_items.append(item)
    return filtered_items

def list_detailed_files_and_directories(items,lf_revrse=False,lf_t=False,filter_option=False,lsize=False):
    """
    Print detailed information about files and directories.

    :param items: List of dictionaries containing file and directory information.
    """
    #pdb.set_trace()
    if lf_t:
        items.sort(key=lambda x: x['time_modified'])
        
    if lf_revrse:
        items = items[::-1]
        
    if filter_option:
        if filter_option in("dir","file"):
            items = filter_items(items,filter_option)
        else:
            print("Invalid")
        
    for item in items:
        if not item['name'].startswith('.'):
            try:
                permissions = item['permissions']
                size = item['size']
                mod_time = format_modification_time(item['time_modified'])
                name = item['name']
                print(f"{permissions} {size} {mod_time} {name}")
            except KeyError as e:
                print(f"Error: Missing key {e} in item.")
                sys.exit(1)
            
def list_simple_files_and_directories(res):
    """
    Print the names of files and directories.

    :param items: List of dictionaries containing file and directory information.
    """
    try:
        if show_all:
            names = [item['name'] for item in res]
        else:
            names = [item['name'] for item in res if not item['name'].startswith('.')]
        
        print(' '.join(names))

    except Exception as e:
        print (e)

    
def Task(directory, show_all=False, lf=False, lf_revrse=False, lf_t=False,filter_option=False, lsize=False):
    # Extract top-level contents    
    res = list_top_level(directory)  

    try:    
        if long_format == False and (lf_revrse==True or lf_t==True or filter_option==True):
            print("Recheck the arguments")
        elif long_format:
            list_detailed_files_and_directories(res,lf_revrse,lf_t,filter_option,lsize)
        else:
            list_simple_files_and_directories(res)
        
        #print(' '.join(names))

    except Exception as e:
        print (e)
        


if __name__ == '__main__':
    # Get the directory path from command-line arguments or default to current directory
    #directory = os.path.dirname(os.path.abspath(__file__))
    directory = "file_structure.json"
    
    parser = argparse.ArgumentParser(description="List top-level files and directories.")
    parser.add_argument('-A', action='store_true', help="Show all files, including the '.<name>' ones.")
    parser.add_argument('-l', action='store_true', help="Show detailed information.")
    parser.add_argument('-r', action='store_true', help="Reverse the detailed information.")
    parser.add_argument('-t', action='store_true', help="Sort the detailed information based on timestamp.")
    parser.add_argument('--filter', choices=['file', 'dir'], help="Filter the output to only show files or directories.")
    #parser.add_argument('--filter', action='store_true', help="Filter the output to only show files or directories.")
    
    # Parse arguments
    try:
        args = parser.parse_args()
    except Exception as e:
        print("Invalid")
    # Determine if any arguments are passed
    show_all = args.A
    long_format = args.l
    lf_revrse = args.r
    lf_t = args.t
    filter_option=args.filter
    
    Task(directory,show_all=args.A,lf=args.l,lf_revrse=args.r,lf_t=args.t,filter_option=args.filter)
