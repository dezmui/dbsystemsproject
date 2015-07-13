#######################################################################################################

#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to generate add video view for insertion of new video to database, uses add_video_html as template

#######################################################################################################

import sys, session, cgi, MySQLdb, redirect, sql_handler as sql, html_template as html, add_video_html as form

#######################################################################################################

#Get Session from cookie and fieldstorage that has been passed on from previous page
sess = session.Session(expires=20*60, cookie_path='/')
loggedIn = sess.data.get('loggedIn')
params = cgi.FieldStorage()

#######################################################################################################
#Create view
def main():
    html.open_html(sess.cookie, loggedIn)
    error = False
    #Print error if any
    if params.has_key('error'):
        error = True
    form.print_details(error)

    html.close_html()
    sess.close()
    return

#######################################################################################################

main()