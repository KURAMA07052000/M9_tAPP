class WalletEntity:
    def __init__(self, user_id: str, wallet_id: str, balance: int):
        self.user_id = user_id
        self.wallet_id = wallet_id
        self.balance = balance
        