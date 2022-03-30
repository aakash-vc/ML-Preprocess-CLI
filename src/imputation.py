from utils import Utils

class Imputation:
    tasks = [
        '1 Show Number of Null Values',
        '2 Remove Columns',
        '3 Fill Null Values (with mean)',
        '4 Fill Null Values (with median)',
        '5 Fill Null Values (with mode)',
        '6 Show Dataset',
        '-1 Go Back'
    ]

    def __init__(self, data):
        self.data = data

    def showNull(self):
        print('\n\n',self.data.isna().sum())

    def fillOption(self, option):
        Utils().showColumns(self.data)

        while True:
            column = input('\nEnter name of column to fill: ')
            if column == '-1':
                break
            confirm = input('Confirm Fill: (y/n): ')

            if confirm == 'y' or confirm == 'Y':
                try:
                    if option == 'mean':
                        self.data[column].fillna(self.data[column].mean(), inplace=True)
                    elif option == 'median':
                        self.data[column].fillna(self.data[column].median(), inplace=True)
                    elif option == 'mode':
                        self.data[column].fillna(self.data[column].mode()[0], inplace=True)
                    else:
                        break

                except KeyError:
                    print(f'\nInvalid Column Name. Try again')
                    continue

                print('\nColumn filled')
                break

            else:
                print('\nTry again with new column name')

    def fillMean(self):
        self.fillOption('mean')

    def fillMedian(self):
        self.fillOption('median')

    def fillMode(self):
        self.fillOption('mode')

    def impute(self):
        while True:
            print('\n\nImputation Tasks:\n')
            choice = Utils().choiceSelect(self.tasks)

            if choice == -1:
                break

            elif choice == 1:
                self.showNull()

            elif choice == 2:
                self.data = Utils().removeTargetColumn(self.data)

            elif choice == 3:
                self.fillMean()

            elif choice == 4:
                self.fillMedian()

            elif choice == 5:
                self.fillMode()

            elif choice == 6:
                Utils().showData(self.data)

            else:
                print('\nInvalid code')

        return self.data

if __name__ == '__main__':
    pass