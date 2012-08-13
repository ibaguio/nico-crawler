#!/usr/bin/env python

import urllib,urllib2
import sys,re,json
from xlwt import *
from urllib2 import HTTPError, URLError
from PlayerParser import *
from OtherDataParser import *
from xls_utils import *

home = "http://www.statsboard.webnatin.com/uaap/seniors/2012/"
user_agent = "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT)"
headers = {'User-Agent': user_agent}

out_dir = "spreadsheets/"

extended_url = "gamestatbypts.asp?gameid=%(game_id)d&qtr=0"

def getPage(url,verbose=False,data=None):
	global responses
	if data:
		data = urllib.urlencode(data)
	try:
		if verbose:
			print 'Trying to fetch',url
		req = urllib2.Request(url,data,headers)
		response = urllib2.urlopen(req)
		page = response.read()
		if verbose:
			print 'Fetch completed; Size:',len(page)
		return page
	except HTTPError, e:
		print 'The server couldn\'t fulfill the request. On URL',url
		print 'Error code:', e.code, responses[int(e.code)]
	except URLError, e:
		print 'Failed to reach',url
		print 'Reason:', e.reason

def parsePage(markup):
	try:
		markup = markup[markup.index("<body"):markup.index("</body>")]
	except:
		print "ERROR 69: Server Error"
		sys.exit()

	jdata = {}
	markup = markup[markup.index("DATE:")+6:]

	jdata["date"] = markup[:markup.index(" 2012")+5]

	#get teams
	team_marker= "<tr>\r\n<td class=\"summarydiv\"><font size=\"+1\">"
	markup = markup[markup.index(team_marker)+len(team_marker):]
	jdata["team1"] = markup[:markup.index("</font></td>")]
	t2 = markup[markup.index(team_marker)+len(team_marker):markup.index(team_marker)+len(team_marker)+15]
	jdata["team2"] = t2[:t2.index("</font></td>")]

	#parse team
	teamA = markup[:markup.index("TECH. FOULS")+63]
	teamB = markup[markup.index("TECH. FOULS")+len("TECH. FOULS")+60:]
	jdata[jdata["team1"]] = parseTeamInfo(teamA)
	jdata[jdata["team2"]] = parseTeamInfo(teamB)

	return jdata

def parseTeamInfo(markup):
	data = {}
	q_scores = []
	#quarter scores
	for i in range(4):
		marker = "<td class=\"summarydiv\">\r\n"
		markup = markup[markup.index(marker)+len(marker):]
		s = markup[:markup.index("</td>")]
		q_scores.append(s)
	data["quarter_scores"] = q_scores

	#fastbreak
	fbreak = {}
	marker = "<td class=\"summarydiv\">ATT</td>\r\n<td class=\"summarydiv\">"
	markup = markup[markup.index(marker)+len(marker):]
	marker = "</td>\r\n<td class=\"summarydiv\">"
	fbreak["ATT"] = markup[:markup.index(marker)]
	markup = markup[20:]
	markup = markup[markup.index(marker)+len(marker):]
	fbreak["2CH"] = markup[:markup.index("</td>")]

	marker = "PTS</td>\r\n<td class=\"summarydiv\">"
	markup = markup[markup.index(marker)+len(marker):]
	marker = "</td>\r\n<td class=\"summarydiv\">"
	fbreak["ATT-PTS"] = markup[:markup.index(marker)]
	markup = markup[20:]
	markup = markup[markup.index(marker)+len(marker):]
	fbreak["TO-PTS"] = markup[:markup.index("</td>")]

	data["fbreak"] = fbreak
	
	#parse players
	marker = "<tr>\r\n<td class=\"data3\" align=\"center\">"
	to_remove = r'</a>|<a href=\"#gameID=(\d)+&amp;playerID=(\d)+\">|<a href="#playerID=(\d)+&amp;gameID=(\d)+&amp;DB=SENIORS&amp;path=current">|<td class=\"summarydiv\">&nbsp;</td>'
	markup = re.sub(to_remove,"",markup)
	markup = re.sub("&nbsp;","NA",markup)
	end_player_marker = "<td class=\"summarydiv\" colspan=\"3\">TEAM </td>"
	
	#markup.index(end_player_marker)
	players_html = markup[markup.index(marker):markup.index(end_player_marker)]
	other_data = markup[markup.index(end_player_marker):]
	playerParser = PlayerParser()
	playerParser.customInit()
	playerParser.feed(players_html)
	players = playerParser.getPlayers()
	data["players"] = players

	other_info = {}
	to_remove = r'<td class="summarydiv" colspan="(\d)+">NA</td>'
	other_data = re.sub(to_remove,"",other_data)
	other_data = other_data[other_data.index("</td>")+7:]
	odp = OtherDataParser()
	odp.customInit()
	odp.feed(other_data[:other_data.index("TOTAL")])
	other_info["team"] = odp.getData()

	tt = PlayerParser()
	tt.customInit(scur=3)
	tt.feed(other_data[other_data.index("TOTAL")+5:])
	other_info["team_total"]=tt.getPlayers()

	gg = OtherDataParser()
	gg.customInit(scur=5)
	gg.feed(other_data[other_data.index("TOTAL FGs")+16:])
	other_info["team_total_fg"] = gg.getData()
	data["summary"] = other_info
	
	return data

