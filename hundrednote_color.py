# -*- coding: utf-8 -*-
import cv2
import itertools
import time
import os
import numpy as np
import configparser
from config import HN_colorStylePath, globalConfigPath, styleSheetPath, HN_colorConfigPath

stylecode = open(HN_colorStylePath, 'r', encoding="utf-8").read()
config = configparser.ConfigParser()
config.read(globalConfigPath)
debug = False if {section: dict(config[section]) for section in config.sections()}['config'][
                     'debug_subtitle'] == "0" else True

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
config2 = configparser.ConfigParser()
config2.read(HN_colorConfigPath, encoding='utf-8')
config_dict = {section: dict(config2[section]) for section in config2.sections()}
for key, subkey in config_dict.items():
    if 'filter_lower' in subkey:
        subkey['filter_lower'] = [int(i) for i in subkey['filter_lower'].split(',')]
    if 'filter_upper' in subkey:
        subkey['filter_upper'] = [int(i) for i in subkey['filter_upper'].split(',')]
    subkey['disabled'] = 'disabled' in subkey and config2.getboolean(key, 'disabled')

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
    # yuito_rate = get_color_rate(img, np.array([132, 92, 229]), np.array([138, 118, 255]))
    # raika_rate = get_color_rate(img, np.array([20, 158, 231]), np.array([25, 194, 255]))
    # keigo_rate = get_color_rate(img, np.array([0, 0, 183]), np.array([0, 0, 200]))
    # lightgreen_rate = get_color_rate(img, np.array([69, 100, 230]), np.array([76, 121, 255]))
    # brown_rate = get_color_rate(img, np.array([11, 71, 157]), np.array([21, 111, 175]))
    # brightgreen_rate = get_color_rate(img, np.array([49, 163, 247]), np.array([55, 205, 255]))
    # skyblue_rate = get_color_rate(img, np.array([91, 187, 218]), np.array([95, 242, 255]))
    # rate_list = [yuito_rate, raika_rate, keigo_rate, lightgreen_rate, brown_rate, skyblue_rate, brightgreen_rate]
    # people_list = ["yuito", "raika", "keigo", "lightgreen", "brown", "skyblue", "brightgreen"]
    people_list = [key for key in config_dict
                   if 'filter_lower' in config_dict[key] and 'filter_upper' in config_dict[key]
                   and not config_dict[key]['disabled']]
    rate_list = [get_color_rate(img, np.array(subkey['filter_lower']), np.array(subkey['filter_upper']))
                 for key, subkey in config_dict.items()
                 if 'filter_lower' in config_dict[key] and 'filter_upper' in config_dict[key]
                 and not config_dict[key]['disabled']]
    max_rate = max(rate_list)
    if max_rate < 0.2:
        return "undefined"
    else:
        return people_list[rate_list.index(max_rate)]


def people2style(people):
    return config_dict[people]['style']


def add_sub(subtext, begintime, endingtime, subpeople):
    global sub_num
    style = people2style(subpeople)
    newsub = f'Dialogue: 1,{begintime},{endingtime},{style},{subpeople},0,0,0,,{subtext}{str(sub_num) if debug else ""}\n'

    outputFile.write(newsub)
    sub_num += 1


# 视频帧总数
current_frame_num = begin_frame_num = last_frame_num = 0
last_pic_hash = ''
op = trans = False
op_match_times = op_bg_num = 0
identity_pass = []
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
    global people
    global Err
    global outputFile
    global identity_pass

    outputFile = open(subpath, 'w', encoding='utf-8')
    outputFile.write(subtitle_head.replace("$$FILE$$", os.path.abspath(videopath)))
    source_video = cv2.VideoCapture(videopath)
    global op_bg_num
    isOpened = bool(source_video.isOpened())
    if isOpened:
        frame_rate = round(source_video.get(5), 2)
        while True:
            ret, frame = source_video.read()
            if not ret:
                break

            current_pic = frame[950:1050, 910:1100]
            assert 0 not in current_pic.shape, "视频分辨率应为1920*1080"
            pic_current_hash = phash(current_pic)
            hmdistant = hamming_distance(last_pic_hash, pic_current_hash)

            # if hamming_distance(switch_hash,'1000110001011000111100100000000000000000000000000000000000000000') < 5:
            #     trans = True  # 识别转场
            if (hmdistant > 16) and (current_frame_num != 0):
                # if current_frame_num - last_frame_num > (frame_rate / 2):
                if current_frame_num - last_frame_num > (frame_rate / 2) - 5:
                    center_count = len(identity_pass) // 2 - 1
                    people = get_people(identity_pass[center_count])

                    print('%3s | %-5d <-> %-5d | hmdst: %-3d | gap: %-3d | %s --> %s | %s'
                          % (sub_num, begin_frame_num, current_frame_num - 1, hmdistant,
                             current_frame_num - last_frame_num,
                             frames_to_timecode(frame_rate, begin_frame_num),
                             frames_to_timecode(frame_rate, current_frame_num), people))

                    add_sub("示范性字幕" if debug else "", frames_to_timecode(frame_rate, begin_frame_num),
                            frames_to_timecode(frame_rate, current_frame_num), people)

                begin_frame_num = current_frame_num
                last_frame_num = current_frame_num
                identity_pass.clear()

            last_pic_hash = pic_current_hash
            people_pic = frame[980:1050, 910:1100]

            # identify by slide window
            if current_frame_num % 2 == 0:
                identity_pass.append(people_pic)

            current_frame_num += 1
    else:
        print("源视频读取出错")
        Err = True
    print("finish!")
    end = time.time()
    print(f'耗时：{str(end - start)}秒')
    return Err
