#######################################################################################################

#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to generate edit achievement view for editting of instancerun, uses player_view_instanceruns_html as template

#######################################################################################################

import sys, session, cgi, MySQLdb, redirect, html_template as html, sql_handler as sql, player_view_instanceruns_html as body

#######################################################################################################

#Get Session from cookie and fieldstorage that has been passed on from previous page
sess = session.Session(expires=20*60, cookie_path='/')
loggedIn = sess.data.get('loggedIn')

#######################################################################################################

def main():
    if not html.check_player(loggedIn):
        return
    html.open_html(sess.cookie, loggedIn)
    #Get data through params and SQL
    instance_runs = sql.run_sql("""SELECT IR.InstanceRunID, IR.Name, IR.RecordedTime, IR.CategoryName, P.GameHandle
                                   FROM InstanceRun as IR, Player as P
                                       WHERE P.PlayerID = IR.SupervisorID""")
    body.print_instances("Instance Runs", ("Name", "Time", "Category Name", "Supervisor Handle"), instance_runs, loggedIn)
    html.close_html()
    return

#######################################################################################################

main()
