from delta_scraper import DeltaScraper


def test_delta_scraper(capsys):
    class Foo(DeltaScraper):
        def fetch_data(self):
            return {"hello": "world"}

    foo = Foo(None)
    foo.test_mode = True
    assert None is foo.scrape_and_store()
    captured = capsys.readouterr()
    assert '{\n  "hello": "world"\n}\n' == captured.out
