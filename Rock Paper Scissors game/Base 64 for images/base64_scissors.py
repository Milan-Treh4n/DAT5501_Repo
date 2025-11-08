import base64

# Replace "rock_win.png" with the file you want
with open("scissors_win.png", "rb") as f:
    b64_string = base64.b64encode(f.read()).decode('utf-8')

print(b64_string)  # This is the base64 text