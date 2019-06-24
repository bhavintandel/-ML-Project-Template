# This program creates directory structure for a data science project
#
import os, errno

project_name = input("Enter project name: ")
project_location = input("Enter the project location: ")

# Check if the path exists
if not os.path.exists(project_location):
    print('Path doesn\'t exists')
    exit()

# Create the parent folder
try:
    os.makedirs(project_name)
except OSError as e:
    if e.errno == errno.EEXIST:
        print("Folder Already Exists ! Please change location or use other name")
    if e.errno != errno.EEXIST:
        raise

data_folder = 'data'
data_folders = ['raw', 'staging', 'processed']
doc_folder = 'docs'
doc_folders = ['project_reports', 'ppt']
code_folder = 'code'
code_folders = ['notebooks', 'code']

# Create folders for docs
os.makedirs('/'.join([project_location, project_name, doc_folder]))
for folders in doc_folders:
    os.makedirs('/'.join([project_location, project_name, doc_folder, folders]))

# Create folder for data
os.makedirs('/'.join([project_location, project_name, data_folder]))
for folders in data_folders:
    os.makedirs('/'.join([project_location, project_name, data_folder, folders]))

# Create code folder
os.makedirs('/'.join([project_location, project_name, code_folder]))
for folders in code_folders:
    os.makedirs('/'.join([project_location, project_name,code_folder,folders]))