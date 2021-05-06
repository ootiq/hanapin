from bs4 import BeautifulSoup
from .lib import Hanapin


class Yandex(Hanapin):
    """
    Yandex.com search

    @note: Yandex detects bot automatically
    """

    search_engine = "https://yandex.com/search/?text={query}&lr=114120"

    def __init__(self, query: str):
        super().__init__(query)

        self._results = self.__get_results()

    @property
    def results(self) -> list:
        return self._results

    def __get_results(self) -> list:
        """
        Yandex.com search resuts
        """

        res = []

        for i in self._soup.find_all("li", class_="serp-item"):
            try:
                # append each search result
                res.append(
                    {
                        "title": i.find("a").text,
                        "link": i.find("a")["href"],
                    }
                )
            except Exception:
                # do nothing if failed above
                continue

        return res