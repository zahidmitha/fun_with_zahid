from nose.tools import *
from ex48.parser import peek, parse_object

# def test_sentence():
# 	pass

# def test_parseerror():
# 	pass

def test_peek():
	sample_list = [("first", "world"), ("hello", "world")]
	expected = "first"
	calculated = peek(sample_list)
	assert_equal(expected, calculated)

# def test_match():
# 	assert_equal(match(("", ""), ("")))
	# test whether first element of first tuple = expecting

# def test_skip():
# 	pass
	# No test

# def test_parse_verb():
# 	pass

# def test_parse_subject():
# 	pass

# def test_parse_sentence():
# 	pass


test_peek()

parse_object([("door", "bear"), ("door", "bear")])

