import bs4 as bs
import urllib
import requests
from time import sleep

header = {'User-Agent' : 'Chrome/24.0.1312.27'}
list = []

def pph_hourlies_crawler(link):
	req = urllib.request.Request(link, headers=header)
	resp = urllib.request.urlopen(req)
	soup = bs.BeautifulSoup(resp, 'lxml')
	soup.prettify()

	print(soup.title.text)

	clientName = soup.find('a', class_="crop member-short-name")
	print('Name : ', clientName.text)

	clientProfession = soup.find('div', class_="member-job-title crop")
	print('Profession : ', clientProfession.text)

	aboutClient = soup.find('div', class_="about-container js-about-container")
	print('About : ', aboutClient.text)

	pricing = soup.find('span', class_="js-hourlie-discounted-price discounted-price")
	print("Price : ", pricing.text)

	rating = soup.find('span', class_="value")
	print('Rating : ', rating.text)

	deliverytime = soup.find('span', class_="value js-delivery-days")
	print('Delivery Time : ', deliverytime.text)

	description = soup.find('div', class_='hourlie-description-text')
	print('Services Description : ', description.text)

	for comments in soup.find_all('div', class_="col-xs-8 col-sm-10 right-col"):
		print('Comments : ',comments.text)



def hourlies_page_crawler(link):
	while True:
		req = urllib.request.Request(link, headers=header)
		resp = urllib.request.urlopen(req)
		soup = bs.BeautifulSoup(resp, 'lxml')
		soup.prettify()

		for url in soup.find_all('a', class_="color-hourlie js-paragraph-crop"):
			urls = url.get('href')
			print(urls)
			pph_hourlies_crawler(urls)

		for nexter in soup.find_all('link', rel='next'):
			link = nexter.get('href')
			#print(link)

		if soup.find('link', rel='next') is None:
			break



def pph_jobs_crawler(link):
	req = urllib.request.Request(link, headers=header)
	resp = urllib.request.urlopen(req)
	soup = bs.BeautifulSoup(resp, 'lxml')
	soup.prettify()

	print('Title : ',soup.title.text)

	clientName = soup.find('span', class_='crop member-short-name disabled')
	print('Client Name : ', clientName.text)

	clientProfession = soup.find('div', class_='member-job-title crop')
	print('Client Profession: ', clientProfession.text)

	clientCountry = soup.find('div', class_="location-container crop")
	print('Client Country: ', clientCountry.text)

	proposalCount = soup.find('span', class_="info-value")
	print('Proposal :', proposalCount.text)

	price = soup.find('div', class_="value price-tag")
	print('Fixed-Price : ',price.text)

	postedDate = soup.find('time', class_="info-value")
	print('Posted : ', postedDate.text)

	experience = soup.find('div', class_='description-experience-level')
	print(experience.text)

	description = soup.find('div', class_='project-description gutter-top')
	print('description : ', description.text)



def page_crawler(link):
	while True:
		req = urllib.request.Request(link, headers=header)
		resp = urllib.request.urlopen(req)
		soup = bs.BeautifulSoup(resp, 'lxml')
		soup.prettify()

		for url in soup.find_all('a', class_="job js-paragraph-crop"):
			urls = url.get('href')
			print(urls)
			pph_jobs_crawler(urls)

		for nexter in soup.find_all('link', rel='next'):
			link = nexter.get('href')

		if soup.find('link', rel='next') is None:
			break

#hourlies_page_crawler("https://www.peopleperhour.com/hourlies")

def pph_freelancers(link):
	req = urllib.request.Request(link, headers=header)
	resp = urllib.request.urlopen(req)
	soup = bs.BeautifulSoup(resp, 'lxml')
	soup.prettify()

	print('Title : ',soup.title.text)

	freelancerName = soup.find('span', class_="member-name")
	print('Name : ', freelancerName.text)

	freelencerProfession = soup.find('span', class_="member-description")
	print('Freelencers Profession : ',freelencerProfession.text)

	hourlyRate = soup.find('ul', class_="clearfix details-list")
	print('Rate : ',hourlyRate.li.text)

	location = soup.find('div', class_="member-location-rate")
	print('Location : ',location.li.text)

	working = soup.find('span', class_="status-label-text")
	print('Working Status : ',working.text)

	rating = soup.find('div', class_="row memberStats-item memberStats-rating")
	print('Rating :',rating.text)

	for skills in soup.find_all(class_="tag-item small"):
		print('Skills : ', skills.text)

	freelancerdescription = soup.find('div', class_="about-container js-about-container")
	print('About Freelencer : ', freelancerdescription.text)

def freelancer_page_crawling(link):
	while True:
		req = urllib.request.Request(link, headers=header)
		resp = urllib.request.urlopen(req)
		soup = bs.BeautifulSoup(resp, 'lxml')
		soup.prettify()

		for url in soup.find_all('a', class_="link"):
			urls = url.get('href')
			print(urls)
			pph_freelancers(urls)

		for nexter in soup.find_all('link', rel='next'):
			link = nexter.get('href')

		if soup.find('link', rel='next') is None:
			break

freelancer_page_crawling('https://www.peopleperhour.com/freelance')