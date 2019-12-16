#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image


class VideoCap():
    def __init__(self):

        self.cap_cam_1 = cv2.VideoCapture(1)
        self.cap_cam_2 = cv2.VideoCapture(2)
        # self.cap_cam.set(cv2.CV_CAP_PROP_EXPOSURE, 10)
        self.width_1 = self.cap_cam_1.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height_1 = self.cap_cam_1.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.count_1 = self.cap_cam_1.get(cv2.CAP_PROP_FRAME_COUNT)
        self.fps_1 = self.cap_cam_1.get(cv2.CAP_PROP_FPS)
        self.width_2 = self.cap_cam_2.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height_2 = self.cap_cam_2.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.count_2 = self.cap_cam_2.get(cv2.CAP_PROP_FRAME_COUNT)
        self.fps_2 = self.cap_cam_2.get(cv2.CAP_PROP_FPS)
        print(self.width_1, self.height_1, self.count_1, self.fps_1)

    def run(self):
        # print(self.cap_cam.isOpened())
        if self.cap_cam_1.isOpened() or self.cap_cam_2.isOpened() is not True:
            print("Video is not ready!!")

        video_buf = []

        while self.cap_cam_1.isOpened() and self.cap_cam_2.isOpened():
            ret_1, frame_1 = self.cap_cam_1.read()
            video_buf.append(frame_1)
            ret_2, frame_2 = self.cap_cam_2.read()

            vel_odom = 0.5  # 現在2sec遅れ。何らかの手法でスピードを取ってきて入れたい。
            time_diff = 1 / vel_odom
            if len(video_buf) > self.fps_1 * time_diff:
                buf_frame_pop_temp = video_buf.pop(0)
                target_hist_1 = cv2.calcHist(
                    [buf_frame_pop_temp], [0], None, [256], [0, 256])
                target_hist_2 = cv2.calcHist(
                    [frame_2], [0], None, [256], [0, 256])
                ret = cv2.compareHist(target_hist_1, target_hist_2, 0)
                print(ret)
                # print(target_hist_1)
                # print(target_hist_2)

                cv2.imshow('Frame_1', buf_frame_pop_temp)
                cv2.imshow('Frame_2', frame_2)
                if cv2.waitKey(int(1000 / self.fps_1)) >= 0:
                    break

            # cv2.putText(frame, index_blight, (0, 50),
            # cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 5)
            # frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # pil_image = Image.fromarray(frame_rgb)
            # draw = ImageDraw.Draw(pil_image)
            # font = ImageFont.truetype(
            #     '/usr/share/fonts/truetype/takao-gothic/TakaoGothic.ttf', 50)
            # draw.text((10, 10), str(index_blight), font=font)
            # rgb_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

            # cv2.imshow('Frame', rgb_image)
            # if cv2.waitKey(int(1000 / self.fps)) >= 0:
            #     break

            #     print(self.cap_cam.get)


if __name__ == "__main__":
    video_capture = VideoCap()
    video_capture.run()
