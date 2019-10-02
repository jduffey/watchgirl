import hashlib
import datetime
import time


def set_secret(secret_string):
    secret_string = secret_string
    return secret_string

def set_period(period_integer):
    period = period_integer
    return period

def hash_the_input(string_input):
    string_to_bytes = bytes(string_input, 'utf-8')
    hashed_input = hashlib.sha256()
    hashed_input.update(string_to_bytes)
    return hashed_input

def get_chunked_time(period, offset):
    time_to_use = time.time() + offset
    unix_sec_to_use = int(time_to_use)
    chunked_time = int(unix_sec_to_use / period)
    return chunked_time

def set_inner_string(secret, chunked_time):
    inner_string = secret + str(chunked_time)
    return inner_string

def return_the_hash(secret_input, period_input, offset):

    """
    This algorithm is a variation of the one found here:
    https://garbagecollected.org/2014/09/14/how-google-authenticator-works/
    
    From that page:
    original_secret = xxxx xxxx xxxx xxxx xxxx xxxx xxxx xxxx
    secret = BASE32_DECODE(TO_UPPERCASE(REMOVE_SPACES(original_secret)))
    input = CURRENT_UNIX_TIME() / 30
    hmac = SHA1(secret + SHA1(secret + input))
    """

    secret = set_secret(secret_input)
    
    period = set_period(period_input)

    chunked_time = get_chunked_time(period, offset)

    inner_string = set_inner_string(secret, chunked_time)

    sha_inner = hash_the_input(inner_string)

    hashed_inner_as_hex = sha_inner.hexdigest()

    sha_outer = hash_the_input(secret + hashed_inner_as_hex)

    outer_hex_digest = sha_outer.hexdigest()

    return outer_hex_digest
