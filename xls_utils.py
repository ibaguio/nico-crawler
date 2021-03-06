def write_game_info(sheet,info,date):
	#quarter scores
	sheet.write(2, 0, "Q1")
	sheet.write(2, 1, "Q2")
	sheet.write(2, 2, "Q3")
	sheet.write(2, 3, "Q4")

	sheet.write(3, 0, info["quarter_scores"][0])
	sheet.write(3, 1, info["quarter_scores"][1])
	sheet.write(3, 2, info["quarter_scores"][2])
	sheet.write(3, 3, info["quarter_scores"][3])

	sheet.write(0, 0, "DATE:")
	sheet.write(0, 1, date)

	sheet.write(0, 7, "FBREAK")
	sheet.write(0, 8, "ATT")
	sheet.write(0, 10, "2CH. PTS")
	sheet.write(1, 8, "PTS")
	sheet.write(1, 10, "T.O PTS")

	sheet.write(0, 9, info["fbreak"]["ATT"])
	sheet.write(0, 11, info["fbreak"]["2CH"])
	sheet.write(1, 9, info["fbreak"]["ATT-PTS"])
	sheet.write(1, 11, info["fbreak"]["TO-PTS"])

def write_players_header(sheet):
	sheet.write(5, 0, 'Players')
	sheet.write(5, 5, '3-PT FGs')
	sheet.write(5, 8, '2-PT FGs')
	sheet.write(5, 11, 'FT')
	sheet.write(5, 14, 'RB')
	sheet.write(5, 16, 'MISC')
	sheet.write(5, 19, 'TO')
	sheet.write(5, 21, 'FOULS')

	sheet.write(6, 0, 'NO.')
	sheet.write(6, 1, 'Pos')
	sheet.write(6, 2, 'Name')
	sheet.write(6, 3, 'Mins. Plyd')
	sheet.write(6, 4, 'Tot Pts')
	sheet.write(6, 5, 'Made')
	sheet.write(6, 6, 'Attempt')
	sheet.write(6, 7, 'pct %')
	sheet.write(6, 8, 'Made')
	sheet.write(6, 9, 'Attempt')
	sheet.write(6, 10, 'pct %')
	sheet.write(6, 11, 'Made')
	sheet.write(6, 12, 'Attempt')
	sheet.write(6, 13, 'pct %')
	sheet.write(6, 14, 'TOT')
	sheet.write(6, 15, 'OFF')
	sheet.write(6, 16, 'AST')
	sheet.write(6, 17, 'STL')
	sheet.write(6, 18, 'BLK')
	sheet.write(6, 19, 'UNF')
	sheet.write(6, 20, 'TOT')
	sheet.write(6, 21, 'TOT')
	sheet.write(6, 22, 'WA')
