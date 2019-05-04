import requests
import json
import time


class PonyChallenge:

    """ Class to find the way towards the exit and save the pony. """

    def __init__(self, width=15, height=15, difficulty=5, name='applejack'):
        self.width = width
        self.height = height
        self.difficulty = difficulty
        self.name = name
        self.maze_id = self.reset_game()



    def reset_game(self):

        """ Reset game and get new ID. """

        url = 'https://ponychallenge.trustpilot.com/pony-challenge/maze'
        data = {
            "maze-width": self.width,
            "maze-height": self.height,
            "maze-player-name": self.name,
            "difficulty": self.difficulty
        }
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        response = requests.post(url, data=json.dumps(data), headers=headers)

        return json.loads(response.text)['maze_id']



    def get_game_data(self):

        """ Get the information about the current maze state. """

        url = 'https://ponychallenge.trustpilot.com/pony-challenge/maze/' + self.maze_id
        headers = {
            "Accept": "application/json"
        }
        response = requests.get(url, headers=headers)

        return json.loads(response.text)



    def make_step(self, direction):

        """ Make step to specified direction in real game. """

        url = 'https://ponychallenge.trustpilot.com/pony-challenge/maze/' + self.maze_id
        data = {
            "direction": direction
        }
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        response = requests.post(url, data=json.dumps(data), headers=headers)

        return json.loads(response.text)



    def print_game(self):

        """ Get visual representation af the maze. """

        url = 'https://ponychallenge.trustpilot.com/pony-challenge/maze/' + self.maze_id + '/print'
        headers = {
            "Accept": "application/json"
        }
        response = requests.get(url, headers=headers)

        return response.text



    def get_possible_directions(self, maze, block_id):

        """ Compute available steps from the current block maze block. """

        directions = []
        last_block = len(maze) - 1
        block_borders = maze[block_id]

        # if no border in 'west'
        if 'west' not in block_borders:
            directions.append('west')

        # if no border in 'north'
        if 'north' not in block_borders:
            directions.append('north')

        # if it's not the last block in 'east' side
        if ((block_id + 1) % self.width) != 0:
            # if no border in 'east'
            if 'west' not in maze[block_id + 1]:
                directions.append('east')

        # if it's not the last block in 'north' side
        if (block_id + self.width) <= last_block:
            # if no border in 'south'
            if 'north' not in maze[block_id + self.width]:
                directions.append('south')

        return directions



    def step(self, maze, block_id, direction):

        """ Make the step in the local copy of the maze while solving. """

        # get valid directions for block
        possible_directions = self.get_possible_directions(maze=maze, block_id=block_id)

        if direction in possible_directions:
            if direction == 'west':
                block_id -= 1
            if direction == 'east':
                block_id += 1
            if direction == 'north':
                block_id -= self.width
            if direction == 'south':
                block_id += self.width
        else:
            print('Invalid direction!')

        return block_id



    def solve_maze(self, game_data, current_block_id=None, last_move=None):

        """ Recursively solve the maze ang get list of steps towards the exit. """

        maze = game_data['data']
        endpoint_id = game_data['end-point'][0]
        if current_block_id is None:
            current_block_id = game_data['pony'][0]

        opposite_direction = {
            'north': 'south',
            'south': 'north',
            'west': 'east',
            'east': 'west',
        }
        
        # stop the process if exit reached
        if current_block_id == endpoint_id:
            return ['exit']

        else:
            # get valid directions for block
            possible_directions = self.get_possible_directions(maze=maze, block_id=current_block_id)

            # prevent going back to previous block
            if last_move is not None:
                possible_directions = [x for x in possible_directions if x != opposite_direction[last_move]]

            # go back if no available directions left
            if possible_directions == []:
                return ['no_way']

            for direction in possible_directions:
                previous_block_id = current_block_id
                current_block_id = self.step(maze=maze, block_id=current_block_id, direction=direction)
                way = [direction] + self.solve_maze(game_data, current_block_id, last_move=direction)
                if way[-1] == 'exit':
                    return [direction]
                if way[-1] == 'no_way':
                    if direction == possible_directions[-1]:
                        return ['no_way']
                    else:
                        current_block_id = previous_block_id
                        continue

                return way


    def print_end_game(self, game_data):
        
        """ Check whether game is ended and print the message if so. """
        
        state = game_data['game-state']['state']
        result = game_data['game-state']['state-result']

        if state == 'over' or state == 'won':
            print("\n" * 50)
            print(result)
            return True
        else:
            return False


    def play(self):
        
        """ Run the solved game in API and show how it goes. """

        game_data = self.get_game_data()
        way = self.solve_maze(game_data)

        for direction in way:
            self.make_step(direction)
            maze_map = self.print_game()
            # make maze visible in terminal
            maze_map = maze_map.replace('+ |', '+\n|').replace('| +', '|\n+')
            print("\n" * 50)
            print(maze_map)
            time.sleep(0.25)
            end = self.print_end_game(self.get_game_data())
            if end:
                return


# Run test
if __name__ == '__main__':
    pony = PonyChallenge()
    pony.play()



