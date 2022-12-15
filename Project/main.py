import os

from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import Session, sessionmaker

from cli import main_menu
import Database.db as db
import threading
from Rabbit import Rabbit


def background_consume(exchange):
    messagge_q = Rabbit()
    messagge_q.consume(exchange)



if __name__ == "__main__":
    # TODO: Check if the db already exist before lauching the program
    '''
    current_path = os.getcwd()
    current_path = '{c}{d}{n}'.format(c=current_path, d='\..\Database', n='\database.db')
    if os.path.isfile(os.path.abspath(current_path)):
        main_menu()
    '''

    db.Base.metadata.create_all(db.engine)
    t = threading.Thread(target=background_consume, args=('useOfMaterials',), daemon=True)
    t.start()
    main_menu()
