from json import dumps as json_dumps



class MakeRequest:
    def login(email: str = None, username: str = None, password: str = None) -> bytes:
        if (not email and not username) or not password:
            raise ValueError()

        out = {"action": "login"}
        
        if email:
            out["email"] = email
        
        elif username:
            out["username"] = username

        out["password"] = password

        return json_dumps(out).encode()
