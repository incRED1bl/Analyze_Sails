from analyze.config import *


class Observe:
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
            df = self.df[self.df[info.AGE].between(min_arg, max_arg)]
            self.df = df
        elif pos_arg == 'SEX':
            sex = kwargs[0]
            df = self.df[self.df[info.SEX] == sex]
            self.df = df
        elif pos_arg == 'QUANTITY':
            min_arg, max_arg = kwargs
            df = self.df[self.df[info.QUANTITY].between(min_arg, max_arg)]
            self.df = df
        elif pos_arg == 'TOTAL':
            min_arg, max_arg = kwargs
            df = self.df[self.df[info.TOTAL].between(min_arg, max_arg)]
            self.df = df
        elif pos_arg == 'TYPE':
            el = kwargs[0]
            print(el)
            if el in ['Laptop', 'Smartphone', 'Headphones', 'Tablet', 'Smartwatch']:
                df = self.df[self.df[info.TYPE] == el]
                self.df = df
            else:
                raise ValueError("Unknown product type")
        else:
            raise ValueError(f"Unknown argument: {pos_arg}")

    @property
    def add_column(self):
        d1 = {}
        self.df['Collection'] = np.nan
        for i, row in self.df.iterrows():
            total_purchase = row[info.PRICE] * row[info.QUANTITY]
            if row[info.ID] in d1:
                d1[row[info.ID]] += total_purchase
            else:
                d1[row[info.ID]] = total_purchase
            if row[info.PAYMENT_METHOD] == 'Cash':
                a = 'Cash'
            elif row[info.PAYMENT_METHOD] in ['Credit Card', 'Debit Card']:
                a = 'Card'
            else:
                a = 'Transaction'
            self.df.at[i, info.MONEY] = a
            if row[info.PAYMENT_METHOD] == 'Paypal':
                self.df.at[i, info.PAYMENT_METHOD] = 'PayPal'
        self.df['Combined Purchases'] = self.df[info.ID].map(d1)




    @classmethod
    def client(cls, filters):
        ob = cls('dataset.csv', TARGET_COLUMNS)
        ob.create
        ob.add_column
        for filter_type, *args in filters:
            ob.filter(filter_type, *args)
        return ob.df
