from hello import more_hello, more_salam


def test_more_hello():
    assert "hi" == more_hello()


def test_more_salam():
    assert "salam" == more_salam()
