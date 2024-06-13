class Settings():    

    API_ID: int
    API_HASH: str

    FARM_MINING_ERA: bool = True
    TAPS: bool = True
    TAPS_AMOUNT: list[int] = [100, 1000]
    CLAIM_SQUAD_REWARD: bool = True
    CLAIM_TASKS: bool = True

    USE_PROXY_FROM_FILE: bool = False


settings = Settings()
