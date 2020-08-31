import colorama


def _prompt():
    actions = {'y': True, 'n': False, 'Y': True, 'yes': True, 'N': False, 'no': False}
    confirmation = input('\nProceed ([y]/n)? ') or 'y'
    try:
        return actions[confirmation]
    except KeyError:
        return False


def _print_command(step, command):
    print(f'Step   : \033[1;37m{step} {colorama.Style.RESET_ALL}')
    print(f'Command: \033[1;96m{command}{colorama.Style.RESET_ALL}')
