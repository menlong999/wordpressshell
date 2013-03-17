import cmd
import locale
import os
import pprint
import shlex

from dropbox import client, rest, session

# XXX Fill in your consumer key and secret below
# You can find these at http://www.dropbox.com/developers/apps
APP_KEY = '0593ug5drsitw6i'
APP_SECRET = '9g0whydpxcoxlr3'
ACCESS_TYPE = 'app_folder'  # should be 'dropbox' or 'app_folder' as configured for your app

TOKEN_FILE = "/root/token_store.txt"


def main():
	sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)
	request_token = sess.obtain_request_token()
	url = sess.build_authorize_url(request_token)
	print "authorize url: ", url
	print "Please authorize in the browser. After you're done, press enter."
	raw_input()
	
	access_token = sess.obtain_access_token(request_token)
	f = open(TOKEN_FILE, 'w')
	f.write(",".join([access_token.key, access_token.secret]))
	f.close()
	
	print "access token wrote into ", TOKEN_FILE

if __name__ == '__main__':
	main()

