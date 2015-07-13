#######################################################################################################
#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to handle sql statements used to get correct player details
#######################################################################################################

# The libraries we'll need
import sys, session, cgi, MySQLdb, redirect, sql_handler as sql, html_template as html, view_player_details_html as form

sess = session.Session(expires=20*60, cookie_path='/')
loggedIn = sess.data.get('loggedIn')

#######################################################################################################

def main():
    params = cgi.FieldStorage()
    playerID = params['playerID'].value
    
    html.open_html(sess.cookie, loggedIn)
    
    print_body(playerID, params)
    html.close_html()
    sess.close()
    return

#######################################################################################################

#Print html body for player details

def print_body(playerID, paramsw):
    print "<div>"
    result = sql.run_sql("""SELECT * FROM Player
                             WHERE PlayerID = %d"""%(int(playerID)))[0]
    form.view_details(result, loggedIn)
    print "</div>"
    return

#######################################################################################################

main()
