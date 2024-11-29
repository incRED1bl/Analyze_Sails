from analyze.config import *


class observe:
    def __init__(self, data, columns):
        self.data = data
        self.columns = columns
    @property
    def create(self):
        df = pd.DataFrame(pd.read_csv(self.data))
        df = df[df["Order Status"] != 'Cancelled']
        df =df[self.columns]
        self.df = df

    def filter(self, pos_arg, *kwargs):
        if pos_arg == 'AGE':
            min_arg, max_arg = kwargs
            df = self.df[self.df[TARGET_COLUMNS[info.AGE]].between(min_arg, max_arg)]
            self.df = df
        elif pos_arg == 'SEX':
            sex = kwargs[0]
            df = self.df[self.df[TARGET_COLUMNS[info.SEX]] == sex]
            self.df = df
        elif pos_arg == 'QUANTITY':
            min_arg, max_arg = kwargs
            df = self.df[self.df[TARGET_COLUMNS[info.QUANTITY]].between(min_arg, max_arg)]
            self.df = df
        elif pos_arg == 'PRICE':
            min_arg, max_arg = kwargs
            df = self.df[self.df[TARGET_COLUMNS[info.PRICE]].between(min_arg, max_arg)]
            self.df = df
        elif pos_arg == 'TOTAL':
            min_arg, max_arg = kwargs
            df = self.df[self.df[TARGET_COLUMNS[info.TOTAL]].between(min_arg, max_arg)]
            self.df = df
        elif pos_arg == 'TYPE':
            sp = kwargs[0]
            flag = False
            for el in sp:
                if el in ['Laptop', 'Smartphone', 'Headphones', 'Tablet', 'Smartwatch']:
                    df = self.df[self.df[TARGET_COLUMNS[info.TYPE]] == el]
                    flag = True
            if flag:
                self.df = df
            else:
                raise ValueError(f"Unknown product type: {sp}")
        else:
            raise ValueError(f"Unknown argument: {pos_arg}")
