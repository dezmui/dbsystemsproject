#######################################################################################################
#Authros: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song
#INFO20003 assessment
#File used to display a single order details, all orders for a viewer, or fields for a player to edit
#a video
#######################################################################################################

import redirect

#######################################################################################################

#Display page if viewer is viewing a single order
def confirm_order(order, paying):
    open_field_form(order)
    print_fields(order, paying)
    close_form()
    return

#######################################################################################################

#Display page if player is editing a video's details
def edit_video(video):
    blank_form_title("Edit Video")
    edit_video_form(video[7])
    edit_video_fields(video)
    close_video_form(video[7])
    return

#######################################################################################################

#Display page if viewer is viewing all orders placed
def show_all_orders(orders, paying, error):
    blank_form_title("Your Orders")
    if error:
        print_error()
    for order in orders:
        open_blank_form()
        print_fields(order, paying)
        print_other_fields(order)
        close_blank_form()
    return

#######################################################################################################

#Print HTML to open a confirm order form
def open_field_form(order):
    print """        <div class="row">
              <div class="col-lg-4 col-md-offset-4">
                <div class="page-header">
                  <h1>Confirm Order</h1>
                </div>
              </div>
            </div>
            <div class="row">
                <div class="col-lg-4 col-md-offset-4">
                    <div class="well">
                        <form method="post" action="%s">
                            <fieldset>"""%redirect.getQualifiedURL("viewer_order_confirm.py?vidid=%s"%order[7])
    return

#######################################################################################################

#Print HTML to open an edit video form
def edit_video_form(vidID):
    print """            <div class="row">
                <div class="col-lg-4 col-md-offset-4">
                     <div class="well">
                        <form method="post" action="%s">
                            <fieldset>"""%redirect.getQualifiedURL("player_edit_video_update.py?videoID=%s"%vidID)
    return

#######################################################################################################

#Handle the fields to print for editting a video
def edit_video_fields(video):
    print_disabled_field("videoID", "Video ID", video[7])
    print_a_field("videoName", "Name", video[0])
    print_a_field("videoType", "Type", video[3])
    print_a_field("supervisorID", "Supervisor ID", video[9])
    print_a_field("URL", "URL", video[8])
    print_a_field("price", "Price", video[6])
    return

#######################################################################################################

#Print the HTML for a single form field
def print_a_field(name, label, data):
    print"""                                <div class="form-group">
                                    <label class="col-lg-5 col-lg-offset-1 control-label" for="%s">%s: </label>
                                    <div class="col-lg-6">
                                        <input class="form-control input-sm control-label" id="%s" name="%s" type="text" value="%s">
                                    </div>
                                </div></br>"""%(name, label, name, name, data)
    return

#######################################################################################################

#Print the HTML for a field that cannot be modified
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

#Print the HTML for a form title
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

#Print the opening HTML for an order to have its details displayed
def open_blank_form():
    print """            <div class="row">
                <div class="col-lg-4 col-md-offset-4">
                    <div class="well">
                        <fieldset>"""
    return

#######################################################################################################

#Print the HTML to display data of an order to be confirmed
def print_fields(order, paying):
    print """                                <div class="form-group">
                                    <label style="align:center" class="col-md- col-md-offset-1 control-label"><h2>%s</h2></label>
                                </div>
                                <div class="form-group">
                                    <label class="col-lg-4 col-lg-offset-1 control-label">Instance Run: </label>
                                    <div class="col-lg-6">
                                        <label class="control-label">%s    </label>
                                    </div>
                                </div></br>
                                <div class="form-group">
                                    <label class="col-lg-4 col-lg-offset-1 control-label">Game: </label>
                                    <div class="col-lg-6">
                                        <label class="control-label">%s</label>
                                    </div>
                                </div></br>
                                <div class="form-group">
                                    <label class="col-lg-4 col-lg-offset-1 control-label">Type: </label>
                                    <div class="col-lg-6">
                                        <label class="control-label">%s</label>
                                    </div>
                                </div></br>
                                <div class="form-group">
                                    <label class="col-lg-4 col-lg-offset-1 control-label">Supervised By: </label>
                                    <div class="col-lg-6">
                                        <label class="control-label">%s %s</label>
                                    </div>
                                </div></br>
                                <div class="form-group">
                                    <label class="col-lg-4 col-lg-offset-1 control-label">Price: </label>
                                    <div class="col-lg-6">
                                        <label class="control-label">%s</label>
                                    </div>
                                </div></br>"""%(order[0], order[1], order[2], order[3], order[4], order[5], ('$' + str(order[6])) if paying else "Free")
    return

#######################################################################################################

#Print extra fields
def print_other_fields(order):
    print """                   <div class="form-group">
                                    <label class="col-lg-4 col-lg-offset-1 control-label">Viewed Status: </label>
                                    <div class="col-lg-6">
                                        <label class="control-label">%s</label>
                                    </div>
                                </div></br>
                                <div class="form-group">
                                    <label class="col-lg-4 col-lg-offset-1 control-label">Date Viewed: </label>
                                    <div class="col-lg-6">
                                        <label class="control-label">%s</label>
                                    </div>
                                </div></br>
                                <div class="form-group">
                                    <label class="col-lg-4 col-lg-offset-1 control-label">URL: </label>
                                    <div class="col-lg-6">
                                        <label class="control-label"><a href="%s">%s</a></label>
                                    </div>
                                </div></br>"""%(order[7], order[10] if order[10] != None else "Not viewed yet", redirect.getQualifiedURL("viewer_order_watch.py?orderID=%s"%order[9]), order[8])
    return

#######################################################################################################

#Close regular form
def close_form():
    print"""                            <div class="form-group">
                                <div class="col-lg-4 col-lg-offset-4">
                                    <button type="submit" class="btn btn-primary btn-block">Submit</button>
                                </div>
                            </div>
                        </fieldset>
                    </form>
                </div>
            </div>
        </div>"""
    return

#######################################################################################################

#Close an edit video form
def close_video_form(vidID):
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
        </div>"""%(redirect.getQualifiedURL("player_edit_video_update.py?videoID=%s&delete=1"%vidID))
    return

#######################################################################################################

#Close a blank from
def close_blank_form():
    print"""                    </fieldset>
                </div>
            </div>
        </div>"""
    return
                                                                                   
#######################################################################################################

#Print HTML to display an error
def print_error():
    print """                                <div class="form-group" style="text-align:center">
                                    <label class="col-lg-8 col-lg-offset-2 control-label" style="color:red">Your video has already been ordered.</label>
                                </div>"""
    return

#######################################################################################################