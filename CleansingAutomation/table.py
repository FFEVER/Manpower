import scipy as sp
import numpy as np


class Table:
    def __init__(self, data):
        self.data = data

    def header(self):
        return self.data[0]

    def body(self):
        return self.data[1:]

    def concatenate(self, data):
        self.data = np.concatenate((self.data, data), axis=0)

    def __iter__(self):
        return iter(self.data)


def tsvtotable(filename, delimiter="\t", autostrip=False):
    data = sp.genfromtxt(filename,
                         delimiter=delimiter,
                         names=None,
                         encoding="utf-8",
                         autostrip=autostrip,
                         dtype=None)
    return Table(data)
