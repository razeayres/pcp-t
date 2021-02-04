# code by Rodrigo Miranda (rodrigo.qmiranda@gmail.com)

from pandas import read_csv
from numpy import nan

class txt(object):
    def __init__(self, f, n):
        """f = filename, r = reach"""
        self.f = f
        self.names = ["RCH", "MON", "FLOW_OUTcms"]
        self.usecols = [1, 3, 6]
        self.df = read_csv(f, header=None, delim_whitespace=True, skiprows=9, usecols=self.usecols, names=self.names)
        self.df = self.df[self.df.MON <= 12]
        self.df = self.df[self.df.RCH == n]
        self.df.insert(0, 'Seq', range(1, 1 + len(self.df)))
        self.df_backup = self.df[:]

    def reset(self):
        self.df = self.df_backup














