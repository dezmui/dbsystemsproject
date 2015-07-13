#######################################################################################################

#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#HTML template file for view of editing game

#######################################################################################################

import redirect

def print_game(data):
    open_form()
    print_fields(data)
    close_form(str(data[0]))
    return

#######################################################################################################

def open_form():
    print"""        <div class="row">
              <div class="col-lg-4 col-md-offset-4">
                <div class="page-header">
                  <h1>Game Details</h1>
                </div>
              </div>
            </div>
            <div class="row">
                <div class="col-lg-4 col-md-offset-4">
                    <div class="well">
                        <form method="post" action="player_manage_a_game_update.py">
                            <fieldset>"""
    return

#######################################################################################################

def print_fields(data):
    print_disabled_field("GameID", "Game ID", str(data[0]))
    print_disabled_field("gameName", "Game Name", str(data[1]))
    print_a_field("genre", "Genre", str(data[2]))
    print_a_field("review", "Review", str(data[3]))
    
    print_drop_menu("starRating", "Star Rating", str(data[4]), range(0, 6))
    print_drop_menu("classificationRating", "Classification Rating", str(data[5]), ("G", "PG", "M", "MA", "R"))
    
    print_a_field("platformNotes", "Platform Notes", str(data[6]))
    print_a_field("promotionLink", "Promotion Link", str(data[7]))
    print_a_field("price", "Price", "$" + str(data[8]))
    return

#######################################################################################################

def print_drop_menu(name, label, data, values):
    open_drop_menu(name, label)
    fill_drop_menu(data, values)
    close_drop_menu()
    return

#######################################################################################################

def open_drop_menu(name, label):
    print """            <div class="form-group">
                <label class="col-lg-4 col-lg-offset-1 control-label">%s:</label>
                <div class="col-lg-6">
                    <select style="height:25px" class="form-control-sm" name="%s" id="%s">"""%(label, name, name)
    return

#######################################################################################################

def fill_drop_menu(data, values):
    for i in values:
        if str(i) == data:
            print """                <option selected="selected">%s</option>"""%str(i)
        else:
            print """                <option>%s</option>"""%str(i)
    return

#######################################################################################################

def close_drop_menu():
    print """                    </select>
                    </div>
                </div></br>"""
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

def close_form(gameID):
    print"""                            <div class="form-group">
                                <div class="col-lg-4 col-lg-offset-1">
                                    <button type="submit" class="btn btn-primary btn-block">Submit</button>
                                </div>
                                <div class="col-lg-4 col-lg-offset-2">
                                    <a class="btn btn-primary btn-block" roll="button" href="%s">Delete</a>
                                </div>
                            </div>
                        </fieldset>
                    </form>
                </div>
            </div>"""%(redirect.getQualifiedURL("player_manage_a_game_update.py?gameID=%s&delete=1"%gameID))
    return

#######################################################################################################
