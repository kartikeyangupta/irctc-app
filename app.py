from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from forms import *
import os
from config import *


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

@app.route('/add/user', methods=['GET'])
def add_user():
    # username = request.para
    return render_template('pages/placeholder.home.html'), 200


@app.route('/add/image/',)
def add_image():
    return render_template('pages/placeholder.add_image.html'), 200

@app.route('/add/image/render/<string:filename>',methods = ['GET', 'POST'])
def render_image(filename):
    if request.method == 'POST':
        image = request.file['image']
        anwser = "THIS IS THE CORRECT ANWSER"
        # anwser = get_anwser(image)
        return anwser, 200
    else:
        return jsonify({'result' : filename }), 200

# Error handlers.


@app.errorhandler(500)
def internal_error(error):
    return jsonify({'result': False, "message":"Internal Server error"}), 500


@app.errorhandler(404) 
def not_found(error):
    return jsonify({'result': False, "message": "API doesn't exist"}), 404
    

# if not app.debug:
#     file_handler = FileHandler('error.log')
#     file_handler.setFormatter(
#         Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
#     )
#     app.logger.setLevel(logging.INFO)
#     file_handler.setLevel(logging.INFO)
#     app.logger.addHandler(file_handler)
#     app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
# if __name__ == '__main__':
#     app.run()

# Or specify port manually:

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # 127.0.0.1
