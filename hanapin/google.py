from .lib import Hanapin


class Google(Hanapin):
    """
    Google search
    """

    search_engine = "https://www.google.com/search?q={query}&num={count}"

    def __init__(self, query: str, count: int = 10):
        super().__init__(query, count)

    def results(self) -> list:
        res = []

        for i in self._soup.find_all("div", class_="g"):
            try:
                # append each search result
                res.append(
                    {"title": i.find("h3").get_text(), "link": i.find("a")["href"]}
                )
            except Exception:
                # do nothing if failed above
                continue

        return res
