from flask import Blueprint, render_template, request
from database.customer import CUSTOMERS

customer_route = Blueprint('customer', __name__)

"""
Rota de Clientes

    -/customers/ (GET) - Listar os clientes
    -/customers/ (POST) - Inserir o cliente no servidor
    -/customers/ (GET) - Renderizar o formulario para criar um cliente
    -/customers/<id> (GET) - Obter dados de um cliente
    -/customers/<id>/edit (GET) - Renderizar um formulario para editer um cliente
    -/customers/<id>/update (PUT) - Atualizar os dados do cliente
    -/customers/<id>/delete (DELETE) - Deleta o registro do usuario

"""


@customer_route.route('/')
def customer_list():
    return render_template('customer_list.html', customers=CUSTOMERS)

@customer_route.route('/', methods=['POST'])
def insert_customer():
    
    data = request.json

    new_customer = {
        "id": len(CUSTOMERS) + 1,
        "nome": data['nome'],
        "email": data['email'],
    }

    CUSTOMERS.append(new_customer)

    return render_template('item_customer.html', customer=new_customer)

@customer_route.route('/new')
def form_customer():
    return render_template('form_customer.html')

@customer_route.route('/<int:custumer_id>')
def detail_customer(customer_id):
    return render_template('detail_customer.html')

@customer_route.route('/<int:custumer_id>/edit')
def form_edit_customer(customer_id):

    customer = None
    for c in CUSTOMERS:
        if c['id'] == customer_id:
            customer = c
    
    return render_template('form_customer.html',customer=customer)

@customer_route.route('/<int:custumer_id>/update', methods=['PUT'])
def update_customer(customer_id):
    pass

@customer_route.route('/<int:customer_id>/delete', methods=['DELETE'])
def delete_customer(customer_id):
    global CUSTOMERS

    CUSTOMERS = [c for c in CUSTOMERS if c['id'] != customer_id]

    return {'deleted': 'ok'}
