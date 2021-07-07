import unittest
from main import get_num_flagstones 

test_input=[(6,6,4)]
test_output = [4]
class TestSum(unittest.TestCase):
    def test_prg(self):
        for i in range(len(test_input)):
            (n,m,a) = test_input[i]
            nF = get_num_flagstones(n,m,a)
            sol = test_output[i]
            self.assertEqual(nF, sol, 
                f'Area is shown {nF} rather than {sol}')
  
if __name__ == '__main__':
    unittest.main()