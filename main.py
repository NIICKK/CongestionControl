import sys
import yaml
import socket

# lock the configuration file
def lockConfig(cfg):
	cfg['lock'] = True
	with open("config.yaml", 'w') as yamlfile:
		yaml.dump(cfg, yamlfile)

# unlock the configuration file
def unlockConfig(cfg):
	cfg['lock'] = False
	with open("config.yaml", 'w') as yamlfile:
		yaml.dump(cfg, yamlfile)

def allocateBandwidth(activeUsers, available, thredshold):
	# Allocate network bandwidth to each active user
	# For example, if available bandwidth is 100, and there are three users having the file.
	# we could assign each user with 33 bandwidth.
	# And when there is new download requests, we could reallocate the bandwitdh for each user.
	# For example, if two additional users join, then each user will have 20 bandwidth.

	# For each bandwidth allocation, the config.yaml file must be update. When the config.yaml is updating,
	# it must be locked, and it should be unlocked after the modification
	pass
	# return allocatedBandwidth

def fileDownload(filename, hosts_ips, hosts_ports, allocatedBandwidth):
	# Download the file using udp socket at certain speed, the download speed will be varied upon new download requests (congestion control, we might need constantly call neworkQuery
	# here, once there is an update in certain feilds, change the download speeds)
	# Add reliability to UDP
	pass

# get all the network information
def networkQuery():
	with open("config.yaml", 'r') as yamlfile:
		cfg = yaml.load(yamlfile)
		lock = cfg['lock']
		while lock:
			with open("config.yaml", 'r') as yamlfile:
				cfg = yaml.load(yamlfile)
				lock = cfg['lock']

		lockConfig(cfg)

		network_info = cfg['network_info']
		bandwidth = network_info['bandwidth']
		thredshold = network_info['thredshold']
		available = network_info['available']
		activeUsers = network_info['activeUsers']

		unlockConfig(cfg)

		return (bandwidth, thredshold, available, activeUsers)

# get the specific file information including all the hosts contain the file
def fileQuery(filename):
	with open("config.yaml", 'r') as yamlfile:
		cfg = yaml.load(yamlfile)
		filesize = cfg['file_info'][filename]['file_size']
		hosts = cfg['file_info'][filename]['hostsWithFile']
		hosts_ips = []
		hosts_ports = []
		for host in hosts:
			hosts_ips.append(host['ip'])
			hosts_ports.append(host['port'])

		return (filesize, hosts_ips, hosts_ports)


def main(filename):
	(filesize, hosts_ips, hosts_ports) = fileQuery(filename)
	(bandwidth, thredshold, available, activeUsers) = networkQuery()
	allocatedBandwidth = allocateBandwidth(activeUsers, available, thredshold)
	fileDownload(filename, hosts_ips, hosts_ports, allocatedBandwidth)

if __name__ == '__main__':
	filename = sys.argv[1]
	main(filename)

