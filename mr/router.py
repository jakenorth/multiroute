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
	jobid = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(3)])
	#Write job file
	jobfile = open("jobs/"+jobid+".job","w+")
	jobfile.write('~&&~'.join([path,str(request.args)]))
	jobfile.close()
	#Write to manifest
	manfile = open("jobs/"+route_goal+".man","a+")
	manfile.write(jobid+".job~&&~")
	return(jobid,route_goal)
def respond(path, request):
	#File Job Request
	jobid, route_goal = route(path,request)
	#Wait for reply
	import time
	import os
	while True:
		time.sleep(0.05)
		try:
			#Get response text
			responsefile = open("jobs/"+jobid+".res","r")
			response = responsefile.read()
			responsefile.close()
			#Remove files from job
			os.system('rm ' + "jobs/" + jobid + ".job")
			os.system('rm ' + "jobs/" + jobid + ".res")
			#Remove job from manifest
			print("about to open man file")
			manfile = open("jobs/"+route_goal+".man","w+")
			print("opened man file")
			manitext = manfile.read()
			print(jobid+".job~&&~")
			manfile.write(manitext.replace(jobid+".job~&&~", ""))
			print(jobid+".job~&&~")
			#Return the respones text
			return(response)
		except:
			pass
