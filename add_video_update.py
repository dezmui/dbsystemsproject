#######################################################################################################

#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to add video into database given user input

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
        redirect.refresh("add_video.py?error=1", sess.cookie)
        return
    #Insertion successful, redirect to newly created video's edit page
    id = addVideoInfo()
    redirect.refresh("viewer_order.py?vidid=%s "%(id), sess.cookie)
    return

#######################################################################################################
#Valide fieldstorage and make sure all required input are given by user
def validate_params():
    if not (params.has_key('videoName') and params.has_key('gameName')
        and params.has_key('videoURL') and params.has_key('videoType')
        and params.has_key('videoPrice') and params.has_key('InstanceName')):
        return 2
    return

#######################################################################################################
#Run SQL insertion and get newly added video's ID
def addVideoInfo():
    gameID = sql.run_sql("""SELECT GameID FROM Game WHERE Name = "%s" """ % (GameName))[0][0]
    instancerunID = sql.run_sql("""SELECT InstanceRunID FROM InstanceRun WHERE Name = "%s" """ % (InstanceRunName))[0][0]

    videoID= sql.run_insert("""INSERT INTO Video VALUES
                                       (DEFAULT, '%s', '%s', '%s', '%s', '%s', '%s')
                               """%(videoName,videoURL,videoPrice,videoType,instancerunID,gameID))
    return videoID
#Check for error
if validate_params() == 2:
    redirect.refresh("home.py?error=2", sess.cookie)
#Add new video given input
else:
    videoName= params['videoName'].value
    videoURL= params['videoURL'].value
    videoType= params['videoType'].value
    videoPrice= params['videoPrice'].value
    InstanceRunName= params['InstanceName'].value
    GameName= params['gameName'].value
    error = 0
    
    main()