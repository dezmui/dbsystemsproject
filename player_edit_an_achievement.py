#######################################################################################################

#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to generate edit achievement view for editting of achievement, uses player_edit_an_achievement_html as template

#######################################################################################################

import sys, session, cgi, MySQLdb, redirect, sql_handler as sql, html_template as html, player_edit_an_achievement_html as body

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
    #Get data through params and SQL
    achievementID= params['achievementID'].value
    achievement_data = sql.run_sql("""SELECT AchievementID, Name, InstanceRunID, WhenAchieved, RewardBody FROM Achievement WHERE AchievementID = %s"""%(achievementID))[0]
    body.print_achievement(achievement_data)
    html.close_html()
    return

main()