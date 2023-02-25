from download import download
import os, sys

os.chdir(sys.path[0])

def clear():
    '''Clear output'''

    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    
def enter_to_continue():
    '''Something like "pause" in batch files'''

    return input('Press any key for continue: ')

def adb(command: str):
    '''Return output from adb'''

    return os.popen('./platform-tools/adb  '+command).read()

def screenstate():
    '''Get screenstate (bad)'''

    state = str(adb("shell dumpsys power | grep 'mHoldingWakeLockSuspendBlocker='").replace('  mHoldingWakeLockSuspendBlocker=','')).replace(' ','').replace('\n','')

    if state == 'true':#screen unlocked
        return True
    elif state == 'false':#screen locked
        return False

def devices():
    '''Get connected devices'''

    _devices = str(adb('devices'))

    devices_ = []

    for device in _devices.split('\n')[1:]:
        if device != '':
            devices_.append(repr(device[:str(repr(device)).find('\\t')]).replace('\\t',''))

    return devices_

def packages_list():

    packages = []

    for package in adb('shell pm list packages').split('\n'):
        packages.append(str(package[package.find('package:')+len('package:'):]))

    return packages[:-1]

def install_app(apk: str, apk_link: str = None):
    '''Install app by apk'''

    if apk_link!=None:
        if not os.path.isfile(apk):
            print('Download: '+apk)
            download(apk_link,'./'+apk, replace=True)
        
    print('Installing: '+apk)

    print(adb('install '+sys.path[0]+'/'+apk))

    print('Installed!')

    print('Delete apk file to save memory!')

    os.remove(apk)#remove apk to save memory

