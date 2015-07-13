#######################################################################################################
#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File used to handle html statements to view the renew subscription page
#######################################################################################################

import redirect

#######################################################################################################

#View the form with message of renewing subscription

def view_form(viewerID, renewalDate):
    open_field_form()
    print_message(viewerID, renewalDate)
    close_form(viewerID)
    return

#######################################################################################################

#Open form of the renew subscription page

def open_field_form():
    print """        <div class="row">
              <div class="col-lg-4 col-md-offset-4">
                <div class="page-header">
                  <h1>Your Premium Subscription Has Been Expired</h1>
                </div>
              </div>
            </div>
            <div class="row">
                <div class="col-lg-6 col-md-offset-3">
                    <div class="well">
                        <form>
                            <fieldset>"""
    return

#######################################################################################################

#Print message with subscription detail

def print_message(viewerID, renewalDate):
    year = str(renewalDate)[0:4]
    month = str(renewalDate)[5:7]
    day = str(renewalDate)[8:10]
    print """                                <div class="form-group" style="text-align:center">
                                    <label class="col-lg-8 col-lg-offset-2 control-label" style="color:white">Your subscription has expired on %s-%s-%s, would you like to renew your subscription for another month?</label>
                                </div>"""%(day, month, year)
    return

#######################################################################################################

#Close html form and add buttons to renew subscription, cancel subscription or Logout

def close_form(viewerID):
    print"""                            <div class="form-group">
                                <div class="col-lg-2 col-lg-offset-2">
                                    <a class="btn btn-primary btn-block" roll="button" href="%s">Yes</a>
                                </div>
                                <div class="col-lg-4">
                                    <a class="btn btn-primary btn-block" roll="button" href="%s">No, I want to cancel my subscription</a>
                                </div>
                                <div class="col-lg-2">
                                    <a class="btn btn-primary btn-block" roll="button" href="%s">Logout</a>
                                </div>
                        </fieldset>
                     </form>
                </div>
            </div>
        </div>"""%(redirect.getQualifiedURL("renew_subscription_update.py?viewerID=%s"%viewerID), redirect.getQualifiedURL("renew_subscription_update.py?viewerID=%s&cancel=1"%viewerID), redirect.getQualifiedURL("do_logout.py"))
    return
                                                                                   
#######################################################################################################