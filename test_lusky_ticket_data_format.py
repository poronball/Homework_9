from main import lucky_ticket

def test(ticket):
    arg1 = lucky_ticket(ticket)

    assert arg1 != str

test(123321)
