from django.core.management.base import BaseCommand, CommandError
from apscheduler.scheduler import Scheduler
from django.core.mail import send_mail
from master.models import IpServer
from django.core.exceptions import ObjectDoesNotExist

def job_function():
	try:
		myip = urllib2.urlopen('http://www.curlmyip.com').read()
	except urllib2.HTTPError, e:
		myip = ''
	if myip:
		myip =  myip.split(' ')[0].split('\n')[0]
		try:
			ip_history 		= IpServer.objects.get(pk=1)
		except ObjectDoesNotExist, e:
			ip_history 		= IpServer()
			ip_history.ip 	= myip
			ip_history.save()
			correo = send_mail('cambio de Ip', myip, 'info hiko',['lastvnm@gmail.com'], fail_silently=True)
		if not myip == ip_history.ip:
			correo = send_mail('cambio de Ip', myip, 'info hiko',['lastvnm@gmail.com'], fail_silently=True)
			ip_history.ip = myip
			ip_history.save()

class comando(BaseCommand):
	def handle(self, *args, **options):
		sched = Scheduler(daemonic=True)
		sched.add_cron_job(job_function,  minute='*')
		sched.configure()
		try:
		    sched.start()
		except (KeyboardInterrupt, SystemExit):
		    pass
		print sched.print_jobs()
