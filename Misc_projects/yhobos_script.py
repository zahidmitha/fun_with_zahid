# This is a sanitized version of my twitter bot's script.

# It's useful as an example, but I make no guarantees to how correct it is.
# Email me if you have questions: al@inventwithpython.com

# The blog article explaining how this script works is here: http://inventwithpython.com/blog/2012/03/25/how-to-code-a-twitter-bot-in-python-on-dreamhost/

# You will have to replace the values in the call to twitter.Api() to get this code to work for you.

LATESTFILE = 'yhoboshavedogs_latest.txt'
LOGFILE = 'yhoboshavedogs_log.txt'

import sys
sys.path = ['/home/Zahid/yhoboshavedogs', '/home/Zahid/local/lib/python/python_twitter-0.8.2-py2.5.egg', '/home/yourusername/local/lib/python/oauth2-1.5.211-py2.5.egg', '/home/yourusername/local/lib/python/httplib2-0.7.4-py2r.5.egg', '/home/yourusername/local/lib/python/simplejson-1.9.2-py2.5-linux-x86_64.egg', '/home/yourusername/local/lib/python/python_twitter-0.8.2-py2.5.egg', '/home/yourusername/local/lib/python/oauth2-1.5.211-py2.5.egg', '/home/yourusername/local/lib/python/simplejson-1.9.2-py2.5-linux-x86_64.egg', '/home/yourusername/local/lib/python2.5', '/home/yourusername/local/lib/python', '/usr/lib/python2.5', '/usr/lib/python2.5/plat-linux2', '/usr/lib/python2.5/lib-tk', '/usr/lib/python2.5/lib-dynload', '/usr/local/lib/python2.5/site-packages', '/usr/lib/python2.5/site-packages', '/usr/lib/python2.5/site-packages/Numeric', '/usr/lib/python2.5/site-packages/PIL', '/var/lib/python-support/python2.5', '/usr/lib/site-python', '/home/yourusername/local/lib/python2.5']

import twitter, os, time
os.chdir('/home/Zahid/yhoboshavedogs')


api = twitter.Api(consumer_key='bJ5IIoEfSuuAWvfBM0Q', 
	consumer_secret='GZZhvI0AP6kimS0IwsD401RfE2IVrXTatBMpnI4a0', 
	access_token_key='766466876-QMw2wH1HedUpTODK4bd9g9iT8nvizQRX92Rj2k0L', 
	access_token_secret='888regJ7oSXY1ClXeUKwKvR6qlHY57YajvRKXfk0')

#api = twitter.Api(consumer_key='',
 #                 consumer_secret='xxx',
  #                access_token_key='xxx',
   #               access_token_secret='xxx')

# grab the last ID that the bot replied to, so it doesn't reply to earlier posts. (spam prevention measure)
if os.path.exists(LATESTFILE):
    fp = open(LATESTFILE)
    lastid = fp.read().strip()
    fp.close()

    if lastid == '':
        lastid = 0
else:
    lastid = 0

# read in the file of users we've already responded to
fp = open(LOGFILE)
alreadyMessaged = fp.readlines()
fp.close()
for i in range(len(alreadyMessaged)):
    if alreadyMessaged[i].strip() == '':
        continue

    alreadyMessaged[i] = alreadyMessaged[i].split('|')[1]
alreadyMessaged.append('YHobosHaveDogs') # don't reply to myself

# perform the search
results = api.GetSearch('"homeless people" dogs', since_id=lastid)
#print 'Found %s results.' % (len(results))
if len(results) == 0:
    #print 'Nothing to reply to. Quitting.'
    sys.exit()
repliedTo = []

for statusObj in results:
    postTime = time.mktime(time.strptime(statusObj.created_at[:-6], '%a, %d %b %Y %H:%M:%S'))

    if time.time() - (24*60*60) < postTime and statusObj.user.screen_name not in alreadyMessaged and '@yhoboshavedogs' not in statusObj.text.lower():
        if [True for x in alreadyMessaged if ('@' + x).lower() in statusObj.text.lower()]:
            #print 'Skipping because it\'s a mention: @%s - %s' % (statusObj.user.screen_name.encode('ascii', 'replace'), statusObj.text.encode('ascii', 'replace'))
            continue

        try:
            #print 'Posting in reply to @%s: %s' % (statusObj.user.screen_name.encode('ascii', 'replace'), statusObj.text.encode('ascii', 'replace'))
            api.PostUpdate('@%s Homeless people have dogs because a dog will love you even if you are homeless.' % (statusObj.user.screen_name), in_reply_to_status_id=statusObj.id)
            repliedTo.append( (statusObj.id, statusObj.user.screen_name, statusObj.text.encode('ascii', 'replace')) )
            time.sleep(1)
        except Exception:
            print "Unexpected error:", sys.exc_info()[0:2]


fp = open(LATESTFILE, 'w')
fp.write(str(max([x.id for x in results])))
fp.close()

fp = open(LOGFILE, 'a')
fp.write('\n'.join(['%s|%s|%s' % (x[0], x[1], x[2]) for x in repliedTo]) + '\n')
fp.write('\n')
fp.close()
