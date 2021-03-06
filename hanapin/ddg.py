from .lib import Hanapin


class DuckDuckGo(Hanapin):
    """
    Duckduckgo search
    """

    search_engine = "https://html.duckduckgo.com/html/?q={query}"

    def __init__(self, query: int):
        super().__init__(query)

        self._results = self.__get_results()

    @property
    def results(self) -> list:
        return self._results

    def __get_results(self) -> list:
        """
        DuckDuckGo.com search resuts
        """

        res = []

        for i in self._soup.find_all(
            "div", class_="result results_links results_links_deep web-result"
        ):
            try:
                # append each search result
                res.append(
                    {"title": i.find("a").get_text(), "link": i.find("a")["href"]}
                )
            except Exception:
                # do nothing if failed above
                continue

        return res
