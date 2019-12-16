#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image


class VideoCap():
    def __init__(self):

        self.cap_cam = cv2.VideoCapture(0)
        # self.cap_cam.set(cv2.CV_CAP_PROP_EXPOSURE, 10)
        self.width = self.cap_cam.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.cap_cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.count = self.cap_cam.get(cv2.CAP_PROP_FRAME_COUNT)
        self.fps = self.cap_cam.get(cv2.CAP_PROP_FPS)
        print(self.width, self.height, self.count, self.fps)

    def run(self):
        # print(self.cap_cam.isOpened())
        if self.cap_cam.isOpened() is not True:
            print("Video is not ready!!")

        while self.cap_cam.isOpened():
            # for i in range(len(self.cap_cam)):
            ret, frame = self.cap_cam.read()
            # print(len(frame))
            # print(frame[1])
            index_blight = int(np.sum(frame) / self.height / self.width)
            print(index_blight)
            # cv2.putText(frame, index_blight, (0, 50),
            # cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 5)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(frame_rgb)
            draw = ImageDraw.Draw(pil_image)
            font = ImageFont.truetype(
                '/usr/share/fonts/truetype/takao-gothic/TakaoGothic.ttf', 50)
            draw.text((10, 10), str(index_blight), font=font)
            rgb_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

            cv2.imshow('Frame', rgb_image)
            if cv2.waitKey(int(1000 / self.fps)) >= 0:
                break

            #     print(self.cap_cam.get)


if __name__ == "__main__":
    video_capture = VideoCap()
    video_capture.run()
