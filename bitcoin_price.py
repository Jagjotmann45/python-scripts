from requests import get
from bs4 import BeautifulSoup
from time import sleep
from win10toast import ToastNotifier

while 1:
	url = 'https://in.finance.yahoo.com/quote/BTC-INR/'
	page = get(url)
	html = page.content
	soup = BeautifulSoup(html,'html.parser')
	price = soup.find_all("span", {'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})[0].text

	t = ToastNotifier()
	t.show_toast('Bitcoin', 'Bitcoin is at Rs. '+price[:-3], icon_path='C:\\Users\\sgurv\\Pictures\\Saved Pictures\\bitcoin.ico',duration=20)
	sleep(1800)