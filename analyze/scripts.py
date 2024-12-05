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
        elif pos_arg == 'Price':
            min_arg, max_arg = kwargs
            df = self.df[self.df[info.PRICE].between(min_arg, max_arg)]
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

    # @property
    # def group_by(self):
    #     self.df = self.df.groupby(info.SEX).sum()
    @property
    def add_column(self):
        d = {}
        for _, row in self.df.iterrows():
            if row[info.ID] in d:
                d[row[info.ID]] += row[info.TOTAL]
            else:
                d[row[info.ID]] = row[info.TOTAL]
        self.df['all_purchases'] = self.df[info.ID].map(d)



    @classmethod
    def client(cls, filters):
        ob = cls('dataset.csv', TARGET_COLUMNS)
        ob.create
        for filter_type, *args in filters:
            ob.filter(filter_type, *args)
        ob.add_column
        return ob.df
