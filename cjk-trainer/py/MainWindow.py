# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui',
# licensing of 'MainWindow.ui' applies.
#
# Created: Thu Mar 28 02:53:55 2019
#      by: pyside2-uic  running on PySide2 5.12.0
#
# WARNING! All changes made in this file will be lost!

from py.utilities.KeyPressEater import KeyPressEater
from PySide2 import QtCore, QtGui, QtWidgets
from py.importDeck import *
import sqlite3





class Ui_MainWindow(object):
    # def getListSelection(self):
    #     model = self.deckList.model()
    #     string = model.index(0)
    #     print(string.toString)

    @QtCore.Slot(QtCore.QModelIndex)
    def on_clicked(self, index):
        if index == self.indexOfCurrentDeck or index == False:  # I guess sometimes its false :S
            print("nothing to do")
        else:
            self.indexOfCurrentDeck = index
            self.nameOfCurrentDeck = index.data()
            self.wordTable.setRowCount(0)
            self.wordTable.clearContents()
            self.wordTable.reset()
            self.deckName.setText("Selected Deck: {}".format(index.data()))
            conn = sqlite3.connect('../data/vocab.db')
            result = conn.execute('SELECT * FROM {}'.format(index.data()))
            self.wordTable.setRowCount(0)
            self.wordTable.setColumnCount(
                6)  # This number should be fixed. In header file, try to fix widths. Columns will be static
            for row_number, row_data in enumerate(result):
                self.wordTable.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.wordTable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            conn.close()


    def __init__(self):
        self.indexOfCurrentDeck = 0
        self.nameOfCurrentDeck = ""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 720)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(960, 720))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/appicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(600, 400))
        self.centralwidget.setMaximumSize(QtCore.QSize(960, 720))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())

        # ADDED KEYPRESS EATER TAB BAR
        tabBar = QtWidgets.QTabBar()
        self.tabWidget.setTabBar(tabBar)
        eater = KeyPressEater(tabBar)
        tabBar.installEventFilter(eater)

        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_wordTable = QtWidgets.QWidget()
        self.tab_wordTable.setObjectName("tab_wordTable")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_wordTable)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem)
        self.label_deckList = QtWidgets.QLabel(self.tab_wordTable)
        self.label_deckList.setAlignment(QtCore.Qt.AlignCenter)
        self.label_deckList.setObjectName("label_deckList")
        self.horizontalLayout_12.addWidget(self.label_deckList)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.deckList = QtWidgets.QListWidget(self.tab_wordTable)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deckList.sizePolicy().hasHeightForWidth())
        self.deckList.setSizePolicy(sizePolicy)
        self.deckList.setMovement(QtWidgets.QListView.Free)
        self.deckList.setResizeMode(QtWidgets.QListView.Adjust)
        self.deckList.setObjectName("deckList")

        # Added - Prevent user from dragging list view objs
        self.deckList.setDragEnabled(False)
        self.deckList.clicked.connect(self.on_clicked)

        self.verticalLayout_5.addWidget(self.deckList)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_wordList_add = QtWidgets.QPushButton(self.tab_wordTable)
        self.pushButton_wordList_add.setObjectName("pushButton_wordList_add")
        self.gridLayout.addWidget(self.pushButton_wordList_add, 0, 1, 1, 1)
        self.pushButton_wordList_select = QtWidgets.QPushButton(self.tab_wordTable)
        self.pushButton_wordList_select.setObjectName("pushButton_wordList_select")
        # Added - Connect
        self.pushButton_wordList_select.clicked.connect(self.on_clicked)

        self.gridLayout.addWidget(self.pushButton_wordList_select, 0, 2, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem2)
        self.deckName = QtWidgets.QLabel(self.tab_wordTable)
        self.deckName.setAlignment(QtCore.Qt.AlignCenter)
        self.deckName.setObjectName("deckName")
        self.horizontalLayout_10.addWidget(self.deckName)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.verticalLayout_12.addLayout(self.horizontalLayout_10)
        self.wordTable = QtWidgets.QTableWidget(self.tab_wordTable)
        self.wordTable.setEditTriggers(
            QtWidgets.QAbstractItemView.DoubleClicked | QtWidgets.QAbstractItemView.EditKeyPressed | QtWidgets.QAbstractItemView.SelectedClicked)
        self.wordTable.setAlternatingRowColors(True)
        self.wordTable.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.wordTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.wordTable.setTextElideMode(QtCore.Qt.ElideRight)
        self.wordTable.setObjectName("wordTable")
        self.wordTable.setColumnCount(0)
        self.wordTable.setRowCount(0)
        self.verticalLayout_12.addWidget(self.wordTable)
        self.horizontalLayout_3.addLayout(self.verticalLayout_12)
        self.tabWidget.addTab(self.tab_wordTable, "")
        self.tab_flashcards = QtWidgets.QWidget()
        self.tab_flashcards.setObjectName("tab_flashcards")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_flashcards)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.label_flashWord = QtWidgets.QLabel(self.tab_flashcards)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_flashWord.setFont(font)
        self.label_flashWord.setObjectName("label_flashWord")
        self.horizontalLayout_2.addWidget(self.label_flashWord)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_nextWord = QtWidgets.QPushButton(self.tab_flashcards)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_nextWord.sizePolicy().hasHeightForWidth())
        self.pushButton_nextWord.setSizePolicy(sizePolicy)
        self.pushButton_nextWord.setObjectName("pushButton_nextWord")
        self.horizontalLayout_4.addWidget(self.pushButton_nextWord)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.checkBox_autoPlay = QtWidgets.QCheckBox(self.tab_flashcards)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_autoPlay.sizePolicy().hasHeightForWidth())
        self.checkBox_autoPlay.setSizePolicy(sizePolicy)
        self.checkBox_autoPlay.setObjectName("checkBox_autoPlay")
        self.horizontalLayout_4.addWidget(self.checkBox_autoPlay)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.verticalLayout_6)
        self.tabWidget.addTab(self.tab_flashcards, "")
        self.tab_typing = QtWidgets.QWidget()
        self.tab_typing.setObjectName("tab_typing")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_typing)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem9)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.label_typingWord = QtWidgets.QLabel(self.tab_typing)
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK JP")
        font.setPointSize(24)
        self.label_typingWord.setFont(font)
        self.label_typingWord.setObjectName("label_typingWord")
        self.horizontalLayout_5.addWidget(self.label_typingWord)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem12)
        self.line_2 = QtWidgets.QFrame(self.tab_typing)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_7.addWidget(self.line_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lineEdit_answer = QtWidgets.QLineEdit(self.tab_typing)
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK JP")
        self.lineEdit_answer.setFont(font)
        self.lineEdit_answer.setText("")
        self.lineEdit_answer.setObjectName("lineEdit_answer")
        self.horizontalLayout_6.addWidget(self.lineEdit_answer)
        self.pushButton_enter = QtWidgets.QPushButton(self.tab_typing)
        self.pushButton_enter.setAutoDefault(False)
        self.pushButton_enter.setDefault(True)
        self.pushButton_enter.setObjectName("pushButton_enter")
        self.horizontalLayout_6.addWidget(self.pushButton_enter)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.progressBar = QtWidgets.QProgressBar(self.tab_typing)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_7.addWidget(self.progressBar)
        self.label_fractionCorrect = QtWidgets.QLabel(self.tab_typing)
        self.label_fractionCorrect.setObjectName("label_fractionCorrect")
        self.horizontalLayout_7.addWidget(self.label_fractionCorrect)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem13)
        self.pushButton_notSure_Skip = QtWidgets.QPushButton(self.tab_typing)
        self.pushButton_notSure_Skip.setObjectName("pushButton_notSure_Skip")
        self.horizontalLayout_7.addWidget(self.pushButton_notSure_Skip)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.verticalLayout_4.addLayout(self.verticalLayout_7)
        self.tabWidget.addTab(self.tab_typing, "")
        self.tab_quiz = QtWidgets.QWidget()
        self.tab_quiz.setObjectName("tab_quiz")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tab_quiz)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_8.addItem(spacerItem14)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem15)
        self.label_quizWord = QtWidgets.QLabel(self.tab_quiz)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_quizWord.setFont(font)
        self.label_quizWord.setObjectName("label_quizWord")
        self.horizontalLayout_8.addWidget(self.label_quizWord)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem16)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_8.addItem(spacerItem17)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pushButton_quizChoice1 = QtWidgets.QPushButton(self.tab_quiz)
        self.pushButton_quizChoice1.setObjectName("pushButton_quizChoice1")
        self.verticalLayout_9.addWidget(self.pushButton_quizChoice1)
        self.pushButton_quizChoice2 = QtWidgets.QPushButton(self.tab_quiz)
        self.pushButton_quizChoice2.setObjectName("pushButton_quizChoice2")
        self.verticalLayout_9.addWidget(self.pushButton_quizChoice2)
        self.horizontalLayout_9.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.pushButton_quizChoice3 = QtWidgets.QPushButton(self.tab_quiz)
        self.pushButton_quizChoice3.setObjectName("pushButton_quizChoice3")
        self.verticalLayout_10.addWidget(self.pushButton_quizChoice3)
        self.pushButton_quizChoice4 = QtWidgets.QPushButton(self.tab_quiz)
        self.pushButton_quizChoice4.setObjectName("pushButton_quizChoice4")
        self.verticalLayout_10.addWidget(self.pushButton_quizChoice4)
        self.horizontalLayout_9.addLayout(self.verticalLayout_10)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        self.verticalLayout_11.addLayout(self.verticalLayout_8)
        self.tabWidget.addTab(self.tab_quiz, "")
        self.tab_tones = QtWidgets.QWidget()
        self.tab_tones.setObjectName("tab_tones")
        self.tabWidget.addTab(self.tab_tones, "")
        self.tab_statistics = QtWidgets.QWidget()
        self.tab_statistics.setObjectName("tab_statistics")
        self.tabWidget.addTab(self.tab_statistics, "")
        self.tab_settings = QtWidgets.QWidget()
        self.tab_settings.setObjectName("tab_settings")
        self.tabWidget.addTab(self.tab_settings, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 30))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.actionFrom_Template = QtWidgets.QAction(MainWindow)
        self.actionFrom_Template.setObjectName("actionFrom_Template")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionTemplate_Data = QtWidgets.QAction(MainWindow)
        self.actionTemplate_Data.setObjectName("actionTemplate_Data")
        self.actionUser_Data = QtWidgets.QAction(MainWindow)
        self.actionUser_Data.setObjectName("actionUser_Data")
        self.actionImport_Data = QtWidgets.QAction(MainWindow)
        self.actionImport_Data.setObjectName("actionImport_Data")
        self.actionHow_to_play = QtWidgets.QAction(MainWindow)
        self.actionHow_to_play.setObjectName("actionHow_to_play")
        self.actionUserGuide = QtWidgets.QAction(MainWindow)
        self.actionUserGuide.setObjectName("actionUserGuide")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionDonate = QtWidgets.QAction(MainWindow)
        self.actionDonate.setObjectName("actionDonate")
        self.menu_file.addAction(self.actionOpen)
        self.menu_file.addAction(self.actionQuit)
        self.menu_help.addAction(self.actionUserGuide)
        self.menu_help.addSeparator()
        self.menu_help.addAction(self.actionAbout)
        self.menu_help.addAction(self.actionDonate)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.lineEdit_answer, QtCore.SIGNAL("returnPressed()"), self.pushButton_enter.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "cjk_trainer 0.2", None, -1))
        self.label_deckList.setText(QtWidgets.QApplication.translate("MainWindow", "Deck List", None, -1))
        self.pushButton_wordList_add.setText(QtWidgets.QApplication.translate("MainWindow", "Add", None, -1))
        self.pushButton_wordList_select.setText(QtWidgets.QApplication.translate("MainWindow", "Select", None, -1))
        self.deckName.setText(QtWidgets.QApplication.translate("MainWindow", "Selected Deck: ", None, -1))
        self.wordTable.setSortingEnabled(True)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_wordTable),
                                  QtWidgets.QApplication.translate("MainWindow", "Word List", None, -1))
        self.label_flashWord.setText(QtWidgets.QApplication.translate("MainWindow", "null", None, -1))
        self.pushButton_nextWord.setText(QtWidgets.QApplication.translate("MainWindow", "Next Word", None, -1))
        self.checkBox_autoPlay.setText(QtWidgets.QApplication.translate("MainWindow", "Autoplay", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_flashcards),
                                  QtWidgets.QApplication.translate("MainWindow", "Flashcards", None, -1))
        self.label_typingWord.setText(QtWidgets.QApplication.translate("MainWindow", "null", None, -1))
        self.lineEdit_answer.setPlaceholderText(
            QtWidgets.QApplication.translate("MainWindow", "Enter your answer", None, -1))
        self.pushButton_enter.setText(QtWidgets.QApplication.translate("MainWindow", "Enter", None, -1))
        self.label_fractionCorrect.setText(QtWidgets.QApplication.translate("MainWindow", "0/0", None, -1))
        self.pushButton_notSure_Skip.setText(QtWidgets.QApplication.translate("MainWindow", "Not sure", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_typing),
                                  QtWidgets.QApplication.translate("MainWindow", "Typing", None, -1))
        self.label_quizWord.setText(QtWidgets.QApplication.translate("MainWindow", "null", None, -1))
        self.pushButton_quizChoice1.setText(QtWidgets.QApplication.translate("MainWindow", "Word1", None, -1))
        self.pushButton_quizChoice2.setText(QtWidgets.QApplication.translate("MainWindow", "Word2", None, -1))
        self.pushButton_quizChoice3.setText(QtWidgets.QApplication.translate("MainWindow", "Word3", None, -1))
        self.pushButton_quizChoice4.setText(QtWidgets.QApplication.translate("MainWindow", "Word4", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_quiz),
                                  QtWidgets.QApplication.translate("MainWindow", "Quiz", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_tones),
                                  QtWidgets.QApplication.translate("MainWindow", "Tones", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_statistics),
                                  QtWidgets.QApplication.translate("MainWindow", "Statistics", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_settings),
                                  QtWidgets.QApplication.translate("MainWindow", "Settings", None, -1))
        self.menu_file.setTitle(QtWidgets.QApplication.translate("MainWindow", "Fi&le", None, -1))
        self.menu_help.setTitle(QtWidgets.QApplication.translate("MainWindow", "&Help", None, -1))
        self.actionFrom_Template.setText(QtWidgets.QApplication.translate("MainWindow", "From Template...", None, -1))
        self.actionQuit.setText(QtWidgets.QApplication.translate("MainWindow", "&Quit", None, -1))
        self.actionOpen.setText(QtWidgets.QApplication.translate("MainWindow", "&Open", None, -1))
        self.actionTemplate_Data.setText(QtWidgets.QApplication.translate("MainWindow", "&Template Data", None, -1))
        self.actionUser_Data.setText(QtWidgets.QApplication.translate("MainWindow", "&User Data", None, -1))
        self.actionImport_Data.setText(QtWidgets.QApplication.translate("MainWindow", "&Import Data", None, -1))
        self.actionHow_to_play.setText(QtWidgets.QApplication.translate("MainWindow", "How to play", None, -1))
        self.actionUserGuide.setText(QtWidgets.QApplication.translate("MainWindow", "&User Guide", None, -1))
        self.actionAbout.setText(QtWidgets.QApplication.translate("MainWindow", "About", None, -1))
        self.actionDonate.setText(QtWidgets.QApplication.translate("MainWindow", "Donate", None, -1))

