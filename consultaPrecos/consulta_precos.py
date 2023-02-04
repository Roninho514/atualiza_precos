from IPython.display import display
import pandas as pd

class Main:
    def __init__(self):
        #self.ler_arquivo()
        df = pd.read_excel('produtos.xlsx', usecols = [0], skiprows= 1 )
        display(df)

    def ler_arquivo():
        df = pd.read_excel('produtos.xlsx')
        display(df)

if __name__ == '__main__':
	try:
		Main()
	except KeyboardInterrupt:
		pass