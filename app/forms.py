from flask.ext.wtf import Form
from wtforms import HiddenField, PasswordField, TextField
from wtforms.validators import Length, Required


class LoginForm(Form):
    app_username = TextField("Username",
      [Required(message="Enter your username"), Length(max=50)])
    app_password = PasswordField("Password", [Required(message="Enter your password")])
    
    def __str__(self):
        return str(self.app_username.data) + " // " + str(self.app_password.data)
