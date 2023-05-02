"""
This is a script that takes a screenshot of the Facebook ludo game while playing the game and records the dice movements of players. (modified)
"""

import cv2 as cv
import numpy as np
import os
from time import time
import win32gui, win32ui, win32con
from PIL import Image

os.chdir(os.path.dirname(os.path.abspath(__file__)))
# loop_time = time()

def get_screenshot():
    hwnd_target = 0x30011c #Edge handle be used for test 
    left, top, right, bot = win32gui.GetWindowRect(hwnd_target)
    w, h = 640, 1140

    hdesktop = win32gui.GetDesktopWindow()
    hwndDC = win32gui.GetWindowDC(hdesktop)
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    saveDC.SelectObject(saveBitMap)
    result = saveDC.BitBlt((-640, -360), (1280, 1500), mfcDC, (left, top), win32con.SRCCOPY)
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    im = Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hdesktop, hwndDC)

    if result == None:
        return cv.cvtColor(np.array(im), cv.COLOR_RGB2BGR)

def match():
    pass
files=[]
prev_player = ''
while(True):
    screenshot = get_screenshot()

    image_folder = r'D:\code\misc\Ludo_analysis\diceimages'
    for filename in os.listdir(image_folder):
        dice_img = cv.imread(os.path.join(image_folder, filename))
        result = cv.matchTemplate(screenshot, dice_img, cv.TM_SQDIFF_NORMED)
        threshold = 0.005
        locations = np.where(result <= threshold)
        locations = list(zip(*locations[::-1]))

        if locations:
            
            if locations[0][0] < 200 and locations [0][1] > 500: player = 'player 1'
            elif locations[0][0] < 200 and locations [0][1] < 500: player = 'player 2'
            elif locations[0][0] > 200 and locations [0][1] < 500: player = 'player 3'
            elif locations[0][0] > 200 and locations [0][1] > 500: player = 'player 4'
            # print(locations)
            if prev_player != player: print(f'Found Dice {filename[5]} by {player}.')
            prev_player = player
            dice_w = dice_img.shape[1]
            dice_h = dice_img.shape[0]
            line_color = (0, 255, 0)
            line_type = cv.LINE_4

            # Loop over all the locations and draw their rectangle
            for loc in locations:
                # Determine the box positions
                top_left = loc
                bottom_right = (top_left[0] + dice_w, top_left[1] + dice_h)
                # Draw the box
                cv.rectangle(screenshot, top_left, bottom_right, line_color, line_type)

            
            # cv.waitKey()
            #cv.imwrite('result.jpg', haystack_img)

        # else:
        #     print('Dice not found.')
        cv.imshow('Matches', screenshot)
        # cv.imshow('Computer Vision', screenshot)

    # debug the loop rate
    # print('FPS {}'.format(1 / (time() - loop_time)))
    # loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')