from random import random
from random import randrange
import time
import datetime
from ftplib import FTP
import socket
import os
import ftplib

fthres = 500
dtime = str(datetime.datetime.now())
Sname = "Sensors " + dtime + ".txt"
Dname = "Device " + dtime + ".txt"

class Device:
  def __init__(self,Name,threshold,volt_range,volt_offset,amp_range,amp_offset, temp_range, temp_offset, hum_range, hum_offset):
  
    self.SubID = Name
    self.threshold = threshold
    self.volt_range = volt_range
    self.volt_offset = volt_offset
    self.amp_range = amp_range
    self.amp_offset = amp_offset
    self.temp_range = temp_range
    self.temp_offset = temp_offset
    self.hum_range = hum_range
    self.hum_offset = hum_offset
    self._recognised_devices = {}
    self.statuses = [
    	'Breaker1',
    	'Breaker2',
    	'Transformer1',
    	'Door1',
    	'SecurityAlarm'
    	]
    self.sensors = [
	'VoltsR',
	'VoltsW',
	'VoltsB',
	'AmpsR',
	'AmpsW',
	'AmpsB',
	'Temp',
	'Humid'
	]
	

def create_sensor_data(self,sensor,value):
	if sensor.startswith('Volts'):
		data = {
			'value' : value,
			'type' : 'Voltage',
			'unit' : 'V',
			'timest': str(datetime.datetime.now())
		}
	if sensor.startswith('Amps'):
	
		data = {
			'value' : value,
			'type': 'Current',
			'unit': 'A',
			'timest': str(datetime.datetime.now())
		}
	if sensor.startswith('Temp'):
	
		data = {
			'value' : value,
			'type': 'Temperature',
			'unit': 'deg C',
			'timest': str(datetime.datetime.now())
		}
	if sensor.startswith('Humid'):
	
		data = {
			'value' : value,
			'type': 'Hmudity',
			'unit': 'g/m3',
			'timest': str(datetime.datetime.now())
		}	
	
			
	file1 = open(Sname, "a+")
		
	file1.write('%s: %s: %s' % (self.SubID, sensor, data))
	
	file1.close()
	
	
def create_device_data(self,status,value):
	if status.startswith('Breaker'):
		data = {
			'value' : value,
			'type' : 'Breaker Position',
			'timest': str(datetime.datetime.now())
		}
	if status.startswith('Transformer'):
	
		data = {
			'value' : value,
			'type': 'Transformer Health',
			'timest': str(datetime.datetime.now())
		}
	if status.startswith('Door'):
	
		data = {
			'value' : value,
			'type': 'Door position',
			'timest': str(datetime.datetime.now())
		}
	if status.startswith('Security'):
	
		data = {
			'value' : value,
			'type': 'Security Alarm',
			'timest': str(datetime.datetime.now())
		}	
			
	file2 = open(Dname, "a+")
		
	file2.write('%s: %s: %s' % (self.SubID, status, data))
	
	file2.close()
	

def create_device_structure(self,Sname):
	
	self._recognised_devices[Sname] = 'Active'
	
	print('connecting to ftp server')
	
	server1 = '10.0.0.1'
	server2 = '10.0.0.2'
	
	ftp = ftplib.FTP()
	
	try: 
		ftp.connect(server1)
		print('connected to: %s' % server1) 
	
	except ftplib.all_errors, error:
   		print "Cannot connect:", error
   		print("Connecting to alternate Gateway")
   		try:
   			ftp.connect(server2)
			print('connected to: %s' % server2)
		except ftplib.all_errors, error:
			raise
		
	print('logging in')
	ftp.login(user='sdn', passwd = 'rocks')
	print('login success')

	
	ftp.cwd('Desktop/containernet/Grids/Greenpoint/')
	
	
	foldername = Sname
	foldernames = ftp.nlst()
	
	if foldername not in foldernames:
		print('I need to create a gateway structure for the device %s.' % foldername)
		ftp.mkd(foldername)
		ftp.cwd(foldername)
		ftp.mkd('Sensor Data')
		ftp.mkd('Device Data') 
	ftp.quit()
	
	
	

