import unittest
from exploit import create_malicious_payload
from utils.helpers import create_rop_chain, create_reverse_shell

class TestExploit(unittest.TestCase):
    def test_create_malicious_payload(self):
        payload = create_malicious_payload('127.0.0.1', 4444)
        self.assertTrue(len(payload) > 1000)  # Пример простого теста
    
    def test_create_rop_chain(self):
        rop_chain = create_rop_chain()
        self.assertTrue(len(rop_chain) > 0)  # Проверяем, что ROP цепочка не пустая
    
    def test_create_reverse_shell(self):
        reverse_shell = create_reverse_shell('127.0.0.1', 4444)
        self.assertTrue(len(reverse_shell) > 0)  # Проверяем, что полезная нагрузка не пустая

if __name__ == '__main__':
    unittest.main()