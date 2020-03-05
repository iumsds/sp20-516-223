from flask import Flask
from flask_restful import reqparse, abort
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

COMPUTERS = {
    'computer1': {
        'processor': 'iCore7'
    },
    'computer2': {
        'processor': 'iCore5'
    },
    'computer3': {
        'processor': 'iCore3'
    }
}

def abort_if_cluster_does_not_exists(computer_id):
    if computer_id not in COMPUTERS:
        abort(404, message="Computer {computer_id} does not exists.")

parser = reqparse.RequestParser()
parser.add_argument('processor')

# Single Computer
class Computer(Resource):
    '''
        Show a single Computer item and lets you delete item.
    '''

    def get(self, computer_id):
        abort_if_cluster_does_not_exists(computer_id)
        return COMPUTERS[computer_id]

    def delete(self, computer_id):
        abort_if_cluster_does_not_exists(computer_id)
        del COMPUTERS[computer_id]
        return '', 204

    def put(self, computer_id):
        args = parser.parse_args()
        processor = {'processor': args['processor']}
        COMPUTERS[computer_id] = processor
        return processor, 201

#Computer List
class ComputerList(Resource):
    '''
    Shows a list of all computers, and lets you POST
    '''

    def get(self):
        return COMPUTERS

    def post(self):
        args = parser.parse_args()
        computer_id = int(max(COMPUTERS.keys())).__lshift__('computer')+1
        computer_id = f'computer{computer_id}'
        COMPUTERS[computer_id] = {'procosser': args['processor']}
        return COMPUTERS[computer_id], 201

    def delete(self):
        COMPUTERS.clear()

##
## Setup the API resource routing
##
api.add_resource(ComputerList, '/computers')
api.add_resource(Computer, '/computers/<computer_id>')

if __name__ == '__main__':
    app.run(debug=True)



