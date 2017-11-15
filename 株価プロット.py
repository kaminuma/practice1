%matplotlib inline
import pandas_datareader.data as web

aapl = web.DataReader('AAPL',"google","2001/12/31","2016/12/31")['Close']
aapl.plot() # Š”‰¿‚Ìƒvƒƒbƒg