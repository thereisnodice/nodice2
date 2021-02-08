# sqlite.py
# 数据库模块，负责与 sqlite3 交互

import sqlite3
import os

DB_FILE=os.path.join(os.path.dirname(__file__),'data','nodice.db')

# 默认骰
def set_defaultdice(group_id:int,default_dice:int)->bool:
    if(insert_db('group_info',{'id':group_id,'default_dice':default_dice})):
        return True
    else:
        return update_db('group_info',{'default_dice':default_dice},{'id':group_id})
def get_defaultdice(group_id:int)->int:
    default_dice=select_db('group_info',('default_dice',),{'id':group_id})
    if default_dice:
        return default_dice[0]
    else:
        set_defaultdice(group_id,100)
        return 100

# 昵称
def set_nickname(qq_id:int,nickname:str)->bool:
    if(insert_db('qq_info',{'id':qq_id,'nickname':nickname})):
        return True
    else:
        return update_db('qq_info',{'nickname':nickname},{'id':qq_id})
def get_nickname(qq_id:int,username:str)->str:
    nickname=select_db('qq_info',('nickname',),{'id':qq_id})
    if nickname:
        return nickname[0]
    else:   
        return username

# 角色卡属性
def set_property(owner:int,name:str,property:dict)->bool:
    if(insert_db('character_card',{'owner':owner,'name':name,'property':str(property)})):
        return True
    else:
        return update_db('character_card',{'property':str(property)},{'owner':owner,'name':name})
def get_property(owner:int,name:str):
    property=select_db('character_card',('property',),{'owner':owner,'name':name})
    if property:
        return eval(property[0])
    else:
        return {}

def py2sql(value)->str:
    if isinstance(value,str):
        result=f'"{value}"'
    else:
        result=str(value)
    return result

def create_db():
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

def update_db(table_name:str,columns:dict,condition:dict)->bool:
    create_db()
    try:
        conn=sqlite3.connect(DB_FILE)
        cur=conn.cursor()
        sql=f"UPDATE {table_name} SET "
        for i,key in enumerate(columns.keys()):
            if i:sql+=','
            sql+=f"{key} = {py2sql(columns[key])}"
        sql+=" WHERE "
        for i,key in enumerate(condition.keys()):
            if i:sql+=' AND '
            sql+=f"{key} = {py2sql(condition[key])}"
        cur.execute(sql)
        conn.commit()
        conn.close()
        return True
    except:
        return False

def insert_db(table_name:str,columns:dict)->bool:
    create_db()
    try:
        conn=sqlite3.connect(DB_FILE)
        cur=conn.cursor()
        sql=f"INSERT INTO {table_name} ("
        for i,key in enumerate(columns.keys()):
            if i:sql+=','
            sql+=key
        sql+=') VALUES ('
        for i,key in enumerate(columns.keys()):
            if i:sql+=','
            sql+=py2sql(columns[key])
        sql+=')'
        cur.execute(sql)
        conn.commit()
        conn.close()
        return True
    except:
        return False

def select_db(table_name:str,columns:tuple,condition:dict):
    create_db()
    try:
        conn=sqlite3.connect(DB_FILE)
        cur=conn.cursor()
        sql="SELECT "
        for i,value in enumerate(columns):
            if i:sql+=','
            sql+=value
        sql+=f' FROM {table_name} WHERE '
        for i,key in enumerate(condition.keys()):
            if i:sql+=' AND '
            sql+=f"{key} = {py2sql(condition[key])}"
        cur.execute(sql)
        return cur.fetchall()[0]
        conn.close()
    except:
        return False

def delete_db(table_name:str,condition:dict):
    create_db()
    try:
        conn=sqlite3.connect(DB_FILE)
        cur=conn.cursor()
        sql=f'DELETE FROM {table_name} WHERE '
        for i,key in enumerate(condition.keys()):
            if i:sql+=' AND '
            sql+=f"{key} = {py2sql(condition[key])}"
        cur.execute(sql)
        conn.commit()
        conn.close()
        return True
    except:
        return False

if __name__=='__main__':
    print(set_property(1290541225,'default',{'斗殴':80}))
    print(get_nickname(1290541225,'jigsaw'))
    print(get_property(1290541225,'default'))

