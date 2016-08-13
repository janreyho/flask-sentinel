from flask import Flask
from flask.ext.sentinel import ResourceOwnerPasswordCredentials, oauth


app = Flask(__name__)

# optionally load settings from py module
app.config.from_object('settings')

@app.route('/endpoint')
@oauth.require_oauth()
def restricted_access():
    return "You made it through and accessed the protected resource!"

if __name__ == '__main__':
    ResourceOwnerPasswordCredentials(app)
    app.run(ssl_context='adhoc')
