# -*- coding: utf-8 -*-
import cv2
import itertools
import time
import os
import sys
import numpy as np
import configparser

# import easygui as eg

stylecode = open('config/mixed.txt', 'r', encoding="utf-8").read()
config = configparser.ConfigParser()
config.read('config/config.ini')
debug = False if {section: dict(config[section]) for section in config.sections()}['config']['debugsubtext'] == "0" else True

opening = ['1001000110010001011010010110011010010110010010010100101010010010',
           '1100001101101100001111101101001111100001001111101001011101101001']

subtitle_head = """
[Script Info]
Title: AutoSubtitle Aegisub file
ScriptType: v4.00+
WrapStyle: 2
ScaledBorderAndShadow: yes
YCbCr Matrix: None
PlayResX: 1920
PlayResY: 1080

[Aegisub Project Garbage]
Audio File: $$FILE$$
Video File: $$FILE$$

[V4+ Styles]
""" + stylecode + """

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""


def phash(img):
    # 加载并调整图片为32x32灰度图片
    img = cv2.resize(img, (8, 8), interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img.astype(np.float32)
    # 离散余弦变换
    img = cv2.dct(img)
    hash_str = ''
    img = img[0:8, 0:8]
    avg = sum(img[i, j] for i, j in itertools.product(range(8), range(8)))
    avg = avg / 64
    # 获得hsah
    for i, j in itertools.product(range(8), range(8)):
        hash_str = f'{hash_str}1' if img[i, j] > avg else f'{hash_str}0'
    return hash_str


def get_color_rate(frame, lower, upper):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    ratio_green = cv2.countNonZero(mask) / (frame.size / 3)
    colorPercent = (ratio_green * 100)
    return np.round(colorPercent, 2)


def hamming_distance(str1, str2):
    # 计算汉明距离
    if len(str1) != len(str2):
        return 0
    return sum(str1[i] != str2[i] for i in range(len(str1)))


def isset(v):
    try:
        type(eval(v))
    except NameError:
        return 0
    return 1


def frames_to_timecode(framerate, frames):
    # 视频 通过视频帧转换成时间|framerate: 视频帧率|frames: 当前视频帧数|return:时间（00:00:01.001）
    return '{0:02d}:{1:02d}:{2:02d}.{3:02d}'.format(int(frames / (3600 * framerate)),
                                                    int(frames / (60 * framerate) % 60),
                                                    int(frames / framerate % 60),
                                                    int(frames / framerate % 1 * 100))


def get_people(img):
    Q_rate_1 = get_color_rate(img, np.array([0, 210, 245]), np.array([180, 210, 255]))
    Q_rate_2 = get_color_rate(img, np.array([0, 190, 195]), np.array([180, 200, 255]))
    E_rate = get_color_rate(img, np.array([85, 95, 140]), np.array([95, 110, 255]))
    W_rate_1 = get_color_rate(img, np.array([15, 110, 245]), np.array([30, 110, 255]))
    W_rate_2 = get_color_rate(img, np.array([15, 190, 245]), np.array([30, 210, 255]))
    darkgreen_rate = get_color_rate(img, np.array([75, 90, 135]), np.array([85, 210, 255]))
    gray_rate = get_color_rate(img, np.array([5, 50, 155]), np.array([15, 75, 180]))
    brown_rate = get_color_rate(img, np.array([15, 55, 180]), np.array([23, 135, 195]))
    orange_rate = get_color_rate(img, np.array([10, 240, 240]), np.array([15, 255, 255]))
    lightgreen_rate = get_color_rate(img, np.array([60, 70, 235]), np.array([70, 90, 250]))
    flesh_rate = get_color_rate(img, np.array([0, 95, 230]), np.array([10, 115, 255]))
    pink_rate = get_color_rate(img, np.array([145, 105, 240]), np.array([150, 120, 255]))
    khaki_rate = get_color_rate(img, np.array([20, 75, 230]), np.array([25, 100, 255]))

    rate_list = [Q_rate_1, Q_rate_2, W_rate_1, W_rate_2, E_rate, darkgreen_rate, gray_rate, brown_rate, orange_rate,
                 lightgreen_rate, flesh_rate, pink_rate, khaki_rate]
    people_list = ["Q", "Q", "W", "W", "E", "darkgreen", "gray", "brown", "orange", "lightgreen", "flesh", "pink",
                   "khaki"]

    max_rate = max(rate_list)
    if max_rate < 0.2 or len([x for x in rate_list if x > 4]) > 1:
        # print(people_list)
        # print(rate_list)
        return "undefined"
    # return "undefined"
    return people_list[rate_list.index(max_rate)]


def people2style(people):
    config = configparser.ConfigParser()
    config.read('config/style.ini', encoding='utf-8')

    style_dict = {section: dict(config[section]) for section in config.sections()}['mixed-blood']
    return style_dict[people.lower()]


def add_sub(subtext, begintime, endingtime, subpeople):
    global sub_num
    global subtitle
    style = people2style(subpeople)
    if debug:
        subtitle = (
                f'{subtitle}Dialogue: 1,{begintime},{endingtime},{style},{subpeople}'
                + ",0,0,0,,"
                + subtext
                + str(sub_num)
                + "\n"
        )
    else:
        subtitle = (
                f'{subtitle}Dialogue: 1,{begintime},{endingtime},{style},{subpeople}'
                + ",0,0,0,,"
                + subtext
                + "\n"
        )

    sub_num += 1


def add_op(frame_rate, begin_frame_num):
    add_sub("三人经营着的万事屋所在之处是…", frames_to_timecode(frame_rate, begin_frame_num),
            frames_to_timecode(frame_rate, begin_frame_num + (2.5 * frame_rate)), "Opening")
    add_sub("转生到异世界的地球！", frames_to_timecode(frame_rate, begin_frame_num + (2.5 * frame_rate)),
            frames_to_timecode(frame_rate, begin_frame_num + (4.8 * frame_rate)), "Opening")
    add_sub("吸血鬼，僵尸—影千夜", frames_to_timecode(frame_rate, begin_frame_num + (4.8 * frame_rate)),
            frames_to_timecode(frame_rate, begin_frame_num + (6.2 * frame_rate)), "Opening")
    add_sub("雪女，康娜卡姆依—冰雨", frames_to_timecode(frame_rate, begin_frame_num + (6.2 * frame_rate)),
            frames_to_timecode(frame_rate, begin_frame_num + (7.5 * frame_rate)), "Opening")
    add_sub("狼人，荷鲁斯—希迪", frames_to_timecode(frame_rate, begin_frame_num + (7.58 * frame_rate)),
            frames_to_timecode(frame_rate, begin_frame_num + (8.88 * frame_rate)), "Opening")
    add_sub("混血万事屋", frames_to_timecode(frame_rate, begin_frame_num + (9.83 * frame_rate)),
            frames_to_timecode(frame_rate, begin_frame_num + (11.5 * frame_rate)), "Opening")


# 视频帧总数
current_frame_num = begin_frame_num = last_frame_num = 0
last_pic_hash = ''
op = trans = False
op_match_times = op_bg_num = 0
sub_num = 1
Err = False


def autosub(videopath, subpath):
    start = time.time()
    global op_match_times
    global op
    global trans
    global last_pic_hash
    global current_frame_num
    global begin_frame_num
    global last_frame_num
    global subtitle
    global sub_num
    global current_pic
    global pic_current_hash
    global hamdistant
    global people_pic
    global people_hash
    global people
    global Err
    subtitle = subtitle_head.replace("$$FILE$$", os.path.abspath(videopath))
    source_video = cv2.VideoCapture(videopath)
    global op_bg_num
    isOpened = bool(source_video.isOpened())
    if isOpened:
        frame_rate = round(source_video.get(5), 2)
        while True:
            ret, frame = source_video.read()
            # print(current_frame_num)
            if ret == False:
                break

            current_pic = frame[950:1045, 810:910]
            assert 0 not in current_pic.shape, "视频分辨率应为1920*1080"
            pic_current_hash = phash(current_pic)
            hmdistant = hamming_distance(last_pic_hash, pic_current_hash)

            if op_match_times < 2:
                match_op_pic = frame
                match_op_hash = phash(match_op_pic)
                # print(hamming_distance(match_op_hash,opening[0]))
                if match_op_hash in opening:
                    if op_match_times == 0:
                        # print(str(current_frame_num) + " | 开场白起点")
                        op_bg_num = current_frame_num
                        add_op(frame_rate, begin_frame_num)
                    op = bool(1 - op)
                    op_match_times += 1
                    if op_match_times == 2:
                        # print(str(current_frame_num) + " | 开场白结束")
                        print(
                            f'{str(op_bg_num)} <-> '
                            + str(
                                current_frame_num + int((28 / 17) * frame_rate)
                            )
                            + " | 开场白"
                        )

                        begin_frame_num = current_frame_num + int((28 / 17) * frame_rate)
                        last_frame_num = begin_frame_num
                if (op):
                    current_frame_num += 1
                    # print(match_op_hash)
                    continue

            # print(str(current_frame_num)+" | "+ match_op_hash)
            if (hmdistant > 13) and (current_frame_num != 0):
                if current_frame_num - last_frame_num > (frame_rate / 2):
                    people = get_people(people_pic)

                    print(
                        f'{str(sub_num)} | {str(current_frame_num - 1)} <-> '
                        + str(current_frame_num)
                        + " | hmdst: "
                        + str(hmdistant)
                        + " | gap: "
                        + str(current_frame_num - last_frame_num)
                        + " | "
                        + frames_to_timecode(frame_rate, begin_frame_num)
                        + " --> "
                        + frames_to_timecode(frame_rate, current_frame_num)
                        + " | people: "
                        + people
                    )

                    add_sub("示范性字幕" if debug else "", frames_to_timecode(frame_rate, begin_frame_num),
                            frames_to_timecode(frame_rate, current_frame_num), people)

                begin_frame_num = current_frame_num
                last_frame_num = current_frame_num

            last_pic_hash = pic_current_hash
            people_pic = frame[940:1060, 700:1300]
            people_hash = phash(people_pic)
            current_frame_num += 1
    else:
        print("源视频读取出错")
        Err = True
    print("finish!")
    if not Err:
        with open(subpath, 'w+', encoding='utf-8') as q:
            q.write(subtitle)
    end = time.time()
    print(f'耗时：{str(end - start)}秒')
    return Err
