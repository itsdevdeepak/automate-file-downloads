from shutil import move
from os import listdir, makedirs
from os.path import expanduser, isfile, join, exists, splitext
from time import sleep

DOWNLOADS_DIR = expanduser("~/Downloads")

# TODO: Add More Extension and Manage them acordint to os i.e. Compressed_exts = linux_compressed_exts + windows_compressed_ext + ... 
# Or something like that more organized 

DOCUMENTS_EXTS = { ".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ods", ".ppt", ".pptx", ".txt", ".md" }     
EXECUTABLES_EXT = { ".exe", ".msi", ".mst", ".msp", ".appimage", ".rpm", ".tgz", ".deb" }
IMAGES_EXTS = { ".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".bmp", ".dib", ".heif", ".heic", ".jp2", ".j2k", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz" }
COMPRESSED_EXTS = { ".RAR", ".zip", ".tar", ".tar.gz", ".7z", ".zz" }
AUDIO_EXT = { ".m4a", ".flac", ".mp3", ".wav", ".wma", ".aac" }
VIDEO_EXT = { ".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd" }

def file_extension_of(file: str):
    return "." + file.split(".")[-1].lower()

def get_file_type_of_extension(file_extension: str):
    file_type = "undefined"
    if file_extension in DOCUMENTS_EXTS: 
        file_type = "document"
    elif file_extension in EXECUTABLES_EXT:
        file_type = "executable"
    elif file_extension in IMAGES_EXTS:
        file_type = "image"
    elif file_extension in COMPRESSED_EXTS:
        file_type = "compressed"
    elif file_extension in AUDIO_EXT:
        file_type = "audio"
    elif file_extension in VIDEO_EXT:
        file_type = "video"
    return file_type

def get_new_file_name(name: str, dest: str):
    filename, extension = splitext(name)
    counter = 1

    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1
    return name

def move_file(file: str, source_path: str, destination_path: str):
    destination_file_path = join(destination_path, file)
    source_file_path = join(source_path, file)
    if (exists(destination_file_path)): 
        destination_file_path = join(destination_path, get_new_file_name(file, destination_path))
    move(source_file_path, destination_file_path)
        

def make_folder_and_return_path(folder: str, directory_path: str):
    if (not exists(directory_path)): raise FileNotFoundError("{} does not exist!".format(directory_path))
    folder_path = join(directory_path, folder) 
    if (not exists(folder_path)): makedirs(folder_path)
    return folder_path

def move_file_to_correct_destination(file: str, current_directory_path: str):
    file_type = get_file_type_of_extension(file_extension_of(file))
    if file_type == "document":
        move_file(file, current_directory_path, make_folder_and_return_path("Documents", current_directory_path))
    elif file_type == "executable":
        move_file(file, current_directory_path, make_folder_and_return_path("Executable", current_directory_path))
    elif file_type == "compressed":
        move_file(file, current_directory_path, make_folder_and_return_path("Compressed", current_directory_path))
    elif file_type == "image":
        move_file(file, current_directory_path, make_folder_and_return_path("Images", current_directory_path))
    elif file_type == "audio":
        move_file(file, current_directory_path, make_folder_and_return_path("Media/Audio", current_directory_path))
    elif file_type == "video":
        move_file(file, current_directory_path, make_folder_and_return_path("Media/Video", current_directory_path))
    elif file_type == "undefined":
        move_file(file, current_directory_path, make_folder_and_return_path("Others", current_directory_path))

def filesInDirectory(dir):
    files = [file for file in listdir(dir) if isfile(join(dir, file))]
    return files

# TODO: Make Driver Function Zzz
while True:
    files = filesInDirectory(DOWNLOADS_DIR)
    if files:
        for file in files:
            move_file_to_correct_destination(file, DOWNLOADS_DIR)
    sleep(60)