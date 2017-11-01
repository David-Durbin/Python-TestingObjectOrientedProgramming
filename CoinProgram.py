import Coin_Class

"""

Here is the rest of the Gaddis program.

"""


def main():
    # create a coin object by calling it from Coin_Class
    my_coin = Coin_Class.Coin()

    # display the side of the coin facing up
    print("This side is up: ", my_coin.get_side_up())

    # flip the coin
    my_coin.toss()

    # display the side of the coin facing up
    print("This side is up: ", my_coin.get_side_up())


main()
