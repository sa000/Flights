
from bs4 import BeautifulSoup
import string
import math
import cookielib





filename='AA.csv'
target.open(filename,'wb')
headers=['From', 'To', 'Depart', 'Arrival', 'Lowest Price','Lowest Price so far','Time scanning']
intervals=30#30 seconds
br = mechanize.Browser()

url='https://www.aa.com/'

response=br.open(url)
br.select_form('reservationFlightSearchForm')
br.set_all_readonly(False)#Dates were initially set as readonly
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_handle_redirect(True)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
br.form['originAirport']='HOU'
br.form['destinationAirport']='PHL'
br.form['departDate']='01/02/2017'
br.form['returnDate']='01/07/2017'
br.submit()
soup = BeautifulSoup(br.response().read())
print soup
fares=[str(fare_price.text).translate(string.maketrans("\n\t\r", "   ")).replace(' $','').replace(' ','') for fare_price in  soup.select('div.product_info label.product_price ')]

