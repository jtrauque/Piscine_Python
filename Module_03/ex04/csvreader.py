import os
import sys
sys.tracebacklimit = 0


class CsvReader():
    def __init__(self, filename=None, sep=',', header=False,
                 skip_top=0, skip_bottom=0):
        if not filename or not os.path.exists(filename):
            raise ValueError("No valid filename")
        if not sep:
            raise ValueError("We neep separator to separate values")
        # with open(filename) as fp:
        # num_lines = sum(1 for line in fp)
        num_lines = sum(1 for line in open(filename))
        self.sep = sep
        self.header = header
        self.top = skip_top
        self.bot = num_lines - skip_bottom
        self.data = []
        self.size = 0
        self.first_line = []
        self.file = filename

    def __enter__(self):
        i = 0
        with open(self.file) as file:
            for line in file:
                line = line.replace("\n", "").replace(" ", "")
                words = line.split(self.sep)
                words = list(filter(bool, words))
                if self.size == 0:
                    self.size = len(words)
                    if self.header is True:
                        self.first_line = words
                        continue
                if self.size == len(words) and i >= self.top and i < self.bot:
                    self.data.append(words)
                elif self.size != len(words):
                    raise ValueError("File Corrupted")
                i += 1
        return self

    def __exit__(self, filename=None, sep=',', header=False,
                 skip_top=0, skip_bottom=0):
        if os.path.exists(self.file):
            try:
                with open(self.file) as file:
                    print("the file is closed")
            except IOError:
                print("the file is still open")
                # pass

    def getdata(self):
        return self.data

    def getheader(self):
        if self.header:
            return self.first_line
        return None

# from csvreader import CsvReader


if __name__ == "__main__":
    filename = sys.argv[1]
    with CsvReader(filename, skip_top=18, skip_bottom=0) as reader:
        if reader is None:
            print("File is corrupted or missing")
        else:
            print(reader.getheader(), end="\n")
            print(reader.getdata(), end="\n\n")

    with CsvReader(filename, header=True, skip_top=17,
                   skip_bottom=0) as reader:
        if reader is None:
            print("File is corrupted or missing")
        else:
            print(reader.getheader(), end="\n")
            print(reader.getdata(), end="\n\n")
