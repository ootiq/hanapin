from .lib import Hanapin


class Ask(Hanapin):
    """
    Ask.com Search
    """

    search_engine = "https://www.ask.com/web?q={query}"

    def __init__(self, query: str):
        super().__init__(query)

        self._results = self.__get_results()

    @property
    def results(self) -> list:
        return self._results

    def __get_results(self) -> list:
        """
        Ask.com search resuts
        """

        res = []

        for i in self._soup.find_all("div", class_="PartialSearchResults-item"):
            try:
                # append each search result
                res.append(
                    {"title": i.find("a").get_text(), "link": i.find("a")["href"]}
                )
            except Exception:
                # do nothing if failed above
                continue

        return res