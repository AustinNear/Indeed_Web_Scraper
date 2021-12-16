import requests
import re
from bs4 import BeautifulSoup


class Job:
    def __init__(self):
        pass

def pulljobs():
    jobs = []
    url = "https://www.indeed.com/jobs?q=Developer&l=Alameda%2C%20CA&radius=50&jt=fulltime&explvl=entry_level&taxo2" \
          "=HFDVW" \
          "&vjk=bd6434efa5f2ac39&advn=4012104096277101 "
    r = requests.get(url)
    bs = BeautifulSoup(r.content, 'html.parser')

    jobtitles = bs.find_all("h2", "jobTitle")
    for job in jobtitles:
        jobs.append(Job())
    for i, job in enumerate(jobtitles):
        jobs[i].jobtitle = job.text

    companynames = bs.find_all("span", "companyName")
    for i, company in enumerate(companynames):
        jobs[i].companyname = company.text

    companylocations = bs.find_all("div", "companyLocation")
    for i, location in enumerate(companylocations):
        jobs[i].companylocation = location.text

    regex = re.compile('.*sj_.*')
    joblinks = bs.find_all("a", {"id": regex})
    for i, link in enumerate(joblinks):
        jobs[i].joblink = link['href']
        print(link['href']

    return jobs


def printjobs(jobslist):
    for job in jobslist:
        print(job.jobtitle)
        print(job.companyname)
        print(job.companylocation)
        print(job.joblink)

def main():
    jobslist = pulljobs()
    printjobs(jobslist)

if __name__ == '__main__':
    main()
