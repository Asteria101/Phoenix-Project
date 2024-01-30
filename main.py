import player

def main():
    player1 = player.Player()
    player2 = player.Player("Alfredo", 13, (1,0))
    player1.kick(1.5)
    print(player2.run())

if __name__ == "__main__":
    main()