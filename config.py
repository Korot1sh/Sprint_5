class Config:
    # Конфигурация проекта
    BASE_URL = "https://qa-desk.education-services.ru"
    TIMEOUT = 10
    IMPLICIT_WAIT = 5
    BROWSER = "chrome"

    # Настройки Chrome
    CHROME_OPTIONS = [
        "--start-maximized",
        "--disable-blink-features=AutomationControlled",
        "--disable-extensions"
    ]