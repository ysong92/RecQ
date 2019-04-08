
def handle_trust():
	f = open("./original/trust.txt", "r")
	new_f = open("trust.txt", "w")
	count = 1
	for line in f.readlines():
		new_line = line.strip().split("  ")
		new_line.append('1')
		new_f.write(" ".join(new_line)+"\n")
		count += 1
		if count%100 == 0:
			print "%d lines done"%(count)

	f.close()
	new_f.close()

def handle_ratings():
	f = open("./original/rating_with_timestamp.txt")
	testf = open("test.txt","w")
	ratingsf = open("ratings.txt", "w")

	current_user_list = []
	current_user = " "

	count = 0

	for line in f.readlines():
		line_list = line.strip().split("  ")
		rating_line = [line_list[0], line_list[1], line_list[3]]
		if current_user == ' ':
			current_user = rating_line[0]

		if rating_line[0] == current_user:
			current_user_list.insert(0, rating_line)
			

		else:
			testf.write(" ".join(current_user_list[-1])+"\n")
			current_user_list = current_user_list[:-1]
			if len(current_user_list) >30:
				current_user_list = current_user_list[-30:]
			for new_line in current_user_list:
				ratingsf.write(" ".join(new_line)+"\n")

			current_user = rating_line[0]
			current_user_list = []
			current_user_list.append(rating_line)
		count += 1
		if count%100==0:
			print "%d lines done"%(count)
	f.close()
	testf.close()
	ratingsf.close()










if __name__ == '__main__':
	# handle_trust()
	handle_ratings()