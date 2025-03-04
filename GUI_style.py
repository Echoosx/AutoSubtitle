# Form implementation generated from reading ui file 'GUI_style.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AutoSubtitle(object):
    def setupUi(self, AutoSubtitle):
        AutoSubtitle.setObjectName("AutoSubtitle")
        AutoSubtitle.resize(632, 281)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AutoSubtitle.sizePolicy().hasHeightForWidth())
        AutoSubtitle.setSizePolicy(sizePolicy)
        AutoSubtitle.setMouseTracking(False)
        AutoSubtitle.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        AutoSubtitle.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(parent=AutoSubtitle)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 631, 281))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.runsub = QtWidgets.QWidget()
        self.runsub.setObjectName("runsub")
        self.Title = QtWidgets.QLabel(parent=self.runsub)
        self.Title.setEnabled(True)
        self.Title.setGeometry(QtCore.QRect(20, 0, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(23)
        font.setBold(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.Title.setFont(font)
        self.Title.setMouseTracking(True)
        self.Title.setStyleSheet("")
        self.Title.setObjectName("Title")
        self.VideoPathEdit = DragAcceptableQLine(parent=self.runsub)
        self.VideoPathEdit.setGeometry(QtCore.QRect(20, 80, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.VideoPathEdit.setFont(font)
        self.VideoPathEdit.setStatusTip("")
        self.VideoPathEdit.setObjectName("VideoPathEdit")
        self.chooseButton = QtWidgets.QToolButton(parent=self.runsub)
        self.chooseButton.setGeometry(QtCore.QRect(500, 80, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.chooseButton.setFont(font)
        self.chooseButton.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        self.chooseButton.setObjectName("chooseButton")
        self.FlagOPcomboBox = QtWidgets.QComboBox(parent=self.runsub)
        self.FlagOPcomboBox.setGeometry(QtCore.QRect(500, 10, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.FlagOPcomboBox.setFont(font)
        self.FlagOPcomboBox.setObjectName("FlagOPcomboBox")
        self.videoTypeList = QtWidgets.QComboBox(parent=self.runsub)
        self.videoTypeList.setGeometry(QtCore.QRect(370, 40, 231, 25))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.videoTypeList.setFont(font)
        self.videoTypeList.setMouseTracking(True)
        self.videoTypeList.setObjectName("videoTypeList")
        self.SubtitleSavePathEdit = QtWidgets.QLineEdit(parent=self.runsub)
        self.SubtitleSavePathEdit.setGeometry(QtCore.QRect(20, 130, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.SubtitleSavePathEdit.setFont(font)
        self.SubtitleSavePathEdit.setAcceptDrops(False)
        self.SubtitleSavePathEdit.setObjectName("SubtitleSavePathEdit")
        self.Title_2 = QtWidgets.QLabel(parent=self.runsub)
        self.Title_2.setEnabled(True)
        self.Title_2.setGeometry(QtCore.QRect(230, 40, 141, 21))
        self.Title_3 = QtWidgets.QLabel(parent=self.runsub)
        self.Title_3.setEnabled(True)
        self.Title_3.setGeometry(QtCore.QRect(360, 10, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(13)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.Title_2.setFont(font)
        self.Title_2.setObjectName("Title_2")
        self.saveButton = QtWidgets.QToolButton(parent=self.runsub)
        self.saveButton.setGeometry(QtCore.QRect(500, 130, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("saveButton")
        self.startButton = QtWidgets.QPushButton(parent=self.runsub)
        self.startButton.setGeometry(QtCore.QRect(20, 180, 581, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        self.startButton.setFont(font)
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.startButton.setMouseTracking(False)
        self.startButton.setStyleSheet("")
        self.startButton.setAutoRepeat(False)
        self.startButton.setAutoRepeatDelay(301)
        self.startButton.setAutoDefault(False)
        self.startButton.setObjectName("startButton")
        self.Title.raise_()
        self.VideoPathEdit.raise_()
        self.FlagOPcomboBox.raise_()
        self.videoTypeList.raise_()
        self.SubtitleSavePathEdit.raise_()
        self.Title_2.raise_()
        self.saveButton.raise_()
        self.startButton.raise_()
        self.chooseButton.raise_()
        self.Title_3.raise_()
        self.tabWidget.addTab(self.runsub, "")
        self.default = QtWidgets.QWidget()
        self.default.setObjectName("default")
        self.flagStylePathEdit = DragAcceptableQLine(parent=self.default)
        self.flagStylePathEdit.setGeometry(QtCore.QRect(20, 20, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.flagStylePathEdit.setFont(font)
        self.flagStylePathEdit.setAcceptDrops(False)
        self.flagStylePathEdit.setStatusTip("")
        self.flagStylePathEdit.setText("")
        self.flagStylePathEdit.setObjectName("flagStylePathEdit")
        self.mixedStylePathEdit = DragAcceptableQLine(parent=self.default)
        self.mixedStylePathEdit.setGeometry(QtCore.QRect(20, 70, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.Title_3.setFont(font)
        self.Title_3.setObjectName("Title_3")
        self.mixedStylePathEdit.setFont(font)
        self.mixedStylePathEdit.setAcceptDrops(False)
        self.mixedStylePathEdit.setStatusTip("")
        self.mixedStylePathEdit.setObjectName("mixedStylePathEdit")
        self.flagStyleSelect = QtWidgets.QToolButton(parent=self.default)
        self.flagStyleSelect.setGeometry(QtCore.QRect(480, 20, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.flagStyleSelect.setFont(font)
        self.flagStyleSelect.setObjectName("flagStyleSelect")
        self.mixedStyleSelect = QtWidgets.QToolButton(parent=self.default)
        self.mixedStyleSelect.setGeometry(QtCore.QRect(480, 70, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.mixedStyleSelect.setFont(font)
        self.mixedStyleSelect.setObjectName("mixedStyleSelect")
        self.saveDefaultButton = QtWidgets.QPushButton(parent=self.default)
        self.saveDefaultButton.setGeometry(QtCore.QRect(220, 200, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.saveDefaultButton.setFont(font)
        self.saveDefaultButton.setObjectName("saveDefaultButton")
        self.label = QtWidgets.QLabel(parent=self.default)
        self.label.setGeometry(QtCore.QRect(20, 160, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.flagRadioButton = QtWidgets.QRadioButton(parent=self.default)
        self.flagRadioButton.setGeometry(QtCore.QRect(120, 110, 110, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.flagRadioButton.setFont(font)
        self.flagRadioButton.setChecked(True)
        self.flagRadioButton.setObjectName("flagRadioButton")
        self.defaultVideoTypeGroup = QtWidgets.QButtonGroup(AutoSubtitle)
        self.defaultVideoTypeGroup.setObjectName("defaultVideoTypeGroup")
        self.defaultVideoTypeGroup.addButton(self.flagRadioButton)
        self.mixedRadioButton = QtWidgets.QRadioButton(parent=self.default)
        self.mixedRadioButton.setGeometry(QtCore.QRect(240, 110, 95, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.mixedRadioButton.setFont(font)
        self.mixedRadioButton.setChecked(False)
        self.mixedRadioButton.setObjectName("mixedRadioButton")
        self.defaultVideoTypeGroup.addButton(self.mixedRadioButton)
        self.label_3 = QtWidgets.QLabel(parent=self.default)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(parent=self.default)
        self.label_5.setGeometry(QtCore.QRect(20, 130, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.useDebugSubtextRadioButton = QtWidgets.QRadioButton(parent=self.default)
        self.useDebugSubtextRadioButton.setGeometry(QtCore.QRect(120, 140, 95, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.useDebugSubtextRadioButton.setFont(font)
        self.useDebugSubtextRadioButton.setChecked(True)
        self.useDebugSubtextRadioButton.setObjectName("useDebugSubtextRadioButton")
        self.isDebugSubtextGroup = QtWidgets.QButtonGroup(AutoSubtitle)
        self.isDebugSubtextGroup.setObjectName("isDebugSubtextGroup")
        self.isDebugSubtextGroup.addButton(self.useDebugSubtextRadioButton)
        self.unuseDebugSubtextRadioButton = QtWidgets.QRadioButton(parent=self.default)
        self.unuseDebugSubtextRadioButton.setGeometry(QtCore.QRect(240, 140, 95, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.unuseDebugSubtextRadioButton.setFont(font)
        self.unuseDebugSubtextRadioButton.setCheckable(True)
        self.unuseDebugSubtextRadioButton.setChecked(False)
        self.unuseDebugSubtextRadioButton.setObjectName("unuseDebugSubtextRadioButton")
        self.isDebugSubtextGroup.addButton(self.unuseDebugSubtextRadioButton)
        self.HN_whiteRadioButton = QtWidgets.QRadioButton(parent=self.default)
        self.HN_whiteRadioButton.setGeometry(QtCore.QRect(340, 110, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.HN_whiteRadioButton.setFont(font)
        self.HN_whiteRadioButton.setChecked(False)
        self.HN_whiteRadioButton.setObjectName("HN_whiteRadioButton")
        self.defaultVideoTypeGroup.addButton(self.HN_whiteRadioButton)
        self.HN_colorRadioButton = QtWidgets.QRadioButton(parent=self.default)
        self.HN_colorRadioButton.setGeometry(QtCore.QRect(400, 110, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.HN_colorRadioButton.setFont(font)
        self.HN_colorRadioButton.setChecked(False)
        self.HN_colorRadioButton.setObjectName("HN_colorRadioButton")
        self.defaultVideoTypeGroup.addButton(self.HN_colorRadioButton)
        self.HN_gameRadioButton = QtWidgets.QRadioButton(parent=self.default)
        self.HN_gameRadioButton.setGeometry(QtCore.QRect(480, 110, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.HN_gameRadioButton.setFont(font)
        self.HN_gameRadioButton.setChecked(False)
        self.HN_gameRadioButton.setObjectName("HN_gameRadioButton")
        self.defaultVideoTypeGroup.addButton(self.HN_gameRadioButton)
        self.tabWidget.addTab(self.default, "")
        self.advanced = QtWidgets.QWidget()
        self.advanced.setObjectName("advanced")
        self.label_2 = QtWidgets.QLabel(parent=self.advanced)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.styleSheetEdit = QtWidgets.QPlainTextEdit(parent=self.advanced)
        self.styleSheetEdit.setGeometry(QtCore.QRect(20, 30, 461, 221))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.styleSheetEdit.setFont(font)
        self.styleSheetEdit.setPlainText("")
        self.styleSheetEdit.setObjectName("styleSheetEdit")
        self.saveStyleSheetButton = QtWidgets.QPushButton(parent=self.advanced)
        self.saveStyleSheetButton.setGeometry(QtCore.QRect(500, 220, 111, 31))
        self.saveStyleSheetButton.setObjectName("saveStyleSheetButton")
        self.defaultStyleSheetButton = QtWidgets.QPushButton(parent=self.advanced)
        self.defaultStyleSheetButton.setGeometry(QtCore.QRect(500, 180, 111, 31))
        self.defaultStyleSheetButton.setObjectName("defaultStyleSheetButton")
        self.label_4 = QtWidgets.QLabel(parent=self.advanced)
        self.label_4.setGeometry(QtCore.QRect(490, 40, 131, 131))
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.advanced, "")
        AutoSubtitle.setCentralWidget(self.centralwidget)

        self.retranslateUi(AutoSubtitle)
        self.tabWidget.setCurrentIndex(0)
        self.chooseButton.clicked.connect(AutoSubtitle.raiseOpenFile) # type: ignore
        self.saveButton.clicked.connect(AutoSubtitle.raiseSaveFile) # type: ignore
        self.startButton.clicked.connect(AutoSubtitle.tryToStart) # type: ignore
        self.SubtitleSavePathEdit.editingFinished.connect(AutoSubtitle.updateSavePath) # type: ignore
        self.videoTypeList.currentIndexChanged['int'].connect(AutoSubtitle.updateVideoType) # type: ignore
        self.FlagOPcomboBox.currentIndexChanged['int'].connect(AutoSubtitle.updateOPstyle) # type: ignore
        self.VideoPathEdit.dropAccepted.connect(AutoSubtitle.updateOpenPath) # type: ignore
        self.defaultStyleSheetButton.clicked.connect(AutoSubtitle.defaultStyleSheet) # type: ignore
        self.saveStyleSheetButton.clicked.connect(AutoSubtitle.saveStyleSheet) # type: ignore
        self.saveDefaultButton.clicked.connect(AutoSubtitle.saveDefaultConfig) # type: ignore
        self.flagStyleSelect.clicked.connect(AutoSubtitle.raiseFlagStyleSelect) # type: ignore
        self.mixedStyleSelect.clicked.connect(AutoSubtitle.raiseMixedStyleSelect) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(AutoSubtitle)

    def retranslateUi(self, AutoSubtitle):
        _translate = QtCore.QCoreApplication.translate
        AutoSubtitle.setWindowTitle(_translate("AutoSubtitle", "AutoSubtitle"))
        self.Title.setText(_translate("AutoSubtitle", "<html><head/><body><p><a href=\"https://github.com/Echoosx/AutoSubtitle\"><span style=\" color:#000000;\">自动打轴机 v1.3.0</span></a></p></body></html>"))
        self.VideoPathEdit.setPlaceholderText(_translate("AutoSubtitle", "可以将视频拖拽到这里"))
        self.chooseButton.setText(_translate("AutoSubtitle", "选择视频"))
        self.SubtitleSavePathEdit.setPlaceholderText(_translate("AutoSubtitle", "请选择字幕文件保存路径"))
        self.Title_2.setText(_translate("AutoSubtitle", "  请选择视频类型"))
        self.Title_3.setText(_translate("AutoSubtitle", "请选择Flag系列OP类型"))
        self.saveButton.setText(_translate("AutoSubtitle", "选择保存位置"))
        self.startButton.setText(_translate("AutoSubtitle", "开始打轴"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.runsub), _translate("AutoSubtitle", "运行"))
        self.flagStylePathEdit.setPlaceholderText(_translate("AutoSubtitle", "请选择全力回避flag酱打轴默认样式"))
        self.mixedStylePathEdit.setPlaceholderText(_translate("AutoSubtitle", "请选择混血万事屋打轴默认样式"))
        self.flagStyleSelect.setText(_translate("AutoSubtitle", "选择flag默认样式"))
        self.mixedStyleSelect.setText(_translate("AutoSubtitle", "选择混血默认样式"))
        self.saveDefaultButton.setText(_translate("AutoSubtitle", "保存"))
        self.label.setText(_translate("AutoSubtitle", "注：保存后，下次运行会默认使用当前设定"))
        self.flagRadioButton.setText(_translate("AutoSubtitle", "全力回避flag酱"))
        self.mixedRadioButton.setText(_translate("AutoSubtitle", "混血万事屋"))
        self.label_3.setText(_translate("AutoSubtitle", "默认视频类型："))
        self.label_5.setText(_translate("AutoSubtitle", "默认字幕文本："))
        self.useDebugSubtextRadioButton.setText(_translate("AutoSubtitle", "示范性字幕n"))
        self.unuseDebugSubtextRadioButton.setText(_translate("AutoSubtitle", "空白"))
        self.HN_whiteRadioButton.setText(_translate("AutoSubtitle", "HN"))
        self.HN_colorRadioButton.setText(_translate("AutoSubtitle", "HN彩色"))
        self.HN_gameRadioButton.setText(_translate("AutoSubtitle", "HN Game"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.default), _translate("AutoSubtitle", "默认"))
        self.label_2.setText(_translate("AutoSubtitle", "样式名对照表"))
        self.saveStyleSheetButton.setText(_translate("AutoSubtitle", "保存"))
        self.defaultStyleSheetButton.setText(_translate("AutoSubtitle", "重置"))
        self.label_4.setText(_translate("AutoSubtitle", "自定义样式名对照表\n"
"参照格式：\n"
"说话人 = 样式名\n"
"\n"
"[flag]和[mixed-blood]\n"
"下方分别是两类视频的\n"
"样式名对照表"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.advanced), _translate("AutoSubtitle", "高级"))
from DragAcceptableQLine import DragAcceptableQLine
