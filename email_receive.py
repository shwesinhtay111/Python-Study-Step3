import imaplib
M = imaplib.IMAP4_SSL('imap.gmail.com')
import getpass
# aojzmunwarmlcmha
# workuse777@gmail.com
user = input("Enter your email: ")
password = getpass.getpass("Enter your password: ")
M.login(user,password)
M.list()
# Connect to your inbox
M.select("inbox")