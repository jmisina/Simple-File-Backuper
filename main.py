import os
import shutil
import schedule
import time
from datetime import datetime

def copy_files(src_dir, dst_dir):
    # New folder creation with current date and time as a folder name
    new_folder = os.path.join(dst_dir, datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    os.makedirs(new_folder, exist_ok=True)

    # Copying files
    for file_name in os.listdir(src_dir):
        src_file = os.path.join(src_dir, file_name)
        if os.path.isfile(src_file):
            shutil.copy(src_file, new_folder)

    # Deleting eldest files if their number is over 5 
    all_folders = [os.path.join(dst_dir, f) for f in os.listdir(dst_dir) if os.path.isdir(os.path.join(dst_dir, f))]
    all_folders.sort(key=os.path.getmtime)
    while len(all_folders) > 5:
        oldest_folder = all_folders.pop(0)
        shutil.rmtree(oldest_folder)
    print(str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) + " backup done")

# Directory paths
dst_dir = '' # Path for directory for files to be copied into
src_dir = '' # Path for directory from which the files should be copied from

# Scheduling the task every ten minutes
schedule.every(10).minutes.do(copy_files, src_dir, dst_dir)

# Main loop
while True:
    schedule.run_pending()
    time.sleep(1)



