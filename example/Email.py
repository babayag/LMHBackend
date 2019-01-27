

import re

from concurrent.futures import ThreadPoolExecutor as PoolExecutor
from bs4 import BeautifulSoup
from .BingSearch import BingSearch
from .Source import Source

from .JsonStructure import JsonStructure

class Email():

    def __init__(self):
        self.emails = []
        self.sources = []
        self.AllData = []

    def getEmail(self,enterUrl):
        urls = BingSearch.nbrPage(BingSearch, enterUrl)
        Source.__init__(Source)
        with PoolExecutor(max_workers=7) as executor:
            for _ in executor.map(BingSearch.initialSearch, urls):
                soup = BeautifulSoup(_, features="html.parser")
                lipath = soup.findAll("li", {"class": "b_algo"})
                li_number = 0
                while True:
                    try:
                        litext = lipath[li_number].text
                        # for line in the drivertextclear
                        for line in litext.splitlines():
                            # search all email in each line, return the objet searchNumbers of type list
                            searchEmails = re.findall(r"[a-zA-Z]+[\.\-]?\w*[\.\-]?\w+\.?\w*\@{}".format(enterUrl), line,flags=re.MULTILINE)
                            # for email in email_1 list

                            if searchEmails:
                                src = Source.search(Source, li_number, lipath)
                                for email in searchEmails:
                                    # add email in the emails list: return an object oy type NoneType
                                    self.emails.append(email)
                                    self.sources = Source.appendSource(Source, src)
                        li_number = li_number + 1
                    except:
                        break
        print(self.emails)
        print(self.sources)
        datasStructured = JsonStructure.JsonStructureReturn(JsonStructure, self.emails, self.sources, enterUrl)
        return datasStructured