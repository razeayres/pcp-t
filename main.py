# code by Rodrigo Miranda (rodrigo.qmiranda@gmail.com)

import swat, handler
from os import path
from handlers import pcp1_pcp
from shutil import copyfile

class setup(object):
    def __init__(self):
        self.project = r"C:\Projetos_SUPer.SwatCup\brigida.Sufi2.SwatCup"
        self.pcp_file = path.join(self.project, "pcp1.pcp")
        self.pcp_backup = path.join(self.project, "pcp1.pcp.bak")
        self.pcp_backup0 = path.join(self.project, "pcp1.pcp.bak0")
        self.output_rch = path.join(self.project, "output.rch")
        self.observed_rch = path.join(self.project, "SUFI2.IN", "observed_rch.txt")

        if not path.exists(self.pcp_backup0):
            print "Creating one-time security backup...",
            copyfile(self.pcp_file, self.pcp_backup0)
            print "OK"
            print "Please check if file is updated!"

        self.indexes = None
        self.nashes = []
        self.best = []

    def make_a_copy(self):
        if path.exists(self.pcp_backup):
            print "Copying from regular backup...",
            copyfile(self.pcp_backup, self.pcp_file)
            print "OK"
        else:
            print "Creating regular backup...",
            copyfile(self.pcp_file, self.pcp_backup)
            print "OK"

    def modify_pcp1_pcp(self, t):
        pcp = pcp1_pcp.txt(self.pcp_file)
        if len(t) != 0:
            pcp.del_cols(t)
        pcp.write_file()
        print "Running with: ", pcp.stations
        if len(t) == 0:
            self.indexes = [i for i in range(1, len(pcp.stations)+1)]

    def simulate(self, t=[]):
        # makes a copy of pcp1.pcp
        # and modifies the original
        self.make_a_copy()
        self.modify_pcp1_pcp(t)

        # runs the SWAT model
        run_swat = swat.project(self.project)
        run_swat.run()
        run_swat.clear()

        # calculates the nash values
        h = handler.handle(self.output_rch, self.observed_rch)
        r = [float(i[1]) for i in h.nash]
        self.nashes.append((t, sum(r)/len(r)))
        print "Nashes until now:", self.nashes

    def select_the_best(self, flush=True):
        self.nashes.sort(key = lambda t: t[1])
        best = self.nashes[-1]
        if flush == True:
            self.nashes = []
        return(best)

    def new_generation(self):
        # iterates through the stations
        # removing one at a time
        print "Making new generation..."
        print "Current indexes: ", self.indexes
        for i in self.indexes:
            self.simulate(self.best + [i])

    def run(self):
        # first run of SWAT without modifications
        self.simulate([])
        b0 = self.select_the_best(flush=False)

        [self.indexes.remove(i) for i in [1,]]
        [self.best.append(i) for i in [1,]]

        # creates new generations and keep
        # going on until the best combination
        # is found
        while True:
            self.new_generation()
            b = self.select_the_best()
            if b[1] > b0[1]:
                print "Selecting the best...", b[0][-1]
                self.indexes.remove(b[0][-1])
                self.best.append(b[0][-1])
                b0 = b
            else:
                break
        print self.best
        print self.indexes

obj = setup()
# obj.simulate([1, 2, 4, 12, 25, 29, 33, 34, 35, 37, 38])
# obj.simulate([4])
obj.run() 