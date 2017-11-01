import unittest
import rpn
from clint.textui import colored, puts

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2, result)
		puts(colored.green("IT WORKS"))

	def test_subtract(self):
		result = rpn.calculate('5 3 -')
		self.assertEqual(2, result)
		puts(colored.green("IT WORKS"))

