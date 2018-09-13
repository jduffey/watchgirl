import json
import jwt
import datetime


# currentTime = datetime.datetime.now()
# expirationJWT = currentTime+datetime.timedelta(minutes=10)

# iss = 'Meetup Group, Event #006'
# sub = 'This token indicates the recipient attended Meetup Group\'s Event #006'
# iat = currentTime
# exp = expirationJWT

# secret = 'ABC'
# alg = 'HS256'

def genjwt(iss, sub, iat, exp, secret, alg):
    generated_JWT = jwt.encode({'iss': iss, 'sub': sub, 'iat': iat, 'exp': exp}, secret, algorithm=alg)
    return generated_JWT