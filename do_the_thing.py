import github3
from datetime import datetime
import random

#authenticate
g = github3.login(token='')

# Retrieve the repo
r = g.repository('csheldonhess', 'daily-commit-app')

time = str(datetime.now())

commit_message = 'Made a change on {0}'.format(time)

sites = {'http://placebear.com/': 'a bear',
		 'http://www.placecage.com/': 'Nick Cage',
		 'http://www.fillmurray.com/': 'Bill Murray',
		 'http://placekitten.com/': 'a kitten'
}

site = random.choice(list(sites.keys()))
alt = sites.get(site)

width = str(random.randrange(1,9) * 100)
height = str(random.randrange(1,9) * 100)

url = site + width + '/' + height

content = 'Daily Commit App\n================\nNo longer will my GitHub streaks be less than perfect!'
content += 'Enjoy this pseudorandom image:\n\n![{0}]({1} "{0}")'.format(alt, url)

# Grab a file
file_to_update = r.contents('README.md')
the_sha = file_to_update.sha

r.update_file('README.md', commit_message, content, the_sha)