from flask import (Flask, render_template)
import pending, member

app = Flask(__name__)
app.register_blueprint(member.bp)
app.register_blueprint(pending.bp)

@app.route("/")
def index():
    if (True):
        loggedIn = True
    return render_template('index.html', loggedIn=loggedIn)

@app.route("/post")
def post():
    # POSTで記事が降ってくるので、これをfirestoreに格納して、必要に応じて公開の審査登録処理をする。
    return render_template('index.html')