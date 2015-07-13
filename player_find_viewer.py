#######################################################################################################

#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#File to search viewers function for player account

#######################################################################################################

import sys, session, cgi, MySQLdb, redirect, html_template as html

#######################################################################################################

#Get Session from cookie and fieldstorage that has been passed on from previous page
params = cgi.FieldStorage()
sess = session.Session(expires=20*60, cookie_path='/')
loggedIn = sess.data.get('loggedIn')

#######################################################################################################

def main():
    if not html.check_player(loggedIn):
        return
    html.open_html(sess.cookie, loggedIn)
    if params.has_key('notFound'):
        print """
             <div style="text-align:center" class="col-lg-4 col-lg-offset-4">
                 <label class="col-lg-3 control-label">User Not Found</label>
             </div>
        """
    search_form()
    html.close_html()
    return

#######################################################################################################

def search_form():
    print"""        <div class="col-md-4 col-md-offset-4">
            <div class="well bs-component">
                <form class="form-horizontal" action="player_edit_viewer.py">
                    <fieldset>
                        <div class="form-group">
                            <label for="viewerID" class="col-lg-3 control-label">Search Viewers:</label>
                            <div class="col-lg-6">
                                <input class="form-control" name="viewerID" placeholder="Viewer ID" type="text">
                            </div>
                            <div class="col-lg-3">
                                <button type="submit" class="btn btn-primary">Search</button>
                            </div>
                        </div>"""
    return

#######################################################################################################

main()
