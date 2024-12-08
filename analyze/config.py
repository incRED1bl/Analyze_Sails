import numpy as np
import pandas as pd
from enum import StrEnum, IntEnum


class info(StrEnum):
    ID = 'Customer ID'
    AGE = 'Age'
    SEX = 'Gender'
    TYPE = 'Product Type'
    PAYMENT_METHOD = 'Payment Method'
    PRICE = 'Unit Price'
    QUANTITY = 'Quantity'
    TOTAL = 'Combined Purchases'
    MONEY = 'Collection'

class ind(IntEnum):
    ID = 0
    AGE = 1
    SEX = 2
    TYPE = 3
    PAYMENT_METHOD = 4
    PRICE = 5
    QUANTITY = 6
    TOTAL = 8
    MONEY = 7



TARGET_COLUMNS = [
    "Customer ID",
    "Age",
    "Gender",
    "Product Type",
    "Payment Method",
    'Unit Price',
    "Quantity"

]
