# -*- coding: utf-8 -*-
import cv2
import time
import os
import sys
import numpy as np
import easygui as eg

opening = ['1000011010001100010000000000000000000000000000000000000000000000','1100100000010000110010111001011101100100001000000001001011000001']

def phash(img):
    #加载并调整图片为32x32灰度图片
    img = cv2.resize(img, (8, 8), interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img.astype(np.float32)
    #离散余弦变换
    img = cv2.dct(img)
    img = img[0:8, 0:8]
    avg = 0
    hash_str = ''
    #计算均值
    for i in range(8):
        for j in range(8):
            avg += img[i, j]
    avg = avg/64
    #获得hsah
    for i in range(8):
        for j in range(8):
            if img[i, j] > avg:
                hash_str = hash_str+'1'
            else:
                hash_str = hash_str+'0'
    return hash_str

def get_color_rate(frame,lower,upper):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    ratio_green = cv2.countNonZero(mask)/(frame.size/3)
    colorPercent = (ratio_green * 100)
    return np.round(colorPercent, 2)

def hamming_distance(str1, str2):
    #计算汉明距离
    if len(str1) != len(str2):
        return 0
    count = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    return count

def isset(v): 
    try : 
        type (eval(v)) 
    except : 
        return  0  
    else : 
        return  1  


def frames_to_timecode(framerate,frames):
    # 视频 通过视频帧转换成时间|framerate: 视频帧率|frames: 当前视频帧数|return:时间（00:00:01.001）
    return '{0:02d}:{1:02d}:{2:02d}.{3:02d}'.format(int(frames / (3600 * framerate)),
                                                    int(frames / (60 * framerate) % 60),
                                                    int(frames / framerate % 60),
                                                    int(frames / framerate % 1 * 100))

def get_people(img):
    mobuo_rate = get_color_rate(img,np.array([100,185,225]),np.array([110,225,255]))
    flag_rate = get_color_rate(img,np.array([27,155,240]),np.array([37,215,255]))
    renai_rate = get_color_rate(img,np.array([150,70,225]),np.array([160,90,255]))
    seizon_rate = get_color_rate(img,np.array([75,150,230]),np.array([80,190,255]))
    mobumi_rate = get_color_rate(img,np.array([20,90,245]),np.array([25,120,255]))
    rate_list = [mobuo_rate,flag_rate,renai_rate,seizon_rate,mobumi_rate]
    people_list = ["mobuo","flag","renai","seizon","mobumi"]
    max_rate = max(rate_list)
    if(max_rate < 0.2 or rate_list.count(max_rate) > 1):
        # print(people_list)
        # print(rate_list)
        return "undefined"
    return people_list[rate_list.index(max_rate)]

subtitle_head = """
[Script Info]
; Script generated by Aegisub 3.2.2
; http://www.aegisub.org/
Title: Default Aegisub file
ScriptType: v4.00+
WrapStyle: 0
ScaledBorderAndShadow: yes
YCbCr Matrix: None
PlayResX: 1920
PlayResY: 1080

[Aegisub Project Garbage]
Audio File: $$FILE$$
Video File: $$FILE$$

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,思源黑體,100,&H00FFFFFF,&H00FFFFFF,&H00000000,&H910E0807,-1,0,0,0,100,100,1.14695,0,1,7,4,2,135,135,50,1
Style: 未定义#1,极影毁片圆 Medium,95,&H00FFFFFF,&H00FFFFFF,&H00000000,&H910E0807,0,0,0,0,100,100,1.14695,0,1,7,0,2,135,135,160,1
Style: 未定义#2,极影毁片圆 Medium,95,&H00FFFFFF,&H00FFFFFF,&H00FFFFFF,&H17000000,0,0,0,0,100,100,1.14695,0,1,11,4,2,135,135,160,1
Style: 路人男#1,极影毁片圆 Medium,95,&H00FFA239,&H00FFFFFF,&H00000000,&H13FFFFFF,0,0,0,0,100,100,1.14695,0,1,7,0,2,135,135,160,1
Style: 死亡flag#1,极影毁片圆 Medium,95,&H0042FFF8,&H00FFFFFF,&H00000000,&H17FFFFFF,0,0,0,0,100,100,1.14695,0,1,7,0,2,135,135,160,1
Style: 生存flag#1,极影毁片圆 Medium,95,&H00C6FF69,&H00FFFFFF,&H00000000,&H13FFFFFF,0,0,0,0,100,100,1.14695,0,1,7,0,2,135,135,160,1
Style: 恋爱flag#1,极影毁片圆 Medium,95,&H00EF9AF5,&H00FFFFFF,&H00000000,&H13FFFFFF,0,0,0,0,100,100,1.14695,0,1,7,0,2,135,135,160,1
Style: 路人美#1,极影毁片圆 Medium,95,&H0091E1FB,&H00FFFFFF,&H00000000,&H13FFFFFF,0,0,0,0,100,100,1.14695,0,1,7,0,2,135,135,160,1
Style: 神#1,极影毁片圆 Medium,95,&H00C5F7F6,&H00FFFFFF,&H00000000,&H17FFFFFF,0,0,0,0,100,100,1.14695,0,1,7,0,2,135,135,160,1
Style: 洋红色【魅力美#1,极影毁片圆 Medium,95,&H00AC42EC,&H00FFFFFF,&H00000000,&H13FFFFFF,0,0,0,0,100,100,1.14695,0,1,7,0,2,135,135,160,1
Style: 东云色【辣妹美#1,极影毁片圆 Medium,95,&H009196F8,&H00FFFFFF,&H00000000,&H13FFFFFF,0,0,0,0,100,100,1.14695,0,1,7,0,2,135,135,160,1
Style: 淡紫色#1,极影毁片圆 Medium,95,&H00E4739F,&H00FFFFFF,&H00000000,&H13FFFFFF,0,0,0,0,100,100,1.14695,0,1,7,0,2,135,135,160,1
Style: 自定义#1,极影毁片圆 Medium,95,&H00FFFFFF,&H00FFFFFF,&H00000000,&H17FFFFFF,0,0,0,0,100,100,1.14695,0,1,7,0,2,135,135,160,1
Style: 开场白,思源黑體,120,&H00FFFFFF,&H00FFFFFF,&H00000000,&H910E0807,-1,0,0,0,100,100,1.14695,0,1,7,4,2,135,135,50,1
Style: 旁白#1,极影毁片辉宋 Bold,95,&H00000000,&H00FFFFFF,&H00FFFFFF,&H910E0807,-1,0,0,0,100,100,1.14695,0,1,8,0,2,135,135,160,1
Style: 转场#1,仓耳渔阳体 W02,100,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,8,0,2,10,10,350,1
Style: 译注,思源黑體,80,&H00FFFFFF,&H00FFFFFF,&H00000000,&H910E0807,-1,0,0,0,100,100,1.14695,0,1,5,2,7,50,0,50,1
Style: 路人男#2,极影毁片圆 Medium,95,&H00FFFFFF,&H00FFFFFF,&H00FFFFFF,&H17000000,0,0,0,0,100,100,1.14695,0,1,11,4,2,135,135,160,1
Style: 死亡flag#2,极影毁片圆 Medium,95,&H00FFFFFF,&H00FFFFFF,&H00FFFFFF,&H17000000,0,0,0,0,100,100,1.14695,0,1,11,4,2,135,135,160,1
Style: 生存flag#2,极影毁片圆 Medium,95,&H00FFFFFF,&H00FFFFFF,&H00FFFFFF,&H17000000,0,0,0,0,100,100,1.14695,0,1,11,4,2,135,135,160,1
Style: 恋爱flag#2,极影毁片圆 Medium,95,&H00FFFFFF,&H00FFFFFF,&H00FFFFFF,&H17000000,0,0,0,0,100,100,1.14695,0,1,11,4,2,135,135,160,1
Style: 路人美#2,极影毁片圆 Medium,95,&H00FFFFFF,&H00FFFFFF,&H00FFFFFF,&H17000000,0,0,0,0,100,100,1.14695,0,1,11,4,2,135,135,160,1
Style: 神#2,极影毁片圆 Medium,95,&H00FFFFFF,&H00FFFFFF,&H00FFFFFF,&H17000000,0,0,0,0,100,100,1.14695,0,1,11,4,2,135,135,160,1
Style: 洋红色【魅力美#2,极影毁片圆 Medium,95,&H00FFFFFF,&H00FFFFFF,&H00FFFFFF,&H17000000,0,0,0,0,100,100,1.14695,0,1,11,4,2,135,135,160,1
Style: 东云色【辣妹美#2,极影毁片圆 Medium,95,&H00FFFFFF,&H00FFFFFF,&H00FFFFFF,&H17000000,0,0,0,0,100,100,1.14695,0,1,11,4,2,135,135,160,1
Style: 淡紫色#2,极影毁片圆 Medium,95,&H00FFFFFF,&H00FFFFFF,&H00FFFFFF,&H17000000,0,0,0,0,100,100,1.14695,0,1,11,4,2,135,135,160,1
Style: 自定义#2,极影毁片圆 Medium,95,&H00FFFFFF,&H00FFFFFF,&H00FFFFFF,&H17000000,0,0,0,0,100,100,1.14695,0,1,11,4,2,135,135,160,1
Style: 旁白#2,极影毁片辉宋 Bold,95,&H00000000,&H00FFFFFF,&H00000000,&H290E0807,-1,0,0,0,100,100,1.14695,0,1,12,4,2,135,135,160,1
Style: 转场#2,仓耳渔阳体 W02,100,&H00FFFFFF,&H000000FF,&H00FFFFFF,&H00000000,-1,0,0,0,100,100,0,0,1,12,4,2,10,10,350,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

def people2style(people):
    if(people == "mobuo"):
        return "路人男#1"
    elif(people == "flag"):
        return "死亡flag#1"
    elif(people == "seizon"):
        return "生存flag#1"
    elif(people == "renai"):
        return "恋爱flag#1"
    elif(people == "Opening"):
        return "开场白"
    elif(people == "trans"):
        return "转场#1"
    elif(people == "mobumi"):
        return "路人美#1"
    elif(people == "undefined"):
        return "未定义#1"

def add_sub(subtext,begintime,endingtime,subpeople):
    global sub_num
    global subtitle
    style = people2style(subpeople)
    subtitle = subtitle + "Dialogue: 1,"+ begintime +","+ endingtime +","+ style +","+ subpeople +",0,0,0,," + subtext + str(sub_num) + "\n"
    sub_num += 1

def add_op(frame_rate,begin_frame_num):
    add_sub("没有任何优点的路人男",frames_to_timecode(frame_rate,begin_frame_num),frames_to_timecode(frame_rate,begin_frame_num+(1.87*frame_rate)),"Opening")
    add_sub("在路人男面前出现的女孩，她的真实身份是...?",frames_to_timecode(frame_rate,begin_frame_num+(1.87*frame_rate)),frames_to_timecode(frame_rate,begin_frame_num+(4.57*frame_rate)),"Opening")
    add_sub("死亡flag?",frames_to_timecode(frame_rate,begin_frame_num+(4.57*frame_rate)),frames_to_timecode(frame_rate,begin_frame_num+(5.77*frame_rate)),"Opening")
    add_sub("路人男能成功回避死亡flag吗!?",frames_to_timecode(frame_rate,begin_frame_num+(5.77*frame_rate)),frames_to_timecode(frame_rate,begin_frame_num+(8.47*frame_rate)),"Opening")
    add_sub("全力回避flag酱!",frames_to_timecode(frame_rate,begin_frame_num+(8.47*frame_rate)),frames_to_timecode(frame_rate,begin_frame_num+(10.84*frame_rate)),"Opening")


# 视频帧总数
current_frame_num = begin_frame_num = last_frame_num = 0
last_pic_hash = ''
op = trans = False
op_match_times = 0
sub_num = 1
Err = False

def autosub(videopath,subpath):
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
    subtitle = subtitle_head.replace("$$FILE$$",os.path.abspath(videopath))
    source_video = cv2.VideoCapture(videopath)
    # 是否成功打开视频
    isOpened = False
    if source_video.isOpened():
        isOpened = True
    if isOpened:
        while True:
            ret, frame = source_video.read()
            if ret == False:
                break
            if(current_frame_num == 0):
                frame_rate = round(source_video.get(5),2)
            
            current_pic = frame[950:1045,810:910]
            pic_current_hash = phash(current_pic)
            hmdistant = hamming_distance(last_pic_hash,pic_current_hash)
            
            switch_pic = frame[940:1060,360:1540]
            switch_hash = phash(switch_pic)
            
            if(op_match_times < 2):
                match_op_pic = frame
                match_op_hash = phash(match_op_pic)
            if(match_op_hash in opening and op_match_times < 2):
                if(op_match_times == 0):
                    # print(str(current_frame_num) + " | 开场白起点")
                    op_bg_num = current_frame_num
                    add_op(frame_rate,begin_frame_num)
                op = bool(1 - op)
                op_match_times += 1
                if(op_match_times == 2):
                    # print(str(current_frame_num) + " | 开场白结束")
                    print(str(op_bg_num) + " <-> " + str(current_frame_num) + " | 开场白")
                begin_frame_num = current_frame_num + 15
            if(op):
                current_frame_num += 1
                continue
            
            if(hamming_distance(switch_hash,'1010010011000000101010001100000001000100000001011000011010100000') < 10):
                trans = True   #识别转场
            if((hmdistant > 13) and (current_frame_num != 0) and (current_frame_num-last_frame_num > (frame_rate/4))):
                people = get_people(people_pic)
                if(trans):
                    people = "trans"
                    trans = False
                
                print(str(sub_num) + " | " + str(current_frame_num-1) + " <-> " + str(current_frame_num) + " | hmdst: " + str(hmdistant)+" | gap: "+str(current_frame_num-last_frame_num) +
                        " | "+frames_to_timecode(frame_rate, begin_frame_num)+" --> "+frames_to_timecode(frame_rate, current_frame_num) + " | people: " + people)
                add_sub("示范性字幕",frames_to_timecode(frame_rate,begin_frame_num),frames_to_timecode(frame_rate,current_frame_num),people)

                begin_frame_num = current_frame_num
                last_frame_num = current_frame_num

            last_pic_hash = pic_current_hash
            people_pic = frame[940:1060,360:1540]
            people_hash = phash(people_pic)
            current_frame_num += 1
    else:
        print("源视频读取出错")
        Err = True
    print("finish!")
    if(not Err):
        with open(subpath,'w+',encoding='utf-8') as q:
            q.write(subtitle)
    end = time.time()
    print('耗时：'+str(end - start)+'秒')
    return Err


def gui():
    print("正在呼起GUI...请稍后...")
    source_path_input = ""
    target_path_input = ""
    while(1):
        choose = eg.indexbox("\t\t\t     "+ "自动打轴机 By Yellowstone\n\n\t\t\t 请选择源视频文件与轴文件输出路径\n\n源视频路径：" + source_path_input + "\n\n轴文件输出路径：" + target_path_input,"AutoSubtitle",choices=("选择源视频","选择轴输出路径","开始打轴","退出程序"))
        if(choose == 0):
            while(1):
                s = eg.fileopenbox("请选择源视频","AutoSubtitle",default="*.mp4",filetypes=[["*.webm","*.mp4","*.mov","*.flv","*.mkv","*.m4v","Video files"],["*.*","All files"]],multiple=False)
                if(s is None):
                    # eg.msgbox("您未选择任何源文件！","未选择文件","重新选择")
                    if(eg.ccbox("\t\t\t您未选择任何文件，是否重新选择？",title="未选择文件",choices=("重新选择","稍后选择"))):
                        pass
                    else:
                        break
                elif(not (s.split('.')[-1] in ["webm","mp4","mov","flv","mkv","m4v"])):
                    if(eg.ccbox("\t\t   您选择的文件疑似非视频文件，是否重新选择？",title="文件格式未识别",choices=("重新选择","选择无误"))):
                        pass
                    else:
                        source_path_input = s
                        break
                else:
                    source_path_input = s
                    break
        elif(choose == 1):
            while(1):
                t = eg.filesavebox("请选择轴保存路径","AutoSubtitle",default="output.ass",filetypes=[["*.ass","ASS files"],["*.*","All files"]])
                if(t is None):
                    if(eg.ccbox("\t\t\t您未选择保存路径，是否重新选择？",title="未选择保存路径",choices=("重新选择","稍后选择"))):
                        pass
                    else:
                        break
                elif(t.split('\\')[-1].split('.')[-1] != 'ass'):
                    target_path_input = t + ".ass"
                    break
                else:
                    target_path_input = t
                    break
        elif(choose == 2):
            # break
            if(not source_path_input or not source_path_input):
                eg.msgbox("\t\t\t    信息有误，请补充相关信息！","AutoSubtitle","确认")
                continue
            if(autosub(source_path_input,target_path_input)):
                eg.msgbox("\t\t\t打轴失败，请检查相关信息或报告错误！","AutoSubtitle","确认")
                continue
            else:
                input("按回车退出...")
                break
        elif(choose == 3):
            break
        else:
            break

# gui()

def show_help():
    print("----------------")
    print("使用帮助：\n")
    print("GUI模式触发条件为无传入参数\n")
    print("命令行模式：")
    print("python main.py 参数1 参数2")
    print("AutoSubtitle.exe 参数1 参数2 \n")
    print("参数1 原视频路径 如 C://xxx/xxx/xx.mp4")
    print("参数2 字幕输出路径 如 C://xxx/xxx/xx.ass \n")
    print("完整示例：python main.py C://xxx/xxx/xx.mp4 C://xxx/xxx/xx.ass")
    print("AutoSubtitle.exe C://xxx/xxx/xx.mp4 C://xxx/xxx/xx.ass")
    print("----------------")
    input("按回车退出...")

if(len(sys.argv) == 3):
    if(autosub(sys.argv[1],sys.argv[2])):
        print()
elif(len(sys.argv) == 1):
    gui()
elif(len(sys.argv) == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help")):
    show_help()
elif(len(sys.argv) < 3 and len(sys.argv) > 1):
    print("参数过少，请检查重试，输入 -h 或 --help 来查看使用帮助")
    input("按回车退出...")
elif(len(sys.argv) > 3):
    print("参数过多，请检查重试，输入 -h 或 --help 来查看使用帮助")
    input("按回车退出...")
