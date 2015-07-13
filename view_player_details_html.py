#######################################################################################################
#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to handle printing html forms for viewing player details
#######################################################################################################

import redirect

#######################################################################################################

# View details of the player

def view_details(player, loggedIn):
    open_field_form(player)
    print_fields(player, loggedIn)
    close_form()
    return

#######################################################################################################

# Open form and print header

def open_field_form(player):
    print """        <div class="row">
              <div class="col-lg-4 col-md-offset-4">
                <div class="page-header">
                  <h1>%s Details</h1>
                </div>
              </div>
            </div>
            <div class="row">
                <div class="col-lg-6 col-md-offset-3">
                    <div class="well">
                        <form>
                            <fieldset>"""%(player[8])
    return

#######################################################################################################

#Print fields of player details

def print_fields(player, loggedIn):
    print """                           <div class="form-group">
                                    <label class="col-lg-3 col-lg-offset-1 control-label">PlayerID: </label>
                                    <div class="col-lg-7">
                                        <label class="control-label">%s</label>
                                    </div>
                                </div></br>
                                <div class="form-group">
                                    <label class="col-lg-3 col-lg-offset-1 control-label">Player GameHandle: </label>
                                    <div class="col-lg-7">
                                        <label class="control-label">%s</label>
                                    </div>
                                </div></br>
                                <div class="form-group">
                                    <label class="col-lg-3 col-lg-offset-1 control-label">Role: </label>
                                    <div class="col-lg-7">
                                        <label class="control-label">%s</label>
                                    </div>
                                </div></br>
                                <div class="form-group">
                                    <label class="col-lg-3 col-lg-offset-1 control-label">Profile Description: </label>
                                    <div class="col-lg-7">
                                        <label class="control-label">%s</label>
                                    </div>
                                </div></br>
                                <div class="form-group">
                                    <label class="col-lg-3 col-lg-offset-1 control-label">Email: </label>
                                    <div class="col-lg-7">
                                        <label class="control-label">%s</label>
                                    </div>
                                </div></br>"""%(player[0], player[8], player[4], player[6], player[7])
    if loggedIn in (1, 2):
        print """                           <div class="form-group">
                                    <label class="col-lg-3 col-lg-offset-1 control-label">VoP: </label>
                                    <div class="col-lg-7">
                                        <label class="control-label">%s</label>
                                    </div>
                                </div></br>"""%player[10]
    return

#######################################################################################################

#Close form and add a button to go back

def close_form():
    print"""                            <div class="form-group">
                                <div class="col-lg-2 col-lg-offset-4">
                                    <button class="btn btn-primary btn-block" type="button" onClick="history.go(-1);return true;">Back</button>
                                </div>
                            </div>
                        </fieldset>
                     </form>
                </div>
            </div>
        </div>"""
    return
                                                                                   
#######################################################################################################