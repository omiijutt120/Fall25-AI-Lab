import random

n = 0
print(""""If the number is divisible by 3, instead of saying the number, the player should say, "Fizz". 
If the number is divisible by 5, instead of saying the number, the player should say, "Buzz". 
If the number is divisible by 3and5, instead of saying the number, the player should say, "Fizz Buzz".
If the number is not divisible by either 3 or 5, Just Press Enter""")

while True:
    no = random.randint(1, 15)
    n1 = n + no
    print(f"The number is : {no}")

    if n1 % 3 == 0 and n1 % 5 == 0:
        c = "Fizz Buzz"
    elif n1 % 3 == 0:
        c = "Fizz"
    elif n1 % 5 == 0:
        c = "Buzz"
    else:
        c = ""

    guess = input("Your Guess: ")

    if guess.lower() == c.lower():
        print("Correct Answer")
    else:
        print("Wrong Answer")
        break
    n = no
