import os
from pathlib import Path
from collections import defaultdict

def find_mp4_files(directory):
    path = Path(directory)
    return list(path.rglob("*.mp4"))


def only_filenames(files):
    dict_filenames = defaultdict(list)
    for file in files:
        full_path = Path(file).resolve()
        dict_filenames[file.name].append(full_path)
    return dict_filenames


def print_duplicates(dict_filenames):
    for key in dict_filenames.keys():
        if len(dict_filenames[key]) > 1:
            for path in dict_filenames[key]:
                full_path = Path(path).resolve()
                print(full_path)


def delete_duplicate_file(mp4_set, files_videos):
    for file in files_videos:
        if file.name in mp4_set:
            file_path = file.resolve();
            if os.path.exists(file_path):
                os.remove(file_path)
                print('deleted: ', file_path)

# scan archive directories

files_archive = find_mp4_files(".")
print(len(files_archive))

dict_filenames = only_filenames(files_archive)
print(len(dict_filenames.keys()))

print_duplicates(dict_filenames)

mp4_set = set(dict_filenames.keys())
print(len(mp4_set))


# delete duplicates in Videos
files_videos = find_mp4_files("../Videos")
print(len(files_videos))

delete_duplicate_file(mp4_set, files_videos)

print()