class UrlShortenerTestCaseMixin(object):
    """Mixin to be used in the TestCases
    """

    def setUp(self):
        super().setUp()
        self.long_url = "https://google.com"
