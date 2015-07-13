#######################################################################################################

#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to generate edit instancerun view for editting of instancerun, uses player_edit_instancerun_html as template

#######################################################################################################

import sys, session, cgi, MySQLdb, redirect, html_template as html, sql_handler as sql, player_edit_instancerun_html as body

def main():
    
    #Get Session from cookie and fieldstorage that has been passed on from previous page
    sess = session.Session(expires=20*60, cookie_path='/')
    username = sess.data.get('userName')
    loggedIn = sess.data.get('loggedIn')
    params= cgi.FieldStorage()
    
    if not html.check_player(loggedIn):
        return
    #Get data through params and SQL
    instanceRunID = params['instancerunID'].value
    
    IR = sql.run_sql("""SELECT InstanceRun.InstanceRunID, InstanceRun.Name, InstanceRun.SupervisorId, InstanceRun.CategoryName FROM InstanceRun
                        WHERE InstanceRun.InstanceRunID = %s"""%instanceRunID)[0]
    
    html.open_html(sess.cookie, loggedIn)
    if IR:
        body.edit_instancerun(IR)
    html.close_html()
    return

main()
