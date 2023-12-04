from collections import defaultdict

MAX_CUBES_RED = 12
MAX_CUBES_GREEN = 13
MAX_CUBES_BLUE = 14


def is_valid(cubes: dict[str, int]) -> bool:
    return cubes['blue'] <= MAX_CUBES_BLUE and cubes['green'] <= MAX_CUBES_GREEN and cubes['red'] <= MAX_CUBES_RED

def game_number_and_sets(line: str) -> tuple[int, list[str]]:

    game, sets = line.split(':')

    _, game_number_str = game.split()
    game_number = int(game_number_str)

    sets_list = sets.split(';')

    return game_number, sets_list

def get_sep_by_color(set_: str) -> list[str]:
    return [s.strip() for s in set_.split(',')]


def possible_games(input, debug=False) -> tuple[int, int]:

    sum_game, power = 0, 0
    with open(input) as fp:
        for line in fp:
            blue, green, red = 0, 0 , 0

            game_number, sets = game_number_and_sets(line)

            valid_sets = []
            for i, set_ in enumerate(sets, start=1):
                set_sep_by_color =  get_sep_by_color(set_)

                cubes = defaultdict(int)
                for s in set_sep_by_color:
                    number, color = s.split()
                    cubes[color] = int(number)

                blue = max(blue, cubes['blue'])
                red = max(red, cubes['red'])
                green = max(green, cubes['green'])

                valid_sets.append(is_valid(cubes))

                if debug:
                    print(f'Game: {game_number} - set: {i} - cubes: {dict(cubes)} - valido: {is_valid(cubes)}')

            valid_game = all(valid_sets)

            if debug:
                print(f'Game: {game_number} - power: {red=} {blue=} {green=} - {red * blue * green}')

            if valid_game:
                sum_game += game_number

            power +=  blue * red * green

    return sum_game, power

if __name__ == "__main__":

    result, power = possible_games("test1_input.txt")
    print(f'Resultado: {result} {power}')
    assert result == 8
    assert power == 2286

    result, power = possible_games("test2_input.txt")
    print(f'Resultado: {result} {power}')
    assert result == 2317
    assert power == 74804

