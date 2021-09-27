dnary = {n:0 for n in range(0,1001)}
dnary[0] = 0
dnary[1] = 3
dnary[2] = 3
dnary[3] = 5
dnary[4] = 4
dnary[5] = 4
dnary[6] = 3
dnary[7] = 5
dnary[8] = 5
dnary[9] = 4
dnary[10] = 3
dnary[11] = 6
dnary[12] = 6
dnary[13] = 8
dnary[14] = 8
dnary[15] = 7
dnary[16] = 7
dnary[17] = 9
dnary[18] = 8
dnary[19] = 8
dnary[20] = 6
dnary[30] = 6
dnary[40] = 5
dnary[50] = 5
dnary[60] = 5
dnary[70] = 7
dnary[80] = 6
dnary[90] = 6

for i in range(21,100):
	tens = int(i/10)*10
	ones = i - tens
	dnary[i]  = dnary[tens]+dnary[ones]

for i in range(100,1000):
	hundreds = int(i/100)
	tens_ones = i - hundreds*100
	if tens_ones == 0:
		dnary[i] = dnary[hundreds] + 7
	else:
		dnary[i] = dnary[hundreds] +10+dnary[tens_ones]

dnary[1000] = 11
print(sum(dnary.values()))
