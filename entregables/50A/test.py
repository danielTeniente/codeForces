import unittest
from main import max_dom 

test_input=[(2,4),(3,3)]
test_output = [4,4]

class TestSum(unittest.TestCase):
    def test_prg(self):
        for i in range(len(test_input)):
            (n,m) = test_input[i]
            nF = max_dom(n,m)
            sol = test_output[i]
            self.assertEqual(nF, sol, 
                f'Case {i} is shown {nF} rather than {sol}')

if __name__ == '__main__':
    unittest.main()