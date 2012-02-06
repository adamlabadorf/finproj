import unittest

import finproj.net as net

class TestNetModule(unittest.TestCase) :

    def setUp(self) :
        self.symbols = "BBDB.TO","NT.TO","GE","MSFT"

    def test_get_symbol_data(self) :
        recs = net.get_symbol_data(self.symbols)
        print recs

if __name__ == '__main__' :
    unittest.main()
