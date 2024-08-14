"""display simple text on screen"""
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def vasu():
#     return 'Hello, Srinivas Raju!'

# if __name__ == '__main__':
#     app.run()



"""creating page based on admin, student, staff"""
# from flask import *


# app = Flask(__name__)

# @app.route('/admin')
# def admin():
#     return 'This is Admin'

# @app.route('/student')
# def student():
#     return 'This is Student'

# @app.route('/staff')
# def staff():
#     return 'This is Staff'

# @app.route('/user/<name>')
# def user(name):
#     if name == 'admin':
#         return redirect(url_for('admin'))
#     if name == 'student':
#         return redirect(url_for('student'))
#     if name == 'staff':
#         return redirect(url_for('staff'))

# if __name__ == '__main__':
#     # app.run()
#     app.run(debug=True)

"""display URL if we paste  http://127.0.0.1:5000/vasu/"""
# from flask import Flask

# app = Flask(__name__)

# @app.route('/vasu')
# def vasu():
#     return 'Hello, Srinivas Raju!'

# if __name__ == '__main__':
#     app.run()


""" concatinate the string in URL and PAGE  http://127.0.0.1:5000/vasu/howRU"""
# from flask import Flask

# app = Flask(__name__)

# @app.route('/vasu/<name>')
# def vasu(name):
#     return 'Hello Srinivas Raju '+name

# if __name__ == '__main__':
#     app.run(debug = True)

""" concatinate the integer in URL and PAGE  http://127.0.0.1:5000/vasu/15000"""
# from flask import Flask

# app = Flask(__name__)

# @app.route('/vasu/<int:sub>')
# def vasu(sub):
#     return 'Please Subscribe=%d ' %sub

# if __name__ == '__main__':
#     app.run(debug = True)

"""add url rule function  http://127.0.0.1:5000/vasu"""
# from flask import Flask

# app = Flask(__name__)

# def vasu():
#     return 'Please Subscribe'

# app.add_url_rule('/vasu','vasu',vasu)

# if __name__ == '__main__':
#     app.run(debug = True)

""" Flask Templates calling the base html file into python file
http://127.0.0.1:5000/user/srinivasRaju
"""

# from flask import *

# app = Flask(__name__)

# @app.route('/user/<name>')
# def vasu(name):
#     return render_template('base.html',name = name)

# if __name__ == '__main__':
#     app.run(debug = True)

"""adding css,html to Flask template"""
# from flask import *

# app = Flask(__name__)

# @app.route('/')
# def vasu():
#     return render_template('base.html')

# if __name__ == '__main__':
#     app.run(debug = True)

"""Flask HTTP Methods"""
"""get method from crud operation"""
# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/login', methods=['GET'])
# def login():
#     uname = request.args.get('uname')
#     passwrd = request.args.get('pass')
#     if uname == "ayush" and passwrd == "google":
#         return "Welcome %s" % uname
#     else:
#         return "Invalid  %s" % uname

# if __name__ == '__main__':
#     app.run(debug=True)

"""post method"""
# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/login', methods=['POST'])
# def login():
#     uname = request.form['uname']
#     passwrd = request.form['pass']
#     if uname == "vasu" and passwrd == "vasu":
#         return "Welcome %s" % uname
#     else:
#         return "Invalid  %s" % uname

# if __name__ == '__main__':
#     app.run(debug=True)




