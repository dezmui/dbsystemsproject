import os, string

#######################################################################################################

def getEnvValue(value):
    """ Return an environment value. """
    env = os.environ
    return env[value]

#######################################################################################################

def isSSL():
    """ Return true if we are on a SSL (https) connection. """
    return os.environ.get('SSL_PROTOCOL', '') != ''

#######################################################################################################

def getScriptname():
    """ Return the scriptname part of the URL ("/path/to/my.cgi"). """
    return os.environ.get('SCRIPT_NAME', '')

#######################################################################################################

def getPathinfo(filename):
    """ Return the remaining part of the URL. """
    #pathinfo = os.environ.get('PATH_INFO', '')
    
    pathinfo = os.path.dirname(os.path.realpath(filename))
    pathinfo = pathinfo.replace("home", "serve");
    # Fix for bug in IIS/4.0
    if os.name == 'nt':
        scriptname = getScriptname()
        if string.find(pathinfo, scriptname) == 0:
            pathinfo = pathinfo[len(scriptname):]                
    
    return pathinfo

#######################################################################################################

def getQualifiedURL(uri = None):
    """ Return a full URL starting with schema, servername and port.

        *uri* -- append this server-rooted uri (must start with a slash)
    """
    schema, stdport = (('http', '80'), ('https', '443'))[isSSL()]
    host = getEnvValue('HTTP_HOST')
    pathinfo = getPathinfo(uri)
    if not host:
        host = getEnvValue('SERVER_NAME')
        port = getEnvValue('SERVER_PORT', '80')
        if port != stdport: host = host + ":" + port

    result = "%s://%s%s/" % (schema, host,pathinfo)
    if uri: result = result +uri
    
    return result

#######################################################################################################

def getBaseURL():
    """ Return a fully qualified URL to this script. """
    return getQualifiedURL(getScriptname())

#######################################################################################################

def refresh(whereTo, cookie):
    print "%s\nContent-Type: text/html\n" % (cookie)
    print """\
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
        <head>
            <meta http-equiv="content-type" content="text/html; charset=utf-8" />
            <meta http-equiv="refresh" content="0;url=%s">
        </head>
        <body>
        </body>
    </html>""" % getQualifiedURL("%s"%whereTo)
    return

#######################################################################################################

def goto(whereTo, cookie):
    print "%s\nContent-Type: text/html\n" % (cookie)
    print """\
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
        <head>
            <meta http-equiv="content-type" content="text/html; charset=utf-8" />
            <meta http-equiv="refresh" content="0;url=%s">
        </head>
        <body>
        </body>
    </html>""" % whereTo
    return

#######################################################################################################

#example (redirect)
#print "Location:", getQualifiedURL("/go/here")
