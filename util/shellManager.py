class shellManager:

    def __init__(self,con):
        self.con = con

    def Begin(self):
        connect = self.con.getURL()
        print('基础链接：',connect)
    '''
    typ = None
    URL = None
    @classmethod
    def Begin(cls):
        if cls.typ == 'php':
            print(cls.URL,cls.typ)
            return
        if cls.typ == 'jsp':
            #jsp_shell()
            return
        if cls.typ == 'asp':
            #aps_shell()
            return
    @classmethod
    def setTyp(cls,typ):
        cls.typ = typ
    @classmethod
    def setURL(cls,URL):
        cls.URL = URL
    '''

