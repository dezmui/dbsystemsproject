#######################################################################################################

#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to generate edit player profile view for editting of player profile, 
#uses player_edit_profile_html as template

#######################################################################################################

import sys, session, cgi, MySQLdb, redirect, sql_handler as sql, html_template as html, player_edit_profile_html as form

#######################################################################################################

#Get Session from cookie and fieldstorage that has been passed on from previous page

sess = session.Session(expires=20*60, cookie_path='/')
loggedIn = sess.data.get('loggedIn')
params = cgi.FieldStorage()

#######################################################################################################

def main():
    if not html.check_logged_in(loggedIn):
        return
    html.open_html(sess.cookie, loggedIn)
    error = False
    #Get data through params and SQL

    username = sess.data['userName']
    if (loggedIn != 2):
        redirect.refresh("home.py", sess.cookie)
        return
    if params.has_key('error'):
        error = True
    print_body(username, error)

    html.close_html()
    sess.close()
    return

#######################################################################################################

def print_body(username, error):

    result = sql.run_sql(("""SELECT * FROM Player WHERE PlayerID = (SELECT PlayerID FROM PlayerLogin WHERE userName = "%s")
                          """%(username)))

    if result[0][1] == None:
        supervisorName = "He is a BOSS"
    else:
        supervisorName = sql.run_sql(("""SELECT * FROM Player WHERE PlayerID = "%s"
                          """%(result[0][1])))

    resultAdd = sql.run_sql(("""SELECT * FROM Address 
                             WHERE AddressID = (SELECT AddressID FROM PlayerAddress 
                                                 WHERE PlayerID = (SELECT PlayerID FROM PlayerLogin WHERE userName = "%s")
                                                 AND EndDate is NULL)
                             """ % (username)))

    form.print_details(result[0], resultAdd[0],supervisorName, error, loggedIn)
    return

#######################################################################################################

main()
