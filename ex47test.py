from ex45 import Player
from nose.tools import *

def test_money():
	p = Player()
	assert_greater(p.money, 1000)

test_money()
