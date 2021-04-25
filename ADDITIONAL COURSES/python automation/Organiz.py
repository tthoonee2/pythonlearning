SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}
 
def pickdirectory(value): #THIS FUNCTION gives the possibility to distribute a file based on the suffix of it.
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
    return 'MISC'
            
            
print(pickdirectory('pdf'))

import os #a folder made for file handling and organizing
from pathlib import Path
def organizedirectory():
    for item in os.scandir(): #scans directory
        if item.is_dir(): 
            continue
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        directory = pickdirectory(filetype)
        directoryPath = Path(directory)
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        filePath.rename(directoryPath.joinpath(filePath))
        
        
            
        