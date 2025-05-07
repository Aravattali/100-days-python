This is a simple Python script that generates a random password using letters, symbols, and numbers. The user decides how many of each character type to include.

How It Works
The program welcomes the user.

It asks for three inputs:

Number of letters

Number of symbols

Number of numbers

It then randomly selects characters based on the user’s input using random.choice().

All characters are added to a list, shuffled with random.shuffle(), and joined to create the final password.

