from flask import Flask, url_for, render_template


# inicialization
app = Flask(__name__)


# routes
@app.route('/')
def hello_world():
    return f"<a href='{ url_for('about_page') }'>About page<a/>"

@app.route('/sobre')
def about_page():
    return """
        <b>Rafael Dantas</b>: é legal!
    """


# execution
app.run(debug=True)