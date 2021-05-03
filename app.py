from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import Story

app = Flask(__name__)
app.config['SECRET_KEY'] = "hush"
# debug = DebugToolbarExtension(app)

vals = ["place", "noun", "verb", "adjective", "plural_noun"]
story = Story(
    vals, """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)


@app.route("/")
def show_form():
    return render_template('form.html', vals=vals)


@app.route("/story")
def show_story():
    return render_template("story.html", story=story.generate(request.args))
