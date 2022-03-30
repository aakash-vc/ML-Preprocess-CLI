import sys
import pandas as pd

class Utils:
    def fileInput(self):
        try:
            file = sys.argv[1]
        except IndexError:
            raise SystemExit("Invalid dataset")

        try:
            data = pd.read_csv(file)
        except pd.errors.EmptyDataError:
            raise SystemExit("Provided dataset is empty")
        except FileNotFoundError:
            raise SystemExit("File not found")

        return data

    def choiceSelect(self, tasks):
        for task in tasks:
            print(task)

        while True:
            try:
                choice = int(input('\nEnter task code: '))
                break
            except ValueError:
                print('\nEnter valid code')

        return choice

    def showData(self, data):
        length = int(input('\n\nNumber of columns to display: '))
        while True:
            try:
                print('\n\n',data.head(length))
                break
            except ValueError:
                print('\nInvalid length')
            except Exception as e:
                print(f'Error: {e}')

    def showColumns(self, data):
        while True:
            try:
                print('\nColumns:')
                for column in data.columns.values:
                    print(column, end=' ')
                break
            except Exception as e:
                print(f'Error: {e}')

    def removeTargetColumn(self, data):
        Utils().showColumns(data)

        while True:
            column = input('\n\nTarget Column (-1 to exit): ')
            if column == '-1':
                break
            confirm = input('Confirm Removal: (y/n): ')

            if confirm == 'y' or confirm == 'Y':
                try:
                    data.drop([column], axis=1, inplace=True)
                except KeyError:
                    print(f'\nNo column with name {column}. Try again')
                    continue

                print('\nColumn removed')
                break

            else:
                print('\nTry again with new column name')
        
        return data

if __name__ == '__main__':
    pass