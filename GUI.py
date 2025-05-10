import os
import sys
from pathlib import Path

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QFileDialog, QMessageBox
from PyQt6.QtCore import Qt

from GUI_style import Ui_AutoSubtitle
from verifyPath import is_path_exists_or_creatable
import configparser
import re
from config import (globalConfigPath, styleSheetPath,
                    flagStylePath, mixedStylePath, HN_whiteStylePath, HN_colorStylePath, HN_gameStylePath, parakoStylePath,
                    flagStyleBackup, mixedStyleBackup, HN_whiteStyleBackup, HN_gameStyleBackup, HN_colorStyleBackup, parakoStyleBackup
                    )
from config import getGlobalConfig, setGlobalConfig


class AutoSubtitle_class(QtWidgets.QMainWindow, Ui_AutoSubtitle):
    stylePathList = [flagStylePath, mixedStylePath, HN_whiteStylePath, HN_colorStylePath, HN_gameStylePath, parakoStylePath]
    styleBackupList = [flagStyleBackup, mixedStyleBackup, HN_whiteStyleBackup, HN_gameStyleBackup, HN_colorStyleBackup, parakoStyleBackup]
    def __init__(self):
        super(AutoSubtitle_class, self).__init__()
        self.setupUi(self)
        self.openPath = self.savePath = str()
        # self.flagStylePath = self.mixedStylePath = str()
        self.stylePath = str()
        self.videoTypeList.addItems(["全力回避Flag酱", "混血万事屋", "HundredNote", "HundredNote彩色", "HundredNote Game", "超能力高校"])
        self.videoTypeList.setCurrentIndex(0)
        self.videoType = self.videoTypeList.currentIndex()
        self.styleTypeList.addItems(
            ["全力回避Flag酱", "混血万事屋", "HundredNote", "HundredNote彩色", "HundredNote Game", "超能力高校"])
        self.styleTypeList.setCurrentIndex(0)
        self.styleType = self.styleTypeList.currentIndex()
        self.configTypeList.addItems(
            ["全力回避Flag酱", "混血万事屋", "HundredNote", "HundredNote彩色", "HundredNote Game", "超能力高校"])
        self.configTypeList.setCurrentIndex(0)
        self.configType = self.configTypeList.currentIndex()
        self.finish = False
        self.opTypes = ["远古OP", "旧OP", "新OP-长", "新OP-短"]
        self.opType = 3
        self.FlagOPcomboBox.addItems(self.opTypes)
        self.FlagOPcomboBox.setCurrentIndex(3)
        self.initAll()
        self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        self.Title.setOpenExternalLinks(True)

    def closeEvent(self, event):
        if not self.finish:
            sys.exit()

    def updateOpenPath(self):
        path = self.VideoPathEdit.text()
        if not Path(path).is_file():
            QMessageBox.warning(self, '无法找到源文件', '请重新选择正确的路径!\t\t\n', QMessageBox.StandardButton.Ok)
            print("源文件路径有误")
        elif self.checkForm(path):
            self.openPath = path
            defaultSubtitlePath = os.path.dirname(path) + '/' + os.path.basename(path).rstrip(
                str(path).split('.')[-1]) + "ass"
            self.SubtitleSavePathEdit.setText(defaultSubtitlePath)
        else:
            self.askforNonVideoFile_box = QMessageBox(QMessageBox.Icon.Question, '文件格式未识别',
                                                      '该文件疑似非视频文件，确认要选择该文件吗？\t\t\n',
                                                      flags=Qt.WindowType.WindowStaysOnTopHint)
            self.askforNonVideoFile_box.setFixedSize(380, 135)
            status_insist = self.askforNonVideoFile_box.addButton('确认', QMessageBox.ButtonRole.NoRole)
            self.askforNonVideoFile_box.addButton('重新选择', QMessageBox.ButtonRole.YesRole)
            self.askforNonVideoFile_box.exec()
            if self.askforNonVideoFile_box.clickedButton() == status_insist:
                self.openPath = path
            else:
                self.VideoPathEdit.clear()

    def checkOpenPath(self):
        path = self.VideoPathEdit.text()
        if not Path(path).is_file():
            QMessageBox.warning(self, '无法找到源文件', '请重新选择正确的路径!\t\t\n', QMessageBox.StandardButton.Ok)
            print("源文件路径有误")
        elif self.checkForm(path):
            print(f"将会打开: {path}")
            self.openPath = path
        else:
            self.askforNonVideoFile_box = QMessageBox(QMessageBox.Icon.Question, '文件格式未识别',
                                                      '该文件疑似非视频文件，确认要选择该文件吗？\t\t\n',
                                                      flags=Qt.WindowType.WindowStaysOnTopHint)
            self.askforNonVideoFile_box.setFixedSize(380, 135)
            status_insist = self.askforNonVideoFile_box.addButton('确认', QMessageBox.ButtonRole.NoRole)
            self.askforNonVideoFile_box.addButton('重新选择', QMessageBox.ButtonRole.YesRole)
            self.askforNonVideoFile_box.exec()
            if self.askforNonVideoFile_box.clickedButton() == status_insist:
                print(f"将会打开: {path}")
                self.openPath = path
            else:
                self.VideoPathEdit.clear()

    # def updateFlagStylePath(self, styleFilePath: str):
    #     if not Path(styleFilePath).is_file():
    #         QMessageBox.warning(self, '无法找到源文件', '请重新选择正确的路径!\t\t\n', QMessageBox.StandardButton.Ok)
    #         print("源文件路径有误")
    #     if not self.checkStyle(styleFilePath):
    #         self.askforNonStyleFile_box = QMessageBox(QMessageBox.Icon.Question, '文件格式未识别',
    #                                                   '该文件不是ass文件，确认要选择该文件吗？\t\t\n',
    #                                                   flags=Qt.WindowType.WindowStaysOnTopHint)
    #         self.askforNonStyleFile_box.setFixedSize(380, 135)
    #         status_insist = self.askforNonStyleFile_box.addButton('确认', QMessageBox.ButtonRole.NoRole)
    #         self.askforNonStyleFile_box.addButton('重新选择', QMessageBox.ButtonRole.YesRole)
    #         self.askforNonStyleFile_box.exec()
    #         if self.askforNonStyleFile_box.clickedButton() == status_insist:
    #             self.flagStylePath = styleFilePath
    #         else:
    #             self.flagStylePathEdit.clear()
    #     else:
    #         self.flagStylePath = styleFilePath
    #
    # def updateMixedStylePath(self, styleFilePath: str):
    #     if not Path(styleFilePath).is_file():
    #         QMessageBox.warning(self, '无法找到源文件', '请重新选择正确的路径!\t\t\n', QMessageBox.StandardButton.Ok)
    #         print("源文件路径有误")
    #     if not self.checkStyle(styleFilePath):
    #         self.askforNonStyleFile_box = QMessageBox(QMessageBox.Icon.Question, '文件格式未识别',
    #                                                   '该文件不是ass文件，确认要选择该文件吗？\t\t\n',
    #                                                   flags=Qt.WindowType.WindowStaysOnTopHint)
    #         self.askforNonStyleFile_box.setFixedSize(380, 135)
    #         status_insist = self.askforNonStyleFile_box.addButton('确认', QMessageBox.ButtonRole.NoRole)
    #         self.askforNonStyleFile_box.addButton('重新选择', QMessageBox.ButtonRole.YesRole)
    #         self.askforNonStyleFile_box.exec()
    #         if self.askforNonStyleFile_box.clickedButton() == status_insist:
    #             self.mixedStylePath = styleFilePath
    #         else:
    #             self.mixedStylePathEdit.clear()
    #     else:
    #         self.mixedStylePath = styleFilePath

    def setSavePathToDefault(self):
        path = self.SubtitleSavePathEdit.text()
        defaultSubtitlePath = os.path.dirname(path) + '/' + os.path.basename(path).rstrip(
            str(path).split('.')[-1]) + "ass"
        self.SubtitleSavePathEdit.setText(defaultSubtitlePath)

    def updateSavePath(self):
        path = self.SubtitleSavePathEdit.text()
        if not is_path_exists_or_creatable(path):
            QMessageBox.warning(self, '保存路径不正确', '请重新选择正确的路径!\t\t\n', QMessageBox.StandardButton.Ok)
            print("保存路径有误")
        else:
            print(f"将会保存至: {path}")
            self.savePath = path

    def updateVideoType(self):
        self.videoType = self.videoTypeList.currentIndex()
        if self.videoType == 0:
            self.FlagOPcomboBox.setEnabled(True)
            print(f'当前视频类型: 全力回避flag酱')
        elif self.videoType == 1:
            self.FlagOPcomboBox.setEnabled(False)
            print(f'当前视频类型: 混血万事屋')
        elif self.videoType == 2:
            self.FlagOPcomboBox.setEnabled(False)
            print(f'当前视频类型: HundredNote')
        elif self.videoType == 3:
            self.FlagOPcomboBox.setEnabled(False)
            print(f'当前视频类型: HundredNote彩色版')
        elif self.videoType == 4:
            self.FlagOPcomboBox.setEnabled(False)
            print(f'当前视频类型: HundredNote Game')
        elif self.videoType == 5:
            self.FlagOPcomboBox.setEnabled(False)
            print(f'当前视频类型: 超能力高校')

    def raiseOpenFile(self):
        video_filter = "视频 (*.webm *.mp4 *.mov *.flv *.mkv *.m4v);;All Files (*)"
        filePath, openStatus = QFileDialog.getOpenFileName(self, '请选择要处理的视频', filter=video_filter)
        if openStatus:
            self.VideoPathEdit.setText(filePath)
            self.updateOpenPath()

    def raiseSaveFile(self):
        path = self.openPath
        defaultSavePath = os.path.basename(path).rstrip(
            str(path).split('.')[-1]) + "ass" if path != '' else 'output.ass'
        filePath, openStatus = QFileDialog.getSaveFileName(self, '请选择字幕要保存的位置', defaultSavePath,
                                                           '字幕文件 (*.ass)')
        if openStatus:
            self.SubtitleSavePathEdit.setText(filePath)
            self.updateSavePath()

    # def raiseFlagStyleSelect(self):
    #     stylePath, openStatus = QFileDialog.getOpenFileName(self, '请选择要处理的视频', filter="字幕 (*.ass)")
    #     if openStatus:
    #         self.flagStylePathEdit.setText(stylePath)
    #         # self.updateFlagStylePath()
    #
    # def raiseMixedStyleSelect(self):
    #     stylePath, openStatus = QFileDialog.getOpenFileName(self, '请选择要处理的视频', filter="字幕 (*.ass)")
    #     if openStatus:
    #         self.mixedStylePathEdit.setText(stylePath)
    #         # self.updateFlagStylePath()

    def checkForm(self, path: str):
        return path.split('.')[-1] in ["webm", "mp4", "mov", "flv", "mkv", "m4v"]

    def checkStyle(self, path: str):
        return path.split('.')[-1] == "ass"

    def updateOPstyle(self):
        self.opTpye = self.FlagOPcomboBox.currentIndex()
        print(f"opType: {self.opTypes[self.opTpye]}")

    def tryToStart(self):
        self.checkOpenPath()
        self.updateSavePath()
        self.updateOPstyle()
        if not (Path(self.openPath).is_file() and is_path_exists_or_creatable(self.savePath)):
            QMessageBox.warning(self, '路径不正确', '请选择正确的路径!\t\t\n', QMessageBox.StandardButton.Ok)
        elif os.path.exists(self.savePath):
            self.askforOverWrite_box = QMessageBox(QMessageBox.Icon.Question, '覆盖', '已存在该字幕文件\n'
                                                                                      '是否要覆盖？\t\t\n',
                                                   flags=Qt.WindowType.WindowStaysOnTopHint)
            self.askforOverWrite_box.setFixedSize(380, 135)
            status_reset = self.askforOverWrite_box.addButton('覆盖', QMessageBox.ButtonRole.YesRole)
            self.askforOverWrite_box.addButton('取消', QMessageBox.ButtonRole.NoRole)
            self.askforOverWrite_box.exec()
            if self.askforOverWrite_box.clickedButton() == status_reset:
                self.finish = True
                print('开始打轴...')
                self.close()
        else:
            self.finish = True
            print('开始打轴...')
            self.close()
            # self.setEnabled(False)

    def updateStyleType(self):
        self.styleType = self.styleTypeList.currentIndex()
        if self.styleType == 0:
            print(f'当前样式表: 全力回避flag酱')
        elif self.styleType == 1:
            print(f'当前样式表: 混血万事屋')
        elif self.styleType == 2:
            print(f'当前样式表: HundredNote')
        elif self.styleType == 3:
            print(f'当前样式表: HundredNote彩色版')
        elif self.styleType == 4:
            print(f'当前样式表: HundredNote Game')
        elif self.styleType == 5:
            print(f'当前样式表: 超能力高校')
        with open(self.stylePathList[self.styleType], 'r', encoding='utf-8') as file:
            stylesheet = file.read()
        self.StylePathEdit.clear()
        self.styleSheetEdit.setPlainText(stylesheet)

    def raiseStyleSelect(self):
        styleFilePath, openStatus = QFileDialog.getOpenFileName(self, '请选择字幕文件', filter="字幕 (*.ass)")
        if openStatus:
            self.StylePathEdit.setText(styleFilePath)
            self.updateStyleSheet()

    def updateStyleSheet(self):
        styleFilePath = self.StylePathEdit.text()
        if not self.checkStyle(styleFilePath):
            self.askforNonStyleFile_box = QMessageBox(QMessageBox.Icon.Question, '文件格式未识别',
                                                      '该文件不是ass文件，确认要选择该文件吗？\t\t\n',
                                                      flags=Qt.WindowType.WindowStaysOnTopHint)
            self.askforNonStyleFile_box.setFixedSize(380, 135)
            status_insist = self.askforNonStyleFile_box.addButton('确认', QMessageBox.ButtonRole.NoRole)
            self.askforNonStyleFile_box.addButton('重新选择', QMessageBox.ButtonRole.YesRole)
            self.askforNonStyleFile_box.exec()
            if self.askforNonStyleFile_box.clickedButton() == status_insist:
                self.stylePath = styleFilePath
            else:
                self.StylePathEdit.clear()
                return
        with open(styleFilePath, 'r', encoding='utf-8') as file:
            content = file.read()
        # 使用正则表达式匹配[V4+ Styles]和[Events]之间的内容
        pattern = r'\[V4\+ Styles\](.*?)\[Events\]'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            extracted_content = match.group(1).strip()
            self.styleSheetEdit.setPlainText(extracted_content)
        else:
            self.StylePathEdit.clear()


    def defaultStyleSheet(self):
        self.askforResetStyleSheet_box = QMessageBox(QMessageBox.Icon.Question, '重置', '重置后，您修改的所有内容将丢失\n'
                                                                                        '是否要重置为默认内容？\n'
                                                                                        '重置后如要保存请点击保存。\n',
                                                     flags=Qt.WindowType.WindowStaysOnTopHint)
        self.askforResetStyleSheet_box.setFixedSize(380, 135)
        status_reset = self.askforResetStyleSheet_box.addButton('重置', QMessageBox.ButtonRole.YesRole)
        self.askforResetStyleSheet_box.addButton('取消', QMessageBox.ButtonRole.NoRole)
        self.askforResetStyleSheet_box.exec()
        if self.askforResetStyleSheet_box.clickedButton() == status_reset:
            self.styleSheetEdit.setPlainText(self.styleBackupList[self.styleType])
            self.StylePathEdit.clear()

    def saveStyleSheet(self):
        self.askforSaveStyleSheet_box = QMessageBox(QMessageBox.Icon.Question, '保存', '随意改动此表可能会导致生成字幕样式异常或生成失败\n'
                                                                                       '请确保您明白自己在做什么\n'
                                                                                       '是否继续保存？\t\t\n',
                                                    flags=Qt.WindowType.WindowStaysOnTopHint)
        self.askforSaveStyleSheet_box.setFixedSize(380, 135)
        status_save = self.askforSaveStyleSheet_box.addButton('保存', QMessageBox.ButtonRole.YesRole)
        self.askforSaveStyleSheet_box.addButton('取消', QMessageBox.ButtonRole.NoRole)
        self.askforSaveStyleSheet_box.exec()
        if self.askforSaveStyleSheet_box.clickedButton() == status_save:
            stylesheet = self.styleSheetEdit.toPlainText()
            with open(self.stylePathList[self.styleType], 'w', encoding='utf-8') as file:
                file.write(stylesheet)
            QMessageBox.information(self, "成功", "样式表已保存", QMessageBox.StandardButton.Ok)

    def updateConfigType(self):
        self.configType = self.configTypeList.currentIndex()
        if self.configType == 0:
            print(f'当前配置文件: 全力回避flag酱')
        elif self.configType == 1:
            print(f'当前配置文件: 混血万事屋')
        elif self.configType == 2:
            print(f'当前配置文件: HundredNote')
        elif self.configType == 3:
            print(f'当前配置文件: HundredNote彩色版')
        elif self.configType == 4:
            print(f'当前配置文件: HundredNote Game')
        elif self.configType == 5:
            print(f'当前配置文件: 超能力高校')

    def saveDefaultConfig(self):
        self.askforSaveDefaultConfig_box = QMessageBox(QMessageBox.Icon.Question, '保存', '是否要保存默认配置?',
                                                       flags=Qt.WindowType.WindowStaysOnTopHint)
        self.askforSaveDefaultConfig_box.setFixedSize(380, 135)
        status_save = self.askforSaveDefaultConfig_box.addButton('保存', QMessageBox.ButtonRole.YesRole)
        self.askforSaveDefaultConfig_box.addButton('取消', QMessageBox.ButtonRole.NoRole)
        self.askforSaveDefaultConfig_box.exec()

        if self.askforSaveDefaultConfig_box.clickedButton() == status_save:
            isSuccess = True
            # # 默认样式文件
            # if self.flagStylePathEdit.text() != "":
            #     if not self.checkStyleFile(self.flagStylePathEdit.text(), flagStylePath):
            #         QMessageBox.warning(self, "警告", "全力回避flag酱样式保存失败！文件已损坏",
            #                             QMessageBox.StandardButton.Ok)
            #         isSuccess = False
            #
            # if self.mixedStylePathEdit.text() != "":
            #     if not self.checkStyleFile(self.mixedStylePathEdit.text(), mixedStylePath):
            #         QMessageBox.warning(self, "警告", "混血万事屋样式保存失败！文件已损坏",
            #                             QMessageBox.StandardButton.Ok)
            #         isSuccess = False

            # 默认视频类型
            setGlobalConfig('config', 'default_videotype', -2 - self.defaultVideoTypeGroup.checkedId())

            # 默认字幕文本类型
            if self.useDebugSubtextRadioButton.isChecked():
                setGlobalConfig('config', 'debug_subtitle', 1)
            else:
                setGlobalConfig('config', 'debug_subtitle', 0)

            if isSuccess:
                QMessageBox.information(self, "成功", "默认配置已保存", QMessageBox.StandardButton.Ok)

    # def checkStyleFile(self, path, savePath):
    #     # 打开并读取原始文件的全部内容
    #     with open(path, 'r', encoding='utf-8') as file:
    #         content = file.read()
    #
    #     # 使用正则表达式匹配[V4+ Styles]和[Events]之间的内容
    #     pattern = r'\[V4\+ Styles\](.*?)\[Events\]'
    #     match = re.search(pattern, content, re.DOTALL)
    #
    #     if match:
    #         # extracted_content = match.group(1).strip()  # 获取匹配的内容
    #         #
    #         # # 将提取的内容写入新文件
    #         # with open(savePath, 'w', encoding='utf-8') as new_file:
    #         #     new_file.write(extracted_content)
    #         return True
    #     else:
    #         return False

    def initAll(self):
        # config = configparser.ConfigParser()
        # config.read(globalConfigPath, encoding='utf-8')
        # global_config_dict = {section: dict(config[section]) for section in config.sections()}['config']
        # 默认视频类型同步
        defaultVideoType = int(getGlobalConfig("config", "default_videotype"))
        self.videoTypeList.setCurrentIndex(defaultVideoType)
        if defaultVideoType == 0:
            self.flagRadioButton.setChecked(True)
        elif defaultVideoType == 1:
            self.mixedRadioButton.setChecked(True)
        elif defaultVideoType == 2:
            self.HN_whiteRadioButton.setChecked(True)
        elif defaultVideoType == 3:
            self.HN_colorRadioButton.setChecked(True)
        elif defaultVideoType == 4:
            self.HN_gameRadioButton.setChecked(True)
        elif defaultVideoType == 5:
            self.parakoRadioButton.setChecked(True)

        # 字幕生成调试模式同步
        debugSubText = int(getGlobalConfig("config", "debug_subtitle"))
        if debugSubText == 0:
            self.unuseDebugSubtextRadioButton.setChecked(True)
        else:
            self.useDebugSubtextRadioButton.setChecked(True)


