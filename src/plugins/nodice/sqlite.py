import sqlite3
import os

DB_FILE=os.path.join(os.path.dirname(__file__),'data','nodice.db')

def create_db()->bool:
    conn=sqlite3.connect(DB_FILE)
    cur=conn.cursor()
    # 用户数据
    # 权限默认 0，黑名单为 -1，骰主为 5，群管在自己群内为 1
    cur.execute('''CREATE TABLE IF NOT EXISTS qq_info (
                id INTEGER PRIMARY KEY NOT NULL,
                nickname TEXT,
                permission INTEGER DEFAULT 0,
                jrrp_value INTEGER,
                jrrp_date TEXT,
                card_chosen TEXT DEFAULT \"default\")''')
    # 角色卡
    cur.execute('''CREATE TABLE IF NOT EXISTS character_card (
                owner INTEGER NOT NULL,
                name TEXT NOT NULL,
                property TEXT NOT NULL,
                PRIMARY KEY (owner,name,property))''')
    # 群数据
    cur.execute('''CREATE TABLE IF NOT EXISTS group_info (
                id INTEGER PRIMARY KEY NOT NULL,
                bot_on INTEGER DEFAULT 1,
                help_on INTEGER DEFAULT 1,
                jrrp_on INTEGER DEFAULT 1,
                permission INTEGER DEFAULT 0,
                default_dice INTEGER NOT NULL DEFAULT 100,
                success_rule INTEGER NOT NULL DEFAULT 0 CHECK (success_rule >= 0 AND success_rule <= 5))''')
    # 群用户
    cur.execute('''CREATE TABLE IF NOT EXISTS group_user_info (
                qq_id INTEGER NOT NULL,
                group_id INTEGER NOT NULL,
                nick_name TEXT,
                card_chosen TEXT DEFAULT \"default\",
                PRIMARY KEY(qq_id, group_id))''')
    conn.commit()
    conn.close()
    return True

def update_db(table_name:str,columns:dict,condition:dict)->bool:
    try:
        conn=sqlite3.connect(DB_FILE)
        cur=conn.cursor()
        sql=f"UPDATE {table_name} SET "
        for i in columns.keys():
            if i:sql+=','
            sql+=f"{i} = {columns[i]}"
        sql+=" WHERE "
        for i in condition.keys():
            if i:sql+=','
            sql+=f"{i} = {condition[i]}"
        cur.execute(sql)
        conn.commit()
        conn.close()
        return True
    except:
        return False

def insert_db(table_name:str,columns:dict)->bool:
    try:
        conn=sqlite3.connect(DB_FILE)
        cur=conn.cursor()
        sql=f"INSERT INTO {table_name} ("
        for i in columns.keys():
            if i != list(columns.keys())[0]:sql+=','
            sql+=str(i)
        sql+=') VALUES ('
        for i in columns.keys():
            if i != list(columns.keys())[0]:sql+=','
            if isinstance(columns[i],str):
                sql+=f'"{columns[i]}"'
            elif isinstance(columns[i],int):
                sql+=str(columns[i])
        sql+=')'
        cur.execute(sql)
        conn.commit()
        conn.close()
        return True
    except:
        return False

def select_db():
    pass


if __name__=='__main__':
    create_db()
    print(insert_db('qq_info',{'id':1290541225,'nickname':'jigsaw'}))
    


