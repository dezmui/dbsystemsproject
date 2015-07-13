#######################################################################################################

#Authors: Beaudan Campbell-Brown, Derek Mui, Ha Jin Song, Jerry Chen
#INFO20003 assessment
#HTML template file for main page

#######################################################################################################

#Get Session from cookie and fieldstorage that has been passed on from previous page

import redirect, session

sess = session.Session(expires=20*60, cookie_path='/')

#######################################################################################################

def open_html(cookie, loggedIn):
    
    print_doctype(cookie)
    banner_start()
    
    if loggedIn == 1:
        banner_viewer()
    
    elif loggedIn == 2:
        banner_player()
    
    else:
        banner_default()
    
    close_banner()
    return

#######################################################################################################

def check_logged_in(loggedIn):
    if loggedIn not in (1, 2):
        redirect.refresh("login.py", sess.cookie)
        return False
    return True

#######################################################################################################

def check_player(loggedIn):
    if loggedIn != 2:
        redirect.refresh("login.py", sess.cookie)
        return False
    return True

#######################################################################################################

def print_doctype(cookie):
    print "%s\nContent-Type: text/html\n" % (cookie)
    return

#######################################################################################################

def banner_start():
    print """
    <!DOCTYPE html>
    <html lang="en">

    <head>

        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="">
        <meta name="author" content="">

        <title>WWAG - Will Wheaton Appreciation Guild</title>

        <!-- Bootstrap Core CSS -->
        <link rel="stylesheet" href="Bootstrap/css/bootstrap.css" media="screen">
        <link rel="stylesheet" href="Bootstrap/css/bootswatch.min.css">

        <!-- Custom CSS -->
        <style>
        body {
            padding-top: 70px;
        }
        </style>

        <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
            <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
            <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
        <![endif]-->

    </head>
    
    <body>

        <!-- Navigation -->
        <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
            <div class="container">
                <!-- Brand and toggle get grouped for better mobile display -->
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <a class="navbar-brand" href="home.py">Will Wheaton Appreciation Guild</a>
                </div>
                <!-- Collect the nav links, forms, and other content for toggling -->
                <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                    <ul class="nav navbar-nav">"""
    return

#######################################################################################################

def banner_viewer():
    print """                        <li>
                            <a href="viewer_order.py">Orders</a>
                        </li>
                        <li>
                            <a href="viewer_edit_profile.py?userName=%s">Edit Profile</a>
                        </li>
                        <li>
                            <a href="do_logout.py">Logout</a>
                        </li>"""%(sess.data['userName'])
    return

#######################################################################################################

def banner_player():
    print """                        <li>
                            <a href="player_find_viewer.py">Manage Viewers</a>
                        </li>
                        <li>
                            <a href="player_view_instanceruns.py">Manage Instances</a>
                        </li>
                        <li>
                            <a href="player_manage_games.py">Manage Games</a>
                        </li>
                        <li>
                            <a href="player_view_achievements.py">Manage Achievements</a>
                        </li>
                        <li>
                            <a href="player_edit_profile.py">Edit Profile</a>
                        </li>
                        <li>
                            <a href="do_logout.py">Logout</a>
                        </li>"""
    return

#######################################################################################################

def banner_default():
    print """                        <li>
                            <a href="login.py">Login</a>
                        </li>"""
    return;

#######################################################################################################

def print_welcome(first_name, last_name):
    print """        <div style="text-align:center" class="col-lg-4 col-lg-offset-4">
            <h3>Welcome back %s</h3>
        </div>"""%(first_name + " " + last_name)
    return

#######################################################################################################

def close_banner():
    print """                    </ul>
                </div>
                <!-- /.navbar-collapse -->
            </div>
            <!-- /.container -->
        </nav>"""
    return

#######################################################################################################

def close_html():
    print """
        <!-- jQuery Version 1.11.0 -->
        <script src="js/jquery-1.11.0.js"></script>

        <!-- Bootstrap Core JavaScript -->
        <script src="js/bootstrap.min.js"></script>

    </body>

    </html>
    """
    return

#######################################################################################################

def print_videos(title, headings, body, loggedIn):
    print_title(title)
    open_table()
    table_heading(headings)
    for row in body:
        table_body(row, loggedIn)
    if loggedIn == 2:
        add_video()
        for i in range(1, len(body[0]) - 3):
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
                    <th><a href="%s">%s</a></th>"""%(redirect.getQualifiedURL("viewer_order.py?vidid=%s"%content[0]) if loggedIn in (1, 2) else redirect.getQualifiedURL("login.py"), content[1])
    for item in content[2:5]:
        print"                    <td>%s</td>"%item
    print"""<td><a href="%s">%s</a></td>"""%(redirect.getQualifiedURL("view_player_details.py?playerID=%s"%content[6]), content[5])
    print"""<td><a href="%s">%s</a></td>"""%(redirect.getQualifiedURL("view_equipment_details.py?equipID=%s"%content[8]), content[7])
    print "                </tr>"
    return

#######################################################################################################

def add_video():
    print """                <tr>
                    <th style="text-align:center"><a class="btn btn-primary btn-block" roll="button" href="%s">Add Video</a></th>"""%(redirect.getQualifiedURL("add_video.py"))
    return

#######################################################################################################

def close_table():
    print """            </tbody>
        </table>
        </div>"""
    return

#######################################################################################################
