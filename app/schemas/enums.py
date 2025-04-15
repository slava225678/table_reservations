from enum import Enum


class TableName(str, Enum):
    TABLE_1 = "Столик №1"
    TABLE_2 = "Столик №2"
    TABLE_3 = "Столик №3"
    VIP_TABLE = "VIP столик"


class TableLocation(str, Enum):
    WINDOW = "У окна"
    BALCONY = "На балконе"
    MAIN_HALL = "Главный зал"
