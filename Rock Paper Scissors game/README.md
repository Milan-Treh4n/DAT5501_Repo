# Rock Paper Scissors

This folder is a small, beginner-friendly Python project that plays a Rock–Paper–Scissors game in the terminal and shows an image for the result. Images are stored both as PNG files and as Base64 strings (in the `base64_for_images` subfolder) so the game can display them even if the PNGs are not loaded directly.

What’s included
- `rock_paper_scissors.py` — main game script (runs in the terminal, shows images on win/lose/tie).
- `image_test.py` — small helper to test image display and base64 decoding.
- `rock_win.png`, `paper_win.png`, `scissors_win.png`, `computer_win.png` — example PNG images.
- `base64_for_images/` — Python files containing Base64 strings and a `base64_variables.py` mapping used by the main script.

What the main script does
- Reads the player's input (rock, paper, scissors, exit).
- Chooses a random move for the computer.
- Prints the result and uses the Base64 mapping to display the appropriate image using Pillow (PIL).

Requirements
- Python 3.x
- Pillow (for image handling)
  - Install with: pip install pillow

How to run (macOS / terminal)
1. Open Terminal in the repository root.
2. (Optional) Create and activate a virtual environment:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install Pillow if needed:
   ```
   pip install pillow
   ```
4. Run the game:
   ```
   python "Rock Paper Scissors game/rock_paper_scissors.py"
   ```

Notes for beginners
- The script decodes Base64 strings and writes temporary PNG files so your OS image viewer can open them. Temporary files are left on disk (named by the OS temp mechanism) — you can delete them later if needed.
- If images do not open, check:
  - Pillow is installed.
  - The Base64 mapping `base64_for_images/base64_variables.py` contains the expected keys (e.g. `"rock_win_b64"`, `"paper_win_b64"`, `"scissors_win_b64"`, `"computer_win_b64"`).
  - Running the script from the repository root ensures relative imports work.

Troubleshooting
- ModuleNotFoundError for `base64_for_images`: run the script from the repository root or add the folder to PYTHONPATH.
- Image decode errors: the Base64 strings should not include a `data:` prefix; if they do, strip the prefix before decoding.

Suggested learning path
1. Open `rock_paper_scissors.py` and read the code (input handling, random choice, result logic).
2. Run `image_test.py` to check image decoding independently.
3. Inspect the files in `base64_for_images/` to see how images are represented as strings.

Extending the project
- Add score tracking and a score summary.
- Replace PNG images with your own and update the Base64 mapping.
- Add a GUI (Tkinter) to display images in a window instead of opening external viewers.

This README is intended to help you run and understand the small game by example. 