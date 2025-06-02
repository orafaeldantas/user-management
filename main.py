from flask import Flask
from routes.home import home_route
from routes.customer import customer_route


# inicialization
app = Flask(__name__)

app.register_blueprint(home_route)
app.register_blueprint(customer_route, url_prefix='/customers')

# execution
app.run(debug=True)