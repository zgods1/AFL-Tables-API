import pandas as pd
import lxml
import os
import flask


# Grabs table from AFLtables.com.au with arguements
def grab_table(url, table_number):
    return 

# Grabs the data from AFLtables.com.au and removes the junk data
# Specifically summary row and labels the headers correctly
def players(team, year):
    
    url = 'https://afltables.com/afl/stats/' + str(year) +'.html'

    # Grabs data from AFL table
    players = pd.read_html(url)[team]

    # Removes the summary row at the end
    players = players[:-1]

    # Turns the Dataframe into a temporary CSV and saves in same directory as python file
    players.to_csv("static/data/data" + str(team) + ".csv", index=False)

    # Grabs CSV and removes top row of nonsense data
    fixed_data = pd.read_csv("static/data/data" + str(team) + ".csv", skiprows=1)
    fixed_data = fixed_data.drop('#', axis=1)
    fixed_data = fixed_data.set_index('Player')

    return fixed_data

def all_time(team):
    url = 'https://afltables.com/afl/stats/alltime/' + team + '.html'
    at = pd.read_html(url)[0]
    at = at[:-1]
    at = at.set_index('Player')
    return at

