from time import sleep as wait
from download import download
from utils import *
import os, sys
os.chdir(sys.path[0])

if os.name == 'nt':
    print('This tool work only on Linux/Unix systems!')
    quit()

#Download platform-tools
if not os.path.isdir('platform-tools'):
    print('Installing platform tools....')

    link = 'https://dl.google.com/android/repository/platform-tools_r33.0.3-linux.zip'

    download(link, './', 'zip', replace=True)


    os.system('chmod u+x ./platform-tools/adb')

#######################


#Main Menu
while True:
    clear()

    print('''Functions: 
1). Install youtube vanced
2). Send command and get output''')
    
    mode = input('Select: ')
        
    if mode == '1':
        if not screenstate():
            print('Please unlock your screen!')
            enter_to_continue() 
        clear()
        print('Installing youtube vanced...')
        
        #micro g
        print('Downloading micro G..')
        download('https://github.com/purpl3-yt/Adb-Helper/blob/main/apps/microg-v0-2-25-224113.apk?raw=true','./microg.apk', replace=True)#micro g
        print('Installing micro G')

        wait(0.5)
        
        print(adb('install '+'microg.apk'))
        
        print('Delete micro G file')
        os.remove('./microg.apk')

        #vanced
        print('Downloading youtube vanced..')

        download('https://github.com/purpl3-yt/Adb-Helper/blob/main/apps/YouTube-Vanced-v17-32-38.apk?raw=true','./vanced.apk')#youtube vanced
        print('Installing youtube vanced')

        print(adb('install '+'vanced.apk'))
        print('Delete micro G file')
        os.remove('./vanced.apk')

        if input('Uninstall official youtube (y,n): ').lower() == 'y':
            print(adb('shell pm uninstall --user 0 com.google.android.youtube'))

    elif mode == '2':
        while True:
            clear()
            command = input('Enter command (without "adb", "exit" for exit): ')
            if command.lower() == 'exit':
                break
            print(adb(command))
            enter_to_continue()
        

    else:
        clear()
        print('Mode not found!')
        enter_to_continue()