# The libraries we'll need
import sys, cgi, session, redirect

# ---------------------------------------------------------------------------------------------------------------------
sess = session.Session(expires=20*60, cookie_path='/')
alreadyLoggedOut = not sess.data.get('loggedIn')

#######################################################################################################

if not alreadyLoggedOut:
    sess.data['loggedIn'] = 0 # log them out
    sess.data['userName'] = "None"
    sess.set_expires('') # expire session
    sess.close()

#######################################################################################################

# send session cookie
print "%s\nContent-Type: text/html\n" % (sess.cookie)

#######################################################################################################

# redirect to home page
print """\
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<meta http-equiv="refresh" content="0;url=%s">
</head>
<body>
</body>
""" % redirect.getQualifiedURL("home.py")

#######################################################################################################

