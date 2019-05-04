from pony import PonyChallenge
import argparse
import sys


def main():

    # Instantiate the argument parser
    parser = argparse.ArgumentParser(description='ml-games')

    # Add arguments
    parser.add_argument('--width', type=int, default=15, help='Maze width.')
    parser.add_argument('--height', type=int, default=15, help='Maze height.')
    parser.add_argument('--difficulty', type=int, default=5, help='Maze difficulty.')
    parser.add_argument('--name', type=str, default='Applejack', help='Pony name.')

    # Parse arguments
    args = parser.parse_args()

    # Check the arguments compatibility
    if args.width not in range(15, 26):
        print("Please select width between 15 and 25.")
        sys.exit()
    if args.height not in range(15, 26):
        print("Please select height between 15 and 25.")
        sys.exit()
    if args.difficulty not in range(0, 11):
        print("Please select difficulty between 0 and 10.")
        sys.exit()
    try:
        PonyChallenge(name=args.name)
    except:
        print("Please enter correct pony name.")
        sys.exit()

    # Create new game object
    pony_challenge = PonyChallenge(width=args.width,
                                   height=args.height,
                                   difficulty=args.difficulty,
                                   name=args.name)

    # Run the game
    pony_challenge.play()





if __name__ == '__main__':
    main()