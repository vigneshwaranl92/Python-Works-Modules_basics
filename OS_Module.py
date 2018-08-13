import os

print(os.path)
os.chdir('C:\\Users\\HP\\Desktop\\PYTHON WORKS\\')


os.chdir('C:\\Users\\HP\\Desktop\\..\\..')
print(os.getcwd())
os.chdir('C:\\Users\\HP\\Desktop\\PYTHON WORKS\\')
#os.mkdir('C:\\Users\\HP\\Desktop\\PYTHON WORKS\\Python_Path_Creation_Testing')
print(os.getcwd())
#os.removedirs('C:\\Users\\HP\\Desktop\\PYTHON WORKS\\Python_Path_Creation_Testing')
print(os.path.exists('C:\\Users\\HP\\Desktop\\PYTHON WORKS\\Python_Path_Creation_Testing'))

