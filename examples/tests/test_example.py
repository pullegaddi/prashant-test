from examples import example
import unittest


class ExampleMethods(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(example.get_hello(), "hello, world!")
