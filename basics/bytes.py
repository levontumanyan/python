text = "hello"

print(text)

btext = b"hello"

print(btext)
print(type(btext))
print(len(btext))

emoji_text = "hello🤣".encode('utf-8')

print(list(emoji_text))

empty_bites = bytes(4)
print(empty_bites)
print(type(empty_bites))
