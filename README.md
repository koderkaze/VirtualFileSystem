# VirtualFileSystem


The Virtual Linux File System is a simple command-line python program that simulates a file system. This program does not interact with your computer's actual file system. 

## Features

- Create directories using the `mkdir` command.
- Change directories using the `cd` command.
- Create files using the `touch` command.
- List the contents of directories using the `ls` command.

## Getting Started

To run the Virtual Linux File System program, you can:

1. Run the program by opening the project solution in Visual Studio.

2. Run the program by entering the following command:
   
   ```
   python FileSystem_CP.py
   ```

**Note that the .py file must be downloaded for both methods**

## Usage

Here are some example commands to get you started:

- Create a directory:
   
   ```
   mkdir myfolder
   ```

- Change to a directory:
   
   ```
   cd myfolder
   ```

- Create a file:
   
   ```
   touch myfile.txt
   ```

- List the contents of the current directory:
   
   ```
   ls
   ```

- Exit the program:
   
   ```
   exit
   ```

## Notes

- The program primarily uses relative paths, except from when switching from root folder to a new directory. You should use the syntax as followed:
  
  ```
  cd /myfolder
  ```