# def noticeAdminRun():
#     if getGlobalConfig("config", "font_init") == "0" and getGlobalConfig("config", "ignore_init") == "0":
#         noticeAdminRun_box = QMessageBox(QMessageBox.Icon.Information, '提示',
#                                          '右键该程序，选择“以管理员身份运行”可自动安装所需字体\n如不需安装字体，请点击不再提醒',
#                                          flags=Qt.WindowType.WindowStaysOnTopHint)
#         noticeAdminRun_box.setFixedSize(380, 135)
#         noticeAdminRun_box.addButton('关闭', QMessageBox.ButtonRole.NoRole)
#         is_ignore = noticeAdminRun_box.addButton('不再提醒', QMessageBox.ButtonRole.NoRole)
#         noticeAdminRun_box.exec()
#         if noticeAdminRun_box.clickedButton() == is_ignore:
#             setGlobalConfig("config", "ignore_init", 1)


def runGUI():
    GUI_APP = QtWidgets.QApplication(sys.argv)
    GUI_mainWindow = AutoSubtitle_class()
    GUI_mainWindow.setFixedSize(GUI_mainWindow.width(), GUI_mainWindow.height())
    GUI_mainWindow.show()
    GUI_APP.exec()
    return GUI_mainWindow.openPath, GUI_mainWindow.savePath, GUI_mainWindow.videoType, GUI_mainWindow.opTpye


if __name__ == "__main__":
    print(runGUI())
