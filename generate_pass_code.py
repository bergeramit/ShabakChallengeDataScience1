
import itertools

a = open("pass_list.txt", "wb")
for length in range(2,7):
	for comb in itertools.product(range(10), repeat=length):
		a.write("".join(map(str,comb)).encode("ascii") + '\n'.encode("ascii"))
