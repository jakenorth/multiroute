# Enter your custom config code here
params = {
	"no-www": True
}
routes = {
	"example.com": "example"
}

def config():
	return([params,routes])