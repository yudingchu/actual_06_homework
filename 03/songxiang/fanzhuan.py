# -*- coding: utf-8 -*-
'''把字典里的key，value翻转'''
d = {
	'woniu':'handsome',
	'WD':'handsome',
	'subin':'handsome',
	'ada':'beautiful'
}
d_new = {}
print d
for i in d:
	if d[i] in d_new:
		if isinstance(d_new[(d[i])],str):
			d_new[d[i]] = [d_new[d[i]],i]
		else:
			d_new[d[i]].append(i)
	else:
		d_new[d[i]] = i
print d_new
