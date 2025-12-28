from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_driver: str
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_pass: str

    db_pool_size: int
    db_max_overflow: int
    db_pool_recycle: int
    db_pool_timeout: int

    debug: bool


settings = Settings()  # type: ignore
