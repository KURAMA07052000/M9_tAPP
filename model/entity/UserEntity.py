class UserEntity:
    def __init__(self, user_id: str, wallet_id: str, name: str, email: str, phone_num: str, password: str, user_kind: str):
        self.user_id = user_id
        self.wallet_id = wallet_id
        self.name = name
        self.email = email
        self.phone_num = phone_num
        self.password = password
        self.user_kind = user_kind