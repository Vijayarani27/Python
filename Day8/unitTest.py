import unittest
from TestDemo import multiply

class test_mul(unittest.TestCase):
  def test_can_mul(self):
      self.assertEqual(multiply(5,2), 10)


if __name__ == '__main__':
    unittest.main()