#######################################################################################################

#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#HTML template file for view of editing instanceRun

#######################################################################################################

import redirect, sql_handler as sql

#######################################################################################################

def edit_instancerun(IR):
    players = sql.run_sql("""SELECT PlayerID FROM Player""")
    blank_form_title("Edit Instance Run")
    edit_instancerun_form(str(IR[0]))
    edit_instancerun_fields(IR, players)
    close_instancerun_form(str(IR[0]))
    return


#######################################################################################################

def blank_form_title(title):
    print """        <div class="row">
              <div class="col-lg-4 col-md-offset-4">
                <div class="page-header">
                  <h1>%s</h1>
                </div>
              </div>
            </div>"""%title
    return

#######################################################################################################

def edit_instancerun_form(InstanceRunID):
    print """            <div class="row">
                <div class="col-lg-4 col-md-offset-4">
                     <div class="well">
                        <form method="post" action="%s">
                            <fieldset>"""%(redirect.getQualifiedURL("player_edit_instancerun_update.py?instancerunID=%s"%(InstanceRunID)))
    return

#######################################################################################################

def edit_instancerun_fields(IR, players):
    print_disabled_field("instancerunID", "Instance Run ID", IR[0])
    print_a_field("instancerunName", "Name", IR[1])
    print_a_field("categoryName", "Category Name", IR[3])
    print"""                                <div class="form-group">
                                    <label class="col-lg-5 col-lg-offset-1 control-label" for="supervisorID">Supervisor ID: </label>"""
    open_drop_menu("supervisorID")
    #Supervisor names for dropdown
    fill_drop_menu(int(IR[2]), players)
    close_drop_menu()
    return

#######################################################################################################

def print_disabled_field(name, label, data):
    print"""                                <div class="form-group">
                                    <label class="col-lg-5 col-lg-offset-1 control-label" for="%s">%s: </label>
                                    <div class="col-lg-6">
                                        <label class="control-label">%s</label>
                                        <input class="form-control input-sm" id="%s" type="hidden" value="%s">
                                    </div>
                                </div></br>"""%(name, label, data, name, data)
    return

#######################################################################################################

def print_a_field(name, label, data):
    print"""                                <div class="form-group">
                                    <label class="col-lg-5 col-lg-offset-1 control-label" for="%s">%s: </label>
                                    <div class="col-lg-6">
                                        <input class="form-control input-sm control-label" id="%s" name="%s" type="text" value="%s">
                                    </div>
                                </div></br>"""%(name, label, name, name, data)
    return

#######################################################################################################


def open_drop_menu(name):
    print """                    <div class="col-lg-2">
                        <select style="height:25px" class="form-control-sm" name="%s" id="%s">"""%(name, name)
    return

#######################################################################################################

def fill_drop_menu(value, values):
    for i in values:
        if i[0] == value:
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
                          
def close_instancerun_form(InstanceRunID):
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
            </div>
        </div>"""%(redirect.getQualifiedURL("player_edit_instancerun_update.py?instancerunID=%s&delete=1"%InstanceRunID))
    return

#######################################################################################################
