#######################################################################################################

def print_form(error):
    print """        <div class="col-md-2 col-md-offset-5">
            <div class="well bs-component">"""
    if error:
        print_error()
    print"""                <form class="form-horizontal" method="post" action="do_login.py">
                    <fieldset>
                        <legend style="text-align:center">Login</legend>
                        <div class="form-group">
                            <label for="username" class="col-lg-2 control-label">Username:</label>
                            <div class="col-lg-8 col-lg-offset-2">
                                <input class="form-control" name="username" placeholder="Username" type="text">
                            </div>
                        </div>
                        <div class="form-group">
                            <label for="password" class="col-lg-2 control-label">Password:</label>
                            <div class="col-lg-8 col-lg-offset-2">
                                <input class="form-control" name="password" placeholder="Password" type="password">
                            </div>
                        </div>
                            <div class="form-group">
                                <label class="col-md-4 control-label">Login as:</label>
                            <div class="col-lg-6 col-lg-offset-2">
                                <div class="radio">
                                    <label>
                                        <input name="loginType" id="Viewer" value="V" checked="" type="radio">
                                            Viewer
                                    </label>
                                    <label>
                                        <input name="loginType" id="Player" value="P" type="radio">
                                            Player
                                    </label>
                                </div>
                            </div>
                        </div>
                        <div class="form-group">
                            <div class="col-lg-5 col-lg-offset-1">
                                <button type="submit" class="btn btn-primary">Login</button>
                            </div>
                            <div class="col-lg-5">
                                <a class="btn btn-primary" roll="button" href="register_viewer.py">Register</a>
                            </div>
                        </div>
                    </fieldset>
                </form>
            </div>
        </div>"""
    return

#######################################################################################################

def print_error():
    print """                                <div class="form-group" style="text-align:center">
                                    <label class="col-lg-8 col-lg-offset-2 control-label" style="color:red">Login error.</label>
                                </div></br>"""
    return

#######################################################################################################
