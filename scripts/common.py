import colorama

RED = '\033[1;31m'
GRN = '\033[1;32m'
YEL = '\033[1;33m'
BLU = '\033[1;34m'
WHT = '\033[1;37m'
MGT = '\033[1;95m'
CYA = '\033[1;96m'
END = '\033[0m'
BLOCK = '\033[1;37m'


def _prompt():
    actions = {'y': True, 'n': False, 'Y': True, 'yes': True, 'N': False, 'no': False}
    confirmation = input('\nProceed ([y]/n)? ') or 'y'
    try:
        return actions[confirmation]
    except KeyError:
        return False


def _print_command(step, command):
    print(f'\n{"<=== "}{"*"*40}{" ===>"}')
    print(f'Step   : {WHT}{step} {colorama.Style.RESET_ALL}')
    print(f'Command: {CYA}{command}{colorama.Style.RESET_ALL}')
