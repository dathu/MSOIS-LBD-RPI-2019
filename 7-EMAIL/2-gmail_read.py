import feedparser # feedparser is library which parses feeds in all known formats including Rich Site Summary (RSS), RDF

USERNAME = "projectjunkieslabs@gmail.com"
PASSWORD = "project123!"

response = feedparser.parse("https://" + USERNAME + ":" + PASSWORD + "@mail.google.com/gmail/feed/atom")


unread_count = int(response["feed"]["fullcount"])

for i in range(0,unread_count):
	print "(" + str((i+1)) + "/" + str(unread_count) + ") " + response['items'][i].title
