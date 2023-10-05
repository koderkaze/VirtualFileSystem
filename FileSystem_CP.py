#Developed by Kezzie Austin

import os

current_dir = "/"
#current_dir = root_dir +
directories = {"/": []}

# class directories:
#     def __init__(self):
#         self.listitems = {"/": []}
        
#     def append(self, listitem):
#         self.listitems = self.listitems + listitem

# making directories

def mkdir(name):

    global current_dir
    if current_dir != "/":
        dir_path = current_dir + "/"+name
    else:
        dir_path = current_dir + name    
            
    if dir_path not in directories:
        directories[dir_path] = []
        directories[current_dir].append(name)
        if current_dir != "/":
          print("Created directory: " + current_dir +"/" + name)
            
        else:
           print("Created directory: " + dir_path) #root > new dir
    else:
        print("Directory" ,name, "already exists!")


#listing files
def ls(dir_name = None):
    if dir_name == None:
        dir_name = current_dir #ls for current dir
    if dir_name.startswith("/"):
        dir_path = dir_name
    else:
        dir_path = current_dir + "/" + dir_name
        
    if dir_name in directories: #ls for specified dir
        print("Contents of", dir_path +":")
        for file in directories[dir_path]:
            print(file)
    else:
        print("'"+dir_name+"' not found.")

#changing directory
def cd(dir_name):
    global current_dir
    if dir_name == "..":
        if current_dir != "/":
            current_dir = current_dir.rsplit("/", 1)[0] or "/" #to update cd and maintain parent dir
    elif dir_name == "/":
            current_dir = "/"
    else:
           if dir_name.startswith("/"):
                dir_path = dir_name
           
           else:
                dir_path = current_dir + "/" + dir_name
            
           if dir_path in directories:
                current_dir = dir_path
    

           else:
                print("'"+dir_name+"'" + " not found.")
#creating files
def touch(file_name):
    directories[current_dir].append(file_name)
    print("Created file: " + current_dir+"/"+file_name)
    

# Main loop

print("Welcome to your Virtual Linux File System!")

print("Current directory: ",  current_dir)
while True:
    
    #split command from file/directory
    command = input(current_dir+"> ").strip()
    str_half = command.split()
    if not str_half:
        continue
    cmd = str_half[0]
    if cmd == "ls":
        if len(str_half) > 1:
             ls(current_dir +"/"+ str_half[1])
             
        else:
            ls()
            
    elif cmd == "mkdir":
        if len(str_half) > 1:
            mkdir(str_half[1])
        else:
            print("Try: 'mkdir <directory_name>'")
            
    elif cmd == "cd":
        if len(str_half) > 1:
            cd(str_half[1])
            
        else:
            print("Try: 'cd <directory_name>'")
    elif cmd == "touch":
        if len(str_half) > 1:
            touch(str_half[1])
        else:
            print("Try: 'touch <file_name>'")
    elif cmd == "exit":
        print("Now exiting the Virtual File System. Goodbye!")
        break
    else:
        print("VFS doesn't know command " +"'"+cmd+"'" +  "... Try available commands: ls, mkdir, cd, touch, exit")
