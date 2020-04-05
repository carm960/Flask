from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store non trovato'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "Store '{}' già esiste".format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'Si è verificato un errore!'}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'Store cancellato'}


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
        # return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}
        # return {'items': [x.json() for x in ItemModel.query.all()]}
