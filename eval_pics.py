#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np


class VideoCap():
    def __init__(self):
        self.cap_cam = cv2.VideoCapture(0)
        # 幅
        self.width = self.cap_cam.get(cv2.CAP_PROP_FRAME_WIDTH)
        # 高さ
        self.height = self.cap_cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
        # 総フレーム数
        self.count = self.cap_cam.get(cv2.CAP_PROP_FRAME_COUNT)
        # fps
        self.fps = self.cap_cam.get(cv2.CAP_PROP_FPS)
        print(self.width, self.height, self.count, self.fps)

    def run(self):
        # print(self.cap_cam.isOpened())
        if self.cap_cam.isOpened() is not True:
            print("Video is not ready!!")

        while True:
            # for i in range(len(self.cap_cam)):
            ret, frame = self.cap_cam.read()
            # print(len(frame))
            # print(frame[1])
            print(int(np.sum(frame) / self.height / self.width))
            cv2.imshow('Frame', frame)

            #     print(self.cap_cam.get)


if __name__ == "__main__":
    video_capture = VideoCap()
    video_capture.run()


# print(type(cap_cam))
# <class 'cv2.VideoCapture'>
