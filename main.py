import argparse
from pony import PonyChallenge


def main():

    # Instantiate the argument parser
    parser = argparse.ArgumentParser(description='ml-games')

    # Add arguments
    parser.add_argument('-width', type=int, default=15, help='Maze width.')
    parser.add_argument('-height', type=int, default=15, help='Maze height.')
    parser.add_argument('-difficulty', type=int, default=5, help='Maze difficulty.')
    parser.add_argument('-name', type=str, default='Applejack', help='Pony name.')

    # Parse arguments
    args = parser.parse_args()

    # Create new game object
    pony_challenge = PonyChallenge(width=args.width,
                                   height=args.height,
                                   difficulty=args.difficulty,
                                   name=args.name)

    # Run the game
    pony_challenge.play()





if __name__ == '__main__':
    main()