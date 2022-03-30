from utils import Utils
import pandas as pd

class Category:
    tasks = [
        '1 Show Categorical Columns',
        '2 Perform One-Hot Encoding',
        '3 Show The Dataset',
        '-1 Go Back'
    ]

    def __init__(self, data):
        self.data = data

    def showCategoryColumns(self):
        print('\n{0: <20}'.format("Categorical Column") + "Unique Values")
        
        for column in self.data.select_dtypes(include="object"):
            print('{0: <20}'.format(column)+'{0: <5}'.format(self.data[column].nunique()))

    def oneHotEncode(self):
        self.showCategoryColumns()
        
        while True:
            column = input('\nEnter column to be encoded (-1 to go back): ')
            if column == '-1':
                break

            try:
                self.data = pd.get_dummies(self.data, columns=[column])
                print('Encoding Done.')
            except:
                print('Invalid column name. Try Again')
                continue

    def categoryEncode(self):
        while True:
            print('\n\nCategory Encoding Tasks:\n')
            choice = Utils().choiceSelect(self.tasks)

            if choice == -1:
                break

            elif choice == 1:
                self.showCategoryColumns()

            elif choice == 2:
                self.oneHotEncode()

            elif choice == 3:
                Utils().showData(self.data)

            else:
                print('\nInvalid Code')


if __name__ == '__main__':
    pass