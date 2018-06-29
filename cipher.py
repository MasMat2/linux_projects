def get_mode():
    while True:
        print("\nDo you want to encrypt or decrypt or brute force? (e,d,b):")
        mode = input()
        if mode.lower().startswith(("e", "d", "b")):
            return mode[0]

def get_message():
    mes = input("\nEnter your message:\n")
    return mes

def get_key():
    while True:
        print("Give me your key:")
        key = int(input())
        if key in range(95):
            return key

def translate_message(mode, message, key):
    translated = ""

    if mode == "d":
        key = -key

    for sign in message:
        num = ord(sign) + key

        if num > 126:
            num -= 95
        elif num < 32:
            num += 95

        translated += chr(num)

    return translated

mode = get_mode()
message = get_message()
if mode != "b":
    key = get_key()

print()
print("This is your message:\n")

if mode == "b":
    for key in range(95):
        print(key, translate_message("d", message, key))

else:
    print(translate_message(mode, message, key))
