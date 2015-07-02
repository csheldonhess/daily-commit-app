import github3
from datetime import datetime
import random

token = ''
username = ''
repo = ''

def get_the_substring(full_string, substring_category):
    # The +1 cuts out the quotation mark
    index1 = full_string.find('"', full_string.rfind(substring_category)) + 1
    # No +1 needed on this end
    index2 = full_string.find('"', index1)
    substring = full_string[index1:index2]
    return substring

with open('auth.txt', 'r') as f:
    text = f.read()
    token = get_the_substring(text, 'token')
    username = get_the_substring(text, 'username')
    repo = get_the_substring(text, 'repo')

    #authenticate
    g = github3.login(token=token)

    # Retrieve the repo
    r = g.repository(username, repo)

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
    content += '\n\nEnjoy this pseudorandom image:\n\n![{0}]({1} "{0}")'.format(alt, url)
    content += '\n\nKnown issue: there are some images missing from some of these. It seems a little random. '
    content += 'Sorry if no image has appeared.'

    # Grab a file
    file_to_update = r.contents('README.md')
    the_sha = file_to_update.sha

    r.update_file('README.md', commit_message, content, the_sha)

    