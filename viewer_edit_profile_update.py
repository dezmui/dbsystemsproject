#######################################################################################################
#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to handle sql statements used to get correct video details for a viewer viewing their orders
#or a player editing a video
#######################################################################################################

# The libraries we'll need
import sys, session, cgi, MySQLdb, redirect, sql_handler as sql, html_template as html, calendar

#######################################################################################################

sess = session.Session(expires=20*60, cookie_path='/')
loggedIn = sess.data.get('loggedIn')
params= cgi.FieldStorage()

#######################################################################################################

short_months = (3, 4, 9, 11)
long_months = (1, 5, 6, 7, 8, 10, 12)

#######################################################################################################

# login logic
# redirect to home page
run = True
if not html.check_logged_in(loggedIn):
    run = False
if params.has_key('delete'):
    run = False

if run:
    viewerID = params['ID'].value
    viewerType = params['viewerType'].value
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
    viewerRenewal = False
    if params.has_key('rday'):
        viewerRDay = params['rday'].value
        viewerRMonth = params['rmonth'].value
        viewerRYear = params['ryear'].value
        viewerRenewal = viewerRYear + "-"
        viewerRenewal += viewerRMonth
        viewerRenewal += "-"
        viewerRenewal += viewerRDay
    
    if params.has_key('renewSub'):
        renewSub = True
    else:
        renewSub = False
    if params.has_key('becomeSub'):
        becomeSub = True
    else:
        becomeSub = False

    username = sql.run_sql("""SELECT UserName FROM ViewerLogin WHERE ViewerLogin.ViewerID = %s"""%viewerID)[0][0]

    isLeap = calendar.isleap(int(viewerDOBYear))

    error = False

    if ((int(viewerDOBMonth) in short_months) and (viewerDOBDay == 31)):
        error = True
    elif (int(viewerDOBMonth) not in long_months):
        if (isLeap and (int(viewerDOBDay) > 29)):
            error = True
        elif (int(viewerDOBDay) > 28):
            error = True


    viewerDOB = viewerDOBYear + "-"
    viewerDOB += viewerDOBMonth
    viewerDOB += "-"
    viewerDOB += viewerDOBDay
    result = sql.run_sql("""SELECT ViewerAddress.AddressID FROM ViewerAddress, Viewer, Address
                      WHERE ViewerAddress.ViewerID = "%s"
                      AND ViewerAddress.EndDate is NULL
                      """ % (viewerID))
    addressID = result[0][0]

#######################################################################################################

#Order functions

def main():
    if loggedIn == 2 and params.has_key('delete'):
        viewerID = params["viewerID"].value
        remove_viewer(viewerID)
        redirect.refresh("home.py",sess.cookie)
        return
    if error:
        redirect.refresh("viewer_edit_profile.py?error=1", sess.cookie)
        return
    updateViewerInfo()
    redirect.refresh("viewer_edit_profile.py?userName=%s"%username, sess.cookie)
    return

#######################################################################################################

#Handle sql to remove a viewer from the database

def remove_viewer(viewerID):

    sql.run_remove(("""DELETE FROM CrowdFundingViewer WHERE ViewerID = "%s"
                   """% (viewerID)))
    sql.run_remove(("""DELETE FROM PremiumViewer WHERE ViewerID = "%s"
                   """% (viewerID)))                                    
    addressIDs = sql.run_sql(("""SELECT AddressID FROM ViewerAddress 
        WHERE ViewerID = "%s" 
        AND AddressID NOT IN (SELECT AddressID FROM ViewerAddress WHERE ViewerID != "%s")
        AND AddressID NOT IN (SELECT DISTINCT(AddressID) FROM PlayerAddress)
        """ %(viewerID,viewerID)))                                        
    sql.run_remove(("""DELETE FROM ViewerAddress WHERE ViewerID = "%s"
                    """ % (viewerID)))
    for i in addressIDs:
        sql.run_remove(("""DELETE FROM Address WHERE AddressID = "%s"
            """ % (i[0])))
    orderIDs = sql.run_sql(("""SELECT ViewerOrderID FROM ViewerOrder WHERE ViewerID = "%s"
                    """ % (viewerID)))  
    for i in orderIDs:
        sql.run_remove(("""DELETE FROM ViewerOrderLine WHERE ViewerOrderID = "%s"
            """ % (i[0])))            
    sql.run_remove(("""DELETE FROM ViewerOrder WHERE ViewerID = "%s"
                    """ % (viewerID)))                              
    sql.run_remove(("""DELETE FROM ViewerLogin WHERE ViewerID = "%s"
                    """ % (viewerID)))     
    sql.run_remove(("""DELETE FROM Viewer WHERE ViewerID = "%s"
                    """ % (viewerID)))     
    return

