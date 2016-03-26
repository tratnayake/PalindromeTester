import unittest
import palindromes
class palindrome_tests(unittest.TestCase):

    #Test that this method returns True only for even numbers.
    def test_is_even(self):
        self.assertEqual(palindromes.is_even(2), True)
        self.assertEqual(palindromes.is_even(3), False)

    def test_validate(self):
        self.assertEqual(palindromes.validate(1234),True)
        self.assertEqual(palindromes.validate("324235cd"),False)

    #Test that chunk splits up into chunks properly.
    def test_chunk(self):
        self.assertEqual(palindromes.chunk(1001), {'left':'10', 'right':'01'})
        self.assertEqual(palindromes.chunk(12321), {'left':'12', 'right':'21'})
        self.assertEqual(palindromes.chunk(123456), {'left':'123', 'right':'456'})
        self.assertEqual(palindromes.chunk(12231), {'left':'12', 'right':'31'})

    #Test that the method actually checks the two strings properly.
    def test_check(self):
        self.assertEqual(palindromes.check('12','21'), True)
        self.assertEqual(palindromes.check('12','31'), False)
        self.assertEqual(palindromes.check('123456','654321'), True)
        self.assertEqual(palindromes.check('1010110101','10124124'), False)

    
    #Test that the parent method works and returns True for palindromes.
    def test_is_palindrome(self):
        self.assertEqual(palindromes.is_palindrome(12321), True);
        self.assertEqual(palindromes.is_palindrome(12345678987654321), True);
        self.assertEqual(palindromes.is_palindrome(12332), False);
        self.assertEqual(palindromes.is_palindrome(100101), False);

    #Test that the method actually finds the next palindrome.
    def test_next_palindrome(self):
        self.assertEqual(palindromes.next_palindrome(100), 101)
        self.assertEqual(palindromes.next_palindrome(1229), 1331)


if __name__ == '__main__':
    unittest.main()