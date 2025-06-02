from flask import Blueprint

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
    return {'pagina': 'lista_clientes'}

@customer_route.route('/', methods=['POST'])
def insert_customer():
    return {'pagina': 'formulario clientes'}

@customer_route.route('/new')
def form_customer():
    pass

@customer_route.route('/<int:>custumer_id')
def get_customer(custumer_id):
    pass

@customer_route.route('/<int:>custumer_id/edit')
def form_edit_customer(custumer_id):
    pass

@customer_route.route('/<int:>custumer_id/update', methods=['PUT'])
def update_customer(custumer_id):
    pass

@customer_route.route('/<int:>custumer_id/delete', methods=['DELETE'])
def delete_customer(custumer_id):
    pass