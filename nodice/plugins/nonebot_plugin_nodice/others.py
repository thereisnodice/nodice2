import httpx


def get_jrrp(bot_qq_id: int, qq_id: int, is_online: bool = True):
    if is_online:
        return get_jrrp_online(bot_qq_id, qq_id)
    else:
        return get_jrrp_local(qq_id)


def get_jrrp_local(qq_id: int):
    pass


def get_jrrp_online(bot_qq_id, qq_id):
    url = "http://api.kokona.tech:5555/jrrp"
    data = {"User-Agent": "NoDice", "QQ": bot_qq_id, "v": "20190114", "QueryQQ": qq_id}
    res = httpx.post(url=url, data=data)
    return res.text


def get_rules(bot_qq_id: int, name: str, is_online: bool = True):
    if is_online:
        return get_rules_online(bot_qq_id, name)
    else:
        return get_rules_local(name)


def get_rules_online(bot_qq_id: int, name: str):
    url = "http://api.kokona.tech:5555/rules"
    data = {"User-Agent": "NoDice", "QQ": bot_qq_id, "v": "20190114", "Name": name}
    res = httpx.post(url=url, data=data)
    return res.text


def get_rules_local(name: str):
    pass


if __name__ == "__main__":
    print(get_rules_online("123456789", "大成功"))
