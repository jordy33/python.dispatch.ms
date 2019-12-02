from tg import RestController
from tg import expose
from pythondispatchms.model import DBSession
from pythondispatchms.model.tables import Assets
from base64 import b64encode,b64decode
__all__ = ['ImagesController']


class ImagesController(RestController):

    @expose('json')
    def get_all(self):
        pets=[]
        return dict(pets=pets)


    @expose('json')
    def put(self, name,breed,id):
        return dict(name=name,breed=breed,id=id)

    @expose('json')
    def post(self, id,data):
        print(data)
        newitem = Assets()
        newitem.assets_id = id
        newitem.data = data
        DBSession.add(newitem)
        DBSession.flush()
        return dict(id=id,data=data)

    @expose('json')
    def post_delete(self,record):
        return dict(id=record)


