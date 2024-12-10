# Example of Hard Disk usage with folders and files
from hard_disk import HardDisk
from file import *
from folder import *

hd1=HardDisk(1000)
print(hd1)
for i in range (3):
    hd1.add_folder(Folder(gen_random_string(5).title()))

#Creating random files and adding them into the folders
for folder in hd1.folders:
    for i in range (3):
        file = File(gen_random_string(5).title(),gen_random_type())
        content_len = random.randint(10,50)
        file.add_content(gen_random_string(content_len))
        folder.add_file(file)
    print(folder)

#randomly updating files contents to change sizes
for folder in hd1.folders:
    for file in folder.files:
        file.change_content(gen_random_string(random.randint(10,250))) # Generating random string with length of 10-250
    folder.update_size()
    print(folder)

hd1.update_used_space()
print(hd1)
delete=input(f"To delete file choose 1 To delete folder choose 2, Enter otherwise: ")
while len(delete)>0:
    if delete == '1':
        answer = input("Enter file name to delete: ")
        while len(answer) > 0:
            found=False
            for folder in hd1.folders:
                for file in folder.files:
                    if file.name == answer:
                        folder.remove_file(file)
                        found = True
                        hd1.update_used_space()
                        break
                if found:
                    break
            if not found:
                print(f"File {answer} not found")
            print(hd1)
            answer=input("Enter file name to delete, press Enter otherwise: ")
    elif delete == '2':
        answer = input("Enter folder name to delete: ")
        while len(answer) > 0:
            hd1.delete_folder(answer)
            print(hd1)
            answer = input("Enter folder name to delete, press Enter otherwise: ")
    delete = input(f"To delete file choose 1 To delete folder choose 2, Enter otherwise: ")
print(hd1)
print('Program finished!')
