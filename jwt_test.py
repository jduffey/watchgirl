import json
import jwt
import datetime


expirationJWT = datetime.datetime.now()+datetime.timedelta(minutes=10)
generated_JWT = jwt.encode({'iss': 'Byrne\'s Pub', 'exp': expirationJWT}, 'THE_SECRET', algorithm='HS256')

print(generated_JWT)