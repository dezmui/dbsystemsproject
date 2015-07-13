#######################################################################################################
#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to handle html prints for viewing equipment details
#######################################################################################################

import redirect

#######################################################################################################

#Print the details of equipment

def view_details(equipment):
    open_field_form(equipment)
    print_fields(equipment)
    close_form()
    return

#######################################################################################################

#Print opening of html form

def open_field_form(equipment):
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
                            <fieldset>"""%(equipment[1])
    return

#######################################################################################################

#Print fields of equipment details

def print_fields(equipment):
    print """                           <div class="form-group">
                                    <label class="col-lg-3 col-lg-offset-1 control-label">EquipmentID: </label>
                                    <div class="col-lg-7">
                                        <label class="control-label">%s</label>
                                    </div>
                                </div></br>
                                <div class="form-group">
                                    <label class="col-lg-3 col-lg-offset-1 control-label">Equipment Name: </label>
                                    <div class="col-lg-7">
                                        <label class="control-label">%s</label>
                                    </div>
                                </div></br>
                                <div class="form-group">
                                    <label class="col-lg-3 col-lg-offset-1 control-label">Review: </label>
                                    <div class="col-lg-7">
                                        <label class="control-label">%s</label>
                                    </div>
                                </div></br>
                                <div class="form-group">
                                    <label class="col-lg-3 col-lg-offset-1 control-label">Processor Speed: </label>
                                    <div class="col-lg-7">
                                        <label class="control-label">%s</label>
                                    </div>
                                </div></br>"""%(equipment[0], equipment[1], equipment[2], equipment[3])
    return

#######################################################################################################

#Close form and add a back button

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