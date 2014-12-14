from hellowWeb import hellowWeb

@hellowWeb.route('/')
@hellowWeb.route('/index')
def index():
    return "Hello, World!"
