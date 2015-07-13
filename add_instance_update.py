#######################################################################################################

#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to add instanceRun into database given user input

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
        redirect.refresh("add_instance.py?error=1", sess.cookie)
        return
    #Insertion successful, redirect to newly created instanceRun's edit page
    id = addInstanceInfo()
    redirect.refresh("player_edit_instancerun.py?instancerunID=%s "%(id), sess.cookie)
    return

#######################################################################################################
#Valide fieldstorage and make sure all required input are given by user
def validate_params():
    if not (params.has_key('Name') and params.has_key('supervisorName')
        and params.has_key('Category')):
        return 2
    return

#######################################################################################################
#Run SQL insertion and get newly added instanceRun's ID
def addInstanceInfo():
    superID= sql.run_sql("""SELECT playerID FROM Player WHERE GameHandle = "%s" """ % (superName))[0][0]
    instancerunID= sql.run_insert("""INSERT INTO InstanceRun VALUES
                                       (DEFAULT, %s, '%s',NOW(), '%s')
                               """%(superID,name,category))
    return instancerunID
#Check for error
if validate_params() == 2:
    redirect.refresh("add_instance.py?error=2", sess.cookie)
#Add new instanceRun given input
else:
    superName= params['supervisorName'].value
    name= params['Name'].value
    category= params['Category'].value
    error = 0
    
    main()