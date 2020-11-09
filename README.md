# virtual-smart-distribution-grids
This repository contains the files that were developed in a project that studied the effectiveness of using software-based networking to improve the reliability of smart distribution grids. It uses the ONOS Tutorial VM with Mininet to create and test virtual network designs capable of supporting batch data acquisition applications for smart grids. 

![alt text](https://github.com/gerhard-brown/virtual-smart-distribution-grids/blob/main/Platform.png?raw=true)

Instructions for setting up this platform are as follows:

1.	Installation:

Download and install VirtualBox (https://www.virtualbox.org/wiki/Downloads) and then launch the ONOS Tutorial VM obtainable from the ONOS project website (https://wiki.onosproject.org/display/ONOS/Basic+ONOS+Tutorial).  

If you are unfamiliar with ONOS, we recommend that you complete the instructions on the tutorial webpage first. When setting up the VM for the first time, we also recommend that you allocate sufficient processing and memory resources to accommodate the size of the network you plan to set up. You may also need to add a NAT and a Host Only network adapter. For our setup we used the following configuration:

Base memory – 6000 MB

Processors – 4

Network adapter 1 – NAT

Network adapter 2 – Host-only adapter


After launching the VM for the first time, ensure that the following additional software has been installed and updated to their latest versions. You may also need to configure the FTP Service and the VM's firewall setting to allow for file exchanges between the host VM's you will be creating. 

-	Python Compiler ( https://docs.python-guide.org/starting/install3/linux/)
-	FTP Client/Server ( https://ubuntu.com/server/docs/service-ftp
-	Mininet: http://mininet.org/download/
-	Wireshark:  (https://www.wireshark.org/docs/wsug_html_chunked/ChBuildInstallUnixInstallBins.html#_installing_from_debs_under_debian_ubuntu_and_other_debian_derivatives)

2.	Network Setup and Configuration

Follow the instructions provided on the ONOS Tutorial Webpage to initialise three ONOS cluster nodes. The ONOS GUI can then be launched to verify each allocated controller’s IP address, which should be noted for the remote controller setup. Also ensure that the Reactive Forwarding application is activated for the the ONOS controllers.
Mininet can then be used to set up a topology for the virtual communication network that will support your chosen distribution grid design. As a more user friendly alternative to the scripting method for setting up network topologies, we recommend using MiniEdit (http://www.brianlinkletter.com/how-to-use-miniedit-mininets-graphical-user-interface/).
A copy of a MiniEdit network topology file (GreenPoint.mn), developed for our model of a small distribution grid section in Cape Town is provided in this repo. This file can opened in MiniEdit using the File -> Open command. 

Once the network topology has been set up, confirm that “controller type” setting for each SDN controllers placed, has been set to “Remote controller” and that each of the controllers are mapped to an ONOS controller instance with the corresponding IP addresses. Also verify that each virtual host has its own unique IP address and that two Gateway virtual hosts have the IP addresses: 10.0.0.1 and 10.0.0.2 respectivly. The Backend host’s IP address must be 10.0.0.3. Lastly, adjust the parameters on the network links according to your grid model. In our model we used a 10 Mbps bandwidth limit on the NAN network links an 100 Mbps on the backhaul networks.

3.	Host Setup and Configuration

This repo includes 15 python files, each representing the 15 substations in the network, that contain the scripts for simulating batch data generation and transfer to a central data repository. It also contains a Python file called “Gateway.py” that contains the script for the Gateway substations that perform data aggregation and scheduling functions. Each of these Python files needs to be placed in its own folder so that it can be easily accessed by the virtual host instances created by Mininet. 

A separate directory also needs to be created on the ONOS Tutorial VM to act as a storage location for Gateway substations since this path is currently hard coded in Python scripts.  The directory structure should be created exactly as follows: /home/sdn/Desktop/containernet/Grids/

Another directory structure also needs to be created for the Backend data repository. The path of this directory must be:  Desktop/containernet/Backend/

4.	Execution

After these directory structures have been created and the files have been copied to their respective folders, the virtual network can be instantiated by hitting the “Run” button in the MiniEdit screen. The detected network topology should now appear on the ONOS GUI’s topology view. The “pingall” command should then be executed in the Mininet CLI to confirm that each created virtual host is reachable by the others. 

With the network active, terminal windows can now be launched for each virtual host from where the relevant Python programs can be executed.  Note, that the “inetd” command may need to be executed on the Gateway terminals if the ftp connections are refused.

The Python programs will simulate the generation and acquisition of data according to the following two procedures:

![alt text](https://github.com/gerhard-brown/virtual-smart-distribution-grids/blob/main/Python%20Procedures.JPG?raw=true)

For those with knowledge with Python programming, the following parameters may be adjusted:

Parameter	Description

fthres:	The file threshold that determines the amount of readings per text file before transfer to a Gateway Host.

volt_range:	The voltage range for generated voltage sensor readings.

volt_offset:	The offset value with which voltage readings can vary. 

amp_range:	The electrical current range for generated current sensor readings.

amp_offset:	The offset value with which current readings can vary. 

temp_range:	The temperature range for generated temperature sensor readings.

temp_offset:	The offset value with which temperature readings can vary. 

hum_range:	The humidity range for generated humidity sensor readings.

hum_offset:	The offset value with which humidity readings can vary. 

waitt:	The time a Gateway host will wait before it transfers its files to the Backend host.

 



