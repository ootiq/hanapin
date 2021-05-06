from .lib import Hanapin


class Bing(Hanapin):
    """
    Bing search
    """

    search_engine = "https://www.bing.com/search?q={query}&count={count}"

    def __init__(self, query: str, count: int = 10):
        super().__init__(query, count)

        self._results = self.__get_results()

    @property
    def results(self) -> list:
        return self._results

    def __get_results(self) -> list:
        """
        Bing.com search resuts
        """

        res = []

        for i in self._soup.find_all("li", class_="b_algo"):
            try:
                # append each search result
                res.append(
                    {"title": i.find("a").get_text(), "link": i.find("a")["href"]}
                )
            except Exception:
                # do nothing if failed above
                continue

        return res
