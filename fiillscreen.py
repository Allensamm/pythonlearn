import shutil

def fill_screen_horizontally(name):
    try:
        columns, _ = shutil.get_terminal_size()
        print(name * (columns // len(name)))
    except Exception as e:
        print(f"Error: Unable to determine terminal size. {e}")

def fill_screen_vertically(name, rows):
    for _ in range(rows):
        print(name)

# Replace "Your Name" with your actual name
your_name = "allen"

# Fill the screen horizontally
fill_screen_horizontally(your_name)

# Fill the screen vertically (adjust the number of rows as needed)
fill_screen_vertically(your_name, 10)
