from utils import Utils
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

class FeatureScaling:
    tasks = [
        '1 Perform Normalization (MinMax Scaler)',
        '2 Perform Standardization (Standard Scaler)',
        '3 Show The Dataset',
        '-1 Go Back'
    ]

    normalize_tasks = [
        '1 Normalize Specific Column',
        '2 Normalize Whole Dataset',
        '3 Show The Dataset',
        '-1 Go Back'
    ]

    standardize_tasks = [
        '1 Standardize Specific Column',
        '2 Standardize Whole Dataset',
        '3 Show The Dataset',
        '-1 Go Back'
    ]

    def __init__(self, data):
        self.data = data

    def columnOperate(self, operation):
        print(self.data.dtypes)
        while True:
            column = input(f'\nEnter column to {operation} (-1 to go back): ')
            if column == '-1':
                break
            try:
                if operation == 'normalize':
                    minVal = self.data[column].min()
                    maxVal = self.data[column].max()
                    self.data[column] = (self.data[column] - minVal)/(maxVal - minVal)
                    print('Operation Done.')

                elif operation == 'standardize':
                    mean = self.data[column].mean()
                    standard_deviation = self.data[column].std()
                    self.data[column] = (self.data[column] - mean)/(standard_deviation)
                    print('Operation Done.')
            
            except:
                print('Operation Not Possible')


    def datasetOperate(self, operation):
        try:
            if operation == 'normalize':
                self.data = pd.DataFrame(MinMaxScaler().fit_transform(self.data), columns=self.data.columns)
                print('Operation Done.')

            elif operation == 'standardize':
                self.data = pd.DataFrame(StandardScaler().fit_transform(self.data), columns=self.data.columns)
                print('Operation Done.')
            
        except:
            print('Operation Not Possible')

    def normalize(self):
        while True:
            print('\n\nNormalization Tasks:\n')
            choice = Utils().choiceSelect(self.normalize_tasks)

            if choice == -1:
                break

            elif choice == 1:
                self.columnOperate('normalize')

            elif choice == 2:
                self.datasetOperate('normalize')

            elif choice == 3:
                Utils().showData(self.data)

            else:
                print('\nInvalid Code')

    def standardize(self):
        while True:
            print('\n\nStandardization Tasks:\n')
            choice = Utils().choiceSelect(self.standardize_tasks)

            if choice == -1:
                break

            elif choice == 1:
                self.columnOperate('standardize')

            elif choice == 2:
                self.datasetOperate('standardize')

            elif choice == 3:
                Utils().showData(self.data)

            else:
                print('\nInvalid Code')

    def scalingOptions(self):
        while True:
            print('\n\nFeature Scaling Tasks:\n')
            choice = Utils().choiceSelect(self.tasks)

            if choice == -1:
                break

            elif choice == 1:
                self.normalize()

            elif choice == 2:
                self.standardize()

            elif choice == 3:
                Utils().showData(self.data)

            else:
                print('\nInvalid Code')
        
