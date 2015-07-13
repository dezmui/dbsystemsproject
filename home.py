#######################################################################################################

#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to generate main page

#######################################################################################################

# The libraries we'll need
import sys, session, cgi, MySQLdb, redirect, sql_handler as sql, html_template as html

#######################################################################################################

def main():
    load_page()
    return

#######################################################################################################

def load_page():
    #Get Session from cookie and fieldstorage that has been passed on from previous page
    sess = session.Session(expires=20*60, cookie_path='/')
    username = sess.data.get('userName')
    loggedIn = sess.data.get('loggedIn')
    #Oepn html using session
    html.open_html(sess.cookie, loggedIn)
    #Is logged in as Viewer
    if loggedIn == 1:
        #get viewer type of the current user
        viewer_type = sql.run_sql(
        """SELECT ViewerType FROM Viewer
           WHERE Viewer.ViewerID = (SELECT ViewerLogin.ViewerID FROM ViewerLogin
                                    WHERE ViewerLogin.UserName = "%s")"""%(username))[0][0]
        if viewer_type == 'C':
            name = sql.run_sql("""SELECT FirstName, LastName FROM CrowdFundingViewer
                                  WHERE CrowdFundingViewer.ViewerID = (SELECT ViewerLogin.ViewerID FROM ViewerLogin
                                                              WHERE ViewerLogin.UserName = "%s")"""%(sess.data.get('userName')))[0]
            
            html.print_welcome(name[0], name[1])
    
    
    if loggedIn in (1, 2):
        videos = sql.run_sql("""SELECT VideoID, Video.Name, Game.Name, VideoType, InstanceRun.Name, Player.GameHandle, Player.PlayerID, Equipment.ModelAndMake, Equipment.EquipmentID FROM Video, Game, InstanceRun, Player, Equipment
                                 WHERE Video.InstanceRunID = InstanceRun.InstanceRunID
                                 AND Video.GameID = Game.GameID
                                 AND InstanceRun.SupervisorID = Player.PlayerID
                                 AND Player.PlayerID = (SELECT Venue.SupervisorID FROM Venue
                                                         WHERE Venue.VenueID = (SELECT VenueEquipment.VenueID FROM VenueEquipment
                                                                                 WHERE VenueEquipment.EquipmentID = Equipment.EquipmentID))
                                 ORDER BY VideoID""")
    else:
        videos = sql.run_sql("""SELECT VideoID, Video.Name, Game.Name, VideoType, InstanceRun.Name, Player.GameHandle, Player.PlayerID, Equipment.ModelAndMake, Equipment.EquipmentID FROM Video, Game, InstanceRun, Player, Equipment
                                 WHERE Video.InstanceRunID = InstanceRun.InstanceRunID
                                 AND Video.GameID = Game.GameID
                                 AND InstanceRun.SupervisorID = Player.PlayerID
                                 AND Player.PlayerID = (SELECT Venue.SupervisorID FROM Venue
                                                         WHERE Venue.VenueID = (SELECT VenueEquipment.VenueID FROM VenueEquipment
                                                                                 WHERE VenueEquipment.EquipmentID = Equipment.EquipmentID))
                                 AND Video.VideoType = 'Free'
                                 ORDER BY VideoID""")
    
    html.print_videos("Videos", ("Name", "Game", "Type", "Instance", "Supervisor", "Equipment"), videos, loggedIn)
    
    html.close_html()

    sess.close()
    return

#######################################################################################################

main()