def write_yahoo(sheet,team,date):
	write_game_info(sheet,team,date)
	write_players_header(sheet)

	#players
	row = 7
	for pinfo in team["players"]:
		sheet.write(row, 0, pinfo["no"])
		sheet.write(row, 1, pinfo["pos"])
		sheet.write(row, 2, pinfo["name"])
		sheet.write(row, 3, pinfo["mins"])
		sheet.write(row, 4, pinfo["tot_pts"])
		sheet.write(row, 5, pinfo["3pt_made"])
		sheet.write(row, 6, pinfo["3pt_attempt"])
		sheet.write(row, 7, pinfo["3pt_pct"])
		sheet.write(row, 8, pinfo["2pct_made"])
		sheet.write(row, 9, pinfo["2pt_attempt"])
		sheet.write(row, 10, pinfo["2pt_pct"])
		sheet.write(row, 11, pinfo["ft_made"])
		sheet.write(row, 12, pinfo["ft_attempt"])
		sheet.write(row, 13, pinfo["ft_pct"])
		sheet.write(row, 14, pinfo["rb_tot"])
		sheet.write(row, 15, pinfo["rb_off"])
		sheet.write(row, 16, pinfo["assist"])
		sheet.write(row, 17, pinfo["steal"])
		sheet.write(row, 18, pinfo["block"])
		sheet.write(row, 19, pinfo["to_unf"])
		sheet.write(row, 20, pinfo["to_tot"])
		sheet.write(row, 21, pinfo["fouls_tot"])
		sheet.write(row, 22, pinfo["fouls_wa"])
		row+=1

def write_to_spreadsheet(jdata):
	fname = out_dir+jdata["team1"]+"_"+jdata["team2"]+".xls"

	xls = Workbook()
	sheet1 = xls.add_sheet(jdata["team1"])
	sheet2 = xls.add_sheet(jdata["team2"])

	team1_ = jdata[jdata["team1"]]
	team2_ = jdata[jdata["team2"]]

	write_yahoo(sheet1,team1_,jdata["date"])
	write_yahoo(sheet2,team2_,jdata["date"])

	xls.save(fname)

def checkDirs():
  if not os.path.exists(log_dir):
    os.makedirs(log_dir)
    print "Created an outfolder.."

def main():
	checkDirs
	#get html main page
	for i in range(1,24):
		html = getPage(home+extended_url%{"game_id":i},verbose=True)
		data = parsePage(html)
		write_to_spreadsheet(data)

if __name__ == "__main__":
	main()