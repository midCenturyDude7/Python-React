import graphene
import json
from datetime import date, datetime

class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    created_at = graphene.DateTime()


class Query(graphene.ObjectType):
    users = graphene.List(User, limit=graphene.Int())
    hello = graphene.String()
    is_admin = graphene.Boolean()
    

    def resolve_hello(self, info):
        return "world"


    def resolve_is_admin(self, info):
        return True


    def resolve_users(self, info, limit=None):
        return [
            User(id="1", username="Fred", created_at=datetime.now()),
            User(id="2", username="Doug", created_at=datetime.now()),
        ][:limit]


schema = graphene.Schema(query=Query, auto_camelcase=False)

result = schema.execute( 
    '''
    {
        users(limit: 1) {
            id
            username
            created_at
        }
    }
    '''
)

dictResult = dict(result.data.items())
print(json.dumps(dictResult, indent=2))
