import random
def winner(p1, p2):
    rps = ['Rock', 'Paper', 'Scissors']
    if(p1 == rps[0]):
        if(p2 == rps[1]):
            print(f"Player 2 won with {p2} against {p1}")
        if(p2 == rps[2]):
            print(f"Player 1 won with {p1} against {p2}")
        if(p2 == rps[0]):
            print(f"It's a draw with {p1} against {p2}")

    if(p1 == rps[1]):
        if(p2 == rps[2]):
            print(f"Player 2 won with {p2} against {p1}")
        if(p2 == rps[0]):
            print(f"Player 1 won with {p1} against {p2}")
        if(p2 == rps[1]):
            print(f"It's a draw with {p1} against {p2}")

    if(p1 == rps[2]):
        if(p2 == rps[0]):
            print(f"Player 2 won with {p2} against {p1}")
        if(p2 == rps[1]):
            print(f"Player 1 won with {p1} against {p2}")
        if(p2 == rps[2]):
            print(f"It's a draw with {p1} against {p2}")
