ab = int(input("Enter number of classrooms:"))
nb = int(input("Enter number of benches:"))
nd = int(input("Enter number of depts:"))
dn = (input("Enter names of depts separated by comma :"))
dn = dn.split(",")
dict = {}
ns = (input("Enter number of students in each dept:"))
ns = ns.split(",")
ns = [int(no) for no in ns]
nrc = int(nb ** (1/2))

it = 0
rn = [ 0 for x in range(nd)]
for room in range(ab):
	a = [['__' for x in range(nrc)] for y in range(nrc)]
	row = 0
	column = 0
	print("Room:",room+1)
	while(row < nrc and column < nrc):
		if  a[row-1][column][0:2] == dn[it]:
			it = (it+1) % nd
			if nd == 1:
				column = co1
				if column == nrc:
					column = 0
					row = row + 1
				else:
					column = column + 1

		if a[row][column] =='__':
			rn[it] = rn[it] + 1
			a[row][column] = dn[it] + str(rn[it])
			column = column + 1
			if column == nrc:
				row = row + 1
				column = 0
			ns[it] = ns[it] - 1
			if ns[it] == 0:
				del ns[it]
				del dn[it]
				del rn[it]
				nd = nd - 1
			if nd == 0:
				break
			it = (it + 1) % nd
	for row in range(nrc):
		for col in range(nrc):
			print(a[row][col],end = " ")
		print('\n')
