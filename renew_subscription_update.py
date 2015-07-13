#######################################################################################################
#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to handle sql statements to update the renewal date of the premium subscription for a viewer
#######################################################################################################

# The libraries we'll need
import sys, session, cgi, MySQLdb, redirect, sql_handler as sql, html_template as html

#######################################################################################################

sess = session.Session(expires=20*60, cookie_path='/')
loggedIn = sess.data.get('loggedIn')
params= cgi.FieldStorage()

#######################################################################################################

#Check if viewerID is in the params in the URL

if params.has_key('viewerID'):
    viewerID = params['viewerID'].value
else:
    viewerID = False
#Check if cancel is in the params in the URL to cancel subscription
    
if params.has_key('cancel'):
    cancel = True
else:
    cancel = False
    
#######################################################################################################

def main():
    if cancel:
        cancelSubscription()
    else:
        renewSubscription()
    redirect.refresh("login.py", sess.cookie)
    return

#######################################################################################################

#Renew subscription, update RenewalDATE to the next month

def renewSubscription():
    sql.run_update("""UPDATE PremiumViewer
                       SET RenewalDATE = CURDATE() + INTERVAL 1 MONTH
                       WHERE ViewerID = "%s"
                   """%viewerID)
    return

#######################################################################################################

#Cancel the subscription, change ViewerType to normal and delete PremiumViewer of viewer

def cancelSubscription():
    sql.run_update("""UPDATE Viewer
                       SET ViewerType = "N"
                       WHERE ViewerID = "%s"
                   """%(viewerID))
    sql.run_remove("""DELETE FROM PremiumViewer WHERE ViewerID = "%s"
                   """%(viewerID))
    return

#######################################################################################################

main()