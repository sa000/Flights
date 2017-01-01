
from bs4 import BeautifulSoup
import string
import math
import csv
from time import localtime, strftime
import time
import mechanize

url='https://www.southwest.com/flight/?clk=GNAV-FLIGHT'
br = mechanize.Browser()

filename='Southwestfare.csv'
target=open(filename,'wb')
headers=['From', 'To', 'Depart', 'Arrival', 'Lowest Price','Lowest Price so far','Time scanning']
csvwriter=csv.writer(target)
csvwriter.writerow(headers)

intervals=5 #search 5 timee
lowest_so_far=10000
for i in xrange(intervals):

	response=br.open(url)
	br.select_form('buildItineraryForm')
	br.set_all_readonly(False)#Dates were initially set as readonly
	br.set_handle_robots( False )

	br.form['originAirport']=['HOU']
	br.form['destinationAirport']=['PHL']
	br.form['outboundDateString']='01/02/2017'
	br.form['returnDateString']='01/07/2017'

	br.submit()
	soup = BeautifulSoup(br.response().read())
	fares=[int(str(fare_price.text).translate(string.maketrans("\n\t\r", "   ")).replace(' $','').replace(' ','')) for fare_price in  soup.select('div.product_info label.product_price ')]

	lowest_fare=min(fares)
	lowest_so_far=min(lowest_fare,lowest_so_far)
	cur_time=strftime("%Y-%m-%d %H:%M:%S", localtime())
	data=['HOU','PHL', '01/02/2017','01/07/2017',lowest_fare, lowest_so_far, cur_time]
	print data
	csvwriter.writerow(data)
	time.sleep(3)
target.close()
