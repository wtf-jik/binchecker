import requests, json, sys, csv, numpy, time

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
#TODO: Make this work.
def eraseToEndOfLine():
	sys.stdout.write("\033[K")
	return 0
def generateRequest():
	print("Test")
	return 0
def output():
	print("test")
	return 0

response200String = "<Response [200]>"
binLength = 6
binCol

reader = csv.reader(open(sys.argv[1], 'r'))
csvout = csv.writer(open(sys.argv[2], 'w'))

binlist = list()
data = list()
output = list(reader)

for row in output[1:]:
	if row[binCol][:binLength] not in binlist:
		binlist.append(row[binCol][:binLength])
		#TODO: Change to output
		print('Compiling list of unique BINs... %d found' % len(binlist), end='\r')

#TODO: Change to output
print(str(len(binlist)) + " BIN numbers found...")
eraseToEndOfLine()

i = 0
while (i < len(binlist)):
	#TODO: Change to output
	print('Processing BIN #' + str(i+1) + ' of ' + str(len(binlist)), end='\r')
	eraseToEndOfLine()
	time.sleep(1.0)
	response = requests.get("https://lookup.binlist.net/" + str(binlist[i]))
	if (str(response) == response200String):
		i += 1
	else:
		#TODO: Change to output
		print("BIN: "+str(binlist[i])+". Fuckin' 404s man...")
	json_flat = flattenjson(json.loads(response.text), " ")
	if (i == 0): csvout.writerow(json_flat.keys())
	csvout.writerow(json_flat.values())


#TODO: Change to output
print("Complete\n")
	