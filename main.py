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

#Check for devices
while True:
    clear()
    if len(devices()) == 0:
        print('Connect any device and press enter!')
        enter_to_continue()
    
    elif len(devices()) >= 1:
        break
##################

print('''
     _    ____  ____    _   _ _____ _     ____  _____ ____  
    / \  |  _ \| __ )  | | | | ____| |   |  _ \| ____|  _ \ 
   / _ \ | | | |  _ \  | |_| |  _| | |   | |_) |  _| | |_) |
  / ___ \| |_| | |_) | |  _  | |___| |___|  __/| |___|  _ < 
 /_/   \_\____/|____/  |_| |_|_____|_____|_|   |_____|_| \_\\ by purpl3
''')
enter_to_continue()

#Main Menu
while True:
    clear()

    print('''Functions: 
1). Apps
2). Send command and get output
3). Tweaks
4). Get installed packages
9). Exit''')
    
    mode = input('Select: ')
        
    if mode == '1':
        while True:
            clear()

            print('''Apps: 
1) Youtube vanced
9) Exit ''')

            app = input('Select: ')

            if app == '1':
                clear()
                print('Installing youtube vanced...')
                
                #micro g
                install_app('./microg.apk','https://github.com/purpl3-yt/Adb-Helper/blob/main/apps/microg-v0-2-25-224113.apk?raw=true')

                #vanced
                install_app('./vanced.apk','https://github.com/purpl3-yt/Adb-Helper/blob/main/apps/YouTube-Vanced-v17-32-38.apk?raw=true')

                if input('Uninstall official youtube (y,n): ').lower() == 'y':
                    print(adb('shell pm uninstall --user 0 com.google.android.youtube'))

                enter_to_continue()
                
            elif app == '9':
                break
                
            else:
                clear()
                print('App not found!')
                enter_to_continue()

    elif mode == '2':
        while True:
            clear()
            command = input('Enter command (without "adb", "exit" for exit): ')
            if command.lower() == 'exit':
                break
            print(adb(command))
            enter_to_continue()
        
    elif mode == '3':
        while True:
            clear()

            print('''Tweaks:
1) Remove nfc icon in status bar (miui, etc.)
9) Exit''')
                  
            tweak_mode = input('Enter an tweak: ')

            if tweak_mode == '1':
                print('Processing "adb shell settings put secure icon_blacklist nfc"')
                print(adb('shell settings put secure icon_blacklist nfc'))
                print('Done!')

            elif tweak_mode == '9':
                break

            else:
                print('Tweak not found!')
                enter_to_continue()

    elif mode == '4':
        clear()
        print(packages_list())
        enter_to_continue()

    elif mode == '9':
        print('Exit..')
        quit()

    else:
        clear()
        print('Mode not found!')
        enter_to_continue()