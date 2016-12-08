import os

def rename_files():
    # 1. Get file names from a folder
    file_list = os.listdir(r"C:\Users\ababen\Desktop\prank")
    print(file_list)

    os.chdir(r"C:\Users\ababen\Desktop\prank")
    
    # 2. For each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "1234567890"))

rename_files()
