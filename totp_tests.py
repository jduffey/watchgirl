import totp


def test_generate_digest_returns_the_full_hash():
    totp_time = [1, 42]
    totp_secret = ["", "shh!"]

    expected = ["e0bc614e4fd035a488619799853b075143deea596c477b8dc077e309c0fe42e9",
                "de0c1b8257e09233913795a926ef2e29831fb2f851afbed56c47bdddc15b0e16"]

    for i in range(len(expected)):
        actual = totp.generate_digest(totp_time[i], totp_secret[i])
        assert expected[i] == actual


def test_generate_digest_returns_portion_of_digest():
    totp_time = [9000, 8675309]
    totp_secret = ["it's over", "rick springfield"]
    totp_portion = [4, 8]

    expected = ["748a",
                "6a27d981"]

    for i in range(len(expected)):
        actual = totp.generate_digest(totp_time[i], totp_secret[i], totp_portion[i])
        assert expected[i] == actual