#######################################################################################################

#Handle sql to update a viewers details using the data passed in through cgi

def updateViewerInfo():
    sql.run_update(("""UPDATE Viewer 
                   SET DATEOfBirth = "%s", Email = "%s", ViewerType = "%s"
                   WHERE viewerID = "%s" 
                   """ % (viewerDOB, viewerEmail, viewerType[0], viewerID)))
    updateAddress()
    # Updating, renewing and adding premium subscriptions
    renewSubscription()
    updateRenewal()
    becomePremium()
    return

#######################################################################################################

#Handle sql to update address details using the data passed in through cgi

def updateAddress():
    if detect_address_change():
        sql.run_update("""
                       UPDATE ViewerAddress 
                       SET EndDATE = CURDATE()
                       WHERE ViewerID = "%s" AND AddressID = "%s"
                       """% (viewerID, addressID))
        next_val = sql.run_insert("""
                       INSERT Address VALUES
                       (DEFAULT, "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")
                       """ % (viewerStNo, viewerStName, viewerStType, viewerSuburb, viewerCity, viewerState, viewerPCode, viewerCountry))
        sql.run_insert("""
                       INSERT INTO ViewerAddress VALUES 
                       ("%s","%s",CURDATE(),NULL) 
                       """ % (viewerID, next_val))
        return
    return

#######################################################################################################

#Handle sql to check if data passed in through cgi is different than that in the database

def detect_address_change():
    result = sql.run_sql("""
                            SELECT StreetNumber, StreetName, StreetType, MinorMunicipality, MajorMunicipality,
                            GoverningDistrict,PostalArea,Country FROM Address
                            WHERE Address.AddressID = "%s"
                        """ % (addressID))
    if result:
        address = result[0]
        if address[0] != int(viewerStNo):
            return True
        elif address[1] != viewerStName:
            return True
        elif address[2] != viewerStType:
            return True
        elif address[3] != viewerSuburb:
            return True
        elif address[4] != viewerCity:
            return True
        elif address[5] != viewerState:
            return True
        elif address[6] != viewerPCode:
            return True
        elif address[7] != viewerCountry:
            return True
        else:
            return False
    return False

#######################################################################################################

def renewSubscription():
    if renewSub:
        sql.run_update("""UPDATE PremiumViewer
                          SET RenewalDATE = DATE_ADD(RenewalDate, INTERVAL 1 MONTH)
                          WHERE ViewerID = '%s'
                       """%viewerID)
    return

#######################################################################################################

def updateRenewal():
    if viewerRenewal:
        sql.run_update("""UPDATE PremiumViewer
                          SET RenewalDATE = '%s'
                           WHERE ViewerID = '%s'
                       """%(viewerRenewal, viewerID))
    return

#######################################################################################################

def becomePremium():
    if becomeSub:
        sql.run_update("""UPDATE Viewer
                       SET ViewerType = 'P'
                       WHERE ViewerID = '%s'
                   """%(viewerID))
        sql.run_insert("""INSERT INTO PremiumViewer VALUES
                           (%s, CURDATE() + INTERVAL 1 MONTH)"""%(viewerID))
    return

#######################################################################################################

main()