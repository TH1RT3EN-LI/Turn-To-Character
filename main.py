from turn_to_character import TurnToCharacter

if __name__ == '__main__':
    character_list = [
        '一',
        '二',
        '三',
        '四',
        '五',
        '六',
        '七',
        '八',
    ]
    character_list.reverse()
    path = r''
    multiple = 4
    tc = TurnToCharacter(path, multiple)
    tc.turn_to_character(character_list, zoom_in=False, zoom_out=True)
