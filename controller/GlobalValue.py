import model.entity as entity
class GlobalValue:
    def __init__(self):
        self.userEntity = None
        self.walletEntity = None
        self.orderEntity = None

    def setUserEntity(self, userEntity: entity.UserEntity):
        self.userEntity = userEntity

    def setWalletEntity(self, walletEntity: entity.WalletEntity):
        self.walletEntity = walletEntity

    def setOrderEntity(self, orderEntity: entity.OrderEntity):
        self.orderEntity = orderEntity
