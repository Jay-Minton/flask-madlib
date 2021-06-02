from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story1

app = Flask(__name__)
app.config['SECRET_KEY'] = "canilive"

debug = DebugToolbarExtension(app)

@app.route("/")
def get_prompts():
    """Page that displays prompts to be put into a story"""
    prompts = story1.prompts

    return render_template("get_prompts.html", prompts = prompts)

@app.route("/story")
def make_story():
    """Page that displays story after prompts have been entered"""

    text = story1.generate(request.args)

    return render_template("make_story.html", text = text)