from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "encrypt"
import random

@app.route("/")
def start():

    if "gold_count" not in session:
        session["gold_count"] = 0

    gold_count = session["gold_count"]

    return render_template("index.html", gold_count = gold_count)

@app.route("/process_money", methods=["POST"])
def get_gold():
    
    if request.form["button"] == "farm":
        rand_num = random.randrange(1,3)
        if rand_num == 1:
            goldval = random.randrange(1,9)
            session["gold_count"] += goldval
        if rand_num == 2:
            goldval = random.randrange(1,9)
            session["gold_count"] -= goldval

    
    if request.form["button"] == "cave":
        rand_num = random.randrange(1,3)
        if rand_num == 1:
            goldval = random.randrange(0,11)
            session["gold_count"] += goldval
        if rand_num == 2:
            goldval = random.randrange(1,11)
            session["gold_count"] -= goldval

    if request.form["button"] == "loot":
        rand_num = random.randrange(1,3)
        if rand_num == 1:
            goldval = random.randrange(2,6)
            session["gold_count"] += goldval
        if rand_num == 2:
            goldval = random.randrange(2,5)
            session["gold_count"] -= goldval

    if request.form["button"] == "casino":
        rand_num = random.randrange(1,3)
        if rand_num == 1:
            goldval = random.randrange(10,101)
            session["gold_count"] += goldval
        
        if rand_num == 2:
            goldval = random.randrange(10,101)
            session["gold_count"] -= goldval
        



    return redirect("/")

@app.route("/restart")
def restart_game():
    session.clear()
    return redirect("/")



if __name__=="__main__":
    app.run(debug=True)