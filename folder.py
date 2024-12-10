from file import File

class Folder:
    def __init__(self, name='New Folder'):
        self.name = name
        self.files = []
        self.size = 0

    def add_file(self, file):
        ###Adds a file to the folder if it's not in it###
        if file not in self.files:
            self.files.append(file)
            self.size += file.size
            print(f"File {file.name} moved to Folder {self.name}")
            self.update_size()
        else:
            print(f"File {file.name} already exists in Folder {self.name}")

    def remove_file(self, file):
        ###Deletes a file in the folder if it's found###
        if file not in self.files:
            print(f"File {file.name} not found in Folder {self.name}")
        else:
            self.files.remove(file)
            self.update_size()
            print(f"File {file.name} removed from Folder {self.name}")

    def get_size(self):
    ###Returns the folder size###
        return f'Folder size: {self.size}'

    def __str__(self):
        files_str = '\n'.join(str(file) for file in self.files)
        return (f'Folder name: {self.name}\n'
                f'Folder size: {self.size}\n'
                f'File list:\n{files_str}\n')

    def change_name(self, name):
        self.name = name

    def update_size(self):
        ###Updates the folder size according to the files in it###
        self.size=0
        for file in self.files:
            self.size+=file.size
