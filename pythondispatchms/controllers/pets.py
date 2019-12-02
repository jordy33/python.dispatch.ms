from tg import RestController
from tg import expose
from pythondispatchms.model import DBSession
from pythondispatchms.model.tables import Pets
__all__ = ['PetsController']


class PetsController(RestController):

    @expose('json')
    def get_all(self):
        pets=[]
        allrecords = DBSession.query(Pets).all()
        for item in allrecords:
            pets.append(dict(id=item.id,name=item.name,breed=item.breed))
            print(item.name)
        return dict(pets=pets)


    @expose('json')
    def put(self, name,breed,id):
        query = DBSession.query(Pets).filter_by(id=int(id)).first()
        if query is not None:
            query.name = name
            query.breed = breed
            DBSession.flush()
        print("PUT Name: {} Breed: {} id:".format(name,breed,id))
        return dict(name=name,breed=breed,id=id)

    @expose('json')
    def post(self, name,breed):
        newitem = Pets()
        newitem.name = name
        newitem.breed = breed
        DBSession.add(newitem)
        DBSession.flush()
        print("Post Name: {} Breed: {}".format(name, breed))
        return dict(name=name, breed=breed,id=newitem.id)

    @expose('json')
    def post_delete(self,record):
        print("DELETE Id: {} ".format(record))
        query = DBSession.query(Pets).filter_by(id=int(record)).first()
        if query is not None:
            DBSession.delete(query)
            DBSession.flush()
        return dict(id=record)


