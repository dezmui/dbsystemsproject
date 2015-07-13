#######################################################################################################

#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to edit given instanceRun using given input
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
if not html.check_logged_in(loggedIn):
    run = False
if params.has_key('delete'):
    run = False
#If run is still set to true, get all the information from CGI fieldstorage
if run:
    instancerunID= params['instancerunID'].value
    instancerunName= params['instancerunName'].value
    categoryName= params['categoryName'].value
    supervisorID= params['supervisorID'].value

#######################################################################################################

def main():
     #Run delete if deletion flag is set
    if loggedIn == 2 and params.has_key('delete'):
        instanceRunID= params["instancerunID"].value
        remove_instance(instanceRunID)
        #redirect to view instanceRun page
        redirect.refresh("player_view_instanceruns.py",sess.cookie)
        return
    #Else, update information
    updateInstanceInfo()
    #redirect to edit page of the instanceRun that just got editted
    redirect.refresh("player_edit_instancerun.py?instancerunID=%s"%instancerunID, sess.cookie)
    return

#######################################################################################################

#Remove from database
def remove_instance(instanceRunID):      
    #Get related achievements    
    sql.run_update(("""UPDATE Achievement
                        SET InstanceRunID = NULL, WhenAchieved = NULL
                        WHERE InstanceRunID = "%s"
            """ % (instanceRunID)))
    #Get related Videos
    videoID = sql.run_sql(("""SELECT VideoID FROM Video WHERE InstanceRunID = "%s" """ % (instanceRunID)))
    if videoID:
        videoID = videoID[0][0]
        #Remove all viewerOrders for that video
        viewerOrders = sql.run_sql(("""SELECT ViewerOrderID FROM ViewerOrderLine WHERE VideoID = "%s" """% (videoID)))
        sql.run_remove(("""DELETE FROM ViewerOrderLine WHERE VideoID = "%s"
                        """ % (videoID)))
        for i in viewerOrders:
            sql.run_remove(("""DELETE FROM ViewerOrder 
                WHERE ViewerOrderID = "%s"
                """ % (i[0])))   
        #Delete Video
        sql.run_remove(("""DELETE FROM Video WHERE VideoID = "%s"
                        """ % (videoID))) 
    #Delete instaceRun
    sql.run_remove(("""DELETE FROM InstanceRun WHERE InstanceRunID= "%s"
                    """ % (instanceRunID)))                              
    return

#######################################################################################################

#Update database using given info        
def updateInstanceInfo():
    sql.run_update(("""UPDATE InstanceRun
                   SET Name = "%s", SupervisorID= "%s", CategoryName = "%s"
                   WHERE InstanceRunID= "%s" 
                   """ % (instancerunName, supervisorID,categoryName,instancerunID)))
    return

#######################################################################################################





main()