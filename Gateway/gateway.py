import time
import ftplib
import os, sys, os.path


sourcep = '/home/sdn/Desktop/containernet/Grids/'
destp = 'Desktop/containernet/Backend/'
filecount = 0
mainsubs = 0
primarysubs = 0
waitt = 5


while True:
	print('Waiting to push data to Backend. Waiting time is:')
	print(waitt)
	
	time.sleep(waitt)
	print('Pushing files to Backend')
	filecount = 0
	mainsubs = 0
	primarysubs = 0
	
	print('connecting to ftp server')
	ftp = ftplib.FTP('10.0.0.3')

	print('logging in')
	ftp.login(user='sdn', passwd = 'rocks')
	print('login success')

	ftp.cwd(destp)
	os.chdir(sourcep)	
	dirgate = os.listdir(sourcep)
	dirback = ftp.nlst()
	
	for foldername in dirgate:
		if foldername not in dirback:
			print('I need to create a directory for %s.' % foldername)
			ftp.mkd(foldername)
			mainsubs = mainsubs + 1
			
		os.chdir(sourcep + '/' + foldername)	
		ftp.cwd(foldername)	
		dirgate2 = os.listdir(sourcep + '/' + foldername)
		
		try:
			dirback2 = ftp.nlst()
		except ftplib.error_perm, resp:
				err = str(resp)
				
				if err == "550 No files found.":
					ftp.mkd('temp')
					dirback2 = ftp.nlst()
			
		for foldername2 in dirgate2:
			if foldername2 not in dirback2:
				print('I need to create a directory for  %s.' % foldername2)
				ftp.mkd(foldername2)
				primarysubs = primarysubs + 1
				
			os.chdir(sourcep + '/' + foldername + '/' + foldername2)	
			ftp.cwd(foldername2)	
			dirgate3 = os.listdir(sourcep + '/' + foldername + '/' + foldername2)
		
			try:
				dirback3 = ftp.nlst()
			
			except ftplib.error_perm, resp:
				err = str(resp)

				if err == "550 No files found.":
					ftp.mkd('temp')
					dirback3 = ftp.nlst()
				else:
					raise
	
			for foldername3 in dirgate3:
				if foldername3 not in dirback3:
					print('I need to create a directory for %s.' % foldername3)
					ftp.mkd(foldername3)
					
				os.chdir(sourcep + '/' + foldername + '/' + foldername2 + '/' + foldername3)
				ftp.cwd(foldername3)	
				dirgate4 = os.listdir(sourcep + '/' + foldername + '/' + foldername2 + '/' + foldername3)

				try:
					dirback4 = ftp.nlst()
				except ftplib.error_perm, resp:
					err = str(resp)

					if err == "550 No files found.":
						ftp.mkd('temp')
						dirback4 = ftp.nlst()
							
				for filename in dirgate4:
					if filename not in dirback4:
						print('I need to copy the file %s.' % filename)
						ftp.storbinary('STOR '+filename, open(filename, 'rb'))
						os.remove(filename)
						filecount = filecount + 1
				newdir = '/home/sdn/' + destp + foldername +'/'+ foldername2 
	   			ftp.cwd(newdir)
	
			newdir2 = '/home/sdn/' + destp + foldername 
	   		ftp.cwd(newdir2)
		
	ftp.quit()
	print('New main substaions added:')
	print(mainsubs)
	print('New primary substaions added:')
	print(primarysubs)
	print('New files copied:')
	print(filecount)