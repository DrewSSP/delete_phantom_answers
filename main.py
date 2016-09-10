import requests, sys, subprocess
from multiprocessing import Pool
from variables import cookies
from lxml import html

course_database_url = sys.argv[1]
headers = {}
headers['Referer'] = course_database_url
headers['X-CSRFToken'] = cookies['csrftoken']

def main(first_database_page, number_of_pages):
	database_urls = []
	for page in range(1, number_of_pages + 1):
		database_urls.append(first_database_page + '?page=' + str(page))
	pool = Pool(processes = 7)
	audio_files = pool.map(get_thing_information, database_urls)

def get_thing_information(database_url):
	print('processing ' + database_url)
	response = requests.get(database_url, cookies = cookies)
	tree = html.fromstring(response.text)
	things = tree.xpath("//tr[contains(@class, 'thing')]")
	for thing in things:
		thing_attributes = thing.xpath("td[contains(@class, 'text')]")
		for thing_attribute in thing_attributes:
			thing_id = thing.attrib['data-thing-id']
			cell_id = thing_attribute.attrib["data-key"]
			cell_type = thing_attribute.attrib["data-cell-type"]
			try:
				inner_content = thing_attribute.xpath("div/div[contains(@class, 'text')]/text()")[0]
				post = requests.post('http://www.memrise.com/ajax/thing/cell/update/', cookies=cookies, data={'thing_id':thing_id, 'cell_id':cell_id, 'cell_type':cell_type, 'new_val':inner_content}, headers=headers)
			except IndexError:
				continue
			except Exception as e:
				print ('OOPS!! Something strange happened for when processing ' + inner_content + '. Please check the course database for this word to make sure that everything looks okay. Here is the error that caused a problem:')
				print (e)
				continue

if __name__ == "__main__":
	if 'Login' in str(requests.get(course_database_url, cookies=cookies).content):
		print("The cookies provided did not give the script access to your memrise account. Please modify the variables.py file to include the proper cookies and headers data, then try again.")
	number_of_pages = int(html.fromstring(requests.get(course_database_url, cookies=cookies).content).xpath("//div[contains(@class, 'pagination')]/ul/li")[-2].text_content())
	main(course_database_url, number_of_pages)
