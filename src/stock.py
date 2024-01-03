import yfinance as yf

def fetch_stock_data(ticker, period, interval):
    return yf.download(ticker, period = period, interval = interval)

def fetch_company_name(ticker):
    stock = yf.Ticker(ticker)
    company_name= stock.info['longName']
    return company_name