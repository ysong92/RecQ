
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

if __name__ == '__main__':
	handle_trust()