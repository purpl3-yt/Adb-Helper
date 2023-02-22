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
1). Install youtube vanced''')
    
    mode = input('Select: ')
        
    if mode == '1':
        if not screenstate():
            print('Please unlock your screen!')
            enter_to_continue() 
        clear()
        print('Installing youtube vanced...')
        
        #micro g
        print('Downloading micro G..')
        download('https://dwdisc.com/fdl/705107cd-6cd9-4a27-9bb9-ef340e5a248c/microg-v0-2-25-224113.apk','./microg.apk', replace=True)#micro g
        print('Installing micro G')

        wait(0.5)
        
        print(adb('install '+'microg.apk'))
        
        print('Delete micro G file')
        os.remove('./microg.apk')

        #print('Downloading youtube vanced..')

        #download('https://dwdisc.com/fdl/c538bf8b-9c46-48bb-a8fe-8a1b7b05e3d8/YouTube-Vanced-v17-32-38.apk','./')#youtube vanced
        enter_to_continue()
    else:
        clear()
        print('Mode not found!')
        enter_to_continue()