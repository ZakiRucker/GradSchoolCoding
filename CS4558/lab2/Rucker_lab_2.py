#####################################################################
# lab2
# NetTraff
# by: Zaki
# parse a pcap file
# header file might be found in: /usr/include/pcap/pcap.h
######################################################################

# import our dependencies
import dpkt				# for packet inspection
import sys
import socket
import numpy as np
import matplotlib.pyplot as plt
import datetime
import pytz
import collections

print ("\nprocessing the data...\n")		# let user know it's a good time to grab tea

# open the pcap
fd = open ("telescope.pcap", "rb")			# the file to read must be in the current directory and named telescope.pcap

# read the file with dpkt
pcap = dpkt.pcap.Reader(fd)				# read the file newly named as fd

# variables
limit = 20000000
packets = 0						# to count how many packets I have looked at
startTime = 0						# to determine the first packet arrival time
endTime = 0						# to determine the last packet arrival time
numBytes = 0						# to count the number of bytes read
timeDifference = 0					# to store the calculated differencs between start and finish times
uniq_IP = set()						# to store the unique IP addresses
dest_ip_list = []					# to store the list of unique destination IPs as a LIST
ip4 = 0							# to count the number of ipv4 packets
src_ip_set = set()					# to store the set of source IPs
protocol_set = set()					# to store the IP protocol types
num_icmp = 0						# to count the number of ICMP packets
num_ipv4 = 0						# to count the number of IPv4 wrapper packets
num_tcp = 0						# to count the number of TCP packets
num_udp = 0						# to count the number of UDP packets
num_gre = 0						# to count the number of GRE packets
protocol_array = [[1,'ICMP',0],[4,'IPv4',0],[6,'TCP',0],[17,'UDP',0],[47,'GRE',0]]
srcip_dstport = {}
#trial = []						# list of lists for key data: ts, srcip, bytes, ipv, dstip, pro, and dstp
#time_stamp = []					# list of ts
#source_ip = []						# list of src ip
#graph_protocols = []					# list of protocols to graph
#num_bytes = []						# list of packet bytes
bytes_dict = {}	
#ip_version = []					# list of ip versions
#destination_ip = []					# list of destination ips
#protocol_num = []					# list of protocol numbers
destination_port = []					# list of destination ports
ports_hit = {}						# dictionary of destination ports
detect_scanners = {}					# dictionary of port scanners
counter = 0						# variable initialized to zero
backscatter_victim = []					# list to store victims of backscatter IPs
attack_times = []					# find the indexes for the most attacked machine
bad_packet = 0
protocol_dict = {'1':0, '4':0, '6':0, '17':0, '47':0}
destination_port_dict = {}
attack_rate_dict = {}
reports = {'23_2323':0}


# iterate over the data
for ts, data in pcap:					# start my loop
	if packets >= 18798590:
		print ('packet #: %s' % packets)
	if packets == 18798594:
		packets += 1
		continue
	if packets >= limit:
		break
	eth = dpkt.ethernet.Ethernet(data)		# name the frame data
	ip = eth.data					# name the packet data
	tcp = ip.data
	if not isinstance(ip.data, object):
		bad_packet += 1
		print ('bad packet: %s' % packets)
		print (isinstance(ip.data, object))
		print ('%s bad packets' % bad_packet)
		packets += 1
		continue
	endTime = ts
	if startTime == 0:
		startTime = ts
	numBytes += eth.data.len
	if eth.type == 0x800:					# matches the type of packet 0x800 is IPv4
		ip4 += 1					# increment the IPv4 counter
		uniq_IP.add (socket.inet_ntoa(ip.dst))		# add the destination IP address to set of unique ips
		src_ip_set.add (socket.inet_ntoa(ip.dst))		# add the destination IP address to the 
		src_ip_set.add (socket.inet_ntoa(ip.src))
	protocol_set.add (ip.p)
#	for x in range (0,4):
#		if ip.p == protocol_array[x][0]:
#			protocol_array[x][2] += 1
#			graph_protocols.append((protocol_array[x][0]))
	if ip.p == 1:
		protocol_dict['1'] += 1
	if ip.p == 4:
		protocol_dict['4'] += 1
	if ip.p == 17:
		protocol_dict['17'] += 1
	if ip.p == 47:
		protocol_dict['47'] += 1
	if ip.p == 6:
		if not isinstance(tcp.dport, int):
			bad_packet += 1
			continue
		protocol_dict['6'] += 1
		if tcp.dport in destination_port_dict:
			destination_port_dict[tcp.dport] += 1
		else:
			destination_port_dict[tcp.dport] = 1  
		srcip_dstport.setdefault(socket.inet_ntoa(ip.src), set()).add(tcp.dport)
		destination_port.append(tcp.dport)
		detect_scanners.setdefault(socket.inet_ntoa(ip.src), []).append(tcp.dport)
		###### backscatter sorting
		if (tcp.flags == 2) or (tcp.flags == 18) or (tcp.flags == 20):
			#backscatter_victim.append(socket.inet_ntoa(ip.src))
			attack_rate_dict.setdefault(ts, socket.inet_ntoa(ip.src))
	if len(eth.data) in bytes_dict:
		bytes_dict[len(eth.data)] += 1
	else:
		bytes_dict[len(eth.data)] = 1
	packets += 1
