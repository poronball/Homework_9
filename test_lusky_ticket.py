from main import lucky_ticket

def test(ticket):
    arg1 = True
    print(arg1)
    assert  lucky_ticket(ticket) == arg1


test(123321)
