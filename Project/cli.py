from sqlalchemy import insert, text, update
from sqlalchemy.orm import sessionmaker

import Database.db as db
from models.material import Material
from models.material_movement import MaterialMovement

Session = sessionmaker(bind=db.engine)
session = Session()


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
    session.add(material)
    session.commit()
    return


def edit_mat():
    # TODO: create sub menu
    material_id = input('Insert the material ID: ')
    q = db.session.query(Material).filter(Material.id == material_id)
    # Check if the material exist

    if bool(db.session.query(q.exists())) is True:
        if input('Change quantity? (Y/N): ').upper() == 'Y':
            new_quantity = int(input('Enter the new quantity: '))
        if input('Change unit price? (Y/N): ').upper() == 'Y':
            new_unit_price = int(input('Enter the new unit price: '))


def del_mat():
    try:
        material_id = str(input('Insert the material ID: ')).upper()
        m = session.query(Material).filter_by(id=material_id).one()
        session.delete(m)
        session.commit()
    except Exception as e:
        print('The material doesnt exist. Exiting...')
    return


def exit_menu():
    print('Leaving')

# if __name__ == '__main__':
