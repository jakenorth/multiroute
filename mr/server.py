from flask import *
import router
app = Flask(__name__)

@app.route('/<path:path>')
def catchall(path):
	return(router.response(path,request))