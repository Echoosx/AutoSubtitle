# -*- coding: utf-8 -*-
import cv2
import itertools
import time
import os
import numpy as np
import configparser

# import easygui as eg

stylecode = open('config/flag.txt', 'r', encoding="utf-8").read()
config = configparser.ConfigParser()
config.read('config/config.ini')
debug = False if {section: dict(config[section]) for section in config.sections()}['config'][
                     'debugsubtext'] == "0" else True

opening_old = ['1000011010001100010000000000000000000000000000000000000000000000',
               '1100100000010000110010111001011101100100001000000001001011000001',
               '1100100000010000110010111001011001100100001000000001001011000001']
opening_new = ['1110010111001100000100010111000010010000000100000001001100000110',
               '1110010110001110000100110010001010011000000110000000001100000110',
               '1101010010110011010000111001000101100000000100000011100010000001']

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
    mobuo_rate = get_color_rate(img, np.array([100, 185, 225]), np.array([110, 225, 255]))
    flag_rate = get_color_rate(img, np.array([27, 155, 240]), np.array([37, 215, 255]))
    renai_rate = get_color_rate(img, np.array([150, 70, 225]), np.array([160, 90, 255]))
    seizon_rate = get_color_rate(img, np.array([75, 150, 230]), np.array([80, 190, 255]))
    mobumi_rate = get_color_rate(img, np.array([20, 90, 245]), np.array([25, 120, 255]))
    lightpurple_rate = get_color_rate(img, np.array([123, 101, 181]), np.array([132, 131, 222]))
    dongyun_rate = get_color_rate(img, np.array([0, 83, 225]), np.array([10, 125, 255]))
    yanghong_rate = get_color_rate(img, np.array([160, 147, 202]), np.array([173, 194, 255]))
    siturenn_rate = get_color_rate(img, np.array([90, 75, 205]), np.array([95, 145, 255]))
    darkgreen_rate = get_color_rate(img, np.array([70, 210, 120]), np.array([75, 255, 155]))
    # rose_rate = get_color_rate(img, np.array([160, 210, 195]), np.array([165, 250, 240]))
    rose_rate = 0
    kami_rate = get_color_rate(img, np.array([25, 110, 245]), np.array([35, 130, 255]))
    darkred_rate = get_color_rate(img, np.array([175, 240, 210]), np.array([180, 255, 225]))
    green_rate = get_color_rate(img, np.array([62, 79, 205]), np.array([70, 255, 255]))
    hametsu_rate = get_color_rate(img, np.array([85, 209, 181]), np.array([90, 255, 211]))
    nana_rate = get_color_rate(img, np.array([7, 151, 240]), np.array([10, 187, 255]))
    red_rate = get_color_rate(img, np.array([175, 148, 214]), np.array([180, 175, 251]))
    lightpink_rate = get_color_rate(img, np.array([161, 104, 232]), np.array([169, 134, 255]))
    blue_rate = get_color_rate(img, np.array([119, 115, 221]), np.array([122, 134, 249]))

    narrator_rate = get_color_rate(img, np.array([0, 0, 225]), np.array([175, 5, 255]))
    rate_list = [mobuo_rate, flag_rate, renai_rate, seizon_rate, mobumi_rate, blue_rate, lightpurple_rate, dongyun_rate, red_rate,
                 yanghong_rate, siturenn_rate, darkgreen_rate, rose_rate, kami_rate, darkred_rate,
                 green_rate, hametsu_rate, nana_rate, lightpink_rate]
    people_list = ["mobuo", "flag", "renai", "seizon", "mobumi", "blue", "lightpurple", "dongyun", "red", "yanghong",
                   "siturenn", "darkgreen", "rose", "kami", "darkred", "green", "hametsu", "nana", "lightpink"]
    max_rate = max(rate_list)
    if (max_rate < 0.2):
        if (len([x for x in rate_list if x > 4]) > 1):
            return "undefined"
        elif (narrator_rate > 25):
            return "narrator"
        else:
            return "undefined"
    return people_list[rate_list.index(max_rate)]


def people2style(people):
    config = configparser.ConfigParser()
    config.read('config/style.ini', encoding='utf-8')

    style_dict = {section: dict(config[section]) for section in config.sections()}['flag']
    return style_dict[people.lower()]


def add_sub(subtext, begintime, endingtime, subpeople):
    global sub_num
    style = people2style(subpeople)
    newsub = f'Dialogue: 1,{begintime},{endingtime},{style},{subpeople},0,0,0,,{subtext}{str(sub_num) if debug else ""}\n'

    outputFile.write(newsub)
    sub_num += 1


