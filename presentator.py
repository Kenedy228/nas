from tabulate import tabulate


class Presentator:
    def __init__(self, title, conclusion, headers, indexes, data):
        self.title = title
        self.conclusion = conclusion
        self.headers = headers
        self.indexes = indexes
        self.data = data

    def print_content(self):
        if (len(self.title) > 0):
            print(self.title)
        
        if (len(self.indexes) > 0):
            print(tabulate(self.data, headers=self.headers, showindex=self.indexes, tablefmt="grid"))
        else:
            print(tabulate(self.data, headers=self.headers, tablefmt="grid"))

        if (len(self.conclusion) > 0):
            print(self.conclusion)
