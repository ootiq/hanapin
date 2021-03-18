from .lib import Hanapin


class Bing(Hanapin):
    """
    Bing search
    """

    search_engine = "https://www.bing.com/search?q={query}"

    def __init__(self, query):
        super().__init__(query)

    def results(self) -> dict:
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
