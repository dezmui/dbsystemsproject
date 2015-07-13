#######################################################################################################

#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to edit given profile using given input

#######################################################################################################

# The libraries we'll need
import sys, session, cgi, MySQLdb, redirect, sql_handler as sql, html_template as html, calendar

#######################################################################################################

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
#If run is still set to true, get all the information from CGI fieldstorage
if run:
    playerID= params['pID'].value
    playerfname= params['fname'].value
    playerlname= params['lname'].value
    playerole= params['role'].value
    plaerdesc= params['describtion'].value
    playeremail = params['email'].value
    playerhandle= params['handle'].value
    playerphone= params['phone'].value
    playervoip= params['voip'].value
    
    addID= params['aID'].value
    addNo= params['stNo'].value
    addName= params['stName'].value
    addType= params['state'].value
    addSuburb= params['stType'].value
    addCity= params['city'].value
    addState = params['state'].value
    addPost = params['postcode'].value
    addCountry = params['country'].value

    username = sql.run_sql("""SELECT UserName FROM PlayerLogin WHERE PlayerLogin.PlayerID= %s"""%playerID)[0][0]


    error = False


    result = sql.run_sql("""SELECT PlayerAddress.AddressID FROM PlayerAddress, Player, Address
                      WHERE PlayerAddress.PlayerID= "%s"
                      AND PlayerAddress.EndDate is NULL
                      """ % (playerID))
    addressID = result[0][0]
    
#######################################################################################################

def main():
    #Print error if any exist
    if error:
        redirect.refresh("player_edit_profile.py?error=1", sess.cookie)
        return
    updateViewerInfo()
    redirect.refresh("player_edit_profile.py", sess.cookie)
    return

#######################################################################################################
    
def updateViewerInfo():
    sql.run_update(("""UPDATE Player
                   SET FirstName = "%s", LastName = "%s", Role = "%s", ProfileDescription = "%s", Email = "%s", GameHandle = "%s", Phone = "%s", VoP = "%s"
                   WHERE PlayerID= "%s" 
                   """ % (playerfname, playerlname,playerole,plaerdesc,playeremail,playerhandle,playerphone,playervoip,playerID)))
    updateAddress()
    return
#######################################################################################################
    
def updateAddress():
    #update address only if it has been changed
    if detect_address_change():
        sql.run_update("""
                       UPDATE PlayerAddress
                       SET EndDATE = CURDATE()
                       WHERE PlayerID = "%s" AND AddressID = "%s"
                       """% (playerID, addressID))
        next_val = sql.run_insert("""
                       INSERT Address VALUES
                       (DEFAULT, "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")
                       """ % (addNo, addName, addType, addSuburb, addCity, addState, addPost, addCountry))
        sql.run_insert("""
                       INSERT INTO PlayerAddress VALUES 
                       ("%s","%s",CURDATE(),NULL) 
                       """ % (playerID, next_val))
    return
    
#######################################################################################################

def detect_address_change():
    result = sql.run_sql("""
                            SELECT StreetNumber, StreetName, StreetType, MinorMunicipality, MajorMunicipality,
                            GoverningDistrict,PostalArea,Country FROM Address
                            WHERE Address.AddressID = "%s"
                        """ % (addressID))
    if result:
        address = result[0]
        if address[0] != int(addNo):
            return True
        elif address[1] != addName:
            return True
        elif address[2] != addType:
            return True
        elif address[3] != addSuburb:
            return True
        elif address[4] != addCity:
            return True
        elif address[5] != addState:
            return True
        elif address[6] != addPost:
            return True
        elif address[7] != addCountry:
            return True
        else:
            return False
    return False

#######################################################################################################

main()