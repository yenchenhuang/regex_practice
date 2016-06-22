import unittest
from getEmailByNonRegex import is_email, get_emails, get_accounts

class TestGetEmailByRegex(unittest.TestCase):
        def test_is_email1(self):
                self.assertEqual(is_email("abcd_aisu123@gmail.com"), True)

        def test_is_email2(self):
                self.assertEqual(is_email("ajkd au123@gmail.com cci aj"), False)
	
	def test_get_emails(self):
		paragraph = "ajskasjdkf asdfoig asdf1234@kkbox.com and 395ajkd0@gmail.com asdfpoig, asudig zxcvaj. Siif xjkc0234_49@demo.tw djjakzkxc, iiiie."
		expected = ["asdf1234@kkbox.com","395ajkd0@gmail.com", 
				"xjkc0234_49@demo.tw"]
		
		self.assertEqual(get_emails(paragraph), expected)
	def test_get_accounts(self):
		paragraph = "ajskasjdkf asdfoig asdf1234@kkbox.com and 395ajkd0@gmail.com asdfpoig, asudig zxcvaj. Siif xjkc0234_49@demo.tw djjakzkxc, iiiie."
		expected = ["asdf1234", "395ajkd0", "xjkc0234_49"]
		
		self.assertEqual(get_accounts(paragraph), expected)


if __name__ == '__main__':
	unittest.main()
