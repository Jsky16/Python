class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    def Display(self):
        print(self.eno,'\t',self.ename,'\t',self.esal,'\t',self.eaddr)