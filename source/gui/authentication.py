# -*- coding: utf-8 -*- 

import requests

class Authentication:

	def __init__(self):
		pass

	def get_vercode(self, vercode_url):
		r = requests.get(vercode_url)
		print unicode(r.text)


def main():
	vercode_url = "https://account.tophant.com/captcha/sid/0.6698824353252733"
	auth = Authentication()
	auth.get_vercode(vercode_url)

if __name__ == '__main__':
	main()