def add_op(frame_rate, begin_frame_num, new=False):
    if not new:
        add_sub("没有任何优点的路人男", frames_to_timecode(frame_rate, begin_frame_num),
                frames_to_timecode(frame_rate, begin_frame_num + (1.87 * frame_rate)), "Opening")
        add_sub("在路人男面前出现的女孩，她的真实身份是...?", frames_to_timecode(frame_rate, begin_frame_num + (1.87 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (4.57 * frame_rate)), "Opening")
        add_sub("死亡flag?", frames_to_timecode(frame_rate, begin_frame_num + (4.57 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (5.77 * frame_rate)), "Opening")
        add_sub("路人男能成功回避死亡flag吗!?", frames_to_timecode(frame_rate, begin_frame_num + (5.77 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (8.47 * frame_rate)), "Opening")
        add_sub("全力回避flag酱!", frames_to_timecode(frame_rate, begin_frame_num + (8.47 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (10.84 * frame_rate)), "Opening")
    else:
        add_sub("立起来了!", frames_to_timecode(frame_rate, begin_frame_num + (2.63 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (3.59 * frame_rate)), "Opening")
        add_sub("全力回避flag酱!", frames_to_timecode(frame_rate, begin_frame_num + (4.9 * frame_rate)),
                frames_to_timecode(frame_rate, begin_frame_num + (6.61 * frame_rate)), "Opening")


# 视频帧总数
current_frame_num = begin_frame_num = last_frame_num = 0
last_pic_hash = ''
op = trans = False
op_match_times = op_bg_num = 0
sub_num = 1
Err = False


def autosub(videopath, subpath, newOP=False):
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
    global outputFile
    opening = opening_new if newOP else opening_old
    # subtitle = subtitle_head.replace("$$FILE$$", os.path.abspath(videopath))
    outputFile = open(subpath, 'w', encoding='utf-8')
    outputFile.write(subtitle_head.replace("$$FILE$$", os.path.abspath(videopath)))
    source_video = cv2.VideoCapture(videopath)
    global op_bg_num
    isOpened = bool(source_video.isOpened())
    if isOpened:
        frame_rate = round(source_video.get(5), 2)
        while True:
            ret, frame = source_video.read()
            # print(current_frame_num)
            if not ret:
                break

            current_pic = frame[950:1045, 810:910]
            assert 0 not in current_pic.shape, "视频分辨率应为1920*1080"
            pic_current_hash = phash(current_pic)
            hmdistant = hamming_distance(last_pic_hash, pic_current_hash)

            switch_pic = frame[940:1060, 360:1540]
            switch_hash = phash(switch_pic)

            if op_match_times < 2:
                match_op_pic = frame
                match_op_hash = phash(match_op_pic)
                # print(match_op_hash)
                # print(hamming_distance(match_op_hash, opening[0]))
                # print(op_match_times)
                if match_op_hash in opening:
                    if op_match_times == 0:
                        print(str(current_frame_num) + " | 开场白起点")
                        op_bg_num = current_frame_num
                        add_op(frame_rate, op_bg_num, newOP)
                    op = bool(1 - op)
                    op_match_times += 1
                    if op_match_times == 2:
                        # print(str(current_frame_num) + " | 开场白结束")
                        print(f'{str(op_bg_num)} <-> {str(current_frame_num)} | 开场白')
                    begin_frame_num = last_frame_num = current_frame_num + 15
                if op:
                    current_frame_num += 1
                    # print(match_op_hash)
                    continue

            if hamming_distance(switch_hash, '1010010011000000101010001100000001000100000001011000011010100000') < 10:
                trans = True  # 识别转场
            if (hmdistant > 13) and (current_frame_num != 0):
                if current_frame_num - last_frame_num > (frame_rate / 2):
                    people = get_people(people_pic)
                    if trans:
                        people = "trans"
                        trans = False
                        begin_frame_num += int(frame_rate / 10)

                    print(
                        f'{sub_num} | {current_frame_num - 1} <-> {current_frame_num} | hmdst: {hmdistant} | gap: {current_frame_num - last_frame_num} | {frames_to_timecode(frame_rate, begin_frame_num)} --> {frames_to_timecode(frame_rate, current_frame_num)} | people: {people}')

                    add_sub("示范性字幕" if debug else "", frames_to_timecode(frame_rate, begin_frame_num),
                            frames_to_timecode(frame_rate, current_frame_num), people)

                begin_frame_num = current_frame_num
                last_frame_num = current_frame_num

            last_pic_hash = pic_current_hash
            people_pic = frame[940:1040, 800:1100]
            people_hash = phash(people_pic)
            current_frame_num += 1
    else:
        print("源视频读取出错")
        Err = True
    print("finish!")
    # if not Err:
    #     with open(subpath, 'w+', encoding='utf-8') as q:
    #         q.write(subtitle)
    end = time.time()
    print(f'耗时：{str(end - start)}秒')
    return Err
