#######################################################################################################

#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to edit given video using given input
#Also deletion

#######################################################################################################

# The libraries we'll need
import sys, session, cgi, MySQLdb, redirect, sql_handler as sql, html_template as html, calendar

#######################################################################################################

#Get Session from cookie and fieldstorage that has been passed on from previous page
sess = session.Session(expires=20*60, cookie_path='/')
loggedIn = sess.data.get('loggedIn')
params= cgi.FieldStorage()

#######################################################################################################

short_months = (3, 4, 9, 11)
long_months = (1, 5, 6, 7, 8, 10, 12)
error = False

#######################################################################################################

videoID = params['videoID'].value

if params.has_key('delete'):
    delete = True
else:
    delete = False
    videoName = params['videoName'].value
    videoType = params['videoType'].value
    supervisorID = params['supervisorID'].value
    URL = params['URL'].value
    videoPrice = params['price'].value.strip('$')

#######################################################################################################

def main():                   
    if delete:
        delete_video(videoID)
        redirect.refresh("home.py", sess.cookie)
        return
    price = process_price(videoPrice)
    error = check_price(price)
    error = check_supervisor(supervisorID)             
    if error:
        redirect.refresh("home.py?error=1", sess.cookie)
        return
    updateVideoInfo(price)
    redirect.refresh(("viewer_order.py?vidid=%s")%(videoID), sess.cookie)
    return

#######################################################################################################

def process_price(price):
    if price[0] == "0" and price[1] != ".":
        price = price[1:]
    return price

#######################################################################################################

def check_price(price):
    legal = "0123456789."
    countdot = 0
    for i in price:
        if i ==".":
            countdot+=1
            if countdot > 1:
                return True
        if i not in legal:
            return True
    return False

#######################################################################################################

def check_supervisor(id):
    existing_players = sql.run_sql("""SELECT DISTINCT(playerID) FROM Player""")
    for i in existing_players:
        if i == id:
            return True
    return False

#######################################################################################################
              
def delete_video(videoID):

    viewerOrders = sql.run_sql(("""SELECT ViewerOrderID FROM ViewerOrderLine WHERE VideoID = "%s" """
                               % (videoID)))
    
    sql.run_remove(("""DELETE FROM ViewerOrderLine WHERE VideoID = "%s"
                    """ % (videoID)))
    for i in viewerOrders:
        sql.run_remove(("""DELETE FROM ViewerOrder 
            WHERE ViewerOrderID = "%s"
            """ % (i[0])))   

    sql.run_remove(("""DELETE FROM Achievement 
                    WHERE InstanceRunID = (SELECT InstanceRunID FROM Video WHERE VideoID = "%s")
                    """ % (videoID)))
    sql.run_remove(("""DELETE FROM Video WHERE VideoID = "%s"
                    """ % (videoID))) 
    sql.run_remove(("""DELETE FROM InstanceRun WHERE InstanceRunID = (SELECT InstanceRunID FROM Video WHERE VideoID = "%s")
                    """ % (videoID))) 
    return

#######################################################################################################
                      
def updateVideoInfo(price):
    sql.run_update(("""UPDATE Video
                   SET Name = "%s", URL = "%s", Price = "%s", VideoType = "%s"
                   WHERE Video.VideoID = "%s" 
                   """ % (videoName, URL, price, videoType, videoID)))
    sql.run_update(("""UPDATE InstanceRun
                    SET SupervisorID = "%s"
                    WHERE InstanceRunID = (SELECT InstanceRunID FROM Video WHERE VideoID = "%s")
                    """ % (supervisorID, videoID)))
    return

#######################################################################################################

main()
