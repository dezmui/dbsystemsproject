#######################################################################################################

#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File to display all game lists

#######################################################################################################

import sys, session, cgi, MySQLdb, redirect, sql_handler as sql, html_template as html, player_manage_games_html as body

#######################################################################################################

#Get Session from cookie and fieldstorage that has been passed on from previous page
sess = session.Session(expires=20*60, cookie_path='/')
username = sess.data.get('userName')
loggedIn = sess.data.get('loggedIn')
params = cgi.FieldStorage()

#######################################################################################################

def main():
    if not html.check_player(loggedIn):
        return
    html.open_html(sess.cookie, loggedIn)
    games = sql.run_sql("""SELECT GameID, Name, StarRating, ClassificationRating, Cost FROM Game""")
    body.print_games(games)
    html.close_html()
    return

#######################################################################################################


main()
