import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename='data/2611996.csv'
with open(filename) as f:
	reader=csv.reader(f)
	header_row=next(reader)

	#Get dates and high and low temperatures from this file.
	highs,dates,lows=[],[],[]
	for row in reader:
		current_date=datetime.strptime(row[5],'%Y-%m-%d')
		try:
			high=int(row[10])
			low=int(row[12])
		except ValueError:
			print(f"Missing data for {current_date}")
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)
		
		
		

#Plot the high and low temperatures.
plt.style.use('seaborn')
fig,ax=plt.subplots()
ax.plot(dates,highs,c='red',alpha=0.5)
ax.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

#Format plot.
plt.title('Daily high and low temperatures for hyderabad, - 2021',fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()