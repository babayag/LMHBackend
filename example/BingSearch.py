import re
import sys
import http.client
import socket
from bs4 import BeautifulSoup


class BingSearch():

    def initialSearch(myUrl):

        # get_Page
        try:
            # always set a timeout when you connect to an external server
            url = "www.bing.com"
            connection = http.client.HTTPSConnection(url, timeout=10)

            connection.request("GET", myUrl)

            response = connection.getresponse()

            return response.read()
        except socket.timeout:
            # in a real world scenario you would probably do stuff if the
            # socket goes into timeout
            pass

    def nbrPage(self, enterUrl):
        myUrl = "/search?q=%40{}&first=11".format(enterUrl)

        result = self.initialSearch(myUrl)
        soup = BeautifulSoup(result, features="html.parser")
        txt = soup.find("span", {"class": "sb_count"}).text
        txt = txt.split(" ")[-2]
        txt = txt.split(",")
        txt1 = ""
        for i in range(0, len(txt)):
            txt1 = txt1 + txt[i]

        liste = []
        for nbrOfPage in range(1, int(txt1), 10):
            liste.append("/search?q=%40{}&first={}".format(enterUrl, nbrOfPage))
            dif = 256 - nbrOfPage
            if dif <= int(txt1):
                liste.append("/search?q=%40{}&first={}".format(enterUrl, nbrOfPage + dif))
        return liste
