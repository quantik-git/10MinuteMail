import unittest
import TenMinuteMailAPI as api

class testTenMinuteMailAPI(unittest.TestCase):

    def setUp(self):
        self.session = api.Mails()

    def test_getEmailAddress(self):
        self.assertNotEqual(self.session.getEmailAddress(), '', 'email adress empty')

    def test_getEmailCount(self):
        self.assertEqual(self.session.getEmailCount(), 0, 'email count different from 0')

    def test_getAllEmails(self):
        self.assertEqual(self.session.getAllEmails(), [], 'email list not empty')

    def test_getSecondsLeft(self):
        self.assertEqual(self.session.getSecondsLeft(), 599, 'seconds left different from 599')

    def test_isExpired(self):
        self.assertFalse(self.session.isExpired(), 'session expired error')
	
    def test_refreshTime(self):
        self.assertTrue(self.session.refreshTime(), 'refreshTime returned false')
	

if __name__ == '__main__':
    unittest.main()
