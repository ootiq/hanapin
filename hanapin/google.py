from bs4 import BeautifulSoup
from .lib import Hanapin


class Google(Hanapin):
    """
    Google search
    """

    search_engine = "https://www.google.com/search?q={query}&num={count}"

    def __init__(self, query: str, count: int = 10):
        super().__init__(query, count)

    def results(self) -> list:
        """
        Google.com search resuts
        """

        res = []

        for i in self._soup.find_all("div", class_="g"):
            try:
                # append each search result
                res.append(
                    {
                        "title": self.__get_result_title(i),
                        "link": i.find("a")["href"],
                    }
                )
            except Exception:
                # do nothing if failed above
                continue

        return res

    def __get_result_title(self, result: BeautifulSoup) -> str:
        # search result could be a video which gets a different title,
        # solution is really clumsy, but it works and eliminates unnecessary titles

        r = result.find_all("h3")

        return r[len(r) - 1].get_text()
