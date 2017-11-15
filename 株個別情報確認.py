#yahooファイナンスから、個別銘柄の情報を取得する関数
import pandas_datareader.data as web
import datetime
tsd=web.DataReader("AAPL","yahoo","2014/1/2","2017/8/17")
print(tsd.head(1))
print(tsd.tail(1))
