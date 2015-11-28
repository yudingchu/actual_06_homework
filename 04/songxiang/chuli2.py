#-*- coding: utf-8 -*-
def select_items(whole_list):
	d_items={}
	for i in whole_list:
		new=['']
		sigle_list=i.split(' ')
		new[0]=(sigle_list[8],sigle_list[6],sigle_list[0])
		#http,访问url,ip
		if i[8] in d_items:
			if i[6] in d_items[i[8]]:
				if i[0] in d_items[i[8]][i[6]]:
					d_items[i[8]][i[6]]=d_items[i[8]][i[6]][i[0]]+1
				else:
					d_items[i[8]][i[6]][i[0]]= 1
			else:
				d_items[i[8]][i[6]] = {}
				d_items[i[8]][i[6]][i[0]]= 1
		else:
			d_items[i[8]] = {}
			d_items[i[8]][i[6]] = {}
			d_items[i[8]][i[6]][i[0]]= 1
	print d_items
#	return d_items
#def pick_top10(d_items):
#	whole_list_tuple=sorted(d_items.items(),key=lambda d_items:d_items[1])
#	items_10=''
#	j = 0
#	for i in whole_list_tuple[::-1]:
#		if j < 10:
#			items_10 = items_10+str([i[0][0],i[0][1],(i[0][2],i[1])])+'\n'
#			j = j +1
#		else:
#			return items_10
#def write(item):
#	fnew = open('new.log','a+')
#	fnew.writelines(item)
#	fnew.close()
if __name__ == '__main__':
	f = open('www_access_20140823.log','r')
	whole_list = f.readlines()
	f.close()
	#  读取文件
	d_items = {}
	d_items = select_items(whole_list)
	#  选取元素
	j = 0
	itmes_top10 = ''
	itmes_top10 = pick_top10(d_items)
	#  进行排序,取前十
	write(itmes_top10)
	print itmes_top10
	#  进行写入
