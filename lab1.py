req = int(input())

dict = {
    301: {"key": 2569, "access": True},
    302: {"key": 3260, "access": False},
    303: {"key": 6925, "access": False},
    304: {"key": 7468, "access": True},
    305: {"key": 8795, "access": True},
    None: {"key": None, "access": False},
}

resp = dict.get(req)
if not resp:
    resp = dict[None]
print(resp.get("key"), resp.get("access"))
