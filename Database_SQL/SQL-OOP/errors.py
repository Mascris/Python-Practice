class CineVaultError(Exception):
    pass

class UserNotFoundError(CineVaultError):
    pass

class MovieNotFoundError(CineVaultError):
    pass

class MovieOutOfStockError(CineVaultError):
    pass

