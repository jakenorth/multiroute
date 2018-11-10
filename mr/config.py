# Enter your custom config code here

routes = {
	"example.com": "example"
}

def route(host):
	return(routes[host])