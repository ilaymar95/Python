from file import File

class HardDisk:
    def __init__(self,size):
        self.size = size
        self.file_list=[]
        self.used_space=0

    def __str__(self):
        return (f"HD Size: {self.size}\n"
                f"File list: {self.file_list}\n"
                f"Used space: {self.used_space}\n")

    def free_space(self):
        return self.size - self.used_space

    def update_space(self,size):
        self.used_space += size

    def update_used_space(self):
        temp=0
        for file in self.file_list:
            temp+= file.size
        self.used_space=temp

    def add_file(self,file: File):
        if file not in self.file_list:
            if file.size <= self.free_space():
                self.file_list.append(file)
                self.update_space(file.size)
            else:
                print(f"Not enough space for file {file}")
        else:
            print(f"File {file} already exists")
        self.update_used_space()


    def del_file(self,file_name: str):
        found = False
        for i in range(len(self.file_list)):
            if self.file_list[i].name == file_name:
                # self.used_space-=self.file_list[i].size
                del self.file_list[i]
                found=True
                print(f"File {file_name} deleted")
                break

        if not found:
            print(f"File {file_name} not found")
        self.update_used_space()


    def update_file(self,file_name,new_size):
        found = False
        for file in self.file_list:
            if file_name == file.name:
                found=True
                old_size = file.size
                temp_size = new_size - old_size
                if self.free_space()>=temp_size:
                    file.size=new_size
                    self.update_space(temp_size)
                    print(F"File {file_name} updated")
                else:
                    print(f"Not enough space to update file {file_name}")
                break
        if not found:
            print(f"File {file_name} not found")
        self.update_used_space()