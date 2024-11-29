import numpy as np
import pandas as pd
from enum import IntEnum


class info(IntEnum):
    ID = 0
    AGE = 1
    SEX = 2
    TYPE = 3
    TOTAL = 4
    PRICE = 5
    QUANTITY = 6


TARGET_COLUMNS = [
    "Customer ID",
    "Age",
    "Gender",
    "Product Type",
    'Total Price',
    "Unit Price",
    "Quantity",
]
