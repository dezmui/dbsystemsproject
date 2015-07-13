#######################################################################################################

#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to generate view for achievements, uses player_view_achievements_html as template

#######################################################################################################

import sys, session, cgi, MySQLdb, redirect, html_template as html, sql_handler as sql, player_view_achievements_html as body

#######################################################################################################

#Get Session from cookie and fieldstorage that has been passed on from previous page
sess = session.Session(expires=20*60, cookie_path='/')
loggedIn = sess.data.get('loggedIn')

#######################################################################################################

def main():
    if not html.check_player(loggedIn):
        return
    html.open_html(sess.cookie, loggedIn)
    #Get data through SQL
    achievements = sql.run_sql("""SELECT Achievement.AchievementID, Achievement.Name, Achievement.InstanceRunID, Achievement.WhenAchieved, Achievement.RewardBody
                                   FROM Achievement""")
    body.print_achievements("Achievements", ("Name", "Instance Run ID", "When Achieved", "Reward Body"), achievements, loggedIn)
    html.close_html()
    return

#######################################################################################################

main()