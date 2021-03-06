import unittest
from dataclasses import dataclass
import sys
import os
sys.path.insert(0, os.getcwd())
from py2sql import py2sql


class TestSaveDeleteObject(unittest.TestCase):
    db_name = "test"
    db_config = py2sql.DBConnectionInfo(db_name, "localhost", "postgres", "postgres")

    def test_save_object_with_no_class_raises_exception(self):
        @dataclass
        class Bar:
            done: bool = True
        py2sql.Py2SQL.db_connect(self.db_config)
        b = Bar()
        with self.assertRaises(NotImplementedError):
            py2sql.Py2SQL.save_object(b)
        py2sql.Py2SQL.db_disconnect()
        py2sql.Py2SQL.db_connect(self.db_config)
        py2sql.Py2SQL.delete_class(Bar)
        self.assertEqual([],
            py2sql.Py2SQL.db_table_structure("bar")
        )
        py2sql.Py2SQL.db_disconnect()

    def test_save_class_and_object(self):
        py2sql.Py2SQL.db_connect(self.db_config)
        @dataclass
        class S:
            foo: str = 0
            bar: int = 1
        py2sql.Py2SQL.save_class(S)
        s = S("one", 1)
        py2sql.Py2SQL.save_object(s)
        py2sql.Py2SQL.db_disconnect()
        py2sql.Py2SQL.db_connect(self.db_config)
        py2sql.Py2SQL.delete_class(S)
        self.assertEqual([],
            py2sql.Py2SQL.db_table_structure("s")
        )
        py2sql.Py2SQL.db_disconnect()

    def test_save_and_delete(self):
        @dataclass
        class Bar():
            bar: int = 2
        b = Bar()
        db_con_info = py2sql.DBConnectionInfo("test", "localhost", "postgres", "postgres")
        py2sql.Py2SQL.db_connect(db_con_info)
        py2sql.Py2SQL.save_class(Bar)
        py2sql.Py2SQL.save_object(b)
        self.assertTrue("bar" in py2sql.Py2SQL.db_tables())
        py2sql.Py2SQL.delete_object(b)
        py2sql.Py2SQL.delete_class(Bar)
        self.assertTrue("bar" not in py2sql.Py2SQL.db_tables())
        py2sql.Py2SQL.db_disconnect()
