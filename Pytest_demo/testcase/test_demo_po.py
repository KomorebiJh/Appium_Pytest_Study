from Pytest_demo.pagebase.app import App


class TestDemo:




    def setup(self):
        self.search_page=App.start().to_search()

    def test_search_po(self):
        self.search_page.search('pdd')
        assert self.search_page.get_current_price() > 10

    def teardown(self):
        App.quit()