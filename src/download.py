import pandas as pd

class Download:
    def __init__(self, data):
        self.data = data

    def getFilename(self):
        name = input('Enter preferred file name (-1 to go back): ')
        if name == '-1':
            return

        return name

    def downloadData(self):
        filename = self.getFilename()
        if filename == None:
            print('File creation Failed.')
            return
        while True:
            try:
                self.data.to_csv(f'{filename}.csv', index=False)
                print('File Download Successful.')
                break
            except Exception as e:
                print('File Download Failed')
                print(f'Error: {e}')

        finish = input('\n\nExit (y/n): ')
        if finish == 'y' or finish == 'Y':
            exit()