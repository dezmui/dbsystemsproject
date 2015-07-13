#######################################################################################################

#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#Template for player_view_achievement

#######################################################################################################

import redirect

#######################################################################################################

def print_achievements(title, headings, body, loggedIn):
    print_title(title)
    open_table()
    table_heading(headings)
    for row in body:
        table_body(row, loggedIn)
    add_achievement()
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
                    <th><a href="%s">%s</a></th>"""%(redirect.getQualifiedURL("player_edit_an_achievement.py?achievementID=%s"%content[0]) if loggedIn == 2 else redirect.getQualifiedURL("login.py"), content[1])
    for item in content[2:]:
        print"                    <td>%s</td>"%item
    print "                </tr>"
    return

#######################################################################################################

def add_achievement():
    print """                <tr>
                    <th style="text-align:center"><a class="btn btn-primary btn-block" roll="button" href="%s">Add Achievement</a></th>"""%(redirect.getQualifiedURL("add_achievement.py"))
    return

#######################################################################################################

def close_table():
    print """            </tbody>
        </table>
        </div>"""
    return

#######################################################################################################