# -*- coding: utf-8 -*-
import os
import urllib2
import urllib
from mechanize import Browser
from bs4 import BeautifulSoup
import re
from PIL import Image

import pyimgur

favi = "/home/ozgur/mount/media/Series/Conan/ConanTheBarbarian/Conan.the.Barbarian.1982.iNTERNAL.DVDRiP.XViD.CD1-HLS.avi"
fmkv = "/home/ozgur/mount/media/TorrentTemp/All.About.Steve.2009.720p.BluRay.DUAL.x264-CBGB(HDA).mkv"

from hachoir_core.error import HachoirError
from hachoir_core.cmd_line import unicodeFilename
from hachoir_parser import createParser
from hachoir_core.tools import makePrintable
from hachoir_metadata import extractMetadata
from hachoir_core.i18n import getTerminalCharset
from sys import argv, stderr, exit

__author__ = 'ozgur'
__creation_date__ = '11.08.2014' '23:15'
CLIENT_ID = "48fa40a51f1c795"
HDR = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


class MovieInfoFetcher():
    def __init__(self):
        pass

    def getunicode(self, soup):
        body = ''
        if isinstance(soup, unicode):
            soup = soup.replace('&#39;', "'")
            soup = soup.replace('&quot;', '"')
            soup = soup.replace('&nbsp;', ' ')
            body += soup
        else:
            if not soup.contents:
                return ''
            con_list = soup.contents
            for con in con_list:
                body = body + self.getunicode(con)
        return body

    @staticmethod
    def parse_movie_divxplanet(link):
        directors = ""
        authors = ""
        actors = ""
        genre = ""
        req = urllib2.Request(link, headers=HDR)
        page = urllib2.urlopen(req)
        soup = BeautifulSoup(page.read())

        temp_list = soup.find_all('div', itemprop='director')
        for item in temp_list:
            directors += item.a.span.text + ", "

        temp_list = soup.find_all('div', itemprop='author')
        for item in temp_list:
            authors += item.a.span.text + ", "

        title = soup.find('span', itemprop='alternativeHeadline').text or ""

        temp_list = soup.find_all('div', itemprop='actor')
        for item in temp_list:
            actors += item.a.span.text + ", "

        temp_list = soup.find_all('span', itemprop='genre')
        for item in temp_list:
            genre += item.text + ", "
        description = soup.find('span', itemprop='description').text or ""

        retval = {
            'directors': directors,
            'authors': authors,
            'title': title,
            'actors': actors,
            'genre': genre,
            'description': description,
        }
        return retval


    def parse_movie_imdb(self, link):
        br = Browser()
        br.open(link)

        link = br.find_link(url_regex=re.compile(r'/title/tt.*'))
        res = br.follow_link(link)

        soup = BeautifulSoup(res.read())

        movie_title = self.getunicode(soup.find('title'))
        rate = soup.find('span', itemprop='ratingValue')
        rating = self.getunicode(rate)

        actors = []
        actors_soup = soup.findAll('a', itemprop='actors')
        for i in range(len(actors_soup)):
            actors.append(self.getunicode(actors_soup[i]))

        des = soup.find('meta', {'name': 'description'})['content']

        genre = []
        infobar = soup.find('div', {'class': 'infobar'})
        r = infobar.find('', {'title': True})['title']
        genrelist = infobar.findAll('a', {'href': True})

        for i in range(len(genrelist) - 1):
            genre.append(self.getunicode(genrelist[i]))
        release_date = self.getunicode(genrelist[-1])

        print movie_title, rating + '/10.0'
        print 'Relase Date:', release_date
        print 'Rated', r
        print ''
        print 'Genre:',
        print ', '.join(genre)
        print '\nActors:',
        print ', '.join(actors)
        print '\nDescription:'
        print des


class ImageProcessor():
    def __init__(self):
        pass

    def _download_image(self, link, path):
        print(link + " >> " + path)
        testfile = urllib.URLopener(HDR)
        testfile.retrieve(link, path)
        testfile.close()

    def _resize_image(self, path):
        size = 500, 500
        im = Image.open(path)
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(path)

    def _upload_image(self, path):
        im = pyimgur.Imgur(CLIENT_ID)
        uploaded_image = im.upload_image(path, title="HDDiyari")
        return uploaded_image.link


    def prepare_image(self, link, name):
        retval = ""
        link = str(link)
        if not os.path.exists("temp"):
            os.makedirs("temp")
        if link != "":
            path = os.path.join("temp", name) + ".jpg"
            self._download_image(link, path)
            self._resize_image(path)
            retval = self._upload_image(path)
        return retval


class MovieMetadata():
    def __init__(self):
        pass

    def get_movie_metadata(self, filename):
        filename, realname = unicodeFilename(filename), filename
        # parser = createParser(filename, realname)
        parser = createParser(filename, filename)
        if not parser:
            print >> stderr, "Unable to parse file"
            exit(1)
        try:
            metadata = extractMetadata(parser)
        except HachoirError, err:
            print "Metadata extraction error: %s" % unicode(err)
            metadata = None
        if not metadata:
            print "Unable to extract metadata"
            exit(1)

        text = metadata.exportPlaintext()
        charset = getTerminalCharset()
        retval = ""
        for line in text:
            retval += makePrintable(line, charset) + u"\n"
        return retval
