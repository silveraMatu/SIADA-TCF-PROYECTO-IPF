class Settings:
    def __init__(
        self, DATABASE_URI:str) -> None:
        self.DATABASE_URI = DATABASE_URI
        pass
    
settings = Settings("postgresql+asyncpg://admin:adminpassword@localhost:5432/siada_db")
print(settings.DATABASE_URI)
