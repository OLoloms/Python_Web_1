import os
import time
import concurrent.futures
import pathlib

# Directory extension and name matching dictionary
extensions = {
    ('.jpeg','.png','.jpg','.svg'): 'images',
    ('.avi', '.mp4', '.mov', 'mkv'): 'videos',
    ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'): 'documents',
    ('.mp3', '.ogg', '.wav', '.amr'): 'musics',
    ('.zip', '.gz', '.tar', '.7z'):'archives',
    (): 'unknown_extensions'}

def create_directories(path: str):
    """A function that creates folders from the specified names"""
    try:
        for name in extensions.values():
            if not os.path.exists(name):
                os.mkdir(os.path.join(path, name))
        return 'Папки успішно створені'
    except:
        return 'При створені папок виникла помилка'


def check_suffix(path: str):
    """A function that checks for extensions """
    extension = pathlib.Path(path).suffix
    return extension

def return_folder_name(suffix: str):
    """A function that matches directory extension and name"""
    name = ''
    for key in extensions:
        if suffix in key:
            name = extensions[key]
    if name:
        return name
    return 'unknown_extensions'

def make_transfer(path: str, target: str, name_folder:str):
    """A function that moves a file to a folder when sorting """
    file_name = pathlib.Path(path).name
    os.rename(path, f'{target}\{name_folder}\{file_name}')

def remove_empty_folder(directory_path: str):
    """A function that deletes empty folders"""
    try:
        os.rmdir(directory_path)
        print(f"Empty directory '{directory_path}' successfully deleted.")
    except OSError as e:
        print(f"Error deleting directory: {e}")

def traverse_folder(original_folder, target_folder):
    """A function that traverse the contents of a folder"""
    entries = os.listdir(original_folder)

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = []
        for entry in entries:
            time.sleep(0.5)  
            future = executor.submit(process_entry, original_folder, entry, target_folder)
            futures.append(future)


def process_entry(path, entry, target_folder):
    """A function that handles each entry"""
    entry_path = os.path.join(path, entry)

    if os.path.isdir(entry_path):
        traverse_folder(entry_path, target_folder)
        remove_empty_folder(entry_path)
    else:
        suffix = check_suffix(entry_path)
        name_folder = return_folder_name(suffix=suffix)
        make_transfer(entry_path, target_folder, name_folder)
        

if __name__ == '__main__':
    original_folder = r'C:\folder_2'
    target_folder = r'C:\folder'
    create_directories(target_folder)
    traverse_folder(original_folder=original_folder, target_folder=target_folder)