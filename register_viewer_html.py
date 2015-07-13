#######################################################################################################
#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to handle HTML for register viewer page
#######################################################################################################

import redirect
from datetime import date

def print_details(error):
    open_form()
    if error:
        print_error(error)
    print_fields()
    close_form()
    return

#######################################################################################################

def open_form():
    print"""        <div class="row">
              <div class="col-lg-4 col-md-offset-4">
                <div class="page-header">
                  <h1>Register</h1>
                </div>
              </div>
            </div>
            <div class="row">
                <div class="col-lg-4 col-md-offset-4">
                    <div class="well">
                        <form method="post" action="register_viewer_add.py">
                            <fieldset>"""
    return

#######################################################################################################

def print_fields():
    print_a_field("username", "User Name", "Enter your username")
    print_a_pwd_field("password1", "Password", "Enter your password")
    print_a_pwd_field("password2", "Confirm Password", "Enter your password again")
    
    print_dob_menu("DoB", "Date of Birth")
    
    print_a_field("email", "Email", "Enter your email")
    print_a_field("streetNo", "Street Number", "Enter your street number")
    print_a_field("streetName", "Street Name", "Enter your street name")
    print_a_field("streetType", "Street Type", "Enter your street type")
    print_a_field("suburb", "Suburb", "Enter your suburb")
    print_a_field("city", "City", "Enter your city")
    print_a_field("state", "State", "Enter your state")
    print_a_field("postcode", "Postcode", "Enter your postcode")
    print_a_field("country", "Country", "Enter your country")
    print_a_checkbox("premium", "Purchase a premium subscription (monthly)")
    return

#######################################################################################################

def print_dob_menu(name, label):
    print """            <div class="form-group">
                <label class="col-lg-4 control-label">Date of Birth:</label>"""
    open_drop_menu("day")
    fill_drop_menu(range(1, 32), "Day")
    close_drop_menu()
    
    open_drop_menu("month")
    fill_drop_menu(range(1, 13), "Month")
    close_drop_menu()
    
    open_drop_menu("year")
    fill_drop_menu(range(1900, date.today().year + 1), "Year")
    close_drop_menu()
    print """                </div></br>"""
    return

#######################################################################################################

def open_drop_menu(name):
    print """                    <div class="col-lg-2" style="width:100px">
                        <select style="height:25px" class="form-control-sm" name="%s" id="%s">"""%(name, name)
    return

#######################################################################################################

def fill_drop_menu(values, value):
    print """                <option value="" disabled selected>%s</option>"""%value
    for i in values:
        print """                <option>%s</option>"""%str(i)
    return

#######################################################################################################

def close_drop_menu():
    print """                    </select>
                    </div>"""
    return

#######################################################################################################

def print_a_field(name, label, placeholder):
    print"""                                <div class="form-group">
                                    <label class="col-lg-4 control-label" for="%s">%s: </label>
                                    <div class="col-lg-7">
                                        <input class="form-control input-sm control-label" id="%s" name="%s" type="text" placeholder="%s">
                                    </div>
                                </div></br>"""%(name, label, name, name, placeholder)
    return

#######################################################################################################

def print_a_pwd_field(name, label, placeholder):
    print"""                                <div class="form-group">
                                    <label class="col-lg-4 control-label" for="%s">%s: </label>
                                    <div class="col-lg-7">
                                        <input class="form-control input-sm control-label" id="%s" name="%s" type="password" placeholder="%s">
                                    </div>
                                </div></br>"""%(name, label, name, name, placeholder)
    return

#######################################################################################################
                      
def print_a_checkbox(name, label):
    print"""                                <div class="checkbox">
                                     <label class="col-lg-4 control-label" for="%s">
                                         <input id="%s" name="%s" type="checkbox" value="%s"> %s
                                     </label>
                                 </div>"""%(name, name, name, name, label)
    return

#######################################################################################################

def close_form():
    print"""                            <div class="form-group">
                                <div class="col-lg-4 col-lg-offset-4">
                                    <button type="submit" class="btn btn-primary btn-block">Register</button>
                                </div>
                            </div>
                        </fieldset>
                    </form>
                </div>
            </div>"""
    return

#######################################################################################################

def print_error(error):
    if error == 1:
        print """                                <div class="form-group" style="text-align:center">
                                        <label class="col-lg-8 col-lg-offset-2 control-label" style="color:red">Invalid date submitted. No changes made.</label>
                                    </div>"""
    elif error == 2:
        print """                                <div class="form-group" style="text-align:center">
                                        <label class="col-lg-8 col-lg-offset-2 control-label" style="color:red">Please enter all fields.</label>
                                    </div>"""
    elif error == 3:
        print """                                <div class="form-group" style="text-align:center">
                                        <label class="col-lg-8 col-lg-offset-2 control-label" style="color:red">Username already exists. Please use another username.</label>
                                    </div>"""
    elif error == 4:
        print """                                <div class="form-group" style="text-align:center">
                                        <label class="col-lg-8 col-lg-offset-2 control-label" style="color:red">Passwords do not match. Please try again.</label>
                                    </div>"""
    return

#######################################################################################################
