class Settings:
    def __init__(
        self, DATABASE_URL:str) -> None:
        self.DATABASE_URL = DATABASE_URL
        pass
    
settings = Settings("postgresql+asyncpg://admin:adminpassword@localhost:5432/siada_db")
print(settings.DATABASE_URL)
