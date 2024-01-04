import os
def create_file(name ,extension):
    a = open(f"{name}.{extension}","w")
    a.close()
def read_file(name, extension):
    a = open(f"{name}.{extension}","r")
    data = a.readlines()
    b = 0
    for i in data:
        b += 1
        print(f"Line{b}: {i}")
def create_folder(name):
    os.mkdir(f"{name}")
def delete_file(name, extension):
    os.remove(f"{name}.{extension}")
def delete_folder(name):
    os.removedirs(f"{name}")
def delete_all():
    a = os.listdir()
    b ="."
    for i in a:
        if i.endswith(f"main.py"):
           print(f"{i} cannot be removed ")
        else:
            try:
               os.remove(f"{i}")
            except Exception as e:
                try:
                    os.removedirs(f"{i}")
                except Exception as e:
                    print(f"We are sorry for the error")
def create_range_of_files(start , stop, name , extension):
    try:
        for i in range(int(start),int(stop) + 1):
            a = open(f"{name}{i}.{extension}","w")
            a.close()
    except Exception as e:
        print(f"{e} is an invalid input")
def create_range_of_folders(start , stop, name):
    try:
        for i in range(int(start),int(stop) + 1):
            os.mkdir(f"{name}{i}")
    except Exception as e:
        print(f"{e} is an invalid input")
def write_file(name,extension):
    a = open(f"{name}.{extension}","w")
    lines_written = 0
    line_open = 0
    while line_open == 0:
        line = str(input("Enter the line you want to write: "))
        lines_written += 1
        a.write(str(f"{line} \n"))
        try:
            line_open_add_value = int(input("Enter 0 to add more lines(or any other value to stop): "))
        except Exception as e:
            print(f"{e} is an invalid input")
        line_open += line_open_add_value
    print(f"{lines_written} lines were written")
def append_file(name,extension):
    a = open(f"{name}.{extension}","a")
    lines_appended = 0
    line_open = 0
    while line_open == 0:
        line = str(input("Enter the line you want to apppend: "))
        lines_appended += 1
        a.write(str(f"{line} \n"))
        try:
            line_open_add_value = int(input("Enter 0 to add more lines(or any other value to stop): "))
        except Exception as e:
            print(f"{e} is an invalid input")
        line_open += line_open_add_value
    print(f"{lines_appended} lines were appended")
    a.close()
def delete_range_of_files(start,stop,name,extension):
    for i in range(start,stop + 1):
        if os.path.exists(f"{name}{i}.{extension}"):
            os.remove(f"{name}{i}.{extension}")
        else:
            print(f"{name}{i}.{extension} was not found")
    print(f"{stop - start} {name}.{extension} files were deleted")
def delete_range_of_folders(start,stop,name):
    for i in range(start,stop + 1):
        if os.path.exists(f"{name}{i}"):
            os.removedirs(f"{name}{i}")
        else:
            print(f"{name}{i} was not found")
    print(f"{stop - start} folders were deleted")
options = ["create_file(0)","read_file(1)","create_folder(2)","delete_file(3)","delete_folder(4)","delete_all(5)","create_range_of_files(6)","create_range_of_folders(7)","write_file(8)","append_file(9)","delete_range_of_files(10)","delete_range_of_folders(11)"]
a = 0
while a == 0:
    print("Hello you are welcome to this program made by Rouhin Roy")
    for i in options:
        print(f"{i}")
    try:
        choice = int(input("Enter your choice(in numbers as per the data given above): "))
        print(f" You chose {options[choice]}")
        try:
            match choice:
                case 0:
                    try:
                        name = input("Enter the name of the file you want to create: ")
                        extension = input("Enter the extension of the file: ")
                        create_file(name,extension)
                        print(f"{name}.{extension} was created")
                    except Exception as e:
                        print(f"{e} is an invalid input")      
                case 1:
                    try:
                        name = input("Enter the name of the file you want to open: ")
                        extension = input("Enter the extension of the file: ")
                        read_file(name,extension)
                        print(f"{name}.{extension} was opened")
                    except Exception as e:
                        print(f"{e} is an invalid input")       
                case 2:
                    try:
                        name = input("Enter the name of the folder you want to create: ")
                        create_folder(name)
                        print(f"{name} Folder was created")
                    except Exception as e:
                        print(f"{e} is an invalid input")       
                case 3:
                    try:
                        name = input("Enter the name of the file you want to delete: ")
                        extension = input("Enter the extension of the file: ")
                        delete_file(name,extension)
                        print(f"{name}.{extension} was deleted")
                    except Exception as e:
                        print(f"{e} is an invalid input")  
                case 4:
                    try:
                        name = input("Enter the name of the folder you want to delete: ")
                        delete_folder(name)
                        print(f"{name} Folder was deleted")
                    except Exception as e:
                        print(f"{e} is an invalid input")   
                case 5:
                    try:
                        delete_all()
                        print(f"All files except main.py were deleted.")
                    except Exception as e:
                        print(f"{e} is an invalid input")  
                case 6:
                    try:
                        start = int(input("Enter the start value: "))
                        stop = int(input("Enter the stop value: "))
                        name = input("Enter the name of the files: ")
                        extension = input("Enter the extension of the files: ")
                        create_range_of_files(start , stop, name, extension)
                        print(f"{stop - start} {name}.{extension} files were created")
                    except Exception as e:
                        print(f"{e} is an invalid input")
                case 7:
                    try:
                        start = int(input("Enter the start value: "))
                        stop = int(input("Enter the stop value: "))
                        name = input("Enter the name of the folders: ")
                        create_range_of_folders(start , stop, name)
                        print(f"{stop - start} {name},{extension} files were created")
                    except Exception as e:
                        print(f"{e} is an invalid input")
                case 8:
                    try:
                        name = input("Enter the name of the files: ")
                        extension = input("Enter the extension of the files: ")
                        write_file(name,extension)
                    except Exception as e:
                        print(f"{e} is an invalid output")
                case 9:
                    try:
                        name = input("Enter the name of the files: ")
                        extension = input("Enter the extension of the files: ")
                        text = input("Enter what you want to append(write (backslash(\) + n) for new line): ")
                        append_file(name,extension,text)
                    except Exception as e:
                        print(f"{e} is an invalid output")
                case 10:
                    try:
                        name = input("Enter the name of the files: ")
                        extension = input("Enter the extension of the files: ")
                        start = int(input("Enter the start value: "))
                        stop = int(input("Enter the stop value: "))
                        delete_range_of_files(start,stop,name,extension)
                    except Exception as e:
                        print(f"{e} is an invalid output")
                case 11:
                    try:
                        name = input("Enter the name of the folders: ")
                        start = int(input("Enter the start value: "))
                        stop = int(input("Enter the stop value: "))
                        delete_range_of_folders(start,stop,name)
                    except Exception as e:
                        print(f"{e} is an invalid output")
        except Exception as e: 
            print(f"{e} is an invalid input")              
    except Exception as e:
        print(f" {e} is an invalid input")
    try: 
        b = int(input("Enter 0 to continue(or any other number to stop): "))
    except Exception as e:
        print(f"{e} is an invalid input")
    a = a + b
    

    
    
        
    


