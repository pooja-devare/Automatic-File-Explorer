import os, shutil

path = r"C:/Users/pooja/OneDrive/Desktop/file_explo/"
file_name = os.listdir(path)
print(file_name)

folder_name = ['csv files', 'images files', 'pdf files']

for loop in range(0,3):
    if not os.path.exists(path+folder_name[loop]):
        os.makedirs(path+folder_name[loop])

for file in file_name:
    if ".csv" in file and not os.path.exists(path+"csv files/"+file):
        shutil.move(path+file, path+"csv files/"+file)
    elif ".jpg" in file and not os.path.exists(path+"images files/"+file):
        shutil.move(path+file, path+"images files/"+file)
    elif ".pdf" in file and not os.path.exists(path+"pdf files/"+file):
        shutil.move(path+file, path+"pdf files/"+file)

        