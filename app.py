import io
import json
import os
import pandas as pd
import datetime
import time
from flask import Flask, render_template, request, url_for, redirect, make_response, send_file, send_from_directory, jsonify
from AFL_API import afl_tables as AFL

app = Flask(__name__)




@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home.html')



####################################
# ALL API END POINTS WILL BE BELOW #
####################################


# AFL Player data based on team and year
@app.route('/api/players', methods=['GET', 'POST'])
def players():
    args = request.args
    
    team = args['team']
    
    start_year = args['start_year']
    
    end_year = args['end_year']
    
    # Loads a list of team names to the number they realate to on AFLTables
    with open('static/json//teams_api.json') as f:
        jd = json.load(f)

    # Create a dictionary that we can update in our loop below
    d1 = {}
    
    # Range of years to cycle through
    for year in range(int(start_year), (int(end_year)+1)):
        data = AFL.players(jd[team], start_year)
        jf = data.to_dict(orient="index")
        
        # Create a dictionary each key is a year with the new dictionary inside
        d = {
            year : [
                jf
            ]
        }
        
        # Updates the dictionary to be turned into a json response
        d1.update(d)

    return jsonify(d1)


 

@app.route('/api/all-time', methods=['GET', 'POST'])
def all_time():
    args = request.args
    team = args['team']
    with open('static/json/teams_at.json') as f:
        jd = json.load(f)
    at = AFL.all_time(jd[team])
    at = at.to_dict(orient='index')

    return jsonify(at)






if __name__ == "__main__":
    print("running py app")
    app.run(host="127.0.0.1", port=5000, debug=True)





