class databaseManager:
    def __init__(self,con):
        self.con = con

    def Begin(self):
        connect = self.con.getURL()
        print('databaseManager基础链接',connect)
