import sqlite3
from pathlib import Path

__DB_FILE = Path() / "data" / "nodice" / "nodice.db"

# 当前角色卡
def set_current_character(user_id: int, group_id: int, current_character: str) -> bool:
    if __insert_db(
        "group_info",
        {
            "user_id": user_id,
            "group_id": group_id,
            "current_character": current_character,
        },
    ):
        return True
    else:
        return __update_db(
            "group_info",
            {"current_character": current_character},
            {"user_id": user_id, "group_id": group_id},
        )


def get_current_character(user_id: int, group_id: int) -> str:
    current_character = __select_db(
        "group_info", ("current_character",), {"user_id": user_id, "group_id": group_id}
    )
    if current_character:
        return current_character[0]
    else:
        set_current_character(user_id, group_id, "default")
        return "default"


# 默认骰
def set_default_dice(group_id: int, default_dice: int) -> bool:
    if __insert_db("group_info", {"group_id": group_id, "default_dice": default_dice}):
        return True
    else:
        return __update_db(
            "group_info", {"default_dice": default_dice}, {"group_id": group_id}
        )


def get_default_dice(group_id: int) -> int:
    default_dice = __select_db("group_info", ("default_dice",), {"group_id": group_id})
    if default_dice:
        return default_dice[0]
    else:
        set_default_dice(group_id, 100)
        return 100


# 昵称
def set_nickname(user_id: int, nickname: str) -> bool:
    if __insert_db("user_info", {"user_id": user_id, "nickname": nickname}):
        return True
    else:
        return __update_db("user_info", {"nickname": nickname}, {"user_id": user_id})


def get_nickname(user_id: int, username: str) -> str:
    nickname = __select_db("user_info", ("nickname",), {"user_id": user_id})
    if nickname:
        return nickname[0]
    else:
        return username


# 角色卡属性
def set_attribute(user_id: int, name: str, attribute: dict) -> bool:
    if __insert_db(
        "character_info",
        {"user_id": user_id, "name": name, "attribute": str(attribute)},
    ):
        return True
    else:
        return __update_db(
            "character_info",
            {"attribute": str(attribute)},
            {"user_id": user_id, "name": name},
        )


def get_attribute(user_id: int, name: str):
    attribute = __select_db(
        "character_info", ("attribute",), {"user_id": user_id, "name": name}
    )
    if attribute:
        return eval(attribute[0])
    else:
        return {}


def py2sql(value) -> str:
    if isinstance(value, str):
        result = f'"{value}"'
    else:
        result = str(value)
    return result


def __create_db():
    conn = sqlite3.connect(__DB_FILE)
    cur = conn.cursor()
    # 用户数据
    # 权限默认 0，黑名单为 -1，骰主为 5，群管在自己群内为 1
    cur.execute(
        """CREATE TABLE IF NOT EXISTS user_info (
                user_id INTEGER PRIMARY KEY NOT NULL,
                nickname TEXT,
                jrrp_value INTEGER,
                jrrp_date TEXT,
                current_character TEXT DEFAULT \"default\"
            )"""
    )
    # 角色卡
    cur.execute(
        """CREATE TABLE IF NOT EXISTS character_info (
                user_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                attribute TEXT NOT NULL,
                PRIMARY KEY (user_id,name,attribute)
            )"""
    )
    # 群数据
    cur.execute(
        """CREATE TABLE IF NOT EXISTS group_info (
                group_id INTEGER PRIMARY KEY NOT NULL,
                help_on INTEGER DEFAULT 1,
                jrrp_on INTEGER DEFAULT 1,
                default_dice INTEGER NOT NULL DEFAULT 100,
                success_rule INTEGER NOT NULL DEFAULT 0 CHECK (success_rule >= 0 AND success_rule <= 5)
            )"""
    )
    # 群用户
    cur.execute(
        """CREATE TABLE IF NOT EXISTS group_user_info (
                user_id INTEGER NOT NULL,
                group_id INTEGER NOT NULL,
                nickname TEXT,
                current_character TEXT DEFAULT \"default\",
                PRIMARY KEY(user_id, group_id)
            )"""
    )
    conn.commit()
    conn.close()


def __update_db(table_name: str, columns: dict, condition: dict) -> bool:
    __create_db()
    try:
        conn = sqlite3.connect(__DB_FILE)
        cur = conn.cursor()
        sql = f"UPDATE {table_name} SET "
        for i, key in enumerate(columns.keys()):
            if i:
                sql += ","
            sql += f"{key} = {py2sql(columns[key])}"
        sql += " WHERE "
        for i, key in enumerate(condition.keys()):
            if i:
                sql += " AND "
            sql += f"{key} = {py2sql(condition[key])}"
        cur.execute(sql)
        conn.commit()
        conn.close()
        return True
    except:
        return False


def __insert_db(table_name: str, columns: dict) -> bool:
    __create_db()
    try:
        conn = sqlite3.connect(__DB_FILE)
        cur = conn.cursor()
        sql = f"INSERT INTO {table_name} ("
        for i, key in enumerate(columns.keys()):
            if i:
                sql += ","
            sql += key
        sql += ") VALUES ("
        for i, key in enumerate(columns.keys()):
            if i:
                sql += ","
            sql += py2sql(columns[key])
        sql += ")"
        cur.execute(sql)
        conn.commit()
        conn.close()
        return True
    except:
        return False


def __select_db(table_name: str, columns: tuple, condition: dict):
    __create_db()
    try:
        conn = sqlite3.connect(__DB_FILE)
        cur = conn.cursor()
        sql = "SELECT "
        for i, value in enumerate(columns):
            if i:
                sql += ","
            sql += value
        sql += f" FROM {table_name} WHERE "
        for i, key in enumerate(condition.keys()):
            if i:
                sql += " AND "
            sql += f"{key} = {py2sql(condition[key])}"
        cur.execute(sql)
        return cur.fetchall()[0]
        conn.close()
    except:
        return False


def __delete_db(table_name: str, condition: dict):
    __create_db()
    try:
        conn = sqlite3.connect(__DB_FILE)
        cur = conn.cursor()
        sql = f"DELETE FROM {table_name} WHERE "
        for i, key in enumerate(condition.keys()):
            if i:
                sql += " AND "
            sql += f"{key} = {py2sql(condition[key])}"
        cur.execute(sql)
        conn.commit()
        conn.close()
        return True
    except:
        return False
