# code by Rodrigo Miranda (rodrigo.qmiranda@gmail.com)

from numpy import array, mean

class nash(object):
    def __init__(self, m, o):
        self.nash = self.calculate(m, o)
    
    def calculate(self, m, o):
        m = array(m)
        o = array(o)

        n = sum((m - o)**2)
        d = sum((o - mean(o))**2)
        r = 1 - (n/d)
        return(r)