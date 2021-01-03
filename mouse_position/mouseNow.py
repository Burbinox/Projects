#! python3
# Program is printing current mouse position all the time
# Run it via CMD!, program works only in Windows.

import pyautogui

print('Program is printing current mouse position all the time')
print('Press Ctrl+C to end program ')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone')
