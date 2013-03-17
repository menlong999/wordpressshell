import locale
import os
import pprint
import shlex
import sys

from dropbox import client, rest, session

# XXX Fill in your consumer key and secret below
# You can find these at http://www.dropbox.com/developers/apps
APP_KEY = '0593ug5drsitw6i'
APP_SECRET = '9g0whydpxcoxlr3'
ACCESS_TYPE = 'app_folder'  # should be 'dropbox' or 'app_folder' as configured for your app

TOKEN_FILE = "/root/token_store.txt"


def main():

	if len(sys.argv) < 3:
	    exit("Usage: python put_to_dropbox.py from_path to_path")

	

	from_path = sys.argv[1]
	to_path = sys.argv[2]

        sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)

	try:
		stored_creds = open(TOKEN_FILE).read()
		sess.set_token(*stored_creds.split(','))
		print "[loaded access token]"
	except IOError:
		exit("please run login_dropbox.py to login and obtain access token.")

	from_file = open(os.path.expanduser(from_path), "rb")
	cli = client.DropboxClient(sess)
	response = cli.put_file("/" + to_path, from_file)
	print "uploaded: ", response
	from_file.close()

if __name__ == '__main__':
        main()

