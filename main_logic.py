import create_npc
import sqlite3


connection = sqlite3.connect("npcs.db")


#generate variables to insert into table
my_npc = create_npc.create_npc()
name = my_npc["name"]
race = my_npc["race"]
alignment = my_npc["alignment"]
occupation = my_npc["occupation"]
age = my_npc["age_in_years"]
weight_in_lbs = my_npc["weight_in_lbs"]
height_in_inches = my_npc["height_in_inches"]
hair_style = my_npc["hair_style"]
hair_color = my_npc["hair_color"]


#cursor to interact with the database
cursor = connection.cursor()

#Below commented statement is used to generate table initially
#cursor.execute("CREATE TABLE npcs (name TEXT, race TEXT, alignment TEXT, occupation TEXT, age_in_years INTEGER, weight_in_lbs INTEGER, height_in_inches INTEGER, hair_style TEXT, hair_color TEXT)")

#if the name inputted is in the table then do something
if cursor.execute("SELECT 1 FROM npcs WHERE name = ?", [name]).fetchone():
    print(f'There is already a npc with name: {name}.')
else:
    cursor.execute("INSERT INTO npcs (name, race, alignment, occupation, age_in_years, weight_in_lbs, height_in_inches, hair_style, hair_color) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, race, alignment, occupation, age, weight_in_lbs, height_in_inches, hair_style, hair_color))

connection.commit()

print(f'{connection.total_changes} total changes made.')

connection.close()





