#yahoo�t�@�C�i���X����A�ʖ����̏����擾����֐�
import pandas_datareader.data as web
import datetime
tsd=web.DataReader("AAPL","yahoo","2014/1/2","2017/8/17")
print(tsd.head(1))
print(tsd.tail(1))