def handle_device_data(self,Sname,sensor,value, status, dvalue):
		if Sname not in self._recognised_devices:
			create_device_structure(self,Sname)
		print('creating a sensor data for: %s' % sensor)
		create_sensor_data(self,sensor,value)
		print('creating a device data for: %s' % status)
		create_device_data(self,status,dvalue)

def get_random_data(self):
	
	if random() > self.threshold:
		sensor = self.sensors[int(random() * len(self.sensors))]
		
		if sensor.startswith('Volts'):
			value_range = self.volt_range
			value_offset = self.volt_offset
		if sensor.startswith('Amps'):
			value_range = self.amp_range
			value_offset = self.amp_offset
		if sensor.startswith('Temp'):
			value_range = self.temp_range
			value_offset = self.temp_offset
		if sensor.startswith('Humid'):
			value_range = self.hum_range
			value_offset = self.hum_offset	
		value = int(random() * value_range + value_offset)
		
		device = self.statuses[int(random() * len(self.statuses))]
		if device.startswith('Breaker'):
			option1 = 'Closed'
			option2 = 'Open'
		if device.startswith('Transformer'):
			option1 = 'Healthy'
			option2 = 'Unhealthy'
		if device.startswith('Door'):
			option1 = 'Closed'
			option2 = 'Open'
		if device.startswith('Security'):
			option1 = 'Alarm'
			option2 = 'No Alarm'	
		outcome = int(random()*10)
		
		if outcome > 4:
			dvalue = option1
		else:
			dvalue = option2
		
		Sname = self.SubID
		handle_device_data(self,Sname,sensor,value, device, dvalue)
	
def push_sensor_data(self):

	print('connecting to ftp server')
	
	server1 = '10.0.0.1'
	server2 = '10.0.0.2'
	
	ftp = ftplib.FTP()
	
	try: 
		ftp.connect(server1)
		print('connected to: %s' % server1) 
	
	except ftplib.all_errors, error:
   		print "Cannot connect:", error
   		print("Connecting to alternate Gateway")
   		try:
   			ftp.connect(server2)
			print('connected to: %s' % server2)
		except ftplib.all_errors, error:
			raise
	print('logging in')
	ftp.login(user='sdn', passwd = 'rocks')
	print('login success')

	
	ftp.cwd('Desktop/containernet/Grids/Greenpoint/'+ self.SubID + '/Sensor Data')
	
	
	filename = Sname
	ftp.storbinary('STOR '+filename, open(filename, 'rb'))
	ftp.quit()
	
	print("sensor data is pushed to gateway")
	
	print('deleting: ' + filename + ' in:')
	print(os.getcwd())
	
	os.remove(filename)

	
def push_device_data(self):

	print('connecting to ftp server')
	
	server1 = '10.0.0.1'
	server2 = '10.0.0.2'
	
	ftp = ftplib.FTP()
	
	try: 
		ftp.connect(server1)
		print('connected to: %s' % server1) 
	
	except ftplib.all_errors, error:
   		print "Cannot connect:", error
   		print("Connecting to alternate Gateway")
   		try:
   			ftp.connect(server2)
			print('connected to: %s' % server2)
		except ftplib.all_errors, error:
			raise

	print('logging in')
	ftp.login(user='sdn', passwd = 'rocks')
	print('login success')

	
	ftp.cwd('Desktop/containernet/Grids/Greenpoint/'+ self.SubID + '/Device Data')
	print(os.getcwd())
	
	filename2 = Dname
	ftp.storbinary('STOR '+filename2, open(filename2, 'rb'))
	ftp.quit()
	
	print("device data is pushed to gateway")
	
	print('deleting: ' + filename2 + ' in:')
	print(os.getcwd())
	os.remove(filename2)
		

d1 = Device('Cape Royal', 0, 20, 400, 3, 10, 10, 45, 5, 30)


Fcount = 0

while True:
	
	time.sleep(0.02)
	get_random_data(d1)
	Fcount = Fcount +1
	
	if Fcount == fthres:
		push_sensor_data(d1)
		push_device_data(d1)
		Fcount = 0
		dtime = str(datetime.datetime.now())
		Sname = "Sensors " + dtime + ".txt"
		Dname = "Device " + dtime + ".txt"
	
		

	