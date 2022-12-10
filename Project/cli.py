from sqlalchemy import insert
import Database.db as db
from models.material import Material
from models.material_movement import MaterialMovement


def main_menu():
    options = {
        '1': ('Manage Materials', submenu),
        '2': ('List Materials', list_material),
        '3': ('Record withdrawal of material', rec_material_withdraw),
        '4': ('Register incoming material', rec_material_input),
        '5': ('Exit', exit_menu)
    }
    generate_menu('Main Menu', options, '5')


def generate_menu(name, options, output_option):
    option = None
    while option != output_option:
        show_menu(name, options)
        option = read_option(options)
        execute_option(option, options)
        print()  # Only for a white line


def submenu():
    options = {
        'a': ('Add Material ', add_mat),
        'b': ('Edit Material', edit_mat),
        'c': ('Delete Mateial', del_mat),
        'd': ('Exit', exit_menu)
    }
    generate_menu('Material Menu', options, 'd')


def show_menu(name, options):
    print(f'# {name}. Choose an option: ')
    for key in sorted(options):
        print(f'{key} {options[key][0]}')


def read_option(options):
    while (a := input('Option >>> ')) not in options:
        print('Wrong option, please try again')
    return a


def execute_option(option, options):
    options[option][1]()


def list_material():
    print('Has elegido la opción 2')


def rec_material_withdraw():
    print('Has elegido la opción 3')


def rec_material_input():
    print('Has elegido la opción 4')


def add_mat():
    print()
    name = input('Insert the name: ').upper()
    quantity = int(input('Insert quantity: '))
    unit_price = int(input('Insert unit price: '))
    id_material = [letter for letter in name if letter not in 'AEIOU']
    id_material = ''.join(map(str, id_material))
    material = Material(id=id_material, name=name, quantity=quantity, unit_price=unit_price)
    db.session.add(material)
    db.session.commit()
    return


def edit_mat():
    pass


def del_mat():
    pass


def exit_menu():
    print('Leaving')
