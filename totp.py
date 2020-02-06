import hashlib


def hash_me(string_input):

    hash_value = hashlib.sha256()
    string_as_bytes = bytes(string_input, 'utf-8')
    hash_value.update(string_as_bytes)

    return hash_value


def generate_digest(time, secret, portion=64):

    sha_inner = hash_me(secret + str(time))
    hashed_inner_as_hex_string = sha_inner.hexdigest()
    sha_outer = hash_me(secret + hashed_inner_as_hex_string)
    outer_hex_digest = sha_outer.hexdigest()

    return outer_hex_digest[:portion]
