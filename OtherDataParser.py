#!/usr/bin/env python
from HTMLParser import HTMLParser
import re
"""
	0		RB Team
	1		RB OFF
	2		Team TO
	5		2pt made fg
	6		2pt attempt fg
	7		2pt fb pct

"""
class OtherDataParser(HTMLParser):
	def customInit(self,scur=0):
		self.cur = scur
		self.data = {}

	def handle_data(self,data):
		if "TOTAL" in data:
			return
		data = re.sub("\r\n","",data)
		if self.cur == 0:
			self.data["rb_team"] = data
		elif self.cur == 1:
			self.data["rb_off"] = data
		elif self.cur == 3:
			self.data["team_to"] = data
		if not data:
			return
		if self.cur == 5:
			self.data["2pt_made"] = data
		elif self.cur == 6:
			self.data["2pt_attempt"] = data
		elif self.cur == 7:
			self.data["2pt_pct"] = data	
		elif self.cur == 9:
			self.data["tech_foul"] = data
		self.cur+=1

	def getData(self):
		return self.data