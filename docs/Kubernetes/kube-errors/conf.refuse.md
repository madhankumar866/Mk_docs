	1.	ECONNREFUSED
		This is caused if there is no process listening at the port specified at Host B.
	2.	ENETUNREACH
		The network is unreachable, that means the routers buffers are full and the packet is dropped ans it is acknowledged by ICMP message.
	3.	EHOSTUNREACH
		The host is unreachable. This is caused if there is no forwarding entry in the routing table of a router.
	4.	ECONNRESET
		If something goes wrong with the Host it sends RST packet. This is caused after connection establishment when the host A or B is unable to receive any packets and it simply wants to quit.
	5.	ECONNABORTED
		Due to some software error.


Host A gets all of the errors except ECONNRESET from connect() call where as in Host B accept() passes already-pending network errors on the new socket as an error code from accept(). This behavior differs from other BSD socket implementations. For reliable operation the application should detect the network errors defined for the protocol after accept() and treat them like EAGAIN by retrying. In the case of TCP/IP, these are ENETDOWN, EPROTO,ENOPROTOOPT, EHOSTDOWN, ENONET, EHOSTUNREACH, EOPNOTSUPP, and ENETUNREACH.

ECONNRESET is received by either Host when the other is trying to reset the connection