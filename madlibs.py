
player1 = input("What's your name, player1 /n")
player2 = input("What's your name, player1 /n")

user1 = input("Pick between 'Rock','paper' or 'scissors ' " + player1)

user2 = input("Pick between 'Rock','paper' or 'scissors ' " + player2)

def compare(a,b):
    if a == b:
        print("It's a tie")


    elif a == "rock" and b == "paper":
        print(player2  + " wins!")
    elif a == "rock" and b == " scissors":
        print(player1  + "wins!")
    elif a == "paper" and b == " rock":
        print(player1  + "wins!")
    elif a == "paper" and b == " scissors":
        print(player2  + "wins!")
    elif a == "scissors" and b == " rock":
        print(player2  + "wins!")
    elif a == "scissors" and b == " paper":
        print(player1  + "wins!")
    else:
        print("Invalid input")


print(compare(user1,user2))