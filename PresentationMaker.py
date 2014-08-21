# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PresentationMaker.ui'
#
# Created: Thu Aug 21 18:13:23 2014
# by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PresentationMakerBackEnd import PresentationMakerBackEnd as PMB

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object, PMB):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 900)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 900))
        MainWindow.setMaximumSize(QtCore.QSize(800, 900))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("resources/skull1.JPG")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtGui.QTabWidget.Triangular)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-2, 9, 791, 791))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_film = QtGui.QWidget()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.tab_film.setFont(font)
        self.tab_film.setObjectName(_fromUtf8("tab_film"))
        self.gridLayoutWidget = QtGui.QWidget(self.tab_film)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 771, 741))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.txt_CapLink4 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txt_CapLink4.setObjectName(_fromUtf8("txt_CapLink4"))
        self.gridLayout.addWidget(self.txt_CapLink4, 16, 1, 1, 1)
        self.btn_CreateCaps = QtGui.QPushButton(self.gridLayoutWidget)
        self.btn_CreateCaps.setObjectName(_fromUtf8("btn_CreateCaps"))
        self.gridLayout.addWidget(self.btn_CreateCaps, 15, 2, 1, 1)
        self.txt_Genre = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txt_Genre.setObjectName(_fromUtf8("txt_Genre"))
        self.gridLayout.addWidget(self.txt_Genre, 6, 1, 1, 3)
        self.line_3 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.gridLayout.addWidget(self.line_3, 18, 0, 1, 4)
        self.btn_SelectMovie = QtGui.QPushButton(self.gridLayoutWidget)
        self.btn_SelectMovie.setObjectName(_fromUtf8("btn_SelectMovie"))
        self.gridLayout.addWidget(self.btn_SelectMovie, 19, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 13, 0, 5, 1)
        self.line = QtGui.QFrame(self.gridLayoutWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 8, 0, 1, 4)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.txt_Head = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txt_Head.setObjectName(_fromUtf8("txt_Head"))
        self.gridLayout.addWidget(self.txt_Head, 1, 1, 1, 3)
        self.txt_CapLink3 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txt_CapLink3.setObjectName(_fromUtf8("txt_CapLink3"))
        self.gridLayout.addWidget(self.txt_CapLink3, 15, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.line_4 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout.addWidget(self.line_4, 12, 0, 1, 4)
        self.label_8 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 11, 0, 1, 1)
        self.txt_Info = QtGui.QTextEdit(self.gridLayoutWidget)
        self.txt_Info.setObjectName(_fromUtf8("txt_Info"))
        self.gridLayout.addWidget(self.txt_Info, 19, 2, 1, 2)
        self.btn_CreateCover = QtGui.QPushButton(self.gridLayoutWidget)
        self.btn_CreateCover.setObjectName(_fromUtf8("btn_CreateCover"))
        self.gridLayout.addWidget(self.btn_CreateCover, 11, 2, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.gridLayoutWidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout.addWidget(self.line_2, 10, 0, 1, 4)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 9, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 19, 0, 1, 1)
        self.txt_Actors = QtGui.QTextEdit(self.gridLayoutWidget)
        self.txt_Actors.setObjectName(_fromUtf8("txt_Actors"))
        self.gridLayout.addWidget(self.txt_Actors, 5, 1, 1, 3)
        self.txt_Author = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txt_Author.setObjectName(_fromUtf8("txt_Author"))
        self.gridLayout.addWidget(self.txt_Author, 4, 1, 1, 3)
        self.txt_CapLink1 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txt_CapLink1.setObjectName(_fromUtf8("txt_CapLink1"))
        self.gridLayout.addWidget(self.txt_CapLink1, 13, 1, 1, 1)
        self.txt_Description = QtGui.QTextEdit(self.gridLayoutWidget)
        self.txt_Description.setObjectName(_fromUtf8("txt_Description"))
        self.gridLayout.addWidget(self.txt_Description, 7, 1, 1, 3)
        self.txt_Director = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txt_Director.setObjectName(_fromUtf8("txt_Director"))
        self.gridLayout.addWidget(self.txt_Director, 3, 1, 1, 3)
        self.txt_CoverLink = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txt_CoverLink.setText(_fromUtf8(""))
        self.txt_CoverLink.setObjectName(_fromUtf8("txt_CoverLink"))
        self.gridLayout.addWidget(self.txt_CoverLink, 11, 1, 1, 1)
        self.txt_CapLink2 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txt_CapLink2.setObjectName(_fromUtf8("txt_CapLink2"))
        self.gridLayout.addWidget(self.txt_CapLink2, 14, 1, 1, 1)
        self.txt_Youtube = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txt_Youtube.setObjectName(_fromUtf8("txt_Youtube"))
        self.gridLayout.addWidget(self.txt_Youtube, 9, 1, 1, 3)
        self.txt_CapLink5 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txt_CapLink5.setObjectName(_fromUtf8("txt_CapLink5"))
        self.gridLayout.addWidget(self.txt_CapLink5, 17, 1, 1, 1)
        self.txt_Cover = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txt_Cover.setObjectName(_fromUtf8("txt_Cover"))
        self.gridLayout.addWidget(self.txt_Cover, 11, 3, 1, 1)
        self.txt_InfoUrl = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txt_InfoUrl.setObjectName(_fromUtf8("txt_InfoUrl"))
        self.gridLayout.addWidget(self.txt_InfoUrl, 0, 1, 1, 3)
        self.btn_MovieInfo = QtGui.QPushButton(self.gridLayoutWidget)
        self.btn_MovieInfo.setObjectName(_fromUtf8("btn_MovieInfo"))
        self.gridLayout.addWidget(self.btn_MovieInfo, 0, 0, 1, 1)
        self.txt_Cap1 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txt_Cap1.setObjectName(_fromUtf8("txt_Cap1"))
        self.gridLayout.addWidget(self.txt_Cap1, 13, 3, 1, 1)
        self.txt_Cap2 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txt_Cap2.setObjectName(_fromUtf8("txt_Cap2"))
        self.gridLayout.addWidget(self.txt_Cap2, 14, 3, 1, 1)
        self.txt_Cap3 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txt_Cap3.setObjectName(_fromUtf8("txt_Cap3"))
        self.gridLayout.addWidget(self.txt_Cap3, 15, 3, 1, 1)
        self.txt_Cap4 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txt_Cap4.setObjectName(_fromUtf8("txt_Cap4"))
        self.gridLayout.addWidget(self.txt_Cap4, 16, 3, 1, 1)
        self.txt_Cap5 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.txt_Cap5.setObjectName(_fromUtf8("txt_Cap5"))
        self.gridLayout.addWidget(self.txt_Cap5, 17, 3, 1, 1)
        self.tabWidget.addTab(self.tab_film, _fromUtf8(""))
        self.tab_oyun = QtGui.QWidget()
        self.tab_oyun.setObjectName(_fromUtf8("tab_oyun"))
        self.tabWidget.addTab(self.tab_oyun, _fromUtf8(""))
        self.tab_muzik = QtGui.QWidget()
        self.tab_muzik.setObjectName(_fromUtf8("tab_muzik"))
        self.tabWidget.addTab(self.tab_muzik, _fromUtf8(""))
        self.tab_output = QtGui.QWidget()
        self.tab_output.setObjectName(_fromUtf8("tab_output"))
        self.txt_Output = QtGui.QPlainTextEdit(self.tab_output)
        self.txt_Output.setGeometry(QtCore.QRect(3, 1, 781, 751))
        self.txt_Output.setObjectName(_fromUtf8("txt_Output"))
        self.tabWidget.addTab(self.tab_output, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuD_n_t_r = QtGui.QMenu(self.menubar)
        self.menuD_n_t_r.setObjectName(_fromUtf8("menuD_n_t_r"))
        self.menuHakk_nda = QtGui.QMenu(self.menubar)
        self.menuHakk_nda.setObjectName(_fromUtf8("menuHakk_nda"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionFilm = QtGui.QAction(MainWindow)
        self.actionFilm.setObjectName(_fromUtf8("actionFilm"))
        self.actionMuzik = QtGui.QAction(MainWindow)
        self.actionMuzik.setObjectName(_fromUtf8("actionMuzik"))
        self.actionOyun = QtGui.QAction(MainWindow)
        self.actionOyun.setObjectName(_fromUtf8("actionOyun"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuD_n_t_r.addAction(self.actionFilm)
        self.menuD_n_t_r.addAction(self.actionOyun)
        self.menuD_n_t_r.addAction(self.actionMuzik)
        self.menuHakk_nda.addAction(self.actionAbout)
        self.menubar.addAction(self.menuD_n_t_r.menuAction())
        self.menubar.addAction(self.menuHakk_nda.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.btn_CreateCover, QtCore.SIGNAL(_fromUtf8("clicked()")), self.create_cover)
        QtCore.QObject.connect(self.btn_CreateCaps, QtCore.SIGNAL(_fromUtf8("clicked()")), self.create_caps)
        QtCore.QObject.connect(self.btn_SelectMovie, QtCore.SIGNAL(_fromUtf8("clicked()")), self.select_movie)
        QtCore.QObject.connect(self.actionFilm, QtCore.SIGNAL(_fromUtf8("activated()")), self.create_presentation_movie)
        QtCore.QObject.connect(self.actionMuzik, QtCore.SIGNAL(_fromUtf8("activated()")), self.create_presentation_audio)
        QtCore.QObject.connect(self.actionOyun, QtCore.SIGNAL(_fromUtf8("activated()")), self.create_presentation_game)
        QtCore.QObject.connect(self.actionAbout, QtCore.SIGNAL(_fromUtf8("activated()")), self.show_about)
        QtCore.QObject.connect(self.btn_MovieInfo, QtCore.SIGNAL(_fromUtf8("clicked()")), self.get_movie_info)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "HDdiyarı.Net Sunum Hazırlayıcı", None))
        self.txt_CapLink4.setPlaceholderText(_translate("MainWindow", "Resmin URLsini giriniz...", None))
        self.btn_CreateCaps.setText(_translate("MainWindow", "Caps Hazırla", None))
        self.btn_SelectMovie.setText(_translate("MainWindow", "Film Dosyasını Seçiniz", None))
        self.label_2.setText(_translate("MainWindow", "Yönetmen", None))
        self.label_3.setText(_translate("MainWindow", "Yazar", None))
        self.label_9.setText(_translate("MainWindow", "CAPS", None))
        self.label.setText(_translate("MainWindow", "Başlık", None))
        self.txt_CapLink3.setPlaceholderText(_translate("MainWindow", "Resmin URLsini giriniz...", None))
        self.label_4.setText(_translate("MainWindow", "Oyuncular", None))
        self.label_5.setText(_translate("MainWindow", "Tür", None))
        self.label_8.setText(_translate("MainWindow", "Afiş", None))
        self.btn_CreateCover.setText(_translate("MainWindow", "Afişi Hazırla", None))
        self.label_6.setText(_translate("MainWindow", "Konu", None))
        self.label_7.setText(_translate("MainWindow", "Youtube", None))
        self.label_10.setText(_translate("MainWindow", "Info", None))
        self.txt_CapLink1.setPlaceholderText(_translate("MainWindow", "Resmin URLsini giriniz...", None))
        self.txt_CoverLink.setPlaceholderText(_translate("MainWindow", "Resmin URLsini giriniz...", None))
        self.txt_CapLink2.setPlaceholderText(_translate("MainWindow", "Resmin URLsini giriniz...", None))
        self.txt_Youtube.setPlaceholderText(_translate("MainWindow", "URL giriniz...(youtube.com)", None))
        self.txt_CapLink5.setPlaceholderText(_translate("MainWindow", "Resmin URLsini giriniz...", None))
        self.txt_InfoUrl.setPlaceholderText(_translate("MainWindow", "Filmin URLsini giriniz...(divxplanet.com)", None))
        self.btn_MovieInfo.setText(_translate("MainWindow", "Film Bilgisi Getir", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_film), _translate("MainWindow", "Film", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_oyun), _translate("MainWindow", "Oyun", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_muzik), _translate("MainWindow", "Müzik", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_output), _translate("MainWindow", "Sunum", None))
        self.menuD_n_t_r.setTitle(_translate("MainWindow", "Sunum Hazırla", None))
        self.menuHakk_nda.setTitle(_translate("MainWindow", "Hakkında", None))
        self.actionFilm.setText(_translate("MainWindow", "Film", None))
        self.actionMuzik.setText(_translate("MainWindow", "Müzik", None))
        self.actionOyun.setText(_translate("MainWindow", "Oyun", None))
        self.actionAbout.setText(_translate("MainWindow", "Sürüm", None))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

