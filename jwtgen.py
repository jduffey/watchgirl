import json
import jwt
import datetime


def genjwt(iss, desc, iat, exp, secret, alg):
    generated_JWT = jwt.encode({'iss': iss, 'desc': desc, 'iat': iat, 'exp': exp}, secret, algorithm=alg)
    return generated_JWT