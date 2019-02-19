class connect:
    _url = None
    _key = None
    _typ = None
    '''
    def __init__(self,url,key,typ):
        self._url = url
        self._key = key
        self._typ = typ
    '''
    @classmethod
    def getURL(cls):#get方法 生成url链接
        CONNECT_URL = cls._url + '?' + cls._key + '='
        return CONNECT_URL

    #   get
    @classmethod
    def getUrl(cls):#post方法直接返回基础链接 不需要添加额外路径与参数
        return cls._url
    @classmethod
    def getKey(cls):
        return cls._key
    @classmethod
    def getTyp(cls):
        return cls._typ

    #   set
    @classmethod
    def setUrl(cls,url):
        cls._url = url
    @classmethod
    def setKey(cls,key):
        cls._key = key
    @classmethod
    def setTyp(cls,typ):
        cls._typ = typ
