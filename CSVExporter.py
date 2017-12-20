import csv
import datetime
import os.path
import subprocess


def export_to_file(CoinPairStr, MarketHistoryJson):
	filename = create_file_name(CoinPairStr)

	#if recording file already exists
	if (os.path.isfile(filename)):
		# Find new market history (we already have old stuff from last call)
		Id = find_last_Id(filename)

		IdIndexInMarketHistoryJson = find_Id_in_Json(Id, MarketHistoryJson)
		
		# If this last Id does not exist in MarketHistoryJson, take all 
		if (IdIndexInMarketHistoryJson == -1):
			MarketHistoryJson = MarketHistoryJson
		else:
			MarketHistoryJson = MarketHistoryJson[0:IdIndexInMarketHistoryJson]

	# Message to User
	if len(MarketHistoryJson):
		print("Updated file {0}".format(CoinPairStr))
	else:
		print("fetched")

	# Write new data to CSV
	write_to_csv(filename, MarketHistoryJson)


def write_to_csv(filename, MarketHistoryJson):
	 with open(filename, 'a') as csvfile:
	    writerCSV = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_NONE)

	    #Printtofile in reverse (so most recent at end of file)
	    for i in range(len(MarketHistoryJson)-1, -1, -1):
	    	event = MarketHistoryJson[i]
	    	writerCSV.writerow([event['Id'], 
	    						event['TimeStamp'], 
	    						event['OrderType'],str(
	    						event['Price']),str(
	    						event['Quantity'])])



def find_last_Id(filename):
	raw_last_line = tail(filename, 1)
	Id = str(raw_last_line,"utf-8").split(",")[0]
	return Id


def find_Id_in_Json(Id, MarketHistoryJson):
	Id = int(Id)

	for event in MarketHistoryJson:
	    if event['Id'] == Id:
	    	return MarketHistoryJson.index(event)
	# If Id not found in Json, return -1
	return -1;


def create_file_name(CoinPairStr):
	dayOfTheMonth = datetime.date.today().strftime("%d")
	month = datetime.date.today().strftime("%B")

	filename = "Recordings/"+CoinPairStr+"_"+month+"_"+dayOfTheMonth+".csv"
	return filename



def tail(f, n):
  cmd = "tail -n "+str(n)+" "+str(f);
  p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, close_fds=True)
  stdin, stdout = (p.stdin, p.stdout)

  stdin.close()
  lines = stdout.readlines(); stdout.close()
  return lines[-n]
