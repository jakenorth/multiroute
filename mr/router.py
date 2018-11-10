def route(path, request):
	#Extract Host
	host = (request.url.split('://',1)[1]).split('/',1)[0]
	if host[0:4] == "www.":
		host = host[4:len(host)]
	#Get Route Goal
	import config
	route_goal  = config.route(host)
	#Generate Job ID
	import string
	import random
	jobid = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
	#Write job file
	jobfile = open("jobs/"+jobid+".job","w+")
	jobfile.write('~&&~'.join([path,str(request.args)]))
	jobfile.close()
	#Write to manifest
	manfile = open("jobs/"+route_goal+".man","a+")
	manfile.write(jobid+".job~&&~")