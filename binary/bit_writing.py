# Define a string of bits
bits = '10110011'

# Convert the bits to a byte
byte = int(bits, 2).to_bytes(1, byteorder='big')

# Write the byte to a file
with open('binary.bin', 'wb') as f:
    f.write(byte)