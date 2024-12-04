import random
import string
from hard_disk import HardDisk
from file import File
# Generates random string according to size
def gen_random_string(length):
    letters = string.ascii_letters  # provides the alphabet as a string inside letters
    return ''.join(random.choice(letters.lower()) for i in range(length))  # random.choice chooses random letters from 'letters'

def gen_random_type():
    lst = ['txt', 'docx', 'pdf']
    return random.choice(lst)


hd1 = HardDisk(500)
file_names = []

# Giving new files random names
for i in range(10):
    new_file = File(gen_random_string(5), gen_random_type())
    new_file.size = 10
    hd1.add_file(new_file)
    file_names.append(new_file)

# Printing the files details with no content
for file in file_names:
    print(file)

# Changing content randomly in the files
for file in file_names:
    temp = random.randrange(10, 500)  # Generate a random number to use as the length for the string
    file.change_content(gen_random_string(temp))  # Generating a random string with length=temp
    hd1.update_file(file.name, file.size)  # Updating the file name and size in the hard disk

# Printing the file details and content after the change
for file in file_names:
    print(file)
    print(file.content + "\n")
print(hd1)
answer = input("Would you want to delete a file? enter its name or press Enter to end: ")
while len(answer) > 0:
    if answer in [file.name for file in file_names]:  # if answer == file.name inside file
        hd1.del_file(answer)
        file_names = [file for file in file_names if
                      file.name != answer]  # Making a new list using foreach file in file_names added if
        for file in file_names:
            print(file)
    else:
        print(f"Error: {answer} is not a valid file name")

    answer = input("Would you want to delete another file? enter its name or press Enter to end: ")

print(hd1)