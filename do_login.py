# The libraries we'll need
import sys, cgi, session, redirect, MySQLdb, sql_handler as sql

#######################################################################################################

sess = session.Session(expires=20*60, cookie_path='/')
form = cgi.FieldStorage()

#######################################################################################################

def main():
    print "%s\nContent-Type: text/html\n" % (sess.cookie)
    if sess.data.get('loggedIn') not in (1, 2):
        if not do_login():
            where_to_next = redirect.getQualifiedURL("renew_subscription.py")
        else:
            where_to_next = redirect.getQualifiedURL("home.py") if sess.data['loggedIn'] in (1, 2) else redirect.getQualifiedURL("login.py?error=1")
    sess.close()
    do_redirect(where_to_next)
    return

#######################################################################################################

def do_login():
    if not (form.has_key('username') and form.has_key('password')):
        sess.data['loggedIn'] = -1
    else:
        if form['loginType'].value == 'V':
            if not viewer_login():
                return False
        elif form['loginType'].value == 'P':
            player_login()
        else:
            sess.data['loggedIn'] = -1
    return True

#######################################################################################################

def viewer_login():
    result = sql.run_sql(""" SELECT * FROM ViewerLogin
        WHERE UserName = "%s"
        AND UserPwd = "%s"
        """ %(form['username'].value, form['password'].value))
    if result:
        sess.data['loggedIn'] = 1
        sess.data['userName'] = result[0][0]
    else:
        sess.data['loggedIn'] = -1
    renew = sql.run_sql("""SELECT RenewalDATE FROM PremiumViewer
                            WHERE ViewerID = (SELECT ViewerID FROM Viewer
                                                WHERE ViewerID = (SELECT ViewerID FROM ViewerLogin
                                                                    WHERE UserName = "%s"
                                                                    AND UserPwd = "%s"))""" %(form['username'].value, form['password'].value))
    if renew:
        check_renew = sql.run_sql("""SELECT RenewalDATE FROM PremiumViewer
                                      WHERE ViewerID = (SELECT ViewerID FROM Viewer
                                                            WHERE ViewerID = (SELECT ViewerID FROM ViewerLogin
                                                                                WHERE UserName = "%s"
                                                                                AND UserPwd = "%s"))
                                      AND RenewalDate < CURDATE()""" %(form['username'].value, form['password'].value))
        if check_renew:
            return False
    return True

#######################################################################################################        
        
def player_login():
    result = sql.run_sql("""
        SELECT * FROM PlayerLogin
        WHERE UserName = "%s"
        AND UserPwd = "%s"
        """%(form['username'].value, form['password'].value))
    if result:
        sess.data['loggedIn'] = 2
        sess.data['userName'] = result[0][0]
    else:
        sess.data['loggedIn'] = -1
    return

#######################################################################################################

def do_redirect(where_to_next):
    print """\
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <meta http-equiv="refresh" content="0;url=%s">
    </head>
    <body>
    </body>
    """ % where_to_next
    return

#######################################################################################################

main()

