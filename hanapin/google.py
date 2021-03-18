from .lib import Hanapin


class Google(Hanapin):
    """
    Google search
    """

    search_engine = "https://www.google.com/search?q={query}"

    def __init__(self, query):
        super().__init__(query)

    def results(self) -> list:
        res = []

        for i in self._soup.find_all("div", class_="g"):
            try:
                # append each search result
                res.append(
                    {"title": i.find("a")["href"], "link": i.find("h3").get_text()}
                )
            except Exception:
                # do nothing if failed above
                continue

        return res
