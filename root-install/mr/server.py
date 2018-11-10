from flask import *
import router
app = Flask(__name__)

@app.route('/<path:path>')
def catchall(path):
	return(router.respond(path,request))

app.run()