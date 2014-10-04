import random
import os
import shutil


def zeros(list_length):
    """Return the zfill parameter"""
    return len(str(list_length))


def clean_up(name):
    """Clean the destination folder and recreate"""
    if os.path.isdir(name):
        shutil.rmtree(name)

    make_destination_dir(name)


def make_destination_dir(name):
    """Create the destination directory"""
    if not os.path.isdir(name):
        os.mkdir(name)


def make_filename(index, file, zfill_param):
    """Make a new name to the file"""
    filename, fileextension = os.path.splitext(file)
    filename = str(index + 1).zfill(zfill_param)
    return filename + fileextension


def main():
    """All the dirty work"""

    # CONFIGURATION
    destinationDIR = "destination"

    # All files from the current folder (folders excluded)
    # Files with extension "py" are excluded so this file won't be copied
    list = [x for x in os.listdir() if not os.path.isdir(x) and x[-2:] != "py"]

    # List length and numbers of digits of the maximum index
    list_length = len(list)
    zfill_param = zeros(list_length)

    # Remove and create the folder again
    clean_up(destinationDIR)

    # copy one by one at random order
    logfileString = ""
    for index, file in enumerate(random.sample(list, list_length)):
        filename = make_filename(index, file, zfill_param)

        shutil.copy2(file, destinationDIR + "/" + filename)

        # Log file
        logfileString += "%s equivalent to %s\n" % (filename, file)

    with open(destinationDIR + "/logfile.txt", "w") as logfile:
        logfile.write(logfileString)

if __name__ == '__main__':
    main()
