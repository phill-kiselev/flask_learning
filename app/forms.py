from flask_wtf import Form
from wtforms import TextField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import Required, Length
from .models import User

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)
    submit = SubmitField('OK')

class LoginForm2(Form):
    nickname = TextField('nickname', validators = [Required()])
    mail = TextField('mail', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)
    submit = SubmitField('OK')
    
class RegisterForm(Form):
    nickname = TextField('nickname', validators = [Required()])
    mail = TextField('mail', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)
    submit = SubmitField('OK')
    
    def validate(self):
        if not Form.validate(self):
            return False
        user1 = User.query.filter_by(nickname = self.nickname.data).first()
        if user1 != None:
            self.nickname.errors.append('This nickname is already in use. Please choose another one.')
            return False
        user1 = User.query.filter_by(email = self.mail.data).first()
        if user1 != None:
            self.mail.errors.append('This nickname is already in use. Please choose another one.')
            return False
        return True
    
class EditForm(Form):
    nickname = TextField('nickname', validators = [Required()])
    about_me = TextAreaField('about_me', validators = [Length(min = 0, max = 140)])
    
    def __init__(self, original_nickname, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname

    def validate(self):
        if not Form.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        user = User.query.filter_by(nickname = self.nickname.data).first()
        if user != None:
            self.nickname.errors.append('This nickname is already in use. Please choose another one.')
            return False
        return True

class PostForm(Form):
    post = TextField('post', validators = [Required()])
    
class SearchForm(Form):
    search = TextField('search', validators = [Required()])