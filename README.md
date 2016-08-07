# Fix Phantom Answers
This script fixes an issue in which outdated information continues to be used for alternate answers in your Memrise courses. It works by sending a post request to Memrise for each piece of information in your course's database. The post request tells Memrise that you modified a piece of information without actually making any changes, which forces Memrise to re-evaluate the invisible information that may have become outdated.

## Set up
This script has the following requirements:
* python 3
* libraries:
  * requests
  * sys
  * subprocess
  * multiprocessing
  * lxml

You must also make a file in the root directory of your script called 'variables.py' and create a python dictionary of your cookies and headers. It should look something like this:
```python
cookies = {'_sp_id.7bc7': '06d67edb75b999999.1466999953.100.1555544393.1234573782',
           '_sp_ses.7bc7': '*',
           'csrftoken': 'nxIto89I10jvMe45lt5xBJ8xnQkWayh3',
           'fbm_143688012353890': 'base_domain=.www.memrise.com',
           'fbsr_143688012353890': 'bGMeJtlEkaCEISsa4th4J1-FvygfuhFgBuu7qnnS1M.eyJhbGdvcml03f6OiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUUNxNTh6ekpDMDlpNGNpTjNyaVRYR3VEN0xHZHM1TEJyMmFCVlJBTmVHeVl4WFlWanM1QVRpMDBtSzFwMWNFV2dxa28wUUxrWUVoT0RKLVdQOG1DdHVncjZhSGdxMVBEaEp3MGhTbV9pRXA3ckcxZU02d2M0LTNubFFCVkVaU0tUVml3eXFKdy1FZmxJYTVuZGJZUlhBXzVlNXdGcFFKWWVJem83ZllwcV9COWExdkJ0S3ZFQlB6OGQ2c2w0azMyOWtxcmFyVjJRYXpodVh3WXVlbVc4ejNlUUc5TE11SXJsakxTbW1hOXN3cUREVzEtcl94WlNLRlRucklsV3FxY3kzN0g1UnFVeTRwOFZ0TVVSXzEzd0Z0TjBrNF9PZjgzalJHYVZjZkV5dWFqUDJLQVhSRkxmT3RrU0R5d3lRSnRncGRMVC1ZZTVRTkNKN0xNRWxfcEVVWSIsImlzc3VlZF9hdCI6MTQ2ODY0Mzk4MiwidXNlcl9pZCI6IjUwMzc3MTY3OCJ9',
           'i18next': 'en',
           'sessionid': 'xrxg3zofonxnfmf5gfdgv5444defa71'}

headers = {
  'Accept':'application/json, text/javascript, */*; q=0.01',
  'Accept-Encoding':'gzip, deflate',
  'Accept-Language':'en-US,en;q=0.8,fr;q=0.6,en-CA;q=0.4',
  'Connection':'keep-alive',
  'Content-Length':'63',
  'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
  'Host':'www.memrise.com',
  'Origin':'http://www.memrise.com',
  'Referer':'http://www.memrise.com/course/1036119/hsk-level-6/edit/database/2000662/',
  'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
  'X-CSRFToken':'mxIto89I10jvWe45lt5xBJ8xnQkWayh3',
  'X-Requested-With':'XMLHttpRequest'}
```

If you need help finding these details, you can get this through chrome. Just go onto the first page of your course database in memrise, then on the Chrome browser, go to `More Tools` and click `Developer Tools`. A window will appear at the bottom of the screen. Click the `Network` tab on that window and then click`XHR` near the top. This is where things get a bit intimidating but just give it a shot. With that page open, add the letter 'A' to one word in your course (you can remove the change later) and then click outside of the textbox to apply the change. You will see the words 'update/' appear in the bottom window. Click on it. You'll see some information there including 'General', 'Response Headers', 'Request Headers', and 'Form Data'. You want the information that's in 'Request Headers'. Take the informaition after 'Cookie' and formation that as shown above under the 'cookies' variable as shown above. The rest of the information should be defined under the 'headers' variable as shown above.

## To run the script
type `python main.py **database_page**`, where `**database_page**` is the url of the first page after you enter your course's database

For example:
`ipython main.py http://www.memrise.com/course/1036119/hsk-level-6/edit/database/2000662/`

This example script will add audio to any words that are missing it for the course `http://www.memrise.com/course/1036119/hsk-level-6`. This course's database page is `http://www.memrise.com/course/1036119/hsk-level-6/edit/database/2000662/`.