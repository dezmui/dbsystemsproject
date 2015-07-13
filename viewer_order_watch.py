#######################################################################################################
#Authros: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song
#INFO20003 assessment
#File used to change an order status from pending to viewed
#######################################################################################################

import sys, session, cgi, MySQLdb, redirect, sql_handler as sql, html_template as html

#Get Session from cookie and fieldstorage that has been passed on from previous page
sess = session.Session(expires=20*60, cookie_path='/')
username = sess.data.get('userName')
loggedIn = sess.data.get('loggedIn')
params = cgi.FieldStorage()
orderID = params['orderID'].value

#######################################################################################################

#Login check, sql to change viewed status to viewed
def update_order():
    if not html.check_logged_in(loggedIn):
        return
    viewedStatus = sql.run_sql("""SELECT ViewedStatus FROM ViewerOrder
                               WHERE ViewerOrderID = '%s'"""%orderID)[0][0]
    if viewedStatus == "Pending":
        sql.run_update("""UPDATE ViewerOrder
                       SET ViewDate = CURDATE(), ViewedStatus = 'Viewed'
                       WHERE ViewerOrderID = '%s'"""%orderID)
    url = sql.run_sql("""SELECT Video.URL FROM Video
                        WHERE VideoID = (SELECT VideoID FROM ViewerOrderLine
                                            WHERE ViewerOrderID = '%s');"""%orderID)[0][0]
    
    redirect.goto(url,sess.cookie)
    return

#######################################################################################################

update_order()
