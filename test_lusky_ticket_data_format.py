from main import lucky_ticket

def test(ticket):
    arg1 = lucky_ticket(ticket)
    print(arg1)
    assert  arg1 == bool()

test(123321)
