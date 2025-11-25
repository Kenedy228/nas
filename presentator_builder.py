from presentator import *


class PresentatorBuilder:
    def set_title(self, title):
        self.title = title

    def set_conclusion(self, conclusion):
        self.conclusion = conclusion

    def set_headers(self, headers):
        self.headers = headers

    def set_indexes(self, indexes):
        self.indexes = indexes

    def set_data(self, data):
        self.data = data

    def build(self):
        return Presentator(self.title, self.conclusion, self.headers, self.indexes, self.data)
