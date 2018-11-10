# Enter your custom config code here

routes = {
	"localhost:5000": "example"
}

def route(host):
	return(routes[host])