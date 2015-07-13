#######################################################################################################
#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to handle sql statements used to get correct video details for a viewer viewing their orders
#or a player editing a video
#######################################################################################################

import sys, session, cgi, MySQLdb, redirect, sql_handler as sql, html_template as html, viewer_order_html as form

#######################################################################################################

#Get session and cgi params

sess = session.Session(expires=20*60, cookie_path='/')
loggedIn = sess.data.get('loggedIn')
params = cgi.FieldStorage()

#######################################################################################################

def main():
    if not html.check_logged_in(loggedIn):
        return
    video_id = get_vid_id(params)
    
    html.open_html(sess.cookie, loggedIn)
    print_body(video_id, params)
    html.close_html()
    
    sess.close()
    return

#######################################################################################################

#Get the video ID from cgi params

def get_vid_id(params):
    if params.has_key('vidid'):
        return params['vidid'].value
    else:
        return -10
    return

#######################################################################################################

#Hnadle sql and printing of the body of the HTML

def print_body(video_id, params):
    print "<div>"
    viewer_type = 'C'
    if loggedIn == 1:
        viewer_type = sql.run_sql("""SELECT ViewerType FROM Viewer WHERE Viewer.ViewerID = (SELECT ViewerLogin.ViewerID FROM ViewerLogin WHERE ViewerLogin.UserName = "%s")"""%(sess.data.get('userName')))[0][0]
    paying = False
    if viewer_type == 'N':
        paying = True
    if video_id == -10:
        results = sql.run_sql("""SELECT Video.Name, InstanceRun.Name, Game.Name, Video.VideoType, Player.FirstName, Player.LastName, Video.Price, ViewerOrder.ViewedStatus, Video.URL, ViewerOrder.ViewerOrderID, ViewerOrder.ViewDate
                                     FROM Video,ViewerOrderLine, InstanceRun, Game, Player,ViewerOrder
                                     WHERE ViewerOrderLine.ViewerOrderID IN (SELECT ViewerOrder.ViewerOrderID FROM ViewerOrder WHERE ViewerOrder.ViewerID =
                                        (SELECT ViewerID FROM ViewerLogin WHERE ViewerLogin.UserName = '%s'))
                                     AND Video.VideoID = ViewerOrderLine.VideoID
                                     And Game.GameID = Video.GameID
                                     And InstanceRun.InstanceRunID = Video.InstanceRunID
                                     AND Player.PlayerID = InstanceRun.SupervisorID
                                     AND ViewerOrder.ViewerOrderID = ViewerOrderLine.ViewerOrderID"""%(sess.data.get('userName')))
        if params.has_key('error'):
            error = True
        else:
            error = False
        form.show_all_orders(results, paying, error)
    else:
        result = sql.run_sql("""
            SELECT Video.Name, InstanceRun.Name, Game.Name, Video.VideoType, Player.FirstName, Player.LastName, Video.Price, Video.VideoID, Video.URL, Player.PlayerID
            FROM Video, Game, InstanceRun, Player
            WHERE Video.VideoID = "%s"
            AND  Game.GameID = Video.GameID
            AND InstanceRun.InstanceRunID = Video.InstanceRunID
            AND Player.PlayerID = InstanceRun.SupervisorID
            """% video_id)
        if loggedIn == 1:
            form.confirm_order(result[0], paying)
        elif loggedIn == 2:
            form.edit_video(result[0])
    print "</div>"
    return

#######################################################################################################

main()
