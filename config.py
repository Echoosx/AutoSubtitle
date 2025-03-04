import os
import sys
import configparser

isPacked = (getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'))
dynamicConfigRoot = f'{os.path.dirname(sys.executable)}/config/' if isPacked \
    else f'{os.path.dirname(os.path.abspath(__file__))}/config/'

globalConfigPath = dynamicConfigRoot + 'config.ini'
styleSheetPath = dynamicConfigRoot + 'style.ini'

flagStylePath = dynamicConfigRoot + 'flag.txt'
mixedStylePath = dynamicConfigRoot + 'mixed.txt'
HN_whiteStylePath = dynamicConfigRoot + 'hn_white.txt'
HN_colorStylePath = dynamicConfigRoot + 'hn_color.txt'
HN_gameStylePath = dynamicConfigRoot + 'hn_game.txt'

styleSheetBackup = """[flag]
mobuo = 路人男#正文#1
flag = 死亡flag#正文#1
seizon = 生存flag#正文#1
renai = 恋爱flag#正文#1
mobumi = 小美#正文#1
lightpurple = 淡紫色#正文#1
dongyun = 东云色#正文#1
yanghong = 洋红色#正文#1
siturenn = 失恋flag#正文#1
hametsu = 毁灭flag#正文#1
lightgreen = 死神No.13#正文#1
fen = 芬#正文#1
mashiro = 真白老师#正文黑#1
siratuchi = 白土#正文#1
rerooze = 雷洛泽#正文#1
rose = 玫瑰色#正文#1
winered = 酒红色#正文#1
kami = 神#正文#1
darkred = 深红色#正文#1
green = 绿色#正文#1
nana = 娜娜#正文#1
red = 愤怒#正文#1
lightpink = 嫉妒#正文#1
blue = 蓝色#正文#1
undefined = 未定义#正文#1
Opening = 开场白
trans = 转场#1
narrator = 旁白#1


[mixed-blood]
Opening = 开场白
undefined = 未定义
Trans = 转场#1
hisa = 冰雨
shidi = 希迪
kage = 千夜
yome = 约梅
botisu = 波提斯
owner = 欧娜
lightyellow = 淡黄色（洛伊可）
pink = 粉色（米提）
lightgreen = 淡绿色（路易）
brown = 棕褐色（马查索）
darkblue = 深蓝色
brightpurple = 亮紫色
redbrown = 红棕色
fleshpink = 肉粉棕色
yellowbrown = 黄褐色
darkgreen = 深绿色
brightgreen = 荧光绿色
orangered = 橘红色
lightorange = 偏浅橘-棕框色
lightbluegreen = 浅蓝绿薄荷
tomorrow = 翌日


[hundred-color]
raika = 雷夏#正文#1
yuito = 結人#正文#1
keigo = 惠吾#正文#1
lightgreen = 浅绿色#正文#1
brightgreen = 荧光绿#正文#1
skyblue = 天蓝色#正文#1
brown = 棕色#正文#1
undefined = 未定义#正文#1

[hundred-white]
text = 正文

[hundred-game]
text = 正文"""


def setGlobalConfig(part, key, value):
    config = configparser.ConfigParser()
    config.read(globalConfigPath, encoding='utf-8')
    global_config_dict = {section: dict(config[section]) for section in config.sections()}[part]
    global_config_dict[key] = value
    config[part] = global_config_dict
    with open(globalConfigPath, 'w') as configfile:
        config.write(configfile)


def getGlobalConfig(part, key):
    config = configparser.ConfigParser()
    config.read(globalConfigPath, encoding='utf-8')
    global_config_dict = {section: dict(config[section]) for section in config.sections()}[part]
    return global_config_dict[key]


def configInit():
    if not os.path.exists(dynamicConfigRoot):
        os.mkdir(dynamicConfigRoot)

    if not os.path.exists(globalConfigPath):
        open(globalConfigPath, 'w', encoding='utf-8').write(
            """[config]
default_videotype = 0
debug_subtitle = 1"""
        )

    if not os.path.exists(flagStylePath):
        open(flagStylePath, 'w', encoding='utf-8').write(
            """Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: 未定义#正文#1,Resource Han Rounded CN,107,&H00FFFFFF,&H00FFFFFF,&H00000000,&H910E0807,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 路人男#正文#1,Resource Han Rounded CN,107,&H00FCA439,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 死亡flag#正文#1,Resource Han Rounded CN,107,&H0042FFF8,&H00FFFFFF,&H00000000,&H17FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 生存flag#正文#1,Resource Han Rounded CN,107,&H00BAFF48,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 恋爱flag#正文#1,Resource Han Rounded CN,107,&H00F4A9FF,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 失恋flag#正文#1,Resource Han Rounded CN,107,&H00FFED7D,&H00FFFFFF,&H00000000,&H17FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 毁灭flag#正文#1,Resource Han Rounded CN,107,&H00BDC805,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 娜娜#正文#1,Resource Han Rounded CN,107,&H00516AEA,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 死神No.13#正文#1,Resource Han Rounded CN,107,&H0089FE97,&H00FFFFFF,&H00000000,&H17FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 神#正文#1,Resource Han Rounded CN,107,&H00D2FEFF,&H00FFFFFF,&H00000000,&H17FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 芬#正文#1,Resource Han Rounded CN,107,&H001854F0,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 真白老师#正文黑#1,Resource Han Rounded CN,107,&H0009458E,&H00FFFFFF,&H00FFFFFF,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 白土#正文#1,Resource Han Rounded CN,107,&H00FFFFFF,&H00FFFFFF,&H00221CC1,&H910E0807,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 雷洛泽#正文#1,Resource Han Rounded CN,107,&H00A03ACC,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 破坏神#正文#1,Resource Han Rounded CN,107,&H0090E199,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 小美#正文#1,Resource Han Rounded CN,107,&H0091E1FB,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 贪婪#正文#1,Resource Han Rounded CN,107,&H00D866AD,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 愤怒#正文#1,Resource Han Rounded CN,107,&H005D54EE,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 嫉妒#正文#1,Resource Han Rounded CN,107,&H00C07DF8,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 死神No.1#正文#1,Resource Han Rounded CN,107,&H008428CA,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 路人妹#正文#1,Resource Han Rounded CN,107,&H00BF7DF7,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 洋红色#正文#1,Resource Han Rounded CN,107,&H00A643F6,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 东云色#正文#1,Resource Han Rounded CN,107,&H009196F8,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 淡紫色#正文#1,Resource Han Rounded CN,107,&H00D97092,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 深红色#正文#1,Resource Han Rounded CN,107,&H00251AF0,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 土黄色#正文#1,Resource Han Rounded CN,107,&H0039B0EB,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 玫瑰色#正文#1,Resource Han Rounded CN,107,&H007848FE,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 酒红色#正文#1,Resource Han Rounded CN,107,&H008A25E1,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 橙色#正文#1,Resource Han Rounded CN,107,&H005183FC,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 蓝色#正文#1,Resource Han Rounded CN,107,&H00F7797C,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 绿色#正文#1,Resource Han Rounded CN,107,&H0090DB83,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 灰蓝#正文#1,Resource Han Rounded CN,107,&H00C08D7D,&H00FFFFFF,&H00000000,&H910E0807,-1,0,0,0,100,100,2,0,1,7,0,2,135,135,160,1
Style: 转场#1,TsangerYuYangT W02,100,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,8,0,2,10,10,350,1
Style: 旁白#1,Source Han Serif CN Heavy,110,&H00FFFFFF,&H00FFFFFF,&H00000000,&H910E0807,0,0,0,0,100,100,2,0,1,9,0,2,135,135,160,1
Style: 开场白,Source Han Sans CN,120,&H00FFFFFF,&H00FFFFFF,&H00000000,&H910E0807,-1,0,0,0,100,100,2,0,1,7,4,2,135,135,50,1
Style: 译注,Source Han Sans CN,80,&H00FFFFFF,&H00FFFFFF,&H00000000,&H910E0807,-1,0,0,0,100,100,2,0,1,5,2,7,50,0,50,1
Style: 转场#2,TsangerYuYangT W02,100,&H00FFFFFF,&H000000FF,&H00FFFFFF,&H00000000,-1,0,0,0,100,100,0,0,1,12,4,2,10,10,350,1
Style: 旁白#2,Source Han Serif CN Heavy,110,&H00FFFFFF,&H00FFFFFF,&H00FFFFFF,&H290E0807,0,0,0,0,100,100,2,0,1,13,4,2,135,135,160,1
Style: 白边框#正文#2,Resource Han Rounded CN,107,&H00FFFFFF,&H00FFFFFF,&H00FFFFFF,&H17000000,-1,0,0,0,100,100,2,0,1,11,4,2,135,135,160,1
Style: 黑边框#正文黑#2,Resource Han Rounded CN,107,&H00000000,&H00000000,&H00000000,&H17FFFFFF,-1,0,0,0,100,100,2,0,1,11,4,2,135,135,160,1"""
        )

    if not os.path.exists(mixedStylePath):
        open(mixedStylePath, 'w', encoding='utf-8').write(
            """Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: 千夜,Source Han Sans CN Heavy,85,&H003332FF,&H00FFFFFF,&H0011243A,&H64000000,-1,0,0,0,105,100,2,0,1,6,3,2,10,10,115,1
Style: 希迪,Source Han Sans CN Heavy,85,&H0039FFFF,&H00FFFFFF,&H00022F4B,&H64000000,-1,0,0,0,105,100,2,0,1,6,3,2,10,10,115,1
Style: 冰雨,Source Han Sans CN Heavy,85,&H00FFFC96,&H00FFFFFF,&H00692F19,&H64000000,-1,0,0,0,105,100,2,0,1,6,3,2,10,10,115,1
Style: 约梅,Source Han Sans CN Heavy,85,&H000F94F4,&H00FFFFFF,&H000C2236,&H64000000,-1,0,0,0,105,100,2,0,1,6,3,2,10,10,115,1
Style: 波提斯,Source Han Sans CN Heavy,85,&H00D299C5,&H00FFFFFF,&H00480032,&H64000000,-1,0,0,0,105,100,2,0,1,6,3,2,10,10,115,1
Style: 欧娜,Source Han Sans CN Heavy,85,&H007D80C2,&H00FFFFFF,&H000F314A,&H64000000,-1,0,0,0,105,100,2,0,1,6,3,2,10,10,115,1
Style: 淡黄色（洛伊可）,Source Han Sans CN Heavy,85,&H00A4E8F7,&H00FFFFFF,&H00123747,&H64000000,-1,0,0,0,105,100,2,0,1,6,3,2,10,10,115,1
Style: 粉色（米提）,Source Han Sans CN Heavy,85,&H00FD8FF6,&H00FFFFFF,&H00112E55,&H64000000,-1,0,0,0,105,100,2,0,1,6,3,2,10,10,115,1
Style: 淡绿色（路易）,Source Han Sans CN Heavy,85,&H00C4FFB3,&H00FFFFFF,&H001D311D,&H64000000,-1,0,0,0,105,100,2,0,1,6,3,2,10,10,115,1
Style: 棕褐色（马查索）,Source Han Sans CN Heavy,85,&H007E8FA3,&H00FFFFFF,&H00080F43,&H64000000,-1,0,0,0,105,100,2,0,1,6,3,2,10,10,115,1
Style: 深蓝色,Source Han Sans CN Heavy,85,&H00F8968D,&H00FFFFFF,&H004D0202,&H64000000,-1,0,0,0,105,100,2,0,1,6,3,2,10,10,115,1
Style: 亮紫色,Source Han Sans CN Heavy,85,&H00F772C2,&H00FFFFFF,&H00560242,&H64000000,-1,0,0,0,105,100,2,0,1,6,3,2,10,10,115,1
Style: 红棕色,Source Han Sans CN Heavy,85,&H007677B7,&H00FFFFFF,&H0006063F,&H64000000,-1,0,0,0,105,100,2,0,1,6,3,2,10,10,115,1
Style: 肉粉棕色,Source Han Sans CN Heavy,85,&H0094A7FE,&H00FFFFFF,&H0002153C,&H64000000,-1,0,0,0,105,100,2,0,1,6,3,2,10,10,115,1
Style: 黄褐色,Source Han Sans CN Heavy,85,&H0064A5BF,&H00FFFFFF,&H00052336,&H64000000,-1,0,0,0,105,100,2,0,1,6,3,2,10,10,115,1
Style: 深绿色,Source Han Sans CN Heavy,85,&H007C9355,&H00FFFFFF,&H00243409,&H64000000,-1,0,0,0,105,100,2,0,1,6,3,2,10,10,115,1
Style: 荧光绿色,Source Han Sans CN Heavy,85,&H0007FF64,&H00FFFFFF,&H00023D10,&H64000000,-1,0,0,0,105,100,2,0,1,6,3,2,10,10,115,1
Style: 橘红色,Source Han Sans CN Heavy,85,&H00085BFF,&H00FFFFFF,&H00041438,&H64000000,-1,0,0,0,105,100,2,0,1,6,3,2,10,10,115,1
Style: 偏浅橘-棕框色,Source Han Sans CN Heavy,85,&H007CBCF3,&H00FFFFFF,&H00123149,&H64000000,-1,0,0,0,105,100,2,0,1,6,3,2,10,10,115,1
Style: 翌日,Source Han Sans CN Heavy,85,&H00FFFFFF,&H00FFFFFF,&H001A333E,&H5C000000,-1,0,0,0,105,100,2,0,1,6,3,2,10,10,115,1
Style: 浅蓝绿薄荷,Source Han Sans CN Heavy,85,&H00C3C9A5,&H00FFFFFF,&H00333B14,&H64000000,-1,0,0,0,105,100,2,0,1,6,3,2,10,10,115,1
Style: 未定义,Source Han Sans CN Heavy,85,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,105,100,2,0,1,6,3,2,10,10,115,1
Style: 译注,Source Han Sans CN Heavy,80,&H00FFFFFF,&H00FFFFFF,&H00000000,&H910E0807,-1,0,0,0,100,100,2,0,1,5,2,7,50,0,50,1
Style: 旁白,Source Han Serif CN Heavy,105,&H00000000,&H00FFFFFF,&H00FFFFFF,&H910E0807,-1,0,0,0,100,100,2,0,1,8,0,2,135,135,160,1
Style: 开场白,Source Han Sans CN Heavy,110,&H00FFFFFF,&H00FFFFFF,&H00000000,&H910E0807,-1,0,0,0,100,100,2,0,1,7,4,2,135,135,20,1
Style: 转场#1,TsangerYuYangT W02,100,&H00FFFFFF,&H000000FF,&H00151833,&H00000000,-1,0,0,0,100,100,0,0,1,8,0,2,10,10,330,1
Style: 转场#2,TsangerYuYangT W02,100,&H00FFFFFF,&H000000FF,&H00FFFFFF,&H00000000,-1,0,0,0,100,100,0,0,1,12,4,2,10,10,330,1"""
        )

    if not os.path.exists(HN_colorStylePath):
        open(HN_colorStylePath, 'w', encoding='utf-8').write(
            """Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: 雷夏#正文#1,思源黑体 CN Heavy,90,&H0042C2F5,&H00FFFFFF,&H00000000,&H00FFFFFF,0,0,0,0,100,100,1.5,0,1,8,0,2,10,10,155,1
Style: 結人#正文#1,思源黑体 CN Heavy,90,&H00EA8EBA,&H00FFFFFF,&H00000000,&H00FFFFFF,0,0,0,0,100,100,1.5,0,1,8,0,2,10,10,155,1
Style: 惠吾#正文#1,思源黑体 CN Heavy,90,&H00C0C0C0,&H00FFFFFF,&H00000000,&H00FFFFFF,0,0,0,0,100,100,1.5,0,1,8,0,2,10,10,155,1
Style: 浅绿色#正文#1,思源黑体 CN Heavy,90,&H00B1DA7B,&H00000000,&H00000000,&H00FFFFFF,0,0,0,0,100,100,1.5,0,1,8,0,2,10,10,155,1
Style: 棕色#正文#1,思源黑体 CN Heavy,90,&H00678BA9,&H00FFFFFF,&H00000000,&H00FFFFFF,0,0,0,0,100,100,1.5,0,1,8,0,2,10,10,155,1
Style: 荧光绿#正文#1,思源黑体 CN Heavy,90,&H0040FD6A,&H00FFFFFF,&H00000000,&H00FFFFFF,0,0,0,0,100,100,1.5,0,1,8,0,2,10,10,155,1
Style: 天蓝色#正文#1,思源黑体 CN Heavy,90,&H00F9CA06,&H00FFFFFF,&H00000000,&H00FFFFFF,0,0,0,0,100,100,1.5,0,1,8,0,2,10,10,155,1
Style: 未定义#正文#1,思源黑体 CN Heavy,90,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00FFFFFF,0,0,0,0,100,100,1.5,0,1,8,0,2,10,10,155,1
Style: 白底#正文#2,思源黑体 CN Heavy,90,&H00FFFFFF,&H00000000,&H00FFFFFF,&H4B000000,0,0,0,0,100,100,1.5,0,1,12,5,2,10,10,155,1"""
        )

    if not os.path.exists(HN_whiteStylePath):
        open(HN_whiteStylePath, 'w', encoding='utf-8').write(
            """Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: 正文,思源黑体 Medium,75,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,2.4,0,1,2.6,0,2,10,10,90,1"""
        )

    if not os.path.exists(HN_gameStylePath):
        open(HN_gameStylePath, 'w', encoding='utf-8').write(
            """Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: 正文,思源黑体 CN,90,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,1.6,0,1,3,3.5,2,10,10,0,1"""
        )

    if not os.path.exists(styleSheetPath):
        open(styleSheetPath, 'w', encoding='utf-8').write(styleSheetBackup)
