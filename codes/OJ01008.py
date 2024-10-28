n = int(input())
print(n)
Hmonths = {'pop': 1, 'no': 2, 'zip': 3, 'zotz': 4, 'tzec': 5, 'xul': 6, 'yoxkin': 7, 'mol': 8, 'chen': 9, 'yax': 10, 'zac': 11, 'ceh': 12, 'mac': 13, 'kankin': 14, 'muan': 15, 'pax': 16, 'koyab': 17, 'cumhu': 18, 'uayet': 19}
Tdays = {0: 'imix', 1: 'ik', 2: 'akbal', 3: 'kan', 4: 'chicchan', 5: 'cimi', 6: 'manik', 7: 'lamat', 8: 'muluk', 9: 'ok', 10: 'chuen', 11: 'eb', 12: 'ben', 13: 'ix', 14: 'mem', 15: 'cib', 16: 'caban', 17: 'eznab', 18: 'canac', 19: 'ahau'}
for i in range(n):
	Haab = input().split()
	Tzolkin = [0, "", 0]
	Haab[0] = int(Haab[0][0:-1])
	Haab[2] = int(Haab[2])
	
	day_of_the_year = 0
	if Hmonths[Haab[1]] <= 18:
		day_of_the_year = 20 * (Hmonths[Haab[1]] - 1) + Haab[0]
	else:
		day_of_the_year = 360 + Haab[0]
	day_tot = Haab[2] * 365 + day_of_the_year
	Tzolkin[2] = day_tot // 260
	Tzolkin_day = day_tot % 260
	Tzolkin[0] = Tzolkin_day % 13 + 1
	Tzolkin[1] = Tdays[Tzolkin_day % 20]
	print(*Tzolkin, sep = " ")