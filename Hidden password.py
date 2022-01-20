"""
This programm in Python get password value and hidding first
and last characters / Python version 3
"""

def hidding_password(password):
    
    stars = "*" * (len(password)-2)
    result = password[0] + stars + password[-1]
    return result

print(hidding_password(input("Enter password:--")))
