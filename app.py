import sqlite3
import random
from flask import Flask, session, render_template, request, g

app = Flask(__name__)
app.secret_key = "suhfdsufgioasfbsdcvpdsiuabvpisdb"

@app.route("/")
def index():
    data = get_db()
    return render_template('index.html', goals=data)




def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('terphockey.db')
        
    cursor = db.cursor()
    cursor.execute("with goal as (select players.player, terpsssss.number, count(terpsssss.number) as goals from terpsssss  natural join players where type='Goal' group by terpsssss.number), assist as (with temp as (select  [1A], count([1A]) as prim_assists from terpsssss where type='Goal' group by [1A]) select  temp.prim_assists, players.player, players.number from players inner join temp on players.number=temp.[1A]) select * from goal natural join assist") 
    goals = cursor.fetchall()
    return goals

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run()