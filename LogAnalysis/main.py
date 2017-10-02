import psycopg2
import os
import time


def clear_shell():
	os.system("clear")


clear_shell()


conn = psycopg2.connect("dbname=news")
cur = conn.cursor()


cur.execute("SELECT * FROM authors;")
authors = cur.fetchall()

cur.execute("SELECT * FROM articles;")
articles = cur.fetchall()


print("Retrieving log data...")
cur.execute("SELECT * FROM log;")
log = cur.fetchall()
logFirst = cur.fetchone()


pages_log = []
author_log = []
daily_log = []


print("Computing log data...")
print("=================================================")
print("Loading articles ...")
for x in articles:
    dic = {}
    dic["title"] = x[1]
    dic["path"] = "/article/"+x[2]
    dic["author"] = authors[x[0]-1][0]
    dic["views"] = 0
    pages_log.append(dic)


print("=================================================")
print("Loading authors...")
for x in authors:
    dic = {}
    dic["name"] = x[0]
    dic["views"] = 0

    author_log.append(dic)


print("=================================================")
print("Calculating article views...")
for x in log:
    if x[0].startswith("/article/"):
        for y in pages_log:
            if(y["path"] == x[0]):
                y["views"] += 1


found = []
print("=================================================")
print("Loading daily logs... This may take a little while!")

for x in log:

	dlog = x[4].strftime("%d. %B %Y")
	dic = {"date": dlog, "errors": 0}

	if(dic not in found):
		found.append(dic)

    
daily_log = found

for x in daily_log:
	for y in log:
		dlog = y[4].strftime("%d. %B %Y") 
		if(dlog == x["date"]):
			if(y[3] != "200 OK"):
				x["errors"] += 1

daily_log = sorted(daily_log, key=lambda x: int(x["errors"]))
daily_log.reverse()



clear_shell()
print("=================================================")
print("Calculating author views...")
pages_log = sorted(pages_log, key=lambda x: int(x['views']))
pages_log.reverse()

for x in pages_log:
    for y in author_log:
        if(y["name"] == x["author"]):
            y["views"] += x["views"]

author_log = sorted(author_log, key=lambda x: int(x['views']))
author_log.reverse()
clear_shell()
print("=================================================")
print("=================================================")
print("Done computing log data! Waiting five seconds...")
print("=================================================")
print("=================================================")
time.sleep(5)
clear_shell()


def print_articles():
    for x in articles:
        print("==========================================")
        print("Author: "+authors[x[0]-1][0])
        print("Title: "+x[1])
        print("Alias: "+x[2])
        print("Description: "+x[3])
        # print("Content: "+str(x[4]))
        print("Written: "+str(x[5]))
        print("Article-ID: "+str(x[6]))

# print_articles()


def article_meta():
    for x in articles:
        print("===================================")
        for y in x:
            print(y)


def all_logs():
    print("Loading... This may take a while!")
    for x in log:
        print("=======================================")
        print(x)


def print_article_ranking():
    i = 1
    print("Ranking list (articles): \n")
    for x in pages_log:
        if i < 4:
            i += 1
            print("\nRanking: "+str(i-1)+"")
            print("===============================================")
            print("Title: "+x["title"])
            print("Views: "+str(x["views"]))
            print("Author: " + str(x["author"]))
            # i += 1

        else:
            break


def print_author_ranking():
    i = 1
    print("Ranking list (authors): \n")
    for x in author_log:
        if i < 4:
            i += 1
            print("\nRanking: "+str(i-1)+"")
            print("=================================")
            print("Name: "+x["name"])
            print("Complete views: "+str(x["views"]))
            # i += 1

        else:
            break


def print_logdays():
    for x in daily_log:
        print("\n")
        print("====================================================")
        print("Day: "+str(x["date"]))

def print_error_ranking():
	i = 1
	print("Error days: \n")
	for x in daily_log:
		if i < 4:
			i += 1
			print("=======================================")
			print("Date: "+x["date"])
			print("Errors: "+str(x["errors"]))
		else:
			break


# article_meta()
# print_articles()
# print(logFirst)
# all_logs()
#print(str(pages_log))
print_article_ranking()
print("\n\n")
print_author_ranking()
print("\n\n")
print_error_ranking()

# print("\n\n\n")
# print_logdays()
#print(str(daily_log))

