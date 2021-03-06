import unittest

from hanapin import Google, Bing, DuckDuckGo, Ask, Yandex


class TestSearch(unittest.TestCase):
    def test_google(self):
        google = Google("google")
        self.assertTrue(len(google.results) > 0, "Google OK")

    def test_bing(self):
        bing = Bing("bing")
        self.assertTrue(len(bing.results) > 0, "Bing OK")

    def test_ddg(self):
        ddg = DuckDuckGo("Duckduckgo")
        self.assertTrue(len(ddg.results) > 0, "DuckDuckGo OK")

    def test_ask(self):
        ask = Ask("Duckduckgo")
        self.assertTrue(len(ask.results) > 0, "Ask OK")

    def test_yandex(self):
        yandex = Yandex("Yandex")
        self.assertTrue(len(yandex.results) > 0, "Yandex OK")

    def test_no_results(self):
        g = Google("alksdjlakjsdklajsdkljasd")
        b = Bing("alksdjlakjsdklajsdkljasd")
        d = DuckDuckGo("alksdjlakjsdklajsdkljasd")
        a = Ask("alksdjlakjsdklajsdkljasd")
        y = Yandex("alksdjlakjsdklajsdkljasd")

        self.assertTrue(len(g.results) == 0, "No results >> Google")
        self.assertTrue(len(b.results) == 0, "No results >> Bing")
        self.assertTrue(len(d.results) == 0, "No results >> DuckDuckGo")
        self.assertTrue(len(a.results) == 0, "No results >> Ask")
        self.assertTrue(len(y.results) == 0, "No results >> Yandex")


if __name__ == "__main__":
    unittest.main()