from boggle import Boggle
from random import randint
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from flask import session, jsonify

boggle_game = Boggle()
app = Flask(__name__)
app.config['SECRET_KEY'] = "quietNow"
debug = DebugToolbarExtension(app)

@app.route('/Docboggleument')
def base_template():
    """Practice with route/view function"""
    html = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Boggle!</title>
        </head>
        <body>
            <h1>Boku Boggle Begin!</h1>
            <p>Welcome to my simple boggle game app. I hope you enjoy yourself here!</p>
            <a href='/'>Go here to show board</a>
        <body>
    </html>
    """
    return html

@app.route('/')
def show_board():
    """Display the boggle board using a Jinja template"""
    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get("highscore", 0)
    nplays = session.get("nplays", 0)
    return render_template('index.html', board = board, highscore =
                           highscore, nplays = nplays)

@app.route("/check-word")
def check_word():
    """Check response word against word dictionary"""
    word = request.args["word"]
    board = session['board']
    response = boggle_game.check_valid_word(board, word)
    return jsonify({'result': response})

@app.route("/post-score", methods=["POST"])
def post_score():
    """Receive score, update nplays, update high score if necessary"""
    score = request.json["score"]
    highscore = session.get("highscore", 0)
    nplays = session.get("nplays", 0)
    session['nplays'] = nplays +1
    session['highscore'] = max(score, highscore)
    return jsonify(brokeRecord = score > highscore)









@app.route('/hello')
def say_hello():
    """Shows hello page"""
    return render_template("hello.html")

@app.route('/lucky')
def lucky_number():
    """Practice with Jinja variables"""
    num = randint(1, 20**400)
    return render_template('lucky.html', lucky_num = num, msg = "You are so lucky!!")

# @app.route('/form')
# def form_template():
#     """Show submission form"""
#     html = """
#     <!DOCTYPE html>
#     <html>
#         <head>
#             <title>BoggleWords</title>
#         </head>
#         <body>
#             <form>
#                 <label for="word">Type in your word:</label><br>
#                 <input type="text" id="word" name="word"><br>
#                 <input type="submit" value="Submit">
#             </form>
#         </body>
#     </html>
#     """
#     return html