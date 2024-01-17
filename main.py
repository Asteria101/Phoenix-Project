import player
import threading

def main():
    player1 = player.Player()
    player2 = player.Player("Alfredo", 13, (1,0))

    player1.run()

    #TH = threading.Thread(target=)

if __name__ == "__main__":
    main()