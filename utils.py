import os, sys
import subprocess

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    
def enter_to_continue():
    return input('Press any key for continue: ')

def adb(command: str):

    return os.popen('./platform-tools/adb  '+command).read()

def screenstate():

    state = str(adb("shell dumpsys power | grep 'mHoldingWakeLockSuspendBlocker='").replace('  mHoldingWakeLockSuspendBlocker=','')).replace(' ','').replace('\n','')

    if state == 'true':#screen unlocked
        return True
    elif state == 'false':#screen locked
        return False