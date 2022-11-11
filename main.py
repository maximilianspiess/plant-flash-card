import mysql.connector as sql


query = "select trivialname, pflanze.sysname from Trivialname join Pflanze on Trivialname.Pflanze_SysName=Pflanze.SysName"

try:
    connection = sql.connect(user="python", password = "pypass", host = "127.0.0.1", database = "toxicarium", auth_plugin='mysql_native_password')
    print("Connection successful!", connection)

    cursor = connection.cursor()

    cursor.execute(query)

    names = []
    for i in cursor:
        names.append(i[0:2])

    connection.close()

except sql.Error as err:
    print("Something went wrong:", err)


name_group = {}

for plant in names:
    name_group[plant[1]] = []

for plant in names:
    name_group[plant[1]] += [plant[0]]

for key in name_group.keys():
    print(key + ": " + ", ".join(name_group[key]))
