def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# Program starts here
if __name__ == "__main__":
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g., 3): "))

    encrypted = encrypt(message, shift)
    print("Encrypted:", encrypted)

    decrypted = decrypt(encrypted, shift)
    print("Decrypted:", decrypted)
