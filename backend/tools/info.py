class Info:

    def __init__(self, infostatus, infomsg, inforesult=None,infodebug=None):
        self.infostatus = infostatus
        self.infomsg = infomsg
        self.inforesult = inforesult
        self.infodebug = infodebug

    def tojson(self):
        return {'infostatus': self.infostatus,
                'infomsg': self.infomsg,
                'inforesult': self.inforesult,
                'infodebug': self.infodebug}
