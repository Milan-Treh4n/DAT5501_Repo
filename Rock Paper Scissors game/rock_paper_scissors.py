import base64
import tempfile
from PIL import Image

rock_win_b64 = """/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMTEhUSEhIVFRUXFxcXFxcYFxcVGBcXFRcXFxcXFRcYHSggGBolGxcXITEhJSkrLi4uFx8zODMtNygtLisBCgoKDg0OGBAQGi0dICUtLS8tKy03Ly0tKy0uLS0tLS0tLS0tKy0tLS8tLS0tKy0rNistLSstKy0rKy0tLy0tK//AABEIAMABBgMBIgACEQEDEQH/xAAbAAACAwEBAQAAAAAAAAAAAAABAgADBQQGB//EAEEQAAEDAgIFCAkCBQMFAQAAAAEAAhEDIQQxBRJBUWEGIlNxkZKh0hMWMoGxwdHh8BRC"""
paper_win_b64 = """/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxAPDw8NDw8NDw8PDQ4PDw4NDw8NDw4OFREWFxURFRYYHSggGBolHRUVLTIhJykrLi4uFx8zODMsNygtLisBCgoKDg0NFQ8PFSsZFRkrKysrKysrKy0rKy0rKzArKysrLS03Kys3LTcrKy0rKy0tLTIrKysrNzc3LS0rKystLf/AABEIALcBEwMBIgACEQEDEQH/xAAbAAACAwEBAQAAAAAAAAAAAAAAAQ"""
scissors_win_b64 = """/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBw8PDw8QDxAPDw8NDw0QDxAPDw8PEA8PFREWFhURFRUYHSggGBolGxUVITEhJSkrLi4uFx8zODMtNygtLisBCgoKDg0OFxAQFy8lIB8tLSstLS0tLSsrKy0tLS0tLS0tNSstLS8uLS0tLS0rLSstLy0rLS0tLS0vLS0rLS0tK//AABEIALcBEwMBEQACEQEDEQH/xAAbAAEBAAMBAQEAAAAAAAAAAAABAAIEBgUDB//EAEcQAAIBAgIGBgQJCgUFAAAAAAABAgMRBAUGEiExUXEiQWGBkaETMnKxI0JSU2KSssHRFBYkM3OCk6Kz4TRDg9LwFVRjwsP/xAAaAQEBAQEBAQEAAAAAAAAAAAAAAQIDBQQG/8QAMREBAAIBAgMECAcBAQAAAAAAAAECAwQRBSExEkFRkRMyUnGBobHRFBUiQmHB4fBD/9oADAMBAAIRAxEAPwD9VUCjJRAyUS7IyURsHVAySIMki7BQ2GVgFIBQCBARBFEBECBAAHDaZ/4+i/8Aw0/6lQkulejpcufQXIrDbAGQQEwCwAwICIMQIDFoAaKMANhRNDJIIysApANibhsAhSkVGRBDcQCBAQEBAIEFAEBw2mv+Nofsaf8AUqEluvR0mWPoLkVhuEAwICAAC4EyAQEAMAYGLKMbAbVjQySCFIikIQIKQEBAgIIQIBAgIKgICAAOG01f6bR7KNP+pMzLdejosqfQXJFZlvMIAICALEFYACoAYAwgAxZQWA20jQUEJAgIFYKUAgQEEIEBAIEBAQVEEAAcBplO+OX0adFe+X3okulejpcol0VyKxL0QiYAQQEwCwVWAABgAAwBlRjcDcNBASIkAoBQUgQEEQUhEAgRBAQDYKrBABAfm2k1TWx1Z/JnTj9WEU/NEl2r0dTkz6MeQhzl6xUFiCAgIACgCAAIAAxZRBG2aCiSiAQFAQUgQCESAgEggICAQECAxA+darGEZTm1GME3KT2JRW9lH5XiK/pK06nzlSU+WtJu3mc5d9tna5M+ijTnL2UVlEAAhQBjJ22vYlvb2Jd5JmI5yREzO0NCvnWGhvqxfsXn9m58d+IaanW8fDn9H24+Ham/Sk/Hl9Xw/OPCfLl/Dn+Bz/NdL7Xyl1/KNV7MecPpTzzCy3Vor21KHvR0pxDTW6Xj48vq534bqq9aT8Np+jfhNSV4tST3OLUl4o+ytotG8TvD4rVms7WjaSVGLKADcNISSiAQJAICBBSERAgQEA2ArAIEASklvCvKxOeUoNxjGU5L2Yx73/Yz2moxy4zSDPZ4l6qdqUXsjHdKXF8ewu7cViHkUt65mWnc5N6qNQ5S9uO4MoCChgeTnGeQoXjG06vC/Rj7T49h5ut4lTB+mvO3h4e/7PS0XDb5/wBVuVfnPu+7j8Zj6lZ"""
computer_win_b64 = """PASTE COMPUTER BASE64 HERE"""


def show_image(filename):
    try:
        img_path = os.path.join(os.path.dirname(__file__), filename)
        img = Image.open(img_path)

        # Display image in a Python window (works on any computer)
        plt.imshow(img)
        plt.axis('off')
        plt.show()
    except Exception:
        pass  # Silent fail if image missing

rounds_played = 0

while True:  # Keep playing until user confirms exit
    user_choice = input("Enter your choice (rock, paper, scissors, exit): ").lower().strip()

    if user_choice == 'exit':
        confirm = input("Are you sure you want to exit? (yes/no): ").lower().strip()
        if confirm == 'yes':
            print("Ok see you next time.")
            break
        else:
            print("Great! Let's play again.")
            continue

    # Validate input
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose rock, paper, or scissors, or exit the game")
        continue

    # Valid round
    rounds_played += 1

    # Computer plays
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"Computer chose: {computer_choice}")

    # Determine winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
        show_image("rock_win.png")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
        show_image("paper_win.png")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
        show_image("scissors_win.png")
    else:
        print("Computer wins!")
        show_image("computer_win.png")

    print("Let's play again.")






    
