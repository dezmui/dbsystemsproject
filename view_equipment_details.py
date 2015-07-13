#######################################################################################################
#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to handle sql statements used to get correct equipment details
#######################################################################################################

# The libraries we'll need
import sys, session, cgi, MySQLdb, redirect, sql_handler as sql, html_template as html, view_equipment_details_html as form

sess = session.Session(expires=20*60, cookie_path='/')
loggedIn = sess.data.get('loggedIn')


#######################################################################################################

def main():
    params = cgi.FieldStorage()
    equipmentID = params['equipID'].value
    
    html.open_html(sess.cookie, loggedIn)
    
    print_body(equipmentID, params)
    html.close_html()
    sess.close()
    return


#######################################################################################################

#Print body of the html for equipment details

def print_body(equipmentID, params):
    print "<div>"
    result = sql.run_sql("""SELECT * FROM Equipment
                             WHERE EquipmentID = %d"""%(int(equipmentID)))[0]
    form.view_details(result)
    print "</div>"
    return


#######################################################################################################

main()
