import requests, json, sys, csv, numpy, time

response200String = "<Response [200]>"
response404String = "<Response [404]>"
response429String = "<Response [429]>"
start_row = 1
bin_len = 6
bin_col = 6
waitTime = 0.1

def flattenjson(b, delim):
	val = {}
	for i in b.keys():
		if isinstance( b[i], dict ):
			get = flattenjson( b[i], delim )
			for j in get.keys():
				val[ i + delim + j ] = get[j]
		else:
			val[i] = b[i]

	return val
def generateRequest(bin):
	request = "https://lookup.binlist.net/" + str(bin)
	return request
def sendRequest(req):
	r = requests.get(req)
	return r
def checkResponse(r, bin):
	if (str(r) == response200String):
		return 0, r
	elif (str(r) == response429String):
		time.sleep(waitTime)
		req = generateRequest(bin)
		r = sendRequest(req)
		ret_val, r = checkResponse(r, bin)
		if not ret_val:
			return 0, r
	elif (str(r) == response404String):
		print("BIN: " + bin + ". Fuckin' 404s man...")
		generateAlternateRequest(bin)
	else:
		return 7, r
def storeResponse(r):
	#TODO: Implement
	return 0
def generateBinList(csv_reader, start_row):
	csv_data = list(reader)
	binlist = list()
	for row in csv_data[start_row:]:
		if row[bin_col][:bin_len] not in binlist:
			binlist.append(row[bin_col][:bin_len])
			print('Compiling list of unique BINs... %d found' % len(binlist), end='\r')
	print(str(len(binlist)) + " BIN numbers found..." + "\033[K")
	return binlist
def main(binlist):
	i = 0
	while (i < len(binlist)):
		print('Processing BIN #' + str(i+1) + ' of ' + str(len(binlist)))#, end='\r')
		request = generateRequest(binlist[i])
		response = sendRequest(request)
		ret_val, response = checkResponse(response, str(binlist[i]))
		if not (ret_val):
			json_flat = flattenjson(json.loads(response.text), " ")
			if (i == 0):
				csvout.writerow(json_flat.keys())
			csvout.writerow(json_flat.values())
			storeResponse(response)
			i += 1

reader = csv.reader(open(sys.argv[1], 'r'))
csvout = csv.writer(open(sys.argv[2], 'w'))

binlist = generateBinList(reader, start_row)
main(binlist)

print("\nComplete\n")
	