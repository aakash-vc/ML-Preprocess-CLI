from utils import Utils

class DataDescription:

    tasks = [
        '1 Describe Specific Column',
        '2 Show Properties of Each Column',
        '3 Show The Dataset',
        '-1 Go Back'
    ]

    def __init__(self, data):
        self.data = data

    def describeColumn(self):
        print('\n\nColumns:')
        for column in self.data.columns.values:
            print(column, end=' ')

        while True:
            column = input('\n\nTarget Column (-1 to go back): ')
            if column == '-1':
                break
            
            try:
                print(self.data[column].describe())
            except:
                print('Invalid column name. Try again')


    def describeData(self):
        print('\n\n',self.data.describe(),'\n\n')
        print(self.data.info())

    def description(self):
        while True:
            print('\n\nData Description Tasks:\n')
            choice = Utils().choiceSelect(self.tasks)

            if choice == -1:
                break

            elif choice == 1:
                self.describeColumn()

            elif choice == 2:
                self.describeData()

            elif choice == 3:
                Utils().showData(self.data)

            else:
                print('\nInvalid code')

if __name__ == '__main__':
    pass