import os
import unittest

import finproj.db as db

class TestDBModule(unittest.TestCase) :

    def setUp(self) :
        self.path = 'test.db'

    def test_create(self) :
        conn = db.create(self.path) # should work

        # test whether db creation fails on existing db w/o replace
        self.assertRaises(db.FileExistsException, db.create, self.path)

        db.create(self.path,replace=True) # should work

        # get rid of the db
        os.remove(self.path)

    def test_connect(self) :

        # get rid of the file in case it exists so connect will fail
        try :
            os.remove(self.path)
        except OSError :
            pass

        self.assertRaises(db.FileNotFoundException,db.connect,self.path)

if __name__ == '__main__' :
    unittest.main()
