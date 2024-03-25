import os
import shutil
import schedule
import time
from datetime import datetime

def copy_files(src_dir, dst_dir):
    # Tworzenie nowego folderu z aktualnym czasem jako nazwą
    new_folder = os.path.join(dst_dir, datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    os.makedirs(new_folder, exist_ok=True)

    # Kopiowanie plików
    for file_name in os.listdir(src_dir):
        src_file = os.path.join(src_dir, file_name)
        if os.path.isfile(src_file):
            shutil.copy(src_file, new_folder)

    # Usuwanie najstarszych folderów, jeśli ich liczba przekracza 5
    all_folders = [os.path.join(dst_dir, f) for f in os.listdir(dst_dir) if os.path.isdir(os.path.join(dst_dir, f))]
    all_folders.sort(key=os.path.getmtime)
    while len(all_folders) > 5:
        oldest_folder = all_folders.pop(0)
        shutil.rmtree(oldest_folder)
    print(str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) + " backup done")

# Ścieżki do folderów źródłowego i docelowego

dst_dir = 'C:\\Users\\qwedr\\Desktop\\bekap'
src_dir = 'C:\\Users\\qwedr\\AppData\\Roaming\\EldenRing\\76561198086944617'

# Planowanie zadania co 10 minut
schedule.every(10).minutes.do(copy_files, src_dir, dst_dir)

# Pętla, która uruchamia zaplanowane zadania
while True:
    schedule.run_pending()
    time.sleep(1)



