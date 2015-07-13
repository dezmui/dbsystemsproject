#######################################################################################################

#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#HTML template for player_manage_games

#######################################################################################################

import redirect

#######################################################################################################

def print_games(games):
    print_title("Games")
    open_table()
    table_heading(("ID", "Name", "Rating", "Classification", "Price"))
    print """        <div class="col-lg-6 col-lg-offset-3">"""
    for game in games:
        table_body(game)
    add_game()
    for i in range(1, len(games[0])):
        print """                    <td></td>"""
    print """                </tr>"""
    close_table()
    print """        </div>"""
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

def table_body(content):
    url = redirect.getQualifiedURL("player_manage_a_game.py?gameID=%s"%(content[0]))
    
    print """                <tr>
                    <th>%s</th>"""%content[0]
    print """                <td><a href="%s">%s</a></td>"""%(redirect.getQualifiedURL("player_manage_a_game.py?gameID=%s"%content[0]), content[1])
    for item in content[2:]:
        print"                    <td>%s</td>"%item
    print "                </tr>"
    return

#######################################################################################################

def add_game():
    print """                <tr>
                    <th style="text-align:center"><a class="btn btn-primary btn-block" roll="button" href="%s">Add Game</a></th>"""%(redirect.getQualifiedURL("add_game.py"))
    return

#######################################################################################################

def close_table():
    print """            </tbody>
        </table>
        </div>"""
    return

#######################################################################################################
