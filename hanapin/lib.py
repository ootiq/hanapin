from bs4 import BeautifulSoup
import requests
import sys
import urllib.parse as urlparser


class Hanapin:
    UAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
    search_engine = ""

    def __init__(self, query):
        self.query = query
        self._soup = self.__init_request()

    def __init_request(self) -> BeautifulSoup:
        try:
            r = requests.get(
                self.search_engine.format(
                    query=urlparser.quote_plus(self.query)
                ),  # encode query strings
                headers={"User-Agent": self.UAgent},
            )

            # assert status code is OK
            assert r.status_code == 200

        except requests.ConnectionError:
            sys.exit("No internet connection...")

        except AssertionError:
            sys.exit("There was a problem with your search, please try again later")

        # return soup
        return BeautifulSoup(r.text, "lxml")  # lxml is faster,

    def results(self) -> dict:
        """
        Get search results (override this method in subclass)
        """
