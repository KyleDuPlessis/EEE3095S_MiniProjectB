# EEE3095S_MiniProjectB
Mini-Project B
----
Overview:
----
Essentially, this is a repeat of the  first project, but using a second Raspberry Pi with MQTT
and Node Red as opposed to Blynk.
For this task, two Raspberry Pis are required. Both are required to publish and subscribe
to data. One Pi must publish the recorded data, and subscribe to an alarm dismissal signal.
A second Pi should publish an alarm dismissal message and subscribe to the data collected
by the first Pi. A web page must be hosted on the second Pi, and it's WiFi interface should
be turned into an access point. Devices should be able to connect to this access point, and
view a web page which can mimic the Blynk App designed in Mini-Project A.

Run program:
----
```sh
$ chmod +x MiniProjectB.py
$ sudo python MiniProjectB.py
```
