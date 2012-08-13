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


def write_book_headers(sheet):
	sheet.write(5, 0, 'Title')
	sheet.write(5, 1, 'Author')
	sheet.write(5, 2, 'Edition')
	sheet.write(5, 3, 'Publisher')
	sheet.write(5, 4, 'ISBN')

	sheet.col(0).width = 12000
	sheet.col(1).width = 5000
	sheet.col(2).width = 3000
	sheet.col(5).width = 4000
	sheet.col(4).width = 5000

def write_class_data(row, col, course,  class_, book_list, sheet):
	col = 0
	sheet.write(row, col, class_.classNumber) #write class_ number
	course_name = "%s %s" % (course.department, class_.courseNumber)
	sheet.write(row, col+1, course_name) #write course name and course number
	sheet.write(row, col+2, class_.section)
	sheet.write(row, col+3, class_.deptLimit)
	sheet.write(row, col+4, class_.schedule)
	sheet.write(row, col+5, get_book_titles(book_list))
	sheet.write(row, col+6, course.department)
	

def write_book_data(row, col, book, sheet):
	col = 0
	sheet.write(row, col, book.title) #write class_ number
	sheet.write(row, col+1, book.author) #write course name and course number
	sheet.write(row, col+2, book.edition)
	sheet.write(row, col+3, book.publisher)
	sheet.write(row, col+4, book.isbn)

def get_book_titles(book_list):
	titles = ""
	arr_len = len(book_list)
	for x in range(5, arr_len):
		titles += "\"%s\"" %(book_list[x].title)
		if x + 1 != arr_len:
			titles += "; "

	return titles