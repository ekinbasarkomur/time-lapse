#!/usr/bin/env python

import pyautogui
import time
import os
import cv2
import numpy as np
import imutils
import ffmpeg

rate = 1
ss_path = "spot_3d"

OUTPUT_OPTIONS = {
    'crf': 20,
    'preset': 'slower',
    'movflags': 'faststart',
    'pix_fmt': 'yuv420p'
}

videos_path = "/home/ekin/Videos"
take = 1

while os.path.isdir(os.path.join(videos_path, ss_path, "take_{}".format(take))):
    take += 1
save_path = os.path.join(videos_path, ss_path, "take_{}".format(take))
os.mkdir(save_path)


id = 1
sleep_time = 1.0/rate


try:
    while True:
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        cv2.imwrite(os.path.join(save_path, "{}.png".format(id)), image)

        print("Screen Shot: ", id )        
        id += 1
        time.sleep(sleep_time)
except KeyboardInterrupt:
    (
        ffmpeg
        .input('{}/*.png'.format(save_path), pattern_type='glob', framerate=25)
        .output('{}/take_{}.mp4'.format(save_path,take), **OUTPUT_OPTIONS)
        .run()
    )
    print("Got {} images at: {}".format(id+1, save_path))
