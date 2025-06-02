from flask import Flask, url_for, render_template


# inicialization
app = Flask(__name__)


# routes
@app.route('/')
def hello_world():
    title = "Customers Management"
    customers = [
        {"name": "Guilherme", "membro_ativo": True},
        {"name": "Joao", "membro_ativo": False},
        {"name": "Maria", "membro_ativo": False},
    ]
    return render_template('index.html', title=title, customers=customers)

@app.route('/sobre')
def about_page():
    return """
        <b>Rafael Dantas</b>: é legal!
    """


# execution
app.run(debug=True)