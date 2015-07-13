#######################################################################################################

#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#HTML template file for view of editing profile

#######################################################################################################

import redirect
from datetime import date

def print_details(playerData, addressData ,supervisor,error, loggedIn):
    open_form()
    if error:
        print_error()
    print_fields(playerData, addressData, supervisor, loggedIn)
    close_form()
    return

#######################################################################################################

def open_form():
    print"""        <div class="row">
              <div class="col-lg-4 col-md-offset-4">
                <div class="page-header">
                  <h1>Details</h1>
                </div>
              </div>
            </div>
            <div class="row">
                <div class="col-lg-4 col-md-offset-4">
                    <div class="well">
                        <form method="post" action="player_edit_profile_update.py">
                            <fieldset>"""
    return


#######################################################################################################

def print_fields(playerData, addressData,supervisor, loggedIn):
    print_disabled_field("pID", "Player ID", str(playerData[0]))
    print_disabled_field("superID", "Supervisor Handle", supervisor)
    print_disabled_field("pType", "Player Type", str(playerData[5]))
    
    print_a_field("fname", "First Name", str(playerData[2]))
    print_a_field("lname", "Last Name", str(playerData[3]))
    print_a_field("role", "Role", str(playerData[4]))
    print_a_field("describtion", "Profile Description", str(playerData[6]))
    print_a_field("email", "Email", str(playerData[7]))
    print_a_field("handle", "Game Handle", str(playerData[8]))
    print_a_field("phone", "Phone Number", str(playerData[9]))
    print_a_field("voip", "Voice IP", str(playerData[10]))
    
    print_disabled_field("aID", "Address ID", str(addressData[0]))
    print_a_field("stNo", "Street Number", str(addressData[1]))
    print_a_field("stName", "Street Name", str(addressData[2]))
    print_a_field("stType", "Street Type", str(addressData[3]))
    print_a_field("suburb", "Suburb", str(addressData[4]))
    print_a_field("city", "City", str(addressData[5]))
    print_a_field("state", "State", str(addressData[6]))
    print_a_field("postcode", "Postcode", str(addressData[7]))
    print_a_field("country", "Country", str(addressData[8]))
    
    return

#######################################################################################################

def print_dob_menu(name, label, data):
    year = str(data)[0:4]
    month = str(data)[5:7]
    day = str(data)[8:10]
    print """            <div class="form-group">
                <label class="col-lg-4 col-lg-offset-1 control-label">Date of Birth:</label>"""
    open_drop_menu("day")
    fill_drop_menu(int(day), range(1, 32))
    close_drop_menu()
    
    open_drop_menu("month")
    fill_drop_menu(int(month), range(1, 13))
    close_drop_menu()
    
    open_drop_menu("year")
    fill_drop_menu(int(year), range(1900, date.today().year + 1))
    close_drop_menu()
    print """                </div></br>"""
    return

#######################################################################################################

def open_drop_menu(name):
    print """                    <div class="col-lg-2">
                        <select style="height:25px" class="form-control-sm" name="%s" id="%s">"""%(name, name)
    return

#######################################################################################################

def fill_drop_menu(value, values):
    for i in values:
        if i == value:
            print """                <option selected="selected">%s</option>"""%str(i)
        else:
            print """                <option>%s</option>"""%str(i)
    return

#######################################################################################################

def close_drop_menu():
    print """                    </select>
                    </div>"""
    return

#######################################################################################################

def print_a_field(name, label, data):
    print"""                                <div class="form-group">
                                    <label class="col-lg-4 col-lg-offset-1 control-label" for="%s">%s: </label>
                                    <div class="col-lg-6">
                                        <input class="form-control input-sm control-label" id="%s" name="%s" type="text" value="%s">
                                    </div>
                                </div></br>"""%(name, label, name, name, data)
    return

#######################################################################################################

def print_disabled_field(name, label, data):
    print"""                                <div class="form-group">
                                    <label class="col-lg-4 col-lg-offset-1 control-label" for="%s">%s: </label>
                                    <div class="col-lg-6">
                                        <label class="control-label">%s</label>
                                        <input class="form-control input-sm" id="%s" name="%s" type="hidden" value="%s">
                                    </div>
                                </div></br>"""%(name, label, data, name, name, data)
    return

#######################################################################################################

def close_form():
    print"""                            <div class="form-group">
                                <div class="col-lg-4 col-lg-offset-4">
                                    <button type="submit" class="btn btn-primary btn-block">Submit</button>
                                </div>
                            </div>
                        </fieldset>
                    </form>
                </div>
            </div>"""
    return

#######################################################################################################

def close_form_player(viewerID):
    print"""                            <div class="form-group">
                                <div class="col-lg-4 col-lg-offset-1">
                                    <button type="submit" class="btn btn-primary btn-block">Submit</button>
                                </div>
                            </div>
                        </fieldset>
                    </form>
                </div>
            </div>"""
    return

#######################################################################################################

def print_error():
    print """                                <div class="form-group" style="text-align:center">
                                    <label class="col-lg-8 col-lg-offset-2 control-label" style="color:red">Invalid date submitted. No changes made.</label>
                                </div>"""
    return

#######################################################################################################