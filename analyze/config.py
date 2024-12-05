import numpy as np
import pandas as pd
from enum import StrEnum, IntEnum
from collections import defaultdict

class info(StrEnum):
    ID = 'Customer ID'
    AGE = 'Age'
    SEX = 'Gender'
    TYPE = 'Product Type'
    PRICE = 'Unit Price'
    TOTAL = 'Total Price'
    QUANTITY = 'Quantity'

class ind(IntEnum):
    ID = 0
    AGE = 1
    SEX = 2
    TYPE = 3
    PRICE = 4
    TOTAL = 5
    QUANTITY = 6



TARGET_COLUMNS = [
    "Customer ID",
    "Age",
    "Gender",
    "Product Type",
    'Unit Price',
    'Total Price',
    "Quantity",
]
