from file import File
from folder import Folder


class HardDisk:
    def __init__(self, size):
        self.size = size
        self.folders = []
        self.used_space = 0

    def __str__(self):
        folders = '\n'.join(str(folder) for folder in self.folders)
        return (f"HD Size: {self.size}\n"
                f"File list:\n{folders}\n"
                f"Used space: {self.used_space}\n")

    def free_space(self):
        self.update_used_space()
        return self.size - self.used_space

    def update_used_space(self):
        self.used_space = 0
        for folder in self.folders:
            for file in folder.files:
                self.used_space += file.size

    def add_file_to_folder(self, file: File, folder: Folder):
        if folder in self.folders:
            if file not in folder:
                if file.size <= self.free_space():
                    self.folders.append(file)
                    self.update_used_space()
                else:
                    print(f"Not enough space for file {file}")
            else:
                print(f"File {file} already exists in folder {folder}")

    def del_file(self, file_name: str):
        for folder in self.folders:
            if file_name in folder:
                self.folders.remove(file_name)
                print(f"File {file_name} deleted")
                self.update_used_space()
                break
        else:
            print(f"File {file_name} not found")

    def delete_folder(self, folder_name: str):
        found = False
        for folder in self.folders:
            if folder_name == folder.name:
                self.folders.remove(folder)
                found = True
                print(f"Folder {folder} deleted")
                self.update_used_space()
        if not found:
            print(f"Folder {folder_name} not found")


    def update_file(self, file_name: str, new_size: int, folder:Folder):
        found = False
        for file in folder.files:
            if file_name == file.name:
                found = True
                old_size = file.size
                temp_size = new_size - old_size
                if self.free_space() >= temp_size:
                     file.size = new_size
                     self.update_used_space()
                     print(F"File {file_name} updated")
                else:
                     print(f"Not enough space to update file {file_name}")
                break
        if not found:
            print(f"File {file_name} not found")

    def add_folder(self, folder: Folder):
        if folder not in self.folders:
            self.folders.append(folder)
