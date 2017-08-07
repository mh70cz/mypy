"""CRUD files on Linux"""
import os
import datetime as dt
import shutil

exclude_folder_names = []
exclude_file_names = []
exclude_file_extensions = []
now = dt.datetime.now()

error_log = []

def main():


    rootFolders = [
        r"/home/mh70/Documents",
        r"/home/mh70/Pictures",
        r"/home/mh70/test"
    ]
    print_details = False

    iterate_over_files(rootFolders, print_details)

def iterate_over_files(rootFolders, print_details):
    """ iterarate over files"""
    grand_total_size = 0
    grand_file_count = 0
    for rootFolder in rootFolders:
        root_folder_size = 0
        root_file_count = 0
        for folderName, subfolders, filenames in os.walk(rootFolder):
            if folderName in exclude_folder_names:
                continue

            folder_total_size = 0
            folder_file_count = 0

            for filename in filenames:                
                if excludedFilenameOrExtension(filename):
                    continue
                path = folderName + "//" + filename
                timeModiTimeStamp = os.path.getmtime(path)
                size = os.path.getsize(path)
                folder_file_count += 1
                folder_total_size += size
            if print_details:
                print("folder: {0}   file count: {1:,}   size:   {2:,}"
                    .format(folderName, folder_file_count, folder_total_size))

            root_file_count += folder_file_count
            root_folder_size += folder_total_size              
        print("root folder: {0}   file count: {1:,}  size: {2:,}"
              .format(rootFolder, root_file_count, root_folder_size))

        grand_file_count += root_file_count
        grand_total_size += root_folder_size
    print("Grand total file count: {0:,}   Grand total file size: {1:,}"
          .format(grand_file_count, grand_total_size))

    def innerLoop():
        pass

def excludedFilenameOrExtension(filename):
    """return True if filename or file extension is in excluded list"""
    if filename in exclude_file_names:
        return True
    extension = os.path.splitext(filename)[-1].lower()
    # splits filename to a name and an extension (extension includes leading ".")
    # This method ignores leading periods so ".mp3" is not considered an mp3 file.
    # This is however the way a leading period should be treated.
    # E.g .gitignore is not a file format
    extension = extension[1:]
    if extension in exclude_file_extensions:
        return True


if __name__ == "__main__":
    main()
