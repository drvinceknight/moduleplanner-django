from django.db import models

# The Module class
class Module():
    user = ReferenceField(User, reverese_delete_rule=CASCADE)
    name = StringField(max_length=200, required=True)
    desc = StringField(required=True)
    desc_length = IntField()
    date_modified = DateTimeField(default=datetime.now)
    is_published = BooleanField()
