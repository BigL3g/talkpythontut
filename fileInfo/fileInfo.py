import os, datetime

for folderName, subfolders, filenames in os.walk('c:\\merge'):
    print('In directory: ' + folderName)

    for txtname in filenames:
        pathName = folderName + '\\'
        fileinfo = str(datetime.datetime.fromtimestamp(int(os.path.getmtime(pathName+txtname))))
        print(txtname + ' Last Modified: ' + fileinfo)

    print('')
