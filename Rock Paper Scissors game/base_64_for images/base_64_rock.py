import base64

# Generate base64 string for rock_win.png
with open("rock_win.png", "rb") as f:
    b64_string = base64.b64encode(f.read()).decode('utf-8')

print(b64_string)  # This is the base64 text
