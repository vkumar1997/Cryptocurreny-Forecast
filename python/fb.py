import numpy as np 
import pandas as pd 
from pandas import DataFrame
from fbprophet import Prophet
import csv

fb=open('myfile.csv','wb')
writer = csv.writer(fb)
print("Hello")

crypto_data = {}

crypto_data['bitcoin'] = pd.read_csv('../csv/1bitcoin.csv', parse_dates=['Date'])
crypto_data['etherum'] = pd.read_csv('../csv/2etherum.csv', parse_dates=['Date'])
crypto_data['ripple'] = pd.read_csv('../csv/3ripple.csv', parse_dates=['Date'])
crypto_data['bitcoin-cash'] = pd.read_csv('../csv/4bitcoin-cash.csv', parse_dates=['Date'])
crypto_data['cardano'] = pd.read_csv('../csv/5cardano.csv', parse_dates=['Date'])
crypto_data['litecoin'] = pd.read_csv('../csv/6litecoin.csv', parse_dates=['Date'])
crypto_data['nem'] = pd.read_csv('../csv/7nem.csv', parse_dates=['Date'])
crypto_data['neo'] = pd.read_csv('../csv/8neo.csv', parse_dates=['Date'])
crypto_data['stellar'] = pd.read_csv('../csv/9stellar.csv', parse_dates=['Date'])
crypto_data['iota'] = pd.read_csv('../csv/10iota.csv', parse_dates=['Date'])
crypto_data['dash'] = pd.read_csv('../csv/11dash.csv', parse_dates=['Date'])
crypto_data['monero'] = pd.read_csv('../csv/12monero.csv', parse_dates=['Date'])
crypto_data['bitcoin-gold'] = pd.read_csv('../csv/13bitcoin-gold.csv', parse_dates=['Date'])
crypto_data['etherum-classic'] = pd.read_csv('../csv/14etherum-classic.csv', parse_dates=['Date'])
crypto_data['qtum'] = pd.read_csv('../csv/15qtum.csv', parse_dates=['Date'])
crypto_data['lisk'] = pd.read_csv('../csv/16lisk.csv', parse_dates=['Date'])
crypto_data['raiblocks'] = pd.read_csv('../csv/17raiblocks.csv', parse_dates=['Date'])
crypto_data['vechain'] = pd.read_csv('../csv/18vechain.csv', parse_dates=['Date'])
crypto_data['zcash'] = pd.read_csv('../csv/19zcash.csv', parse_dates=['Date'])
crypto_data['verge'] = pd.read_csv('../csv/20verge.csv', parse_dates=['Date'])
crypto_data['stratis'] = pd.read_csv('../csv/21stratis.csv', parse_dates=['Date'])
crypto_data['siacoin'] = pd.read_csv('../csv/22siacoin.csv', parse_dates=['Date'])
crypto_data['bytecoin'] = pd.read_csv('../csv/23bytecoin.csv', parse_dates=['Date'])
crypto_data['steem'] = pd.read_csv('../csv/24steem.csv', parse_dates=['Date'])
crypto_data['bitshares'] = pd.read_csv('../csv/25bitshares.csv', parse_dates=['Date'])
crypto_data['dogecoin'] = pd.read_csv('../csv/26dogecoin.csv', parse_dates=['Date'])
crypto_data['electroneum'] = pd.read_csv('../csv/27electroneum.csv', parse_dates=['Date'])
crypto_data['waves'] = pd.read_csv('../csv/28waves.csv', parse_dates=['Date'])
crypto_data['kucoin-shares'] = pd.read_csv('../csv/29kucoin-shares.csv', parse_dates=['Date'])
crypto_data['komodo'] = pd.read_csv('../csv/30komodo.csv', parse_dates=['Date'])
crypto_data['decred'] = pd.read_csv('../csv/31decred.csv', parse_dates=['Date'])
crypto_data['smartcash'] = pd.read_csv('../csv/32smartcash.csv', parse_dates=['Date'])
crypto_data['ark'] = pd.read_csv('../csv/33ark.csv', parse_dates=['Date'])
crypto_data['digibyte'] = pd.read_csv('../csv/34digibyte.csv', parse_dates=['Date'])
crypto_data['hshare'] = pd.read_csv('../csv/35hshare.csv', parse_dates=['Date'])
crypto_data['byteball-bytes'] = pd.read_csv('../csv/36byteball-bytes.csv', parse_dates=['Date'])
crypto_data['pivx'] = pd.read_csv('../csv/37pivx.csv', parse_dates=['Date'])
crypto_data['zclassic'] = pd.read_csv('../csv/38zclassic.csv', parse_dates=['Date'])
crypto_data['factom'] = pd.read_csv('../csv/39factom.csv', parse_dates=['Date'])
crypto_data['reddcoin'] = pd.read_csv('../csv/40reddcoin.csv', parse_dates=['Date'])

for coin in crypto_data:
    print(coin)
    panda_data = pd.DataFrame(crypto_data[coin])
    panda_data = panda_data[["Date","Close"]]
    current_value = panda_data.as_matrix()[0][1]    
    panda_data.columns = ["ds","y"]    
    m=Prophet()
    m.daily_seasonality=True 
    m.fit(panda_data)
    future = m.make_future_dataframe(periods = 100)
    forecast = m.predict(future)
    average,mini,maxi = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail().as_matrix()[4][1:4]
    plt=m.plot(forecast)
    plt.savefig('images/forecast/'+coin+'.png')
    increase = str((average-current_value)/float(current_value)*100)+'%'
    writer.writerow([coin,current_value,average,mini,maxi,increase])
    fb.flush()
fb.close()
