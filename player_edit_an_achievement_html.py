#######################################################################################################

#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#HTML template file for view of editing achievemnt

#######################################################################################################

import sql_handler as sql, redirect

#######################################################################################################

def print_achievement(data):
    open_form()
    print_fields(data)
    close_form(data[0])
    return

#######################################################################################################

def open_form():
    print"""        <div class="row">
              <div class="col-lg-4 col-md-offset-4">
                <div class="page-header">
                  <h1>Achievement Details</h1>
                </div>
              </div>
            </div>
            <div class="row">
                <div class="col-lg-4 col-md-offset-4">
                    <div class="well">
                        <form method="post" action="player_edit_an_achievement_update.py">
                            <fieldset>"""
    return

#######################################################################################################

def print_fields(data):
    instancerunIDs = sql.run_sql("""SELECT InstanceRunID FROM InstanceRun""")
    
    print_disabled_field("achievementID", "Achievement ID", str(data[0]))
    print_a_field("achievementName", "Achievement Name", str(data[1]))
    print_drop_menu("instancerunID", "Instance Run ID", str(data[2]), instancerunIDs)
    print_disabled_field("whenAchieved", "When Achieved", str(data[3]))
    print_a_field("rewardBody", "Reward Body", str(data[4]))
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
                <div class="col-lg-2">
                    <select style="height:25px" class="form-control-sm" name="%s" id="%s">"""%(label, name, name)
    return

#######################################################################################################

def fill_drop_menu(data, values):
    for i in values:
        if str(i[0]) == data:
            print """                <option selected="selected">%s</option>"""%str(i[0])
        else:
            print """                <option>%s</option>"""%str(i[0])
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

def close_form(achievementID):
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
            </div>"""%(redirect.getQualifiedURL("player_edit_an_achievement_update.py?achievementID=%s&delete=1"%achievementID))
    return

#######################################################################################################