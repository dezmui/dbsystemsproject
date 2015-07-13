#######################################################################################################

#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to add game into database given user input

#######################################################################################################

# The libraries we'll need
import sys, session, cgi, MySQLdb, redirect, sql_handler as sql, html_template as html, calendar

#######################################################################################################

#Get Session from cookie and fieldstorage that has been passed on from previous page
sess = session.Session(expires=20*60, cookie_path='/')
params= cgi.FieldStorage()

#######################################################################################################

def main():
    #If error, redirect back to add page
    if error == 1:
        redirect.refresh("add_game.py?error=1", sess.cookie)
        return
    #Insertion successful, redirect to newly created game's edit page
    addGameInfo()
    redirect.refresh("player_manage_games.py", sess.cookie)
    return

#######################################################################################################
#Valide fieldstorage and make sure all required input are given by user
def validate_params():
    if not (params.has_key('gameName') and params.has_key('genre')
        and params.has_key('review') and params.has_key('starRating')
        and params.has_key('classificationRating') and params.has_key('platformNotes')
        and params.has_key('promotionLink') and params.has_key('price')):
        return 2
    return

#######################################################################################################
#Run SQL insertion and get newly added game's ID
def addGameInfo():
    addressID = sql.run_insert("""INSERT INTO Game VALUES
                                       (DEFAULT, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')
                               """%(gameName, genre, review, starRating, classificationRating, platformNotes, promotionLink, price))
    return
#Check for error
if validate_params() == 2:
    redirect.refresh("add_game.py?error=2", sess.cookie)
#Add new game given input
else:
    gameName = params['gameName'].value
    genre = params['genre'].value
    review = params['review'].value
    starRating = params['starRating'].value
    classificationRating = params['classificationRating'].value
    platformNotes = params['platformNotes'].value
    promotionLink = params['promotionLink'].value
    price = params['price'].value
    error = 0
    
    main()