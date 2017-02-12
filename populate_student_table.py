import pdb
import MySQLdb

connection = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="john",  # your password
                     db="test_vtu") 
cursor = connection.cursor()

f_path = "/home/cabox/workspace/pop/home/john/vtu/results/student_usn/"


def main():
	count =0	
	sql = "select id,college_prefix from college"
	cursor.execute(sql)
	for i in cursor.fetchall():
		li =[]
		try :
			fp = open(f_path+i[1]+".csv",'r')
			for rows in fp.readlines():
				li.append(rows.split(','))
			for row in li :
				sql = "insert into student (usn,name,college_id) values('%s','%s','%s')" %(row[0].strip(),row[1].strip().replace("'",'`'),i[0])
				count +=1
				#cursor.execute(sql)
		except Exception as e:
			print e
			
	#connection.commit()		
	print count		
if __name__ =='__main__':
	main()
