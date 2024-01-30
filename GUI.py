import os
import sys
from pathlib import Path

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QLineEdit
from PyQt6.QtCore import Qt

from GUI_style import Ui_AutoSubtitle
from verifyPath import is_path_exists_or_creatable
import configparser
from io import StringIO
import re

global_config_dict = {}


class AutoSubtitle_class(QtWidgets.QMainWindow, Ui_AutoSubtitle):
    def __init__(self):
        super(AutoSubtitle_class, self).__init__()
        self.setupUi(self)
        self.openPath = self.savePath = str()
        self.flagStylePath = self.mixedStylePath = str()
        self.videoTypeList.addItems(["全力回避Flag酱", "混血万事屋"])
        self.videoTypeList.setCurrentIndex(0)
        self.videoType = self.videoTypeList.currentIndex()
        self.finish = False
        self.newOP = True
        self.initAll()
        # self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)

    def closeEvent(self, event):
        if not self.finish:
            sys.exit()

    def updateOpenPath(self):
        path = self.VideoPathEdit.text()
        if not Path(path).is_file():
            QMessageBox.warning(self, '无法找到源文件', '请重新选择正确的路径!\t\t\n', QMessageBox.StandardButton.Ok)
            print("源文件路径有误")
        elif self.checkForm(path):
            print(f"将会打开: {path}")
            self.openPath = path
            defaultSubtitlePath = os.path.dirname(path) + '/' + os.path.basename(path).rstrip(
                str(path).split('.')[-1]) + "ass"
            self.SubtitleSavePathEdit.setText(defaultSubtitlePath)
        else:
            self.askforNonVideoFile_box = QMessageBox(QMessageBox.Icon.Question, '文件格式未识别',
                                                      '该文件疑似非视频文件，确认要选择该文件吗？\t\t\n')
            self.askforNonVideoFile_box.setFixedSize(380, 135)
            status_insist = self.askforNonVideoFile_box.addButton('确认', QMessageBox.ButtonRole.NoRole)
            self.askforNonVideoFile_box.addButton('重新选择', QMessageBox.ButtonRole.YesRole)
            self.askforNonVideoFile_box.exec()
            if self.askforNonVideoFile_box.clickedButton() == status_insist:
                print(f"将会打开: {path}")
                self.openPath = path
            else:
                self.VideoPathEdit.clear()

    def updateFlagStylePath(self, styleFilePath: str):
        if not Path(styleFilePath).is_file():
            QMessageBox.warning(self, '无法找到源文件', '请重新选择正确的路径!\t\t\n', QMessageBox.StandardButton.Ok)
            print("源文件路径有误")
        if not self.checkStyle(styleFilePath):
            self.askforNonStyleFile_box = QMessageBox(QMessageBox.Icon.Question, '文件格式未识别',
                                                      '该文件不是ass文件，确认要选择该文件吗？\t\t\n')
            self.askforNonStyleFile_box.setFixedSize(380, 135)
            status_insist = self.askforNonStyleFile_box.addButton('确认', QMessageBox.ButtonRole.NoRole)
            self.askforNonStyleFile_box.addButton('重新选择', QMessageBox.ButtonRole.YesRole)
            self.askforNonStyleFile_box.exec()
            if self.askforNonStyleFile_box.clickedButton() == status_insist:
                self.flagStylePath = styleFilePath
            else:
                self.flagStylePathEdit.clear()
        else:
            self.flagStylePath = styleFilePath

    def updateMixedStylePath(self, styleFilePath: str):
        if not Path(styleFilePath).is_file():
            QMessageBox.warning(self, '无法找到源文件', '请重新选择正确的路径!\t\t\n', QMessageBox.StandardButton.Ok)
            print("源文件路径有误")
        if not self.checkStyle(styleFilePath):
            self.askforNonStyleFile_box = QMessageBox(QMessageBox.Icon.Question, '文件格式未识别',
                                                      '该文件不是ass文件，确认要选择该文件吗？\t\t\n')
            self.askforNonStyleFile_box.setFixedSize(380, 135)
            status_insist = self.askforNonStyleFile_box.addButton('确认', QMessageBox.ButtonRole.NoRole)
            self.askforNonStyleFile_box.addButton('重新选择', QMessageBox.ButtonRole.YesRole)
            self.askforNonStyleFile_box.exec()
            if self.askforNonStyleFile_box.clickedButton() == status_insist:
                self.mixedStylePath = styleFilePath
            else:
                self.mixedStylePathEdit.clear()
        else:
            self.mixedStylePath = styleFilePath

    def setSavePathToDefault(self):
        path = self.openPath
        defaultSavePath = str(path).rstrip(str(path).split('.')[-1]) + "ass" if path != '' else os.path.join(
            os.getcwd(), 'output.ass')
        self.SubtitleSavePathEdit.setText(defaultSavePath)
        self.updateSavePath()

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
            self.FlagNewOPcheckBox.setEnabled(True)
            print(f'当前视频类型: 全力回避flag酱')
        elif self.videoType == 1:
            self.FlagNewOPcheckBox.setEnabled(False)
            print(f'当前视频类型: 混血万事屋')

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
        filePath, openStatus = QFileDialog.getSaveFileName(self, '请选择字幕要保存的位置', defaultSavePath, '字幕文件 (*.ass)')
        if openStatus:
            self.SubtitleSavePathEdit.setText(filePath)
            self.updateSavePath()

    def raiseFlagStyleSelect(self):
        stylePath, openStatus = QFileDialog.getOpenFileName(self, '请选择要处理的视频', filter="字幕 (*.ass)")
        if openStatus:
            self.flagStylePathEdit.setText(stylePath)
            # self.updateFlagStylePath()

    def raiseMixedStyleSelect(self):
        stylePath, openStatus = QFileDialog.getOpenFileName(self, '请选择要处理的视频', filter="字幕 (*.ass)")
        if openStatus:
            self.mixedStylePathEdit.setText(stylePath)
            # self.updateFlagStylePath()

    def checkForm(self, path: str):
        return path.split('.')[-1] in ["webm", "mp4", "mov", "flv", "mkv", "m4v"]

    def checkStyle(self, path: str):
        return path.split('.')[-1] == "ass"

    def updateOPstyle(self):
        self.newOP = self.FlagNewOPcheckBox.isChecked()
        print(f'NewOP: {str(self.newOP)}')

    def tryToStart(self):
        self.updateOpenPath()
        self.updateSavePath()
        self.updateOPstyle()
        if not (Path(self.openPath).is_file() and is_path_exists_or_creatable(self.savePath)):
            QMessageBox.warning(self, '路径不正确', '请选择正确的路径!\t\t\n', QMessageBox.StandardButton.Ok)
        else:
            self.finish = True
            print('开始打轴...')
            self.close()
            # self.setEnabled(False)

    def defaultStyleSheet(self):
        self.askforResetStyleSheet_box = QMessageBox(QMessageBox.Icon.Question, '重置', '重置后，用户修改的所有内容都将丢失\n'
                                                                                      '是否确认要重置样式对照表？\t\t\n')
        self.askforResetStyleSheet_box.setFixedSize(380, 135)
        status_reset = self.askforResetStyleSheet_box.addButton('重置', QMessageBox.ButtonRole.YesRole)
        self.askforResetStyleSheet_box.addButton('取消', QMessageBox.ButtonRole.NoRole)
        self.askforResetStyleSheet_box.exec()
        if self.askforResetStyleSheet_box.clickedButton() == status_reset:
            with open('config/style_backup.ini', 'r', encoding='utf-8') as file:
                default_stylesheet = file.read()
                self.styleSheetEdit.setPlainText(default_stylesheet)
                with open('config/style.ini', 'w', encoding='utf-8') as file:
                    file.write(default_stylesheet)

    def saveStyleSheet(self):
        stylesheet = self.styleSheetEdit.toPlainText()
        config = configparser.ConfigParser()
        try:
            config.read_file(StringIO(stylesheet))
            style_dict = {section: dict(config.items(section)) for section in config.sections()}

            self.askforSaveStyleSheet_box = QMessageBox(QMessageBox.Icon.Question, '保存', '保存后，将按照此表中设定的样式名进行打轴\n'
                                                                                         '是否继续保存样式对照表？\t\t\n')
            self.askforSaveStyleSheet_box.setFixedSize(380, 135)
            status_save = self.askforSaveStyleSheet_box.addButton('保存', QMessageBox.ButtonRole.YesRole)
            self.askforSaveStyleSheet_box.addButton('取消', QMessageBox.ButtonRole.NoRole)
            self.askforSaveStyleSheet_box.exec()
            if self.askforSaveStyleSheet_box.clickedButton() == status_save:
                stylesheet = self.styleSheetEdit.toPlainText()
                with open('config/style.ini', 'w', encoding='utf-8') as file:
                    file.write(stylesheet)
                QMessageBox.information(self, "成功", "样式名对照表已保存", QMessageBox.StandardButton.Ok)

        except Exception as e:
            QMessageBox.warning(self, "失败", "格式错误，无法保存", QMessageBox.StandardButton.Ok)

    def saveDefaultConfig(self):
        self.askforSaveDefaultConfig_box = QMessageBox(QMessageBox.Icon.Question, '保存', '是否要保存默认配置?')
        self.askforSaveDefaultConfig_box.setFixedSize(380, 135)
        status_save = self.askforSaveDefaultConfig_box.addButton('保存', QMessageBox.ButtonRole.YesRole)
        self.askforSaveDefaultConfig_box.addButton('取消', QMessageBox.ButtonRole.NoRole)
        self.askforSaveDefaultConfig_box.exec()

        if self.askforSaveDefaultConfig_box.clickedButton() == status_save:
            isSuccess = True
            # 默认样式文件
            if self.flagStylePathEdit.text() != "":
                if not self.checkStyleFile(self.flagStylePathEdit.text(), "config/flag.txt"):
                    QMessageBox.warning(self, "警告", "全力回避flag酱样式保存失败！文件已损坏", QMessageBox.StandardButton.Ok)
                    isSuccess = False
            if self.mixedStylePathEdit.text() != "":
                if not self.checkStyleFile(self.mixedStylePathEdit.text(), "config/mixed.txt"):
                    QMessageBox.warning(self, "警告", "混血万事屋样式保存失败！文件已损坏", QMessageBox.StandardButton.Ok)
                    isSuccess = False

            # 默认视频类型
            config = configparser.ConfigParser()
            if self.flagRadioButton.isChecked():
                global_config_dict['defaultVideoType'] = "0"
            else:
                global_config_dict['defaultVideoType'] = "1"

            # 默认字幕文本类型
            if self.useDebugSubtextRadioButton.isChecked():
                global_config_dict['debugSubText'] = "1"
            else:
                global_config_dict['debugSubText'] = "0"

            config['config'] = global_config_dict
            with open('config/config.ini', 'w') as configfile:
                config.write(configfile)

            if isSuccess:
                QMessageBox.information(self, "成功", "默认配置已保存", QMessageBox.StandardButton.Ok)

    def checkStyleFile(self, path, savePath):
        print(path)
        # 打开并读取原始文件的全部内容
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        print(content)
        # 使用正则表达式匹配[V4+ Styles]和[Events]之间的内容
        pattern = r'\[V4\+ Styles\](.*?)\[Events\]'
        match = re.search(pattern, content, re.DOTALL)

        if match:
            extracted_content = match.group(1).strip()  # 获取匹配的内容

            # 将提取的内容写入新文件
            with open(savePath, 'w') as new_file:
                new_file.write(extracted_content)
            return True
        else:
            return False

    def initAll(self):
        config = configparser.ConfigParser()
        config.read('config/config.ini')
        global_config_dict = {section: dict(config[section]) for section in config.sections()}['config']
        # 默认视频类型同步
        defaultVideoType = int(global_config_dict['defaultvideotype'])
        self.videoTypeList.setCurrentIndex(defaultVideoType)
        if defaultVideoType == 0:
            self.flagRadioButton.setChecked(True)
        else:
            self.mixedRadioButton.setChecked(True)

        # 字幕生成调试模式同步
        debugSubText = int(global_config_dict['debugsubtext'])
        if debugSubText == 0:
            self.unuseDebugSubtextRadioButton.setChecked(True)
        else:
            self.useDebugSubtextRadioButton.setChecked(True)

        # styleSheet初始化同步
        with open('config/style.ini', 'r', encoding='utf-8') as file:
            stylesheet = file.read()
        self.styleSheetEdit.setPlainText(stylesheet)


def runGUI():
    GUI_APP = QtWidgets.QApplication(sys.argv)
    GUI_mainWindow = AutoSubtitle_class()
    GUI_mainWindow.setFixedSize(GUI_mainWindow.width(), GUI_mainWindow.height())
    GUI_mainWindow.show()
    GUI_APP.exec()
    return GUI_mainWindow.openPath, GUI_mainWindow.savePath, GUI_mainWindow.videoType, GUI_mainWindow.newOP


if __name__ == "__main__":
    print(runGUI())
