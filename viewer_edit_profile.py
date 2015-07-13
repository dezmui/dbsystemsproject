#######################################################################################################
#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to handle sql statements used to get correct viewer details for editing details
#or for players editing viewer details
#######################################################################################################

import sys, session, cgi, MySQLdb, redirect, sql_handler as sql, html_template as html, viewer_edit_profile_html as form

sess = session.Session(expires=20*60, cookie_path='/')
loggedIn = sess.data.get('loggedIn')
params = cgi.FieldStorage()

#######################################################################################################

def main():
    if not html.check_logged_in(loggedIn):
        return
    html.open_html(sess.cookie, loggedIn)
    error = False
    username = params['userName'].value
    if (loggedIn != 2) and (sess.data['userName'] != username):
        redirect.refresh("home.py", sess.cookie)
        return
    if params.has_key('error'):
        error = True
    print_body(username, error)

    html.close_html()
    sess.close()
    return

#######################################################################################################

#Print the viewer details through sql queries that extract viewer details

def print_body(username, error):
    viewerType = sql.run_sql("""SELECT ViewerType FROM Viewer
                                 WHERE ViewerID = (SELECT ViewerID FROM ViewerLogin
                                                     WHERE ViewerLogin.UserName = "%s")"""%username)[0][0]
    if viewerType != 'P':
        result = sql.run_sql("""SELECT Viewer.ViewerID, Viewer.ViewerType, Viewer.DATEOfBirth, Viewer.Email, 
                                       Address.StreetNumber, Address.StreetName, Address.StreetType, Address.MinorMunicipality, Address.MajorMunicipality, Address.GoverningDistrict, Address.PostalArea, Address.Country
                                FROM Viewer, ViewerLogin, Address, ViewerAddress
                                    WHERE ViewerLogin.Username = "%s"
                                    AND ViewerAddress.viewerID = ViewerLogin.viewerID
                                    AND Address.addressID = ViewerAddress.addressID
                                    AND ViewerLogin.viewerID = Viewer.viewerID
                                    AND ViewerAddress.endDATE is null""" % (username))[0]
    else:
        result = sql.run_sql("""SELECT Viewer.ViewerID, Viewer.ViewerType, PremiumViewer.RenewalDATE, Viewer.DATEOfBirth, Viewer.Email,
                                     Address.StreetNumber, Address.StreetName, Address.StreetType, Address.MinorMunicipality, Address.MajorMunicipality, Address.GoverningDistrict, Address.PostalArea, Address.Country
                                 FROM Viewer, ViewerLogin, Address, ViewerAddress, PremiumViewer
                                     WHERE ViewerLogin.Username = "%s"
                                     AND ViewerAddress.viewerID = ViewerLogin.viewerID
                                     AND Address.addressID = ViewerAddress.addressID
                                     AND ViewerLogin.viewerID = Viewer.viewerID
                                     AND ViewerAddress.endDATE is null""" % (username))[0]
    
    form.print_details(result, error, loggedIn)
    return

#######################################################################################################

main()
