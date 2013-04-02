from skein import skein1024
import os, string, random

def simple_diff(a,b):
    return sum ( a[i] != b[i] for i in range(len(a)) )

def to_binary(hexdecimal_string):
	binary_string = ""
	for char in hexdecimal_string:
		binary_string += bin(int(char, 16))[2:].zfill(4)
	return binary_string

goal = "5b4da95f5fa08280fc9879df44f418c8f9f12ba424b7757de02bbdfbae0d4c4fdf9317c80cc5fe04c6429073466cf29706b8c25999ddd2f6540d4475cc977b87f4757be023f19b8f4035d7722886b78869826de916a79cf9c94cc79cd4347d24b567aa3e2390a573a373a48a5e676640c79cc70197e1c5e7f902fb53ca1858b6"
count = 0

while True:
	hash = skein1024(digest_bits=1024)   # Create new Skein hash

	# Random Bytes
	# data_guess = os.urandom(1024)        # 1024 bytes
	# hash.update(data_guess)

	# Random Ascii/Digit String
	data_guess = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(random.randint(512, 1536)))
	encoded_guess = data_guess.encode('latin-1')
	hash.update(encoded_guess)

	digest = hash.hexdigest()

	bit_diff_count = simple_diff(to_binary(goal), to_binary(digest))

	if bit_diff_count <= 401:
		print(bit_diff_count)
		print(data_guess)
		print("Yay!!")

	if (count % 500000 == 0):
		print("Running...")

	count += 1












