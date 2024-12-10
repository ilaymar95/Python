import string
import random
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
        ###Changes the content of the file, using a string that the function gets and updates the file size###
        self.content = content
        self.size_calc()
        print("File updated.")

    def add_content(self, content):
        ###Adds content into a file, using a string and updates the file size###
        self.content += content
        self.size_calc()
        print("File updated.")

    def size_calc(self):
        ###Updates the file size - PDF size is doubled###
        if self.type == 'pdf':
            self.size = (len(self.content) / 5)
        else:
            self.size = (len(self.content) / 10)  # every 10 characters equal to 1 in size

    def __eq__(self, other):
        if isinstance(other,File):
            return self.name == other.name and self.size == other.size and self.type == other.type
        return False


def gen_random_string(length):
    ###Generates a random string of letters the size of length###
    letters = string.ascii_letters  # provides the alphabet as a string inside letters
    return ''.join(random.choice(letters.lower()) for i in range(length))  # random.choice chooses random letters from 'letters'

def gen_random_type():
    ###Generates a random file type from list = ['txt','docx,'pdf']###
    lst = ['txt', 'docx', 'pdf']
    return random.choice(lst)