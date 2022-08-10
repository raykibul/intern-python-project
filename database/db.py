import  sqlite3

class DB():

    def __init__(self):
        con = sqlite3.connect('database.db')


    @staticmethod
    def props(cls):
        return [i for i in cls.__dict__.keys() if i[:1] != '_']


    @staticmethod
    def create(instance):
        print(type(instance).__name__)
        for attribute, value in instance.__dict__.items():
            print(attribute, '=', value)
    #
    # c.execute(
    #     "INSERT INTO admin_manager('app_name','setting_py','phone_no','service_json','app_domain','package_name','google_service','ftp_details') VALUES(:app_name,:setting_py,:phone_no,:service_json,:app_domain,:package_name,:google_service,:ftp_details)",
    #     {
    #         'app_name': app_name,
    #         'setting_py': setting,
    #         'phone_no': phone,
    #         'service_json': service,
    #         'app_domain': domain,
    #         'package_name': package,
    #         'google_service': google,
    #         'ftp_details': ftp,
    #     })



    def save(self):
        class_name = type(self).__name__
        if class_name=='DB':
            return
        attributes =[]
        values =[]

        for attribute, value in self.__dict__.items():
            attributes.append(attribute)
            values.append(value)

        table_name = class_name+'_table'
        sql = f"INSERT INTO {table_name}({str(attributes)[1:-1]}) values ({str(values)[1:-1]})"
        print(sql)


