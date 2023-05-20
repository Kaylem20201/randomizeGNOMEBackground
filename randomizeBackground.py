import subprocess
import os
import random

def main() :
    FILEPATH = get_background_dir()

    BACKGROUND_PATHS = get_background_paths(FILEPATH)

    #current background may come from gnome's own folder, check the name at the end instead
    CURR_BACKGROUND_NAME = get_current_gnome_background_name()
    print(CURR_BACKGROUND_NAME)

    random_index = random.randrange(0,len(BACKGROUND_PATHS))
    while (CURR_BACKGROUND_NAME in BACKGROUND_PATHS[random_index]) :
        random_index = random.randrange(0,len(BACKGROUND_PATHS))
    new_background_path = BACKGROUND_PATHS[random_index]

    set_current_gnome_background(new_background_path)
    return

def get_background_dir() :
    HOME_PATH = os.environ['HOME']
    FILEPATH = HOME_PATH + "/Pictures/Backgrounds/"
    return FILEPATH

def get_background_paths(background_dir) :
    FILES = list(filter(os.DirEntry.is_file, os.scandir(background_dir)))
    FILENAMES = [x.path for x in FILES]
    print(FILENAMES)
    return FILENAMES

def get_current_gnome_background_name() :
    OUTPUT = subprocess.run("gsettings get org.gnome.desktop.background picture-uri", shell=True, capture_output=True)
    FILEPATH = OUTPUT.stdout.decode()
    #byte output is surrounded with single quotes and ended with \n
    FILENAME = os.path.basename(FILEPATH).rstrip("'\n")
    return FILENAME

def set_current_gnome_background(background_path) :
    normalized_path = "\"" + background_path + "\""
    subprocess.run("gsettings set org.gnome.desktop.background picture-uri " + normalized_path, shell=True)
    return

main()
