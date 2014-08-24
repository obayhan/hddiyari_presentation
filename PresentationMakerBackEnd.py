# -*- coding: utf-8 -*-
from PyQt4.QtCore import QString
from PyQt4.QtGui import QFileDialog, QMessageBox, QMainWindow

__author__ = 'ozgur'
__creation_date__ = '13.08.2014' '00:45'
from engine import MovieInfoFetcher, ImageProcessor, MovieMetadata


class PresentationMakerBackEnd():
    # from PresentationMakerBackEnd import PresentationMakerBackEnd as PMB
    # QtCore.QObject.connect(self.btn_CreateCover, QtCore.SIGNAL(_fromUtf8("clicked()")), self.create_cover)
    # QtCore.QObject.connect(self.btn_CreateCaps, QtCore.SIGNAL(_fromUtf8("clicked()")), self.create_caps)
    # QtCore.QObject.connect(self.btn_SelectMovie, QtCore.SIGNAL(_fromUtf8("clicked()")), self.select_movie)
    # QtCore.QObject.connect(self.actionFilm, QtCore.SIGNAL(_fromUtf8("activated()")), self.create_presentation_movie)
    # QtCore.QObject.connect(self.actionMuzik, QtCore.SIGNAL(_fromUtf8("activated()")), self.create_presentation_audio)
    # QtCore.QObject.connect(self.actionOyun, QtCore.SIGNAL(_fromUtf8("activated()")), self.create_presentation_game)
    # QtCore.QObject.connect(self.actionAbout, QtCore.SIGNAL(_fromUtf8("activated()")), self.show_about)
    # QtCore.QObject.connect(self.btn_MovieInfo, QtCore.SIGNAL(_fromUtf8("clicked()")), self.get_movie_info)

    def create_cover(self):
        ip = ImageProcessor()
        self.txt_Cover.setText(ip.prepare_image(self.txt_CoverLink.text(), "cover"))

    def create_caps(self):
        ip = ImageProcessor()
        if self.txt_CapLink1.text() != "":
            self.txt_Cap1.setText(ip.prepare_image(self.txt_CapLink1.text(), "1"))
        if self.txt_CapLink2.text() != "":
            self.txt_Cap2.setText(ip.prepare_image(self.txt_CapLink2.text(), "2"))
        if self.txt_CapLink3.text() != "":
            self.txt_Cap3.setText(ip.prepare_image(self.txt_CapLink3.text(), "3"))
        if self.txt_CapLink4.text() != "":
            self.txt_Cap4.setText(ip.prepare_image(self.txt_CapLink4.text(), "4"))
        if self.txt_CapLink5.text() != "":
            self.txt_Cap5.setText(ip.prepare_image(self.txt_CapLink5.text(), "5"))

    def select_movie(self):
        movie_path = QFileDialog.getOpenFileName().toUtf8()
        print movie_path
        mmd = MovieMetadata()
        info = mmd.get_movie_metadata(movie_path)
        self.txt_Info.setText(info)


    def create_presentation_movie(self):
        output = ""
        output += u"[align=center][color=#FF0000][size=x-large][b]" + self.txt_Head.text() + u"[/b][/size][/color]\n"
        output += u"[IMG]" + self.txt_Cover.text() + u"[/IMG]\n"
        output += u"[img]http://hddiyari.net/sablonlar/Filmdetaylariii.png[/img]\n"
        output += u"[size=small][b][color=#FF0000]Yönetmen :[/color] " + self.txt_Director.text() + u"\n"
        output += u"[color=#FF0000]Yazar: [/color] " + self.txt_Author.text() + u"\n"
        output += u"[color=#FF0000]Oyuncular : [/color] " + self.txt_Actors.toPlainText() + u"\n"
        output += u"[color=#FF0000]Tür : [/color] " + self.txt_Genre.text() + u" [/b][/size]\n"
        output += u"[img]http://hddiyari.net/sablonlar/Filmkonusu.png[/img]\n"
        output += u"[size=small][b]" + self.txt_Description.toPlainText() + u"[/b][/size]\n"
        output += u"[img]http://hddiyari.net/sablonlar/Fragman.png[/img]\n"
        output += u"[youtube]" + self.txt_Youtube.text() + u"[/youtube]\n"
        output += u"[img]http://hddiyari.net/sablonlar/EkranGoruntusu.png[/img]\n"
        output += u"[IMG]" + self.txt_Cap1.text() + u"[/IMG]\n"
        output += u"[IMG]" + self.txt_Cap2.text() + u"[/IMG]\n"
        output += u"[IMG]" + self.txt_Cap3.text() + u"[/IMG]\n"
        output += u"[IMG]" + self.txt_Cap4.text() + u"[/IMG]\n"
        output += u"[IMG]" + self.txt_Cap5.text() + u"[/IMG]\n"
        output += u"[IMG]http://hddiyari.net/sablonlar/seedediniz.png[/IMG]\n"
        output += u"[img]http://hddiyari.net/sablonlar/infobilgi.png[/img]\n"
        output += u"[code]+" + self.txt_Info.toPlainText() + u"+[/code][/align]\n"

        self.txt_Output.setPlainText(output)
        self.tabWidget.setCurrentIndex(3)

    def create_presentation_audio(self):
        pass

    def create_presentation_game(self):
        pass

    def get_movie_info(self):
        mif = MovieInfoFetcher()
        if self.txt_InfoUrl.text() != "":
            url = unicode(self.txt_InfoUrl.text())
            parsed = mif.parse_movie_divxplanet(url) or {}
            self.txt_Head.setText(parsed["title"])
            self.txt_Director.setText(parsed["directors"])
            self.txt_Author.setText(parsed["authors"])
            self.txt_Genre.setText(parsed["genre"])
            self.txt_Actors.setText(parsed["actors"])
            self.txt_Description.setText(parsed["description"])

    def show_about(self):
        QMessageBox.about(QMainWindow(),"Hakkinda", "v:1.1 \nby mozgur \nHdDiyari.net")