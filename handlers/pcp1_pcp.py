# code by Rodrigo Miranda (rodrigo.qmiranda@gmail.com)

from os import remove, path
from pandas import DataFrame

class txt(object):
    def __init__(self, f):
        self.f = f
        self.df = DataFrame(self.read(5))
        self.df_backup = self.df[:]
        self.stations = None

    def reset(self):
        self.df = self.df_backup

    def read(self, n):
        with open(self.f, 'r') as reader:
            i = reader.next()
            i = i.replace("\n","")
            i = [i[0:7]] + i[7:].split(",")[:-1]
            yield(i)

            for i in reader:
                i = i.replace("\n","")
                i = [i[0:7]] + [i[j:j+n] for j in range(7, len(i), n)]
                yield(i)

    def del_cols(self, t):
        for i in t:
            self.df = self.df.drop(columns=[i])

    def write_file(self):
        tmp = path.join(path.dirname(self.f), 'temp.txt')
        self.df.to_csv(tmp, header=None, index=None, sep=',', mode='w')
        with open(tmp, mode = 'r') as reader:
            with open(self.f, mode = 'w') as writer:
                lines = reader.readlines()
                h = lines[0]
                h = h.replace(' ', '')
                self.stations = h[8:].replace('\n', '').split(",")
                h = h[:8].replace(',', '  ') + h[8:]
                writer.write(h)
                for i in lines[1:]:
                    i = i.replace(",", "")
                    writer.write(i)
        remove(tmp)