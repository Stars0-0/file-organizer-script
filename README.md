# file-organizer-script
A lightweight Python script that automatically categorizes and sorts files into dedicated folders based on their extensions.



File Organizer Script is a Python-based utility designed to declutter messy directories. By scanning a target folder, it intelligently identifies file types (Images, Documents, Code, etc.) and moves them into organized subdirectories, saving you the manual effort of digital housekeeping.


Features

    Smart Categorization: Automatically maps common extensions to folders like Archives, Code, and Documents.

    Case-Insensitive Matching: Handles .JPG and .jpg with the same logic.

    Safety First: Skips subfolders and handles existing directories without overwriting data.

    "Others" Fallback: Ensures no file is left behind, even if its extension isn't explicitly defined.