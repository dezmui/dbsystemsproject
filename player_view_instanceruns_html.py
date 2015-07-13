#######################################################################################################

#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#HTML template file for view of instance Runs

#######################################################################################################

import redirect
#######################################################################################################

def print_instances(title, headings, body, loggedIn):
    print_title(title)
    open_table()
    table_heading(headings)
    for row in body:
        table_body(row, loggedIn)
    add_instancerun()
    for i in range(1, len(body[0]) - 1):
        print """                    <td></td>"""
    print """                </tr>"""
    close_table()
    return

#######################################################################################################

def print_title(title):
    print """        <div class="col-lg-6 col-lg-offset-3">
            <div class="page-header">
                <h1>%s</h1>
            </div>"""%title
    return

#######################################################################################################

def open_table():
    print """        <table class="table table-striped table-hover">
            <thead>
                <tr>"""
    return

#######################################################################################################

def table_heading(content):
    for item in content:
        print "                    <th>%s</th>"%item
    print"""                </tr>
            </thead>
            <tbody>"""
    return

#######################################################################################################

def table_body(content, loggedIn):
    print """                <tr>
                    <th><a href="%s">%s</a></th>"""%(redirect.getQualifiedURL("player_edit_instancerun.py?instancerunID=%s"%content[0]) if loggedIn == 2 else redirect.getQualifiedURL("login.py"), content[1])
    for item in content[2:]:
        print"                    <td>%s</td>"%item
    print "                </tr>"
    return

#######################################################################################################

def add_instancerun():
    print """                <tr>
                    <th style="text-align:center"><a class="btn btn-primary btn-block" roll="button" href="%s">Add Instance Run</a></th>"""%(redirect.getQualifiedURL("add_instance.py"))
    return

#######################################################################################################

def close_table():
    print """            </tbody>
        </table>
        </div>"""
    return

#######################################################################################################
