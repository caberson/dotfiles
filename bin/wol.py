#!/usr/bin/env python
# wol.py

import socket
import struct

def wake_on_lan(mac_address):
    """ Switches on remote computers using WOL. """

    # Check macaddress format and try to compensate.
    mac_address_len = len(mac_address)
    if mac_address_len == 12:
        pass
    elif mac_address_len == 12 + 5:
        sep = mac_address[2]
        mac_address = mac_address.replace(sep, '')
    else:
        raise ValueError('Incorrect MAC address format')
 
    # Pad the synchronization stream.
    data = ''.join(['FFFFFFFFFFFF', mac_address * 20])
    send_data = '' 

    # Split up the hex values and pack.
    for i in range(0, len(data), 2):
        send_data = ''.join(
			[send_data, struct.pack('B', int(data[i: i + 2], 16))]
		)

    # Broadcast it to the LAN.
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(send_data, ('<broadcast>', 7))
    

if __name__ == '__main__':
	import argparse
    # Use macaddresses with any seperators.
    # wake_on_lan('0F:0F:DF:0F:BF:EF')
    # wake_on_lan('0F-0F-DF-0F-BF-EF')
    # or without any seperators.
    # wake_on_lan('0F0FDF0FBFEF')
	wake_on_lan('00:16:cb:b0:a8:15')
	parser = argparse.ArgumentParser(
		description='Wake computers using mac address.'
	)
	parser.add_argument('mac_address', nargs='?')
	args = parser.parse_args()
	try:
		wake_on_lan(args.mac_address)
	except Exception as e:
		print e
