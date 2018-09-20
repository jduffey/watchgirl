import json
import jwt
import datetime


def genjwt(iss, iat, exp, secret, alg):
    generated_JWT = jwt.encode({'iss': iss, 'iat': iat, 'exp': exp}, secret, algorithm=alg)
    return generated_JWT