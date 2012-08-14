#!/usr/bin/env python
from HTMLParser import HTMLParser

"""
	0		Player No
	1		Position
	2		Name
	3		Mins played
	4		tot points
	5		3pt Made
	6		3pt attempt
	7		3pt pct
	8		2pt Made
	9		2pt attempt
	10		2pt pct
	11		FT Made
	12		FT attempt
	13		FT pct
	14		Rb total
	15		Rb OFF
	16		assist
	17		steal
	18		block
	19		TO UNF
	20		TO TOT
	21		fouls TOT
	22		fouls WA
"""

class PlayerParser(HTMLParser):
	def customInit(self,scur=-1):
		self.cur = scur
		self.tmp_player = {}
		self.data = []

	def getPlayers(self):
		return self.data

	def handle_starttag(self,tag,attrs):
		if tag == "tr":
			self.cur = -1

	def handle_data(self,data):
		data = data.strip()
		if not data and self.cur > -1:
			return

		if self.cur == 0:
			self.tmp_player["no"] = data
		elif self.cur == 1:
			self.tmp_player["pos"] = data
		elif self.cur == 2:
			self.tmp_player["name"] = data
		elif self.cur == 3:
			self.tmp_player["mins"] = data
		elif self.cur == 4:
			self.tmp_player["tot_pts"] = data
		elif self.cur == 5:
			self.tmp_player["3pt_made"] = data
		elif self.cur == 6:
			self.tmp_player["3pt_attempt"] = data
		elif self.cur == 7:
			self.tmp_player["3pt_pct"] = data
		elif self.cur == 8:
			self.tmp_player["2pt_made"] = data
		elif self.cur == 9:
			self.tmp_player["2pt_attempt"] = data
		elif self.cur == 10:
			self.tmp_player["2pt_pct"] = data
		elif self.cur == 11:
			self.tmp_player["ft_made"] = data
		elif self.cur == 12:
			self.tmp_player["ft_attempt"] = data
		elif self.cur == 13:
			self.tmp_player["ft_pct"] = data
		elif self.cur == 14:
			self.tmp_player["rb_tot"] = data
		elif self.cur == 15:
			self.tmp_player["rb_off"] = data
		elif self.cur == 16:
			self.tmp_player["assist"] = data
		elif self.cur == 17:
			self.tmp_player["steal"] = data
		elif self.cur == 18:
			self.tmp_player["block"] = data
		elif self.cur == 19:
			self.tmp_player["to_unf"] = data
		elif self.cur == 20:
			self.tmp_player["to_tot"] = data
		elif self.cur == 21:
			self.tmp_player["fouls_tot"] = data
		elif self.cur == 22:
			self.tmp_player["fouls_wa"] = data
		self.cur+=1

	def handle_endtag(self,tag):
		if tag == "tr":
			self.data.append(self.tmp_player)
			self.tmp_player = {}





