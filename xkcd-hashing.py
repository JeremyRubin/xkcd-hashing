#!/usr/bin/env python3
import multiprocessing, signal, time, skein, random, string, urllib.request, urllib.parse

TARGET = '5b4da95f5fa08280fc9879df44f418c8f9f12ba424b7757de02bbdfbae0d4c4fd' + \
	'f9317c80cc5fe04c6429073466cf29706b8c25999ddd2f6540d4475cc977b87f4757be' + \
	'023f19b8f4035d7722886b78869826de916a79cf9c94cc79cd4347d24b567aa3e2390' + \
	'a573a373a48a5e676640c79cc70197e1c5e7f902fb53ca1858b6'

TARGET = int(TARGET, 16)

RANDOM_BIT_LEN = 512

def init_worker():
	signal.signal(signal.SIGINT, signal.SIG_IGN)

def submit(word):
	url = "http://almamater.xkcd.com/?edu=mit.edu"
	data = urllib.parse.urlencode({'hashable': word})
	binarydata = data.encode('ascii')
	urllib.request.urlopen(url, binarydata)
	
def run_worker():
	best = float('inf')
	r = random.SystemRandom()
	while True:
		guess = hex(r.getrandbits(RANDOM_BIT_LEN))[2:]
		encoded = guess.encode('utf-8')
		digest = int(skein.skein1024(encoded).hexdigest(), 16)
		diff = bin(digest ^ TARGET).count('1')
		if diff < best:
			best = diff
			submit(guess)
			print('Found new best input with diff [%.3d]: \"%s\"' %
				(diff, guess))

def main():
	run_worker()
	cpus = multiprocessing.cpu_count()
	pool = multiprocessing.Pool(cpus, init_worker)
	for i in range(cpus):
		pool.apply_async(run_worker)
	try:
		while True:
			time.sleep(100)
	except KeyboardInterrupt:
		print('Terminating...')
		pool.terminate()
		pool.join()
	else:
		print('Quitting...')
		pool.close()
		pool.join()

if __name__ == '__main__':
	main()