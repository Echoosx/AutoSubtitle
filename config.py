import os
import sys

isPacked = (getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'))
dynamicConfigRoot = f'{os.path.dirname(sys.executable)}/config/' if isPacked \
    else f'{os.path.dirname(os.path.abspath(__file__))}/config/'

globalConfigPath = dynamicConfigRoot + 'config.ini'
styleSheetPath = dynamicConfigRoot + 'style.ini'
flagStylePath = dynamicConfigRoot + 'flag.txt'
mixedStylePath = dynamicConfigRoot + 'mixed.txt'
styleSheetBackup = """[flag]
mobuo = 路人男#正文#1
flag = 死亡flag#正文#1
seizon = 生存flag#正文#1
renai = 恋爱flag#正文#1
Opening = 开场白
trans = 转场#1
mobumi = 小美#正文#1
lightpurple = 淡紫色#正文#1
dongyun = 东云色#正文#1
yanghong = 洋红色#正文#1
undefined = 未定义#正文#1
narrator = 旁白#1
siturenn = 失恋flag#正文#1
hametsu = 毁灭flag#正文#1
rose = 玫瑰色#正文#1
kami = 神#正文#1
darkred = 深红色#正文#1
darkgreen = 未定义#正文#1
green = 绿色#正文#1
nana = 娜娜#正文#1
red = 愤怒#正文#1
lightpink = 嫉妒#正文#1
blue = 蓝色#正文#1
lightgreen = 死神No.13#正文#1


[mixed-blood]
Opening = 开场白
undefined = 未定义
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
lightbluegreen = 浅蓝绿薄荷"""


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
Style: 未定义#正文#1,极影毁片圆 Medium,95,&H00FFFFFF,&H00FFFFFF,&H00000000,&H910E0807,-1,0,0,0,100,100,1,0,1,7,0,2,135,135,160,1
Style: 路人男#正文#1,极影毁片圆 Medium,95,&H00FCA439,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,1,0,1,7,0,2,135,135,160,1
Style: 死亡flag#正文#1,极影毁片圆 Medium,95,&H0042FFF8,&H00FFFFFF,&H00000000,&H17FFFFFF,-1,0,0,0,100,100,1,0,1,7,0,2,135,135,160,1
Style: 生存flag#正文#1,极影毁片圆 Medium,95,&H00BAFF48,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,1,0,1,7,0,2,135,135,160,1
Style: 恋爱flag#正文#1,极影毁片圆 Medium,95,&H00F4A9FF,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,1,0,1,7,0,2,135,135,160,1
Style: 失恋flag#正文#1,极影毁片圆 Medium,95,&H00FFED7D,&H00FFFFFF,&H00000000,&H17FFFFFF,-1,0,0,0,100,100,1,0,1,7,0,2,135,135,160,1
Style: 毁灭flag#正文#1,极影毁片圆 Medium,95,&H00BDC805,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,1,0,1,7,0,2,135,135,160,1
Style: 路人妹#正文#1,极影毁片圆 Medium,95,&H00BF7DF7,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,1,0,1,7,0,2,135,135,160,1
Style: 娜娜#正文#1,极影毁片圆 Medium,95,&H004F83FA,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,1,0,1,7,0,2,135,135,160,1
Style: 小美#正文#1,极影毁片圆 Medium,95,&H0091E1FB,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,1,0,1,7,0,2,135,135,160,1
Style: 死神No.13#正文#1,极影毁片圆 Medium,95,&H0089FE97,&H00FFFFFF,&H00000000,&H17FFFFFF,-1,0,0,0,100,100,1,0,1,7,0,2,135,135,160,1
Style: 死神No.1#正文#1,极影毁片圆 Medium,95,&H008428CA,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,1,0,1,7,0,2,135,135,160,1
Style: 贪婪#正文#1,极影毁片圆 Medium,95,&H00D866AD,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,1,0,1,7,0,2,135,135,160,1
Style: 愤怒#正文#1,极影毁片圆 Medium,95,&H005D54EE,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,1,0,1,7,0,2,135,135,160,1
Style: 嫉妒#正文#1,极影毁片圆 Medium,95,&H00C07DF8,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,1,0,1,7,0,2,135,135,160,1
Style: 神#正文#1,极影毁片圆 Medium,95,&H00D2FEFF,&H00FFFFFF,&H00000000,&H17FFFFFF,-1,0,0,0,100,100,1,0,1,7,0,2,135,135,160,1
Style: 洋红色#正文#1,极影毁片圆 Medium,95,&H00A643F6,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,1,0,1,7,0,2,135,135,160,1
Style: 东云色#正文#1,极影毁片圆 Medium,95,&H009196F8,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,1,0,1,7,0,2,135,135,160,1
Style: 淡紫色#正文#1,极影毁片圆 Medium,95,&H00D97092,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,1,0,1,7,0,2,135,135,160,1
Style: 深红色#正文#1,极影毁片圆 Medium,95,&H00251AF0,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,1,0,1,7,0,2,135,135,160,1
Style: 土黄色#正文#1,极影毁片圆 Medium,95,&H0039B0EB,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,1,0,1,7,0,2,135,135,160,1
Style: 玫瑰色#正文#1,极影毁片圆 Medium,95,&H007848FE,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,1,0,1,7,0,2,135,135,160,1
Style: 橙色#正文#1,极影毁片圆 Medium,95,&H005183FC,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,1,0,1,7,0,2,135,135,160,1
Style: 蓝色#正文#1,极影毁片圆 Medium,95,&H00F7797C,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,1,0,1,7,0,2,135,135,160,1
Style: 绿色#正文#1,极影毁片圆 Medium,95,&H0090DB83,&H00FFFFFF,&H00000000,&H13FFFFFF,-1,0,0,0,100,100,1,0,1,7,0,2,135,135,160,1
Style: 转场#1,仓耳渔阳体 W02,100,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,8,0,2,10,10,350,1
Style: 旁白#1,极影毁片辉宋 Bold,95,&H00FFFFFF,&H00FFFFFF,&H00000000,&H910E0807,0,0,0,0,102,100,1,0,1,9,0,2,135,135,160,1
Style: 开场白,思源黑体 CN,120,&H00FFFFFF,&H00FFFFFF,&H00000000,&H910E0807,-1,0,0,0,100,100,1,0,1,7,4,2,135,135,50,1
Style: 转场#2,仓耳渔阳体 W02,100,&H00FFFFFF,&H000000FF,&H00FFFFFF,&H00000000,-1,0,0,0,100,100,0,0,1,12,4,2,10,10,350,1
Style: 旁白#2,极影毁片辉宋 Bold,95,&H00FFFFFF,&H00FFFFFF,&H00FFFFFF,&H290E0807,0,0,0,0,102,100,1,0,1,13,4,2,135,135,160,1
Style: 白边框#正文#2,极影毁片圆 Medium,95,&H00FFFFFF,&H00FFFFFF,&H00FFFFFF,&H17000000,-1,0,0,0,100,100,1,0,1,11,4,2,135,135,160,1
Style: 译注,思源黑体 CN,80,&H00FFFFFF,&H00FFFFFF,&H00000000,&H910E0807,-1,0,0,0,100,100,1,0,1,5,2,7,50,0,50,1"""
        )

    if not os.path.exists(mixedStylePath):
        open(mixedStylePath, 'w', encoding='utf-8').write(
            """Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,思源黑体 CN Heavy,70,&H00FFFFFF,&H00FFFFFF,&H00000000,&H910E0807,-1,0,0,0,100,100,1.14695,0,1,3,0,2,135,135,50,1
Style: 千夜,思源黑体 CN Heavy,85,&H00381DED,&H00FFFFFF,&H000F2434,&H6D000000,-1,0,0,0,105,100,1.6,0,1,6.2,3,2,10,10,115,1
Style: 希迪,思源黑体 CN Heavy,85,&H0039FFFF,&H00FFFFFF,&H00022F4B,&H5C000000,-1,0,0,0,105,100,1.6,0,1,6.2,3,2,10,10,115,1
Style: 冰雨,思源黑体 CN Heavy,85,&H00FFFFA2,&H00FFFFFF,&H006D2E1B,&H5E000000,-1,0,0,0,105,100,1.6,0,1,6.2,3,2,10,10,115,1
Style: 约梅,思源黑体 CN Heavy,85,&H000F94F4,&H00FFFFFF,&H000C2236,&H23303032,-1,0,0,0,105,100,1.6,0,1,6.2,3,2,10,10,115,1
Style: 波提斯,思源黑体 CN Heavy,85,&H00D299C5,&H00FFFFFF,&H00480032,&H41000000,-1,0,0,0,105,100,1.6,0,1,6.2,3,2,10,10,115,1
Style: 欧娜,思源黑体 CN Heavy,85,&H008078C3,&H00FFFFFF,&H00183146,&H62000000,-1,0,0,0,105,100,1.6,0,1,6.2,3,2,10,10,115,1
Style: 洛伊可（浅黄色）,思源黑体 CN Heavy,85,&H00A3EBFB,&H00FFFFFF,&H000B3446,&H61000000,-1,0,0,0,105,100,1.6,0,1,6.2,3,2,10,10,115,1
Style: 米提（粉色）,思源黑体 CN Heavy,85,&H00F97CEF,&H00FFFFFF,&H00152A54,&H58000000,-1,0,0,0,105,100,1.6,0,1,6.2,3,2,10,10,115,1
Style: 淡绿色（路易）,思源黑体 CN Heavy,85,&H00C4FFB3,&H00FFFFFF,&H001D311D,&H65000000,-1,0,0,0,105,100,1.6,0,1,6.2,3,2,10,10,115,1
Style: 棕褐色（马查索）,思源黑体 CN Heavy,85,&H00828DA7,&H00FFFFFF,&H0006063F,&H4E000000,-1,0,0,0,105,100,1.6,0,1,6.2,3,2,10,10,115,1
Style: 深蓝色,思源黑体 CN Heavy,85,&H00F8968D,&H00FFFFFF,&H004D0202,&H64000000,-1,0,0,0,105,100,1.6,0,1,6.2,3,2,10,10,115,1
Style: 亮紫色,思源黑体 CN Heavy,85,&H00F464BE,&H00FFFFFF,&H00470033,&H55000000,-1,0,0,0,105,100,1.8,0,1,6.2,3,2,10,10,115,1
Style: 红棕色,思源黑体 CN Heavy,85,&H007677B7,&H00FFFFFF,&H0006063F,&H48000000,-1,0,0,0,105,100,1.6,0,1,6.2,3,2,10,10,115,1
Style: 肉粉棕色,思源黑体 CN Heavy,85,&H00A1A2F7,&H00FFFFFF,&H00121332,&H5C000000,-1,0,0,0,105,100,1.6,0,1,6.2,3,2,10,10,115,1
Style: 黄褐色,思源黑体 CN Heavy,85,&H0066A9C1,&H00FFFFFF,&H00082331,&H71000000,-1,0,0,0,105,100,1.6,0,1,6.2,3,2,10,10,115,1
Style: 深绿色,思源黑体 CN Heavy,85,&H00819D5A,&H00FFFFFF,&H00353F0E,&H00000000,-1,0,0,0,105,100,1.6,0,1,6.2,3,2,10,10,115,1
Style: 荧光绿色,思源黑体 CN Heavy,85,&H0007FF64,&H00FFFFFF,&H00023D10,&H57000000,-1,0,0,0,105,100,1.6,0,1,6.2,3,2,10,10,115,1
Style: 橘红色,思源黑体 CN Heavy,85,&H00054FF0,&H00FFFFFF,&H00051536,&H59000000,-1,0,0,0,105,100,1.6,0,1,6.2,3,2,10,10,115,1
Style: 偏浅橘-棕框色,思源黑体 CN Heavy,85,&H007DB8EF,&H00FFFFFF,&H00152F47,&HA0000000,-1,0,0,0,105,100,1.6,0,1,6.2,3,2,10,10,115,1
Style: 翌日,思源黑体 CN Heavy,85,&H00FFFFFF,&H00FFFFFF,&H001A333E,&H5C000000,-1,0,0,0,105,100,1.6,0,1,6.2,3,2,10,10,115,1
Style: 浅蓝绿薄荷,思源黑体 CN Heavy,85,&H00C8C9A5,&H00FFFFFF,&H00383F0F,&H84000000,-1,0,0,0,105,100,1.4,0,1,6.2,3,2,10,10,115,1
Style: 未定义,思源黑体 CN Heavy,85,&H00FFFFFF,&H00FFFFFF,&H00000000,&H910E0807,-1,0,0,0,105,100,1.6,0,1,6.2,3,2,10,10,115,1
Style: 译注,思源黑体 CN Heavy,80,&H00FFFFFF,&H00FFFFFF,&H00000000,&H910E0807,-1,0,0,0,100,100,1.14695,0,1,5,2,7,50,0,50,1
Style: 旁白,极影毁片辉宋 Bold,95,&H00000000,&H00FFFFFF,&H00FFFFFF,&H910E0807,-1,0,0,0,100,100,1.14695,0,1,8,0,2,135,135,160,1
Style: 开场白,思源黑体 CN Heavy,110,&H00FFFFFF,&H00FFFFFF,&H00000000,&H910E0807,-1,0,0,0,100,100,1.14695,0,1,7,4,2,135,135,20,1"""
        )

    if not os.path.exists(styleSheetPath):
        open(styleSheetPath, 'w', encoding='utf-8').write(styleSheetBackup)
