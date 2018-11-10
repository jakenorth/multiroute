from flask import *
import router
app = Flask(__name__)

@app.route('/<path:path>')
def catchall(path):
	router.route(path,request)
	return("Done!")

app.run()