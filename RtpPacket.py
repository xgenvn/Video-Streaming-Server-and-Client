__author__ = 'Tibbers'
import sys
from time import time
# from VideoStream import VideoStream


import VideoStream
HEADER_SIZE = 12

class RtpPacket:
	header = bytearray(HEADER_SIZE)

	def __init__(self):
		pass

	def encode(self, version, padding, extension, cc, seqnum, marker, pt, ssrc, payload):
		"""Encode the RTP packet with header fields and payload."""

		timestamp = int(time())
		print timestamp
		header = bytearray(HEADER_SIZE)
		#--------------
		# TO COMPLETE
		#--------------
		# Fill the header bytearray with RTP header fields

		#RTP-version filed(V), must set to 2
		#padding(P),extension(X),number of contributing sources(CC) and marker(M) fields all set to zero in this lab

		#Because we have no other contributing sources(field CC == 0),the CSRC-field does not exist
		#Thus the length of the packet header is therefore 12 bytes


			#Above all done in ServerWorker.py

		# ...
		#header[] =

		#header[0] = version + padding + extension + cc + seqnum + marker + pt + ssrc
		header[0] = version << 6
		header[0] = header[0] | padding << 5
		header[0] = header[0] | extension << 4
		header[0] = header[0] | cc
		header[1] = marker << 7
		header[1] = header[1] | pt

		header[2] = seqnum >> 8
		header[3] = seqnum

		header[4] = bytes(timestamp >> 24)
		header[5] = bytes(timestamp >> 16)
		header[6] = timestamp >> 8
		header[7] = timestamp

		header[8] = ssrc >> 24
		header[9] = ssrc >> 16
		header[10] = ssrc >> 8
		header[11] = ssrc
		print '-'*60 + "header endoing done...\n" + '-'*60
		# Get the payload from the argument
		# self.payload = ...
		self.payload = payload
	def decode(self, byteStream):
		"""Decode the RTP packet."""
		print "decoding bug..."
		self.header = bytearray(byteStream[:HEADER_SIZE])
		self.payload = byteStream[HEADER_SIZE:]

	def version(self):
		"""Return RTP version."""
		return int(self.header[0] >> 6)

	def seqNum(self):
		"""Return sequence (frame) number."""
		seqNum = self.header[2] << 8 | self.header[3]  #header[2] shift left for 8 bits then does bit or with header[3]
		return int(seqNum)

	def timestamp(self):
		"""Return timestamp."""
		timestamp = self.header[4] << 24 | self.header[5] << 16 | self.header[6] << 8 | self.header[7]
		return int(timestamp)

	def payloadType(self):
		"""Return payload type."""
		pt = self.header[1] & 127
		return int(pt)

	def getPayload(self):
		"""Return payload."""
		return self.payload

	def getPacket(self):
		"""Return RTP packet."""
		return self.header + self.payload