import os
import pickle
import click
from click_shell import shell
from model.Gamemap import World
from interface import *

@shell(prompt='> ', intro='Launching CLI application...')
@click.option(
    '--use-save',
    default=False,
    help="Set this parameter as 'True' to upload previous session, otherwise 'False'."
)
@click.option(
    '--interface-type',
    default='CLI',
    help="Sets type of interface that application will use. Possible parameters are GUI and CLI."
)
def app(use_save,  interface_type):
    pass

def run_cli_interface(model: World):
    global garden
    garden = model
    app()

@app.command(help='Create garden plot.', name='start-garden')
def start_gerden():
    garden.start_garden()


@app.command(help='One day passes.', name='next-day')
def next_day():
    garden.commands("next_day")

@app.command(help='Adds a plant to the plot.', name='add-plant')
def add_plant():
    garden.commands("add_plant")

@app.command(help='Adds a tree to the plot.', name='add-tree')
def add_tree():
    garden.commands("add_tree")
    
@app.command(help='Adds a pest to the plot.', name='add-pests')
def add_pests():
    garden.commands("add_pests")
    
@app.command(help='Adds a pest to the plot.', name='weeding')
def add_pests():
    garden.commands("weeding")
    
@app.command(help='Watering plants.', name='water-plants')
def water_plants():
    garden.commands("water_plants")
    
@app.command(help='Save in file.', name='save-garden')
def save_garden():
    garden.commands("save")
    
@app.command(help='Inforamtion about any object.', name='info')
def save_garden():
    garden.commands("info")
    
if __name__ == '__main__':
    app()

