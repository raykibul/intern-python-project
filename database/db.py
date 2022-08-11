import sqlite3


class DB():

    @staticmethod
    def execute(query,method=None):
        conn = sqlite3.connect('database.sqlite3')
        cursor = conn.cursor()
        res = {}
        try:
            cursor.execute(query)
            conn.commit()
            res['status'] = 'ok'
            if method=='one':
                res['data'] = cursor.fetchone()
                res['body'] = ''
            elif method =='all':
                res['data'] = cursor.fetchall()
                res['body'] = ''
            else:
                res['body'] ='executed'
                res['data'] = 'Query Executed'

            return res
        except Exception as e:
            res['status'] = 'Exception'
            res['body'] = f'{e}'
            return res
        finally:
            conn.close()


    @staticmethod
    def create(instance):
        print(type(instance).__name__)
        for attribute, value in instance.__dict__.items():
            print(attribute, '=', value)


class DBModel:
    def save(self):
        class_name = type(self).__name__
        if class_name == 'DB':
            return
        attributes = []
        values = []
        for attribute, value in self.__dict__.items():
            attributes.append(attribute)
            values.append(value)
        table_name = class_name + '_table'
        sql = f"INSERT OR REPLACE INTO {table_name}({str(attributes)[1:-1]}) values ({str(values)[1:-1]})"
        res = DB.execute(sql)

        # just checking if table not exist exception (can be improved):(
        if "no such table:" in res['body'] and res['status'] == 'Exception':
            self.__create_object_table()
            res = DB.execute(sql)

    def get_one(self,id):
        table_name = type(self).__name__+ '_table'
        sql_to_load_one = f"SELECT * from {table_name}  where id={id} ;"
        res = DB.execute(sql_to_load_one,'one')
        if res['status'] == 'Exception':
            return None
        else:
            return res['data']

    def __create_object_table(self):
        types = []
        class_name = type(self).__name__
        table_name = class_name + '_table'
        table_attr_query = f"CREATE TABLE IF NOT EXISTS {table_name} ( id integer PRIMARY KEY"
        for attribute, value in self.__dict__.items():
            vartype = type(value)
            if attribute=='id':
                continue
            if isinstance(value,str):
                table_attr_query = table_attr_query + f",{attribute} text NOT NULL"
            elif isinstance(value,int):
                table_attr_query = table_attr_query + f",{attribute} integer NOT NULL"
            elif isinstance(value,float):
                table_attr_query = table_attr_query + f",{attribute} real NOT NULL"

        res = DB.execute(table_attr_query+");")



