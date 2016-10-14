import os 

def rename_files():
    file_list = os.listdir(r".\prank")
    path = os.getcwd()
    os.chdir(r".\prank")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
        print("File "+ file_name+ " has been renamed to "+ file_name.translate(None, "0123456789"))
    # changing back to original path 
    os.chdir(path)

rename_files()