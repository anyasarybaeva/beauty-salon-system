import pandas as pd
from utils.utils import db
dbase=db()
sql=('SELECT Название,Цена FROM Услуга WHERE Статус=%s')
cursor = dbase.conn.cursor()

cursor.execute('SELECT ФИО FROM Сотрудник WHERE Код=%s',(56764,))
material_df=pd.read_sql('SELECT * FROM Материал', dbase.conn)
print(material_df[material_df.Название.str.startswith('лак')].values.tolist())
material_df.loc[material_df.Название=='лак','Количество']+=32
print(material_df[material_df.Название.str.startswith('лак')].values.tolist())
material_df.loc[material_df.Название=='лак','Количество']-=1
print(material_df[material_df.Название.str.startswith('лак')].values.tolist())

dbase.conn.close()
