def main_menu():
    options = {
        '1': ('Option 1', adm_material),
        '2': ('Option 2', list_material),
        '3': ('Option 3', reg_material_withdraw),
        '4': ('Option 4', reg_material_input),
        '5': ('Exit', exit_menu)
    }
    generate_menu(options, '5')


def generate_menu(options, output_option):
    option = None
    while option != output_option:
        show_menu(options)
        option = read_option(options)
        execute_option(option, options)
        print()  # Only for a white line


def show_menu(options):

    for key in sorted(options):
        print(f'{key} {options[key][0]}')


def read_option(options):
    while (a := input('Option >>> ')) not in options:
        print('Wrong option, please try again')
    return a


def execute_option(option, options):
    options[option][1]()


def adm_material():
    print('Has elegido la opción 1')


def list_material():
    print('Has elegido la opción 2')


def reg_material_withdraw():
    print('Has elegido la opción 3')


def reg_material_input():
    print('Has elegido la opción 4')


def exit_menu():
    print('Finished system')
