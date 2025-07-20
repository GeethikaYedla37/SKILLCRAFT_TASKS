# SCT_CYB_01 – Caesar Cipher Encryption Tool

## Description

This project is part of the SkillCraft Technology Internship, Task 01.  
It is a command-line based Caesar Cipher encryption and decryption tool written in Python.

The Caesar Cipher is a simple substitution cipher where each letter in the plaintext is shifted a fixed number of places down or up the alphabet.

---

## Features

- Encrypt plaintext using a shift key.
- Decrypt ciphertext using the same shift key.
- Handles both uppercase and lowercase letters.
- Ignores non-alphabetic characters.
- Simple CLI (Command Line Interface) tool.

---

## How It Works

### Encryption Formula:
```
Encrypted Character = (Original Character + Shift Key) % 26
```

### Decryption Formula:
```
Decrypted Character = (Encrypted Character - Shift Key) % 26
```

---

## How to Run

### Step 1: Open Terminal
Navigate to the folder where `caesar_cipher.py` is saved:

```bash
cd ~/SkillCraft_Tasks/SCT_CYB_01
```

### Step 2: Run the Script

```bash
python3 caesar_cipher.py
```

You’ll be prompted to enter a message and shift key.

---

## Example Input/Output

### Example 1:
```
Enter your message: HELLO every One
Enter shift value (e.g., 3): 4
Encrypted: LIPPS izivc Sri
Decrypted: HELLO every One
```

### Example 2:
```
Enter your message: This is CyberSecurity Task
Enter shift value (e.g., 3): 5
Encrypted: Ymnx nx HdzjwXjhwzjyd Yfxp
Decrypted: This is CyberSecurity Task
```

## Tags

`#SkillCraft #CyberSecurity #Python #Cryptography #CaesarCipher #Internship`

