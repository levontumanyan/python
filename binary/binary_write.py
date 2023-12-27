
with open('binary_file', 'wb') as bf:
	bf.write(b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09x0A\x0B\x0C\x0D\x0E\x0F')

with open('binary_file', 'wb') as bf:
	bf.write(b'\x1\x0\x1\x0\x1')

with open('binary_file', 'r') as f:
	text_data = f.read()

print()