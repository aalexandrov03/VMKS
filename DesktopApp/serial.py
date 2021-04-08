import subprocess

class SerialDriver:
    def __init__(self, prog):
        self.exec = prog

    def out(self, list):
        out_list = [self.exec, ]
        for el in list:
            out_list.append(el)
        
        res = subprocess.run(out_list)
        stat = res.check_returncode()
        if stat != None:
            return -1
        
        return 0
