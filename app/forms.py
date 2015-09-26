from flask.ext.wtf import Form
from wtforms import HiddenField, PasswordField, TextField
from wtforms.validators import Length, Required


class LoginForm(Form):
    librarian_username = TextField("Username",
      [Required(message="Enter your username"), Length(max=50)])
    librarian_password = PasswordField("Password", [Required(message="Enter your password")])
