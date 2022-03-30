from utils import Utils
from description import DataDescription
from imputation import Imputation
from category import Category
from featurescaling import FeatureScaling
from download import Download
    
class Preprocess:
    tasks = [   
        '1 Data Description',
        '2 Handling NULL Values',
        '3 Encoding Categorical Data',
        '4 Feature Scaling of the Dataset',
        '5 Download the modified dataset',
        '-1 Exit'
    ]

    def __init__(self):
        self.data = Utils().fileInput()
        print('\nMACHINE LEARNING PREPROCESSOR CLI')

    def preprocessor(self):
        self.data = Utils().removeTargetColumn(self.data)
        
        while True:
            print('\n\nTasks:')
            choice = Utils().choiceSelect(self.tasks)
            
            if choice == -1:
                break

            elif choice == 1:
                DataDescription(self.data).description()

            elif choice == 2:
                self.data = Imputation(self.data).impute()

            elif choice == 3:
                self.data = Category(self.data).categoryEncode()

            elif choice == 4:
                self.data = FeatureScaling(self.data).scalingOptions()

            elif choice == 5:
                Download(self.data).downloadData()

            else:
                print('\nInvalid code')

if __name__ == '__main__':
    obj = Preprocess()
    obj.preprocessor()