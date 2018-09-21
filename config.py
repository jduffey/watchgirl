settings = dict (
    delayBetweenCodesInSeconds = 3,
    codesToGenerate = 5,
    qrCodeSize = 5,
    )

header = dict(
    alg = 'HS256',
    )

payload = dict(
    iss = 'This is the issuer\'s identifier.',
    desc = 'This is the description field of the paylod.',
    )

signature = dict(
    secret = 'ABC',
    )