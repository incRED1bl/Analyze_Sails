from analyze.scripts import *



if __name__ == "__main__":
    observe = observe('dataset.csv', TARGET_COLUMNS)
    observe.create
    observe.filter('SEX', 'Male')
    observe.filter('AGE', 25, 30)
    observe.filter('QUANTITY', 10, 50)
    observe.filter('PRICE', 100, 2000)
    observe.filter('TOTAL', 50, 10000)
    observe.filter('TYPE', ['Laptop'])
    print(observe.df)
