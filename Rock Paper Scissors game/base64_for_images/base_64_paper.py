import base64

# Generate base64 string for paper_win.png
with open("paper_win.png", "rb") as f:
    b64_string = base64.b64encode(f.read()).decode('utf-8')

print(b64_string)  # This is the base64 text