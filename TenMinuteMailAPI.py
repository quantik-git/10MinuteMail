import requests as rq


class Mails(object):
    """
    Mails is a interface for the https://10minutemail.com website that
    supplies single use mails.
    
    ...
    
    Attributes
    ----------
    cookies : str
        a string with all the cookies
    emailAddress : str
        supplied email address
        
    Methods
    -------
    getEmailAddress(self) : str
        Prints the animals name and what sound it makes
    getEmailCount(self) : int
        Counts the number of emails in the inbox
    getAllEmails(self) : list
        Gets all the emails in the inbox
    getSecondsLeft(self) : int
        Gets the remaining time in the email
    isExpired(self) : bool
        Verifies if the session has expired
    refreshTime(self) : bool
        Refreshes the duration of the email
    """
    

    def __init__(self):
        """Init method establishes a session and stores the email"""
    
        response = rq.get('https://10minutemail.com/session/address')
        
        self.cookies = response.headers['set-cookie']
        self.emailAddress = response.json().get('address')


    def getEmailAddress(self) -> str:
        return self.emailAddress


    def getEmailCount(self) -> int:
        """Counts the number of emails in the inbox
        
        Returns
        -------
        bool
            the number of emails in the inbox
        """
        
        response = rq.get(
            'https://10minutemail.com/messages/messageCount',
            headers = {'Cookie': self.cookies}
        )

        return response.json().get('messageCount')


    def getAllEmails(self) -> list:
        """Gets all the emails in the inbox
        
        Returns
        -------
        list
            a list of all emails in the inbox
        """
        
        emails = rq.get(
            'https://10minutemail.com/messages/messagesAfter/0',
            headers = {'Cookie': self.cookies}
        )

        return emails.json()
        

    def getSecondsLeft(self) -> int:
        """Gets the remaining time in the email
        
        Returns
        -------
        int
            the number of seconds until the email expires
        """
        
        response = rq.get(
            'https://10minutemail.com/session/secondsLeft',
            headers = {'Cookie': self.cookies}
        )

        return int(response.json().get('secondsLeft'))


    def isExpired(self) -> bool:
        """Verifies if the session has expired
        
        Returns
        -------
        bool
            True if the session has expired and False otherwise
        """
        
        response = rq.get(
            'https://10minutemail.com/session/expired',
            headers = {'Cookie': self.cookies}
        )

        return response.json().get('expired')


    def refreshTime(self) -> bool:
        """Refreshes the duration of the email
        
        Returns
        -------
        bool
            True if the refresh was successfull and False otherwise
        """
        
        response = rq.get(
            'https://10minutemail.com/session/reset',
            headers = {'Cookie': self.cookies}
        )

        return response.json().get('Response') == 'reset'
