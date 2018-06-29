
def reverse(encoding):
    revEncoding = {value: key for key, value in encoding.items()}
    return revEncoding

def encode(sequence):
    #Create an empty string for the encoding of the sequence
    encoded_string = ''

    #For each letter, append its encoding to the encoded string
    for letter in range(len(sequence)):
        encoded_string += encoding[sequence[letter]]
    return encoded_string

def decode(encoding):
    decoded = ''
    index = 0
    while index + 1 < len(encoding):
        if index + 2 <= len(encoding):
            if encoding[index: index + 2] in revEncoding:
                print('if 2', index)
                decoded += revEncoding[encoding[index: index +2]]
                index += 2
        if index + 1 <= len(encoding):
            if encoding[index: index + 1] in revEncoding:
                print('if 1', index)
                decoded += revEncoding[encoding[index: index +1]]
                index += 1
    return decoded

def combinations(seq):
    if len(seq) % 2 == 1:
        pairs = int((len(seq)/2) + 0.5)
    else:
        pairs = int((len(seq)/2))



encoding = {'C' : '1', 'G' : '0', 'A' : '00', 'T': '01'}
revEncoding = reverse(encoding)

print(revEncoding)
seq = encode('gataca'.upper())
print(seq)
print(decode(seq))
