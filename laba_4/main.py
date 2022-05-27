from gui import run_gui_interface
import console
import click
from click_shell import shell
from model.Gamemap import World
from interface import *
from restore.restore_service import RestoreService
@click.command()
@click.option(
    '--use-save',
    default=False,
    help="Set this parameter as 'True' to upload previous session, otherwise 'False'."
)
@click.option(
    '--interface-type',
    default='CLI',
    help="Sets type of interface that application will use. Possible parameters are GUI and CLI.")


def main(use_save, interface_type):
    '''Model of a garden plot'''
    global garden
    garden = None
    
    restore_service = RestoreService()

    if use_save:
        garden = restore_service.restore_garden()

    if garden is None:
        garden = World()
        
    if interface_type.lower() == 'gui':
        run_gui_interface()
    elif interface_type.lower() == 'cli':
        console.run_cli_interface(garden)
    else:
        print('Unavailable format.')
        exit()

if __name__ == '__main__':
    main()
