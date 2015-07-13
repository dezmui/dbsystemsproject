#######################################################################################################

#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File to handle editting of viewer player using player

#######################################################################################################

import cgi, sql_handler as sql, redirect, session, html_template as html

#######################################################################################################

#Get Session from cookie and fieldstorage that has been passed on from previous page
sess = session.Session(expires=20*60, cookie_path='/')
loggedIn = sess.data.get('loggedIn')
params = cgi.FieldStorage()

#######################################################################################################

viewerID = params['viewerID'].value
result= sql.run_sql("""SELECT UserName FROM ViewerLogin WHERE ViewerLogin.ViewerID = %s"""%viewerID)
if result:
    username = result[0][0]
    if html.check_logged_in(loggedIn):
        redirect.refresh("viewer_edit_profile.py?userName=%s"%(username), sess.cookie)
else:
    redirect.refresh("player_find_viewer.py?notFound=1", sess.cookie)     
