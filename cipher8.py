
mode = input('Do you want to encrypt or decrypt (e,d)? ').lower()
words = [' the ',' be ',' to ',' of ',' and ',' in ',' that ',' have ',' I ',' it ',' for ',' not ',' on ',' with ',' he ',' as ',' you ',' do ',' at ',' this ',' but ',' his ',' by ',' from ',' they ',' we ',' say ',' her ',' she ',' or ',' an ',' will ',' my ',' one ',' all ',' would ',' there ',' their ',' what ',' so ',' up ',' out ',' if ',' about ',' who ',' get ',' which ',' go ',' me ',' when ',' make ',' can ',' like ',' time ',' no ',' just ',' him ',' know ',' take ',' people ',' into ',' year ',' your ',' good ',' some ',' could ',' them ',' see ',' other ',' than ',' then ',' now ',' look ',' only ',' come ',' its ',' over ',' think ',' also ',' back ',' after ',' use ',' two ',' how ',' our ',' work ',' first ',' well ',' way ',' even ',' new ',' want ',' because ',' any ',' these ',' give ',' day ',' most ',' us ']
def encrypt():
    box = []
    row = []
    count = 1
    for letter in message:
        if len(row) < key:
            row.append(letter)
        elif len(row) == key:
            box.append(row)
            row = []
            row.append(letter)
        if count ==  len(message):
            spaces = key - len(row)
            for space in range(spaces):
                row.append(' ')
            box.append(row)
        count += 1


    fencryption = ''

    for letter in range(key):
        for row in box:
            fencryption += row[letter]

    return fencryption



def decrypt():
    deciphers = []
    for answer in range(2,len(code)):
        decryption = ''
        cipher = []
        row = []
        count = 1
        for letter in code:
            if len(row) < answer:
                row.append(letter)
            elif len(row) == answer:
                cipher.append(row)
                row = []
                row.append(letter)
            if count ==  len(code):
                spaces = answer - len(row)
                for space in range(spaces):
                    row.append(' ')
                cipher.append(row)

            count += 1


        for letter in range(answer):
            for row in cipher:
                decryption += row[letter]
        cipherkey = len(code)/answer

        matches = 0
        for word in words:
            if word in decryption:
                matches += 1
        if matches != 0:
            deciphers.append((decryption,matches))



    deciphers = sorted(deciphers, key=lambda matches: matches[1])[::-1]
    return deciphers





while True:
    if mode.startswith('e'):
        message = input('What\'s your message? ')

        key = input('Choose your key man ')
        while True:
            try:
                key = int(key)
                break
            except ValueError:
                key = input('Try to enter a number')



        fencryption = encrypt()
        print('\n'+ fencryption)
        break


    if mode.startswith('d'):
        code = input('Enter your code: ')
        decryptions = decrypt()
        for i in decryptions:
            print(i[0])
        break

    else:
        mode = input('I\'m sorry i didn\'t get it ("encrypt" or "decrypt")').lower()


# create a dictionary with the most common words webscrap https://en.wikipedia.org/wiki/Most_common_words_in_English
