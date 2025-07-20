# SCT_CYB_03 – Password Strength Checker

## Description

This project is part of the SkillCraft Technology Internship, Task 03.  
It is a command-line based Python tool that evaluates how strong a password is based on five key factors:
- Minimum length
- Uppercase characters
- Lowercase characters
- Numbers
- Special symbols

---

## Features

- Simple command-line interface.
- Real-time password strength evaluation.
- Detects weak, medium, and strong passwords.
- Uses regular expressions for pattern checking.

---

## How to Run

### Step 1: Open Terminal
Navigate to the folder:

```bash
cd ~/SkillCraft_Tasks/SCT_CYB_03
```

### Step 2: Run the Script

```bash
python3 password_strength_checker.py
```

---

## How It Works

### Criteria:
| Rule                        | Points |
|-----------------------------|--------|
| At least 8 characters       | 1      |
| Contains uppercase letter   | 1      |
| Contains lowercase letter   | 1      |
| Contains digits             | 1      |
| Contains special characters | 1      |

### Score:
- **0–2 points** → Weak   
- **3–4 points** → Medium  
- **5 points** → Strong 

---

## Example Input/Output

### Example 1:
```
Enter your password: abc123
Password strength: Weak
```

### Example 2:
```
Enter your password: Hello2024!
Password strength: Strong
```

---

## File Structure

```
SCT_CYB_03/
├── password_strength_checker.py
└── README.md
```

---

## Tags

`#SkillCraft #Python #PasswordChecker #CyberSecurity #Internship #Regex #CLI`

