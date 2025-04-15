from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Booking API'
    app_description: str = 'Restaurant table booking service'

    # Настройки PostgreSQL
    postgres_user: str = 'admin'
    postgres_password: str = 'secret'
    postgres_db: str = 'table_reservations'
    postgres_host: str = 'db'
    postgres_port: int = 5432

    database_url: str

    class Config:
        env_file = '.env'


settings = Settings()  # type: ignore
