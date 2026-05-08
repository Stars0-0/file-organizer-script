

import os
import shutil

def organize_folder(folder_path):
    
    # Dictionary mapping category names to file extensions
    file_types={
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        "Audio": [".mp3", ".wav", ],
        "Videos": [".mp4", ".avi", ".mov"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Code": [".py", ".js", ".html", ".css", ".java", ".cpp"],
        "Others": []
    }
    
    # Create category folders if they don't exist
    for category in file_types.keys():
        category_path = os.path.join(folder_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)  
            
            
    for filename in os.listdir(folder_path):
        
        #Build the full path -e.g. "/home/user/Downloads/file.txt"
        file_path = os.path.join(folder_path, filename)
        
        #Skip subfolders - only process actual files
        if not os.path.isfile(file_path):
            continue
        
        #Split the filename into name and extension - e.g. ("Report", ".pdf")
        _, extension = os.path.splitext(filename)
        extension = extension.lower()  # Convert to lowercase for case-insensitive matching
        moved = False
        
        #Find which category this extention belongs to
        destination_folder = "Others"  # Default category
        for folder_name, extensions in file_types.items():
            if extension in extensions:
                destination_folder = folder_name
                break
            
        #Build the full path for the destination subfolder
        destination_path = os.path.join(folder_path, destination_folder)
        
        #Create the subfolder if it doesnt exist yet
        os.makedirs(destination_path, exist_ok=True)
        
        #Move the file into the subfolder
        shutil.move(file_path, os.path.join(destination_path, filename))
        print(f"Moved: {filename} to {destination_folder}")
        
#Ask the user which folder to organize
folder_path = input("Enter the path of the folder to organize: ")
organize_folder(folder_path)
print("Folder organization complete!")