#######################################################################################################
#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to handle sql statements add a new viewer
#######################################################################################################

# The libraries we'll need
import sys, session, cgi, MySQLdb, redirect, sql_handler as sql, html_template as html, calendar

#######################################################################################################

sess = session.Session(expires=20*60, cookie_path='/')
params= cgi.FieldStorage()

short_months = (3, 4, 9, 11)
long_months = (1, 5, 6, 7, 8, 10, 12)


#######################################################################################################

def main():
    if error == 1:
        redirect.refresh("register_viewer.py?error=1", sess.cookie)
        return
    if checkAccount() == 3:
        redirect.refresh("register_viewer.py?error=3", sess.cookie)
        return
    if checkAccount() == 4:
        redirect.refresh("register_viewer.py?error=4", sess.cookie)
        return
    addViewerInfo()
    redirect.refresh("login.py", sess.cookie)
    return

#######################################################################################################

#Make sure all parameters were supplied

def validate_params():
    if not (params.has_key('username') and params.has_key('password1')
        and params.has_key('password2') and params.has_key('year')
        and params.has_key('month') and params.has_key('day')
        and params.has_key('email') and params.has_key('streetNo')
        and params.has_key('streetName') and params.has_key('streetType')
        and params.has_key('suburb') and params.has_key('city')
        and params.has_key('state') and params.has_key('postcode')
        and params.has_key('country')):
        error = 2
        return error
    return

#######################################################################################################

#Checks to make sure there are no username conflicts and that both passwords entered match

def checkAccount():
    usernames = sql.run_sql("""SELECT UserName FROM ViewerLogin
                                WHERE UserName = '%s'"""%viewerUserName)
    if usernames:
        error = 3
        return error
    if viewerPwd1 != viewerPwd2:
        error = 4
        return error
    return

#######################################################################################################

#Sql to insert viewer data

def addViewerInfo():
    if viewerSubscription:
        addressID = sql.run_insert("""INSERT INTO Address VALUES
                                       (DEFAULT, %d, '%s', '%s', '%s', '%s', '%s', '%s', '%s')"""%(int(viewerStNo), viewerStName,
                                                                                                   viewerStType, viewerSuburb,
                                                                                                   viewerCity, viewerState,
                                                                                                   viewerPCode, viewerCountry))
        viewerID = sql.run_insert("""INSERT INTO Viewer VALUES
                                      (DEFAULT, 'P', '%s-%s-%s', '%s')"""%(viewerDOBYear, viewerDOBMonth, viewerDOBDay, viewerEmail))
        sql.run_insert("""INSERT INTO ViewerLogin VALUES
                           ('%s', '%s', %d)"""%(viewerUserName, viewerPwd1, viewerID))
        sql.run_insert("""INSERT INTO ViewerAddress VALUES
                           (%d, %d, CURDATE(), NULL)"""%(viewerID, addressID))
        sql.run_insert("""INSERT INTO PremiumViewer VALUES
                           (%d, CURDATE() + INTERVAL 1 MONTH)"""%(viewerID))
    else:
        addressID = sql.run_insert("""INSERT INTO Address VALUES
                                       (DEFAULT, %d, '%s', '%s', '%s', '%s', '%s', '%s', '%s')"""%(int(viewerStNo), viewerStName,
                                                                                                   viewerStType, viewerSuburb,
                                                                                                   viewerCity, viewerState,
                                                                                                   viewerPCode, viewerCountry))
        viewerID = sql.run_insert("""INSERT INTO Viewer VALUES
                                      (DEFAULT, 'N', '%s-%s-%s', '%s')"""%(viewerDOBYear, viewerDOBMonth, viewerDOBDay, viewerEmail))
        sql.run_insert("""INSERT INTO ViewerLogin VALUES
                           ('%s', '%s', %d)"""%(viewerUserName, viewerPwd1, viewerID))
        sql.run_insert("""INSERT INTO ViewerAddress VALUES
                           (%d, %d, CURDATE(), NULL)"""%(viewerID, addressID))
    return

#######################################################################################################

#Only store paramater values if they have all been entered, check date is valid

if validate_params() == 2:
    redirect.refresh("register_viewer.py?error=2", sess.cookie)

else:
    viewerUserName = params['username'].value
    viewerPwd1 = params['password1'].value
    viewerPwd2 = params['password2'].value
    viewerDOBYear = params['year'].value
    viewerDOBMonth = params['month'].value
    viewerDOBDay = params['day'].value
    viewerEmail = params['email'].value
    viewerStNo = params['streetNo'].value
    viewerStName = params['streetName'].value
    viewerStType = params['streetType'].value
    viewerSuburb = params['suburb'].value
    viewerCity = params['city'].value
    viewerState = params['state'].value
    viewerPCode = params['postcode'].value
    viewerCountry = params['country'].value

    if params.has_key('premium'):
        viewerSubscription = True
    else:
        viewerSubscription = False

    isLeap = calendar.isleap(int(viewerDOBYear))

    error = 0

    if ((int(viewerDOBMonth) in short_months) and (viewerDOBDay == 31)):
        error = 1
    elif (int(viewerDOBMonth) not in long_months):
        if (isLeap and (int(viewerDOBDay) > 29)):
            error = 1
        elif (int(viewerDOBDay) > 28):
            error = 1

    viewerDOB = viewerDOBYear + "-"
    viewerDOB += viewerDOBMonth
    viewerDOB += "-"
    viewerDOB += viewerDOBDay
    
    main()