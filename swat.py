# code by Rodrigo Miranda (rodrigo.qmiranda@gmail.com)

import os, subprocess
from shutil import copyfile

class project(object):
    def __init__(self, p):
        self.project = os.path.join(p)  # , "Scenarios", "Default", "TxtInOut")
        self.swatexe = r"C:\SWAT\ArcSWAT\SWAT_64rel.exe"
        self.cmd = os.path.join(self.project,"swat_pcp-t.exe")	# SUFI2_Run.bat
        copyfile(self.swatexe, self.cmd)

    def run(self):
        try:
            p = subprocess.Popen(self.cmd,cwd=os.path.dirname(self.cmd),creationflags=subprocess.CREATE_NEW_CONSOLE)
            p.wait()
            return(0)
        except:
            return(1)

    def clear(self):
        os.remove(self.cmd)