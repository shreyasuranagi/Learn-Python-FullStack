class HeadOffice:
    hname='penta'
    ceo='mr.ravi'
    hloc='btm'

    courses=['ds','ai']

    @classmethod
    def display(cls):
        print(cls.hname,cls.hloc,cls.ceo)

    @staticmethod
    def announce(*companies):
        print('Upcoming requirement schedulings:')
        for c in companies:
            print(c)

class BranchOffice(HeadOffice):
    bname = 'penta V'
    bloc='vijaynagar'

    def __init__(self,*courses):
        super().__init__()
        self.courses=courses
        

    def display_head(self):
        super().display()

    def display_branch(self):
        print(self.bname, self.bloc)

b=BranchOffice('PFS','JFS')
b2=BranchOffice('Testing','Automation')

print(b.bname)
print(b.ceo)
print(b.announce("abc","caltech","cognizent"))
print(HeadOffice.announce("abc","caltech","cognizent"))
print(b.courses)