# virtual-smart-distribution-grids
This repository contains the files that were developed in a project that studied the effectiveness of using software-based networking to improve the reliability of smart distribution grids.
Virtual Networks for Smart Distribution Grids

This repo contains a VM that was used to set up a virtual networking platform for evaluating networks designs for batch data acquisition in smart grids. It created using the ONOS Tutorial VM basis for creating virtual networks using Mininet. The architecture for this platform is shown in the diagram below. 
 
Instructions for setting up this platform are as follows:

1.	Installation:

Download and install VirtualBox (https://www.virtualbox.org/wiki/Downloads) and then launch the Virtual Smart Distribution Girds VM supplied in the repo. If you are unfamiliar with Mininet or ONOS, we recommend that you complete Mininet (http://mininet.org/ ) and ONOS (https://wiki.onosproject.org/display/ONOS/Basic+ONOS+Tutorial) tutorials first. 

2.	Network Setup and Configuration

a.	Initialise three ONOS cluster nodes by double clicking on the shortcut: “Setup ONOS Cluster”

b.	Activate the Reactive Forwarding application  by entering the following command in the ONOS CLI: app.activate org.onosproject.fwd

c.	The ONOS GUI can then be launched by double clicking on the “ONOS GUI” shortcut.

Mininet is used to set up a topology for the virtual communication network that will support your chosen distribution grid design. As a more user friendly alternative to the scripting method for setting up network topologies, we recommend using MiniEdit (http://www.brianlinkletter.com/how-to-use-miniedit-mininets-graphical-user-interface/).

Launch MiniEdit using shortcut: “Launch MiniEdit”

A copy of a MiniEdit network topology file (GreenPoint.mn), developed for our model of a small distribution grid section in Cape Town is provided in this VM in the following folder:/home/sdn/Desktop/containernet/examples/MiniEdit Topology/

This file can opened in MiniEdit using the File -> Open command. 

Once the network topology has been set up, confirm that “controller type” setting for each SDN controllers placed, has been set to “Remote controller” and that each of the controllers are mapped to an ONOS controller instance with the corresponding IP addresses. Also verify that each virtual host has its own unique IP address and that two Gateway virtual hosts have the IP addresses: 10.0.0.1 and 10.0.0.2. The Backend host’s IP address must be 10.0.0.3. Lastly, adjust the parameters on the network links according to your grid model. For our model we limited the bandwidth of the NAN networks to 10 MBbps.

3.	Host Setup and Configuration

This VM includes folders with 15 python files, each representing the 15 substations in the network, that contain the scripts for simulating batch data generation and transfer to a central data repository. They are labled: sh, gp,oj,rf,bs,rs,pr,gb,grb,vv,dh,3ab,clr,mp and cr . This folder also contains a Python file called “Gateway.py” that contains the script for the Gateway substations that perform data aggregation and scheduling functions. The path for these folders is: 

home/sdn/Desktop/containernet/Grids/

A separate directory was created to act as the storage location for Gateway substations: 

/home/sdn/Desktop/containernet/Grids/

And for the Backend data repository: 

Desktop/containernet/Backend/

4.	Execution

The virtual network must be instantiated by hitting the “Run” button in the MiniEdit screen. The detected network topology should now appear on the ONOS GUI’s topology view. The “pingall” command should now be executed in the Mininet CLI to confirm that each created virtual host is reachable by the others.

With the network active, terminal windows can now be launched for each virtual host from where the relevant Python programs can be executed.  Note, that the “inetd” command may need to be executed on the Gateway terminals to enable access to the FTP services on these hosts.

The Python programs will simulate the generation and acquisition of data according to the procedures shown below. Acquisition of this data will be observed with the creation and movement of text files in the folders listed above. The ONOS GUI and Wireshark may also be used to observe network traffic during this acquisition process. 
 
For those with knowledge with Python programming, the following parameters may be adjusted to influence the data generation and acquisition processes:
Parameter	Description

fthres	The file threshold that determines the amount of readings per text file before transfer to a Gateway Host.

volt_range	The voltage range for generated voltage sensor readings.

volt_offset	The offset value with which voltage readings can vary. 

amp_range	The electrical current range for generated current sensor readings.

amp_offset	The offset value with which current readings can vary. 

temp_range	The temperature range for generated temperature sensor readings.

temp_offset	The offset value with which temperature readings can vary. 

hum_range	The humidity range for generated humidity sensor readings.

hum_offset	The offset value with which humidity readings can vary. 

waitt	The time a Gateway host will wait before it transfers its files to the Backend host.

 
