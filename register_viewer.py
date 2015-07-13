import sys, session, cgi, MySQLdb, redirect, sql_handler as sql, html_template as html, register_viewer_html as form

sess = session.Session(expires=20*60, cookie_path='/')
loggedIn = sess.data.get('loggedIn')
params = cgi.FieldStorage()

#######################################################################################################

def main():
    html.open_html(sess.cookie, loggedIn)
    error = False
    if params.has_key('error'):
        error = True
    print_body(error)

    html.close_html()
    sess.close()
    return

#######################################################################################################

def print_body(error):
    form.print_details(error)
    return

#######################################################################################################

main()
