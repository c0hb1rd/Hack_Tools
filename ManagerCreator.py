import pymysql


DB = ''
DB_HOST = '127.0.0.1'
DB_USER = 'root'
DB_PASSWORD = ''
DB_CHARSET = 'utf8'


SHOW_TABLES = 'SHOW TABLES'
SHOW_TABLE_TMP = 'Tables_in_%s' % DB

import_tmp = '''from Core.BaseManager import BaseManager\nfrom Core.BaseObj import BaseObj\n\n'''
MANAGER_TMP = '''class M_%(table)s(BaseManager):
    def __init__(self, obj=T_%(table)s):
        super().__init__(obj)

%(table)sManager = M_%(table)s()
'''
TABLE_TMP = '''class T_%(table)s(BaseObj):
    def __init__(self):
        super().__init__()
'''
METHOD_TMP = '''    @staticmethod
    def table():
        return '%(table)s'

    @staticmethod
    def searchKeys():
        return [
        %(searchKeys)s
    ]

    @staticmethod
    def updateKeys():
        return [
        %(updateKeys)s
    ]

    @staticmethod
    def insertKeys():
        return [
        %(insertKeys)s
    ]
'''




class DBResult:
    Suc = False
    Result = None
    Err = None
    Rows = None

    def __init__(self):
        pass


class BaseDB:
    def __init__(self):
        self.dbConn = None
        self.cursor = None

    # Return DBResult
    def select(self, sql, params=None):
        with pymysql.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB, charset=DB_CHARSET,
                             cursorclass=pymysql.cursors.DictCursor) as cursor:

            r = DBResult()
            try:
                if params is None or len(params) == 0 or type(params) != dict:
                    r.Rows = cursor.execute(sql)
                else:
                    r.Rows = cursor.execute(sql, params)
                r.Result = cursor.fetchall() if r.Rows != 0 else []
                for i in range(0, len(r.Result)):
                    for k, v in r.Result[i].items():
                        r.Result[i][k] = str(v)
                r.Suc = True
            except Exception as e:
                r.Err = e

        return r

    # Return DBResult
    def callProc(self, func, params=None):
        with pymysql.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB, charset=DB_CHARSET,
                             cursorclass=pymysql.cursors.DictCursor) as cursor:
            r = DBResult()
            try:
                if params:
                    cursor.callproc(func, params)
                else:
                    cursor.callproc(func)
                r.Result = cursor.fetchall()
                r.Suc = True
            except Exception as e:
                r.Err = e

        return r

    # Return DBResult
    def execute(self, sql, params=None):
        self.dbConn = pymysql.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB,
                                      charset=DB_CHARSET,
                                      cursorclass=pymysql.cursors.DictCursor)
        with pymysql.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB, charset=DB_CHARSET,
                             cursorclass=pymysql.cursors.DictCursor) as cursor:

            r = DBResult()
            try:
                if not params:
                    r.Rows = cursor.execute(sql)
                else:
                    r.Rows = cursor.execute(sql, params)
                r.Result = cursor.fetchall() if r.Rows != 0 else []
                r.Suc = True
                self.dbConn.commit()
            except Exception as e:
                r.Err = e
                print(e, 'execute Error')
                self.dbConn.rollback()

        try:
            self.dbConn.close()
        except:
            pass
        return r

    # Return DBResult
    def insert(self, sql, params=None):
        r = self.execute(sql, params)
        return r

    def getLastID(self):
        r = self.execute("SELECT LAST_INSERT_ID()")
        r.Result = r.Result[0]['LAST_INSERT_ID()']
        return r

    # Return DBResult
    def getValue(self, sql, params=None):
        r = self.select(sql, params)

        if r.Suc:
            if r.Result:
                r.Result = r.Result[0]
            else:
                r.Result = -1
        return r


class Creator:
    def __init__(self):
        self.dbConn = BaseDB()

    def getTables(self):
        table_ret = self.dbConn.select(SHOW_TABLES)
        for line in table_ret.Result:
            yield line[SHOW_TABLE_TMP]

    def getColumns(self, table):
        sql = '''SHOW COLUMNS  FROM %s''' % table
        for line in self.dbConn.select(sql).Result:
            yield line['Field']


creator = Creator()
tables = creator.getTables()
for table in tables:
    class_tmp = TABLE_TMP % {'table': table}
    cols = ''
    columns = creator.getColumns(table)
    key_tmp = []
    for column in columns:
        cols += "        self.%s = None\n" % column
        key_tmp.append("'" + column + "'")
    method_tmp = '''    @staticmethod
    def table():
        return '%(table)s'

    @staticmethod
    def searchKeys():
        return [
            %(searchKeys)s
    ]

    @staticmethod
    def updateKeys():
        return [
            %(updateKeys)s
    ]

    @staticmethod
    def insertKeys():
        return [
            %(insertKeys)s
    ]
''' % {
        'searchKeys': ", ".join(key_tmp),
        'updateKeys': ", ".join(key_tmp),
        'insertKeys': ", ".join(key_tmp),
        'table': table
    }
    obj_tmp = import_tmp + '\n' + class_tmp + '\n' + cols + '\n' + method_tmp + '\n\n' + MANAGER_TMP % {'table': table}
    with open('%sManager.py' % table, 'w') as f:
        f.write(obj_tmp)


