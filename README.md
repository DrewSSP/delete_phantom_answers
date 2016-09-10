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

You must also make a file in the root directory of your script called 'variables.py' and create a python dictionary of your cookies. It should look something like this:
```python
cookies = {'_sp_id.7bc7': '06d67edb75b999999.1466999953.100.1555544393.1234573782',
           '_sp_ses.7bc7': '*',
           'csrftoken': 'nxIto89I10jvMe45lt5xBJ8xnQkWayh3',
           'fbm_143688012353890': 'base_domain=.www.memrise.com',
           'fbsr_143688012353890': 'bGMeJtlEkaCEISsa4th4J1-FvygfuhFgBuu7qnnS1M.eyJhbGdvcml03f6OiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUUNxNTh6ekpDMDlpNGNpTjNyaVRYR3VEN0xHZHM1TEJyMmFCVlJBTmVHeVl4WFlWanM1QVRpMDBtSzFwMWNFV2dxa28wUUxrWUVoT0RKLVdQOG1DdHVncjZhSGdxMVBEaEp3MGhTbV9pRXA3ckcxZU02d2M0LTNubFFCVkVaU0tUVml3eXFKdy1FZmxJYTVuZGJZUlhBXzVlNXdGcFFKWWVJem83ZllwcV9COWExdkJ0S3ZFQlB6OGQ2c2w0azMyOWtxcmFyVjJRYXpodVh3WXVlbVc4ejNlUUc5TE11SXJsakxTbW1hOXN3cUREVzEtcl94WlNLRlRucklsV3FxY3kzN0g1UnFVeTRwOFZ0TVVSXzEzd0Z0TjBrNF9PZjgzalJHYVZjZkV5dWFqUDJLQVhSRkxmT3RrU0R5d3lRSnRncGRMVC1ZZTVRTkNKN0xNRWxfcEVVWSIsImlzc3VlZF9hdCI6MTQ2ODY0Mzk4MiwidXNlcl9pZCI6IjUwMzc3MTY3OCJ9',
           'i18next': 'en',
           'sessionid': 'xrxg3zofonxnfmf5gfdgv5444defa71'}

If you need help finding these details, you can get this through Chrome. Just log in to Memrise through the Chrome browser. With Memrise.com open and logged in, press the three dots on the right of your toolbar at the top. Go to `More Tools` and click `Developer Tools`. A window will appear at the bottom of the screen. Click the `Resources` tab on that window. On the left you'll see a folder called `Cookies`. Expand that folder by clicking the arrow to the left of the word "Resources". clicke `www.memrise.com`. Those are your cookies. Format them as shown above.

## To run the script
type `python main.py **database_page**`, where `**database_page**` is the url of the first page after you enter your course's database

For example:
`ipython main.py http://www.memrise.com/course/1036119/hsk-level-6/edit/database/2000662/`

This example script will add audio to any words that are missing it for the course `http://www.memrise.com/course/1036119/hsk-level-6`. This course's database page is `http://www.memrise.com/course/1036119/hsk-level-6/edit/database/2000662/`.