#######################################################################################################

#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to edit given achievement using given input
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


#######################################################################################################
#edit only if run ends up being true
run = True
#Check if user is loggedIn with authority and does not have deletion flag set up
if not html.check_player(loggedIn):
    run = False
if params.has_key('delete'):
    run = False
#If run is still set to true, get all the information from CGI fieldstorage
if run:
    achievementID= params['achievementID'].value
    achievementName= params['achievementName'].value
    instancerunID= params['instancerunID'].value
    whenAchieved= params['whenAchieved'].value
    rewardBody= params['rewardBody'].value

#######################################################################################################

def main():
    #Run delete if deletion flag is set
    if loggedIn == 2 and params.has_key('delete'):
        achievementid= params["achievementID"].value
        remove_achievement(achievementid)
        #redirect to view achievement page
        redirect.refresh("player_view_achievements.py",sess.cookie)
        return
    #Else, update information
    updateAchievementInfo()
    #redirect to edit page of the achievement that just got editted
    redirect.refresh("player_edit_an_achievement.py?achievementID=%s"%achievementID, sess.cookie)
    return

#######################################################################################################

#Remove from database
def remove_achievement(achievementID):                        
    
    #Firstly, get videoIDs
    videoID = sql.run_sql(("""SElECT VideoID FROM Video
                               WHERE InstanceRunID = (SELECT InstanceRunID From Achievement WHERE AchievementID = "%s")
                           """ %(achievementID)))
    #If video exist for this achievement
    if videoID:
        videoID = videoID[0][0]
        #Get all the viewerOrders for the video
        viewerOrders = sql.run_sql(("""SELECT ViewerOrderID FROM ViewerOrderLine WHERE VideoID = "%s" """% (videoID)))
        #Remove all ViewerOrderLine data with the VideoID
        sql.run_remove(("""DELETE FROM ViewerOrderLine WHERE VideoID = "%s"
                        """ % (videoID)))
        #Remove all ViewerOrders
        for i in viewerOrders:
            sql.run_remove(("""DELETE FROM ViewerOrder 
                WHERE ViewerOrderID = "%s"
                """ % (i[0])))   
        #finall,y remove Video
        sql.run_remove(("""DELETE FROM Video WHERE VideoID = "%s"
                        """ % (videoID)))
    #Remove Achievement    
    sql.run_remove(("""DELETE FROM Achievement 
                    WHERE AchievementID = "%s"
                    """ % (achievementID)))
    #Remove InstanceRun to keep the logic we have decided
    sql.run_remove(("""DELETE FROM InstanceRun WHERE InstanceRunID = (SELECT InstanceRunID FROM Achievement WHERE AchievementID = "%s")
                    """ % (achievementID))) 
    return

#######################################################################################################

#Update database using given info    
def updateAchievementInfo():
    #Get date for new instanceRun
    date = sql.run_sql(("""SELECT RecordedTime FROM InstanceRun WHERE InstanceRunID = "%s" """ %(instancerunID)))[0][0]
    sql.run_update(("""UPDATE Achievement
                   SET InstanceRunID= "%s", WhenAchieved= "%s", Name= "%s", RewardBody = "%s"
                   WHERE AchievementID= "%s" 
                   """ % (instancerunID, date,achievementName,rewardBody,achievementID)))
    return

#######################################################################################################






main()