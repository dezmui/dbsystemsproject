#######################################################################################################
#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to handle sql statements add a new viewer
#######################################################################################################

import sys, session, cgi, MySQLdb, redirect, sql_handler as sql, html_template as html, renew_subscription_html as form

sess = session.Session(expires=20*60, cookie_path='/')
loggedIn = sess.data.get('loggedIn')
username = sess.data.get('userName')

#######################################################################################################

def main():
    if not html.check_logged_in(loggedIn):
        return
    html.open_html(sess.cookie, loggedIn)
    
    print_body()
    html.close_html()
    sess.data['loggedIn'] = 0 # log them out
    sess.data['userName'] = "None"
    sess.set_expires('')
    sess.close()
    return

#######################################################################################################

#Sql queries for viewer ID and renewel date to show in body

def print_body():
    print "<div>"
    viewerID = sql.run_sql("""SELECT ViewerID FROM ViewerLogin
                             WHERE UserName = '%s'"""%username)[0][0]
    renewalDate = sql.run_sql("""SELECT RenewalDATE FROM PremiumViewer
                              WHERE ViewerID = %d"""%viewerID)[0][0]
    form.view_form(viewerID, renewalDate)
    print "</div>"
    return

#######################################################################################################

main()
