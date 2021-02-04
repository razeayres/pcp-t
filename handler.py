# code by Rodrigo Miranda (rodrigo.qmiranda@gmail.com)

from handlers import output_rch, observed_rch
from functions import nash
from numpy import nan
from pandas import concat
from math import isnan

class handle(object):
    def __init__(self, f0, f1):
        self.sim = f0
        self.obs = f1
        self.nash = self.get_nash()

    def get_nash(self):
        obs = observed_rch.txt(self.obs).df
        for i in list(obs.columns.values):
            if not i == 'Seq':
                n = int(i.split("_")[1])
                sim = output_rch.txt(self.sim, n).df
                sim = sim[sim.Seq.isin(obs['Seq'].tolist())]    # updates sim using the Seq list from obs

                m = sim["FLOW_OUTcms"].tolist()
                o = obs[i].tolist()

                mo = []
                for j in zip(m, o):
                    a = float(j[0])
                    b = float(j[1])
                    if (isnan(a) == False) and (isnan(b) == False):
                        mo.append((a, b))
                m = [j[0] for j in mo]
                o = [j[1] for j in mo]
                obj_f = nash.nash(m, o)
                yield((i, obj_f.nash))