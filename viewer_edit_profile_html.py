#######################################################################################################
#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to handle HTML for a player to edit their profile
#######################################################################################################

import redirect
from datetime import date

def print_details(data, error, loggedIn):
    open_form()
    if error:
        print_error()
    print_fields(data, loggedIn)
    if loggedIn == 2:
        close_form_player(data[0])
    else:
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
                        <form method="post" action="viewer_edit_profile_update.py">
                            <fieldset>"""
    return

#######################################################################################################

def print_fields(data, loggedIn):
    print_disabled_field("ID", "ID", str(data[0]))
    viewerType = "Normal"
    if str(data[1]) == "P":
        viewerType = "Premium"
    elif str(data[1]) == "C":
        viewerType = "Crowd Funding"
    else:
        viewerType = "Normal"
    if loggedIn == 2:
        print """            <div class="form-group">
                <label class="col-lg-4 col-lg-offset-1 control-label">Viewer Type:</label>"""
        open_drop_menu("viewerType")
        fill_drop_menu(str(data[1]), ('P', 'C', 'N'))
        close_drop_menu()
        print """                </div></br>"""
    else:
        if viewerType == "Normal":
            print_upgrade_renewal_field("viewerType", "Viewer Type", viewerType)
        else:
            print_disabled_field("viewerType", "Viewer Type", viewerType)
    
    if viewerType != "Premium":
        print_dob_menu("DoB", "Date of Birth", str(data[2]))
        print_a_field("email", "Email", str(data[3]))
        print_a_field("streetNo", "Street Number", str(data[4]))
        print_a_field("streetName", "Street Name", str(data[5]))
        print_a_field("streetType", "Street Type", str(data[6]))
        print_a_field("suburb", "Suburb", str(data[7]))
        print_a_field("city", "City", str(data[8]))
        print_a_field("state", "State", str(data[9]))
        print_a_field("postcode", "Postcode", str(data[10]))
        print_a_field("country", "Country", str(data[11]))
        return
    else:
        year = str(data[2])[0:4]
        month = str(data[2])[5:7]
        day = str(data[2])[8:10]
        print_disabled_renewal_field("renewalDate", "Subscription Expires", day+"-"+month+"-"+year) if loggedIn == 1 else print_date_menu("renewalDate", "Renew Date", str(data[2]))
        print_dob_menu("DoB", "Date of Birth", str(data[3]))
        print_a_field("email", "Email", str(data[4]))
        print_a_field("streetNo", "Street Number", str(data[5]))
        print_a_field("streetName", "Street Name", str(data[6]))
        print_a_field("streetType", "Street Type", str(data[7]))
        print_a_field("suburb", "Suburb", str(data[8]))
        print_a_field("city", "City", str(data[9]))
        print_a_field("state", "State", str(data[10]))
        print_a_field("postcode", "Postcode", str(data[11]))
        print_a_field("country", "Country", str(data[12]))
        return

#######################################################################################################

def print_dob_menu(name, label, data):
    year = str(data)[0:4]
    month = str(data)[5:7]
    day = str(data)[8:10]
    print """            <div class="form-group">
                <label class="col-lg-4 col-lg-offset-1 control-label">%s:</label>"""%label
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
                                                                                                                                         
def print_date_menu(name, label, data):
    year = str(data)[0:4]
    month = str(data)[5:7]
    day = str(data)[8:10]
    print """            <div class="form-group">
                <label class="col-lg-4 col-lg-offset-1 control-label">%s:</label>"""%label
    open_drop_menu("rday")
    fill_drop_menu(int(day), range(1, 32))
    close_drop_menu()
    
    open_drop_menu("rmonth")
    fill_drop_menu(int(month), range(1, 13))
    close_drop_menu()
    
    open_drop_menu("ryear")
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

def print_disabled_renewal_field(name, label, data):
    print"""                                <div class="form-group">
                                    <label class="col-lg-4 col-lg-offset-1 control-label" for="%s">%s: </label>
                                    <div class="col-lg-3">
                                        <label class="control-label">%s</label>
                                        <input class="form-control input-sm" id="%s" name="%s" type="hidden" value="%s">
                                    </div>
                                    <div class="checkbox">
                                        <label class="col-lg-3 control-label" for="renewSub">
                                        <input id="renewSub" name="renewSub" type="checkbox" value="renewSub"> Renew Subscription
                                        </label>
                                    </div>
                                </div></br>"""%(name, label, data, name, name, data)
    return

#######################################################################################################

def print_upgrade_renewal_field(name, label, data):
    print"""                                <div class="form-group">
                                    <label class="col-lg-4 col-lg-offset-1 control-label" for="%s">%s: </label>
                                    <div class="col-lg-4">
                                        <label class="control-label">%s</label>
                                        <input class="form-control input-sm" id="%s" name="%s" type="hidden" value="%s">
                                    </div>
                                    <div class="checkbox">
                                        <label class="col-lg-3 control-label" for="becomeSub">
                                        <input id="becomeSub" name="becomeSub" type="checkbox" value="becomeSub"> Become Premium
                                        </label>
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
                                <div class="col-lg-4 col-lg-offset-2">
                                    <a class="btn btn-primary btn-block" roll="button" href="%s">Delete Account</a>
                                </div>
                            </div>
                        </fieldset>
                    </form>
                </div>
            </div>"""%(redirect.getQualifiedURL("viewer_edit_profile_update.py?viewerID=%s&delete=1"%viewerID))
    return

#######################################################################################################

def print_error():
    print """                                <div class="form-group" style="text-align:center">
                                    <label class="col-lg-8 col-lg-offset-2 control-label" style="color:red">Invalid date submitted. No changes made.</label>
                                </div>"""
    return

#######################################################################################################
