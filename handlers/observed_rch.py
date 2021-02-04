# code by Rodrigo Miranda (rodrigo.qmiranda@gmail.com)

from pandas import DataFrame

class txt(object):
    def __init__(self, f):
        self.f = f
        self.df = DataFrame(self.load())
        self.df = self.df.where(self.df != "NaN")
        self.df_backup = self.df[:]

    def reset(self):
        self.df = self.df_backup

    def load(self):
        with open(self.f, 'r') as reader:
            i = reader.next()
            lock = True
            r = {}
            for i in reader:
                if len(i) > 5:
                    i = i.replace("\n","")
                    i = i.split(":")
                    if len(i) > 1:
                        if not lock == True:
                            col = i[0].strip()
                            lock = True
                    else:
                        i = i[0].split("\t")
                        try:
                            r[col].append((i[0], i[2]))
                        except:
                            r[col] = [(i[0], i[2]),]
                        lock = True
                else:
                    lock = False
            seq = []
            for i in r.keys():
                for j in r[i]:
                    seq.append(int(j[0]))
            seq = list(set(seq))
            seq.sort()
            seq = map(str, seq)

            for i in r.keys():
                for j in seq:
                    lock = True
                    for l in r[i]:
                        if j.split(",")[0] == l[0]:
                            seq[seq.index(j)] = seq[seq.index(j)] + "," + l[1]
                            lock = False
                    if lock == True:
                        seq[seq.index(j)] = seq[seq.index(j)] + "," + "NaN"

            k = ["Seq"] + r.keys()
            r = {}
            for i in k:
                r[i] = [j.split(",")[k.index(i)] for j in seq]
            return(r)