#print (attack_rate_dict.values())
#print (backscatter_victim)

################################# to answer question 10 and determine the highest rate-DoS attack

print ('Most attacked host: %s'% collections.Counter(attack_rate_dict.values()).most_common(1)[0][0])

################################# Question 11

attack_times = sorted(attack_rate_dict.keys())
attack_times.sort()							# sort the list of all attack times
first_attack = attack_times[0]						# find the first time of attack
last_attack = attack_times[len(attack_times) - 1]			# find the last time of attack
#attack_duration = 0							# declare the duration variable
attack_duration = last_attack - first_attack		# attack duration in seconds
attack_rate = len(attack_rate_dict)/attack_duration
full_attack_rate = (len(attack_times) * 16777216)/attack_duration
print ("Rate of attack detected by the telescope (packets per second): %s" % attack_rate)
print ("Estimated actual rate of attack (packets per second): %s" % full_attack_rate)

################################## Question 12

port_counter = collections.Counter(destination_port).most_common(5)
print ("\nTop 5 ports attacked: %s" % port_counter)


#################################

# calculations

timeDifference = endTime - startTime					# calculate trace duration
bitRate = ((numBytes * 8)/timeDifference)				# convert bytes to bits
dest_ip_list = sorted(uniq_IP)						# sort the list of uniq IPs
dest_ip_list.sort(key=lambda ip: map(int, ip.split('.')))		# sort the set in dotted decimal form

# find 23 and 2323 scanners
for k,v in srcip_dstport.items():
	if len(v) == 2:
		if 23 in v:
			if 2323 in v:
				reports['23_2323'] += 1

# return my results to the user
print ("\n%s packets were scanned." % packets)
if ip4 < packets:
	print ("%s IPv4 packets" % ip4)
if bad_packet > 0:
	print ('%s bad packets' % bad_packet)
print ("\nThe trace duration in seconds: %s." % timeDifference)
print ("\n%s Unique IP destinations." % len(uniq_IP))
print ("\nThe lowest addressed packet in the telescope is: %s" % dest_ip_list[0])
print ("The highest addressed packet in the telescope is: %s" % dest_ip_list[len(dest_ip_list)-1])
print ("\nTotal bytes: %s" % numBytes)
print ("Bitrate: %.3f bits per second" % bitRate)
print ("\n%s unique source IPs" % len(src_ip_set))
print ("%s scanned ports 23 & 2323 and no others" % reports['23_2323'])
print ("\n%s protocols" % protocol_dict)
for x in range (0,len(protocol_array)):
	if protocol_array[x][2] > 0:
		print ("%s %s packets" % (protocol_array[x][2], protocol_array[x][1]))
if len(attack_rate_dict.values()) > 0:
	print ('\nbackscatter victims: %s' % len(attack_rate_dict.values()))


#####################################################################
#####################################################################
####################### print charts ################################
#####################################################################
#####################################################################


# chart for packet size
pfig, ps = plt.subplots (figsize=(9,6))
#N, bins, patches = plt.hist(bytes_dict.keys(),bytes_dict.values(), )
plt.bar(bytes_dict.keys(),bytes_dict.values(), 1)
ps.grid (True)
ps.set_title ('Packet Size Distibution')
ps.set_xlabel ('packet size in bytes')
ps.set_ylabel ('# of occurences')

# chart for protocol distribution
pfig, pr = plt.subplots (figsize=(9,6))
plt.bar (protocol_dict.keys(), protocol_dict.values(), 1)
pr.grid (True)
pr.set_title ('Protocol Distibution')
pr.set_xlabel ('protocols (by protocol number)')
pr.set_ylabel ('# of packets')
#plt.show ()

################################## Question 13
scanning = []
for v in detect_scanners.itervalues():
	scanning.append(len(v))
fig, a = plt.subplots(figsize=(9,6))

# Use the histogram function to bin the data
counts, bin_edges = np.histogram(scanning, bins='auto', density=True)

# Now find the cdf
cdf = np.cumsum(counts)

# And finally plot the cdf
#plt.figure(1)
a.set_title('Hosts and Number of Unique Destination Ports')
a.set_xlabel('number of unique ports probed per source')
a.set_ylabel('cummulative fraction of sources')
plt.plot(bin_edges[1:], cdf/cdf[-1])
a.grid (True)
plt.show()

#####################################################################
#####################################################################
##################### Close and exit ################################
#####################################################################
#####################################################################

fd.close()
sys.exit(-1)

