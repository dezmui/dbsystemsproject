# The libraries we'll need
import sys, cgi, redirect, session, html_template as html, login_form_html as form

sess = session.Session(expires=20*60, cookie_path='/')
loggedIn = sess.data.get('loggedIn')

#######################################################################################################

def main():
    if loggedIn in (1, 2):
        redirect.refresh("home.py", sess.cookie)
        return
    
    params = cgi.FieldStorage()
    cookie = sess.cookie
    html.open_html(cookie, 0)
    form.print_form(params.has_key('error'))
    html.close_html()
    sess.close()
    return

#######################################################################################################

main()
