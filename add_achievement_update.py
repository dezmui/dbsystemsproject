#######################################################################################################

#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to add achievement into database given user input

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
        redirect.refresh("add_achievement.py?error=1", sess.cookie)
        return
    #Insertion successful, redirect to newly created achievement's edit page
    id = addAchievementInfo()
    redirect.refresh("player_edit_an_achievement.py?achievementID=%s "%(id), sess.cookie)
    return

#######################################################################################################
#Valide fieldstorage and make sure all required input are given by user
def validate_params():
    if not (params.has_key('AchievementName') and params.has_key('RewardBody')):
        return 2
    return

#######################################################################################################
#Run SQL insertion and get newly added achievement's ID
def addAchievementInfo():
    achievementID= sql.run_insert("""INSERT INTO Achievement VALUES
                                       (DEFAULT, NULL, NULL, '%s', '%s')
                               """%(name,reward))
    return achievementID
#Check for error
if validate_params() == 2:
    redirect.refresh("add_achievement.py?error=2", sess.cookie)
#Add new achievement given input
else:
    name= params['AchievementName'].value
    reward= params['RewardBody'].value
    error = 0
    
    main()