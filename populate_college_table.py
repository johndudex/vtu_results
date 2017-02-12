#import request
import urllib2
from bs4 import BeautifulSoup
import pdb
import MySQLdb

connection = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="john",  # your password
                     db="vtu_results")        # name of the data base

cursor = connection.cursor()
hdr = {'User-Agent': 'Mozilla/6.0'}
site = "http://www.fastvturesults.com/college_codes"

def main():

	requ= urllib2.Request(site,headers=hdr)
	page = urllib2.urlopen(requ)
	soup = BeautifulSoup(page,'lxml')
	tables= soup.findAll("table",{"class":"table table-striped table-hover"})

	for table in tables:
		row  = table.findAll("tr")
		for i in  row:
			td_tag = i.findAll('td')
			if td_tag:
				sql = "insert into college (college_name, college_prefix) values('%s','%s')" %(td_tag[1].text,td_tag[2].text)
				cursor.execute(sql)


if __name__ == '__main__':
	main()
