"""
Star pyramid Print a centred pyramid of a given height. Hint: each row needs
height - row spaces and 2*row - 1 stars.
"""
def start_pyramid(height):
  for i in range(height,0,-1):
    spaces = " "*(height - i)
    stars = "*"*(2 * i - 1)
    print(spaces + stars)
start_pyramid(4)
