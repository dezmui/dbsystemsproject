#######################################################################################################

#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#HTML template file for view of adding new game for user

#######################################################################################################

import redirect

#######################################################################################################

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
                  <h1>Add Game</h1>
                </div>
              </div>
            </div>
            <div class="row">
                <div class="col-lg-4 col-md-offset-4">
                    <div class="well">
                        <form method="post" action="add_game_update.py">
                            <fieldset>"""
    return

#######################################################################################################

def print_fields():
    print_a_field("gameName", "Game Name", "Enter Game Name")
    print_a_field("genre", "Genre", "Enter Genre")
    print_a_field("review", "Game Review", "Enter Game Review")
    print_drop_menu("starRating", "Enter Star Rating", range(0, 6))
    print_drop_menu("classificationRating", "Enter Classification", ("G", "PG", "M", "MA", "R"))
    print_a_field("platformNotes", "Platform Notes", "Enter Platform Notes")
    print_a_field("promotionLink", "Promotion Link", "Enter Promotion Link")
    print_a_field("price", "Price", "Enter Price")
    return

#######################################################################################################

def print_drop_menu(name, label, values):
    print """            <div class="form-group">
                <label class="col-lg-4 control-label">%s:</label>""" % (label)
    open_drop_menu(name)
    fill_drop_menu(values[0], values)
    close_drop_menu()
    
    print """                </div></br>"""
    return

#######################################################################################################

def open_drop_menu(name):
    print """                    <div class="col-lg-7">
                        <select style="height:25px" class="form-control-sm" name="%s" id="%s">"""%(name, name)
    return

#######################################################################################################

def fill_drop_menu(data, values):
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

def close_form():
    print"""                            <div class="form-group">
                                <div class="col-lg-4 col-lg-offset-4">
                                    <button type="submit" class="btn btn-primary btn-block">Create Game</button>
                                </div>
                            </div>
                        </fieldset>
                    </form>
                </div>
            </div>"""
    return

#######################################################################################################

def print_error(error):
    print """                                <div class="form-group" style="text-align:center">
                                    <label class="col-lg-8 col-lg-offset-2 control-label" style="color:red">Invalid date submitted. No changes made.</label>
                                </div>"""
    return

#######################################################################################################