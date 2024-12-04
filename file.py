class File:
    def __init__(self, name, file_type):
        self.name = str(name)
        self.size = 0
        self.content = ""
        self.type = file_type

    def __str__(self):
        return (f"File Name: {self.name}\n"
                f"File Size: {str(self.size)} MB\n"
                f"File Type: {self.type}\n")

    def change_name(self, name):
        self.name = name
        print(f"New file name: {self.name}")

    def change_type(self, file_type):
        self.type = file_type
        if self.type == 'pdf':
            self.size_calc()
        print(f"File type changed: {self.type}")

    def change_content(self, content):
        self.content = content
        self.size_calc()
        print("File updated successfully.")

    def add_content(self, content):
        self.content += content
        self.size_calc()
        print("File updated successfully.")

    def size_calc(self):
        if self.type == 'pdf':
            self.size = (len(self.content) / 5)
        else:
            self.size = (len(self.content) / 10)  # every 10 characters equal to 1 in size
        print(f"Calculated size: {self.size} MB")

