#######################################################################################################

#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to edit given game using given input
#Also deletion

#######################################################################################################

# The libraries we'll need
import sys, session, cgi, MySQLdb, redirect, sql_handler as sql, html_template as html

#######################################################################################################

#Get Session from cookie and fieldstorage that has been passed on from previous page
sess = session.Session(expires=20*60, cookie_path='/')
loggedIn = sess.data.get('loggedIn')
params= cgi.FieldStorage()
error = False

#######################################################################################################

#edit only if run ends up being true
run = True
#Check if user is loggedIn with authority and does not have deletion flag set up
if not html.check_logged_in(loggedIn):
    run = False
if params.has_key('delete'):
    run = False
#If run is still set to true, get all the information from CGI fieldstorage
if run:
    gameID = params['gameID'].value
    gameName = params['gameName'].value
    gameGenre = params['genre'].value
    gameReview = params['review'].value
    gameRate = params['starRating'].value
    gameCRate = params['classificationRating'].value
    gamePlatform = params['platformNotes'].value
    gameLink = params['promotionLink'].value
    gamePrice = params['price'].value.strip('$')

#######################################################################################################

def main():
    #Run delete if deletion flag is set
    if loggedIn == 2 and params.has_key('delete'):
        gameID = params['gameID'].value
        delete_game(gameID)
        #redirect to view achievement page
        redirect.refresh("player_manage_games.py",sess.cookie)
        return
    #Else, update information
    price = process_price(gamePrice)
    error = check_price(price)
    if error:
        redirect.refresh("player_manage_games.py?error=1", sess.cookie)
        return
    updateGameInfo(price)
    #redirect to edit page of the achievement that just got editted
    redirect.refresh("player_manage_games.py", sess.cookie)
    return

#######################################################################################################

def delete_game(gameID):
    videoID = sql.run_sql("""SELECT VideoID FROM Video WHERE GameID = %s"""%gameID)
    if videoID:
        delete_video(videoID[0][0])
    sql.run_remove(("""DELETE FROM Game WHERE GameID = "%s" """%gameID))
    return

#######################################################################################################
#Remove from database              
def delete_video(videoID):
    #Get all the viewerOrders for the video
    viewerOrders = sql.run_sql(("""SELECT ViewerOrderID FROM ViewerOrderLine WHERE VideoID = "%s" """
                               % (videoID)))
    
    sql.run_remove(("""DELETE FROM ViewerOrderLine WHERE VideoID = "%s"
                    """ % (videoID)))
    for i in viewerOrders:
        sql.run_remove(("""DELETE FROM ViewerOrder
            WHERE ViewerOrderID = "%s"
            """ % (i[0])))   
    #Remove Achievement    
    sql.run_remove(("""DELETE FROM Achievement
                    WHERE InstanceRunID = (SELECT InstanceRunID FROM Video WHERE VideoID = "%s")
                    """ % (videoID)))
    #Remove Video
    sql.run_remove(("""DELETE FROM Video WHERE VideoID = "%s"
                    """ % (videoID)))
    #Remove InstanceRunID
    sql.run_remove(("""DELETE FROM InstanceRun WHERE InstanceRunID = (SELECT InstanceRunID FROM Video WHERE VideoID = "%s")
                    """ % (videoID)))
    return

#######################################################################################################

#Update database using given info    
def updateGameInfo(price):
    sql.run_update(("""UPDATE Game
                   SET Genre = "%s", Review = "%s", StarRating = "%s", ClassificationRating = "%s", PlatformNotes= "%s", PromotionLink = "%s", Cost = "%s"
                   WHERE Game.gameID = "%s" 
                   """ % (gameGenre, gameReview, gameRate, gameCRate, gamePlatform, gameLink, price, gameID)))
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

main()
