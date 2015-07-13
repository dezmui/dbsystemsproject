#######################################################################################################
#Authros: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song
#INFO20003 assessment
#File used to handle sql statements when confirming an order
#######################################################################################################

import sys, session, cgi, MySQLdb, redirect, sql_handler as sql, html_template as html

sess = session.Session(expires=20*60, cookie_path='/')
username = sess.data.get('userName')
loggedIn = sess.data.get('loggedIn')
params = cgi.FieldStorage()
vidid = params['vidid'].value

#######################################################################################################

def confirm_order():
    if not html.check_logged_in(loggedIn):
        return
    viewerID = sql.run_sql("""SELECT ViewerID FROM ViewerLogin
                               WHERE UserName = '%s'"""%username)[0][0]
    videoids = sql.run_sql("""SELECT VideoID FROM ViewerOrderLine
                               WHERE ViewerOrderID IN (SELECT ViewerOrderID FROM ViewerOrder
                                                           WHERE ViewerID = %d)"""%viewerID)

    for item in videoids:
        if int(vidid) in item:
            redirect.refresh("viewer_order.py?error=1", sess.cookie)
            return
    

    viewerorderID = sql.run_insert("""INSERT INTO ViewerOrder VALUES
                                           (DEFAULT, CURDATE(), NULL, 'Pending', %d)"""%viewerID)
    viewerType = sql.run_sql("""SELECT ViewerType FROM Viewer
                                     WHERE ViewerID = %d"""%viewerID)[0][0]
    if viewerType == 'C':
        viewerType = 1
    else:
        viewerType = 0
    sql.run_insert("""INSERT INTO ViewerOrderLine VALUES
                       (%s, %s, %s)"""%(vidid, viewerorderID, str(bool(viewerType)).upper()))
    redirect.refresh("viewer_order.py", sess.cookie)

    return

#######################################################################################################

confirm_order()