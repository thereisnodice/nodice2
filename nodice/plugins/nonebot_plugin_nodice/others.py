import httpx


async def get_jrrp(self_id: int, user_id: int, is_online: bool = True) -> str:
    if is_online:
        return await get_jrrp_online(self_id, user_id)
    else:
        return get_jrrp_local(user_id)


def get_jrrp_local(user_id: int) -> str:

    pass

async def get_jrrp_online(self_id: int, user_id: int) -> str:
    url = "http://api.kokona.tech:5555/jrrp"
    data = {"User-Agent": "NoDice", "QQ": self_id, "v": "20190114", "QueryQQ": user_id}
    async with httpx.AsyncClient() as client:
        res = await client.post(url=url, data=data)
    return res.text


async def get_rules(self_id: int, keyword: str, is_online: bool = True):
    if is_online:
        return await get_rules_online(self_id, keyword)
    else:
        return get_rules_local(keyword)


async def get_rules_online(self_id: int, keyword: str) -> str:
    url = "http://api.kokona.tech:5555/rules"
    data = {"User-Agent": "NoDice", "QQ": self_id, "v": "20190114", "Name": keyword}
    async with httpx.AsyncClient() as client:
        res = await client.post(url=url, data=data)
    return res.text


def get_rules_local(keyword: str) -> str:
    pass