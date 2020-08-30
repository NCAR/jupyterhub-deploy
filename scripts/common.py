def _prompt():
    actions = {'y': True, 'n': False, 'Y': True, 'yes': True, 'N': False, 'no': False}
    confirmation = input('\nProceed ([y]/n)? ') or 'y'
    try:
        return actions[confirmation]
    except KeyError:
        return False


def _print_command(command):
    print(f'Command: {command}')
