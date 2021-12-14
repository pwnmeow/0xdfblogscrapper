from bs4 import BeautifulSoup
import requests
 
req = requests.get('https://0xdf.gitlab.io/')
soup = BeautifulSoup(req.text, "html5lib")

linklist = []

for eachpost in soup.find_all(class_='post-link'):
    linklist.append(eachpost['href'])

for link in linklist:
    url = "https://0xdf.gitlab.io/" + link
    pages = requests.get(url).text
    if not 'javascript' and not 'Javascript' or 'Java' or 'java' or 'JAVA' or 'log4j' in pages:
        page = BeautifulSoup(pages, "html5lib")
        print(page.find(class_='post-title'))




# _posts/2018-09-01-htb-stratosphere.md
# _posts/2018-11-17-htb-jerry.md
# _posts/2018-12-01-htb-hawk.md
# _posts/2019-02-27-playing-with-jenkins-rce-vulnerability.md
# _posts/2019-03-09-htb-ethereal.md
# _posts/2019-04-10-commando-vm-overview.md
# _posts/2019-05-25-htb-chaos.md
# _posts/2019-07-01-darling-running-macos-binaries-on-linux.md
# _posts/2019-08-10-htb-arkham.md
# _posts/2019-09-07-htb-bastion.md
# _posts/2019-10-02-flare-on-2019-flarebear.md
# _posts/2019-10-05-htb-ghoul.md
# _posts/2019-11-02-htb-haystack.md
# _posts/2019-11-23-htb-chainsaw.md
# _posts/2020-01-01-hackvent2019-medium.md
# _posts/2020-01-25-htb-ai.md
# _posts/2020-02-01-htb-re.md
# _posts/2020-02-15-htb-json.md
# _posts/2020-03-24-update-alternatives.md
# _posts/2020-04-02-jar-files-analysis-and-modifications.md
# _posts/2020-04-18-htb-mango.md
# _posts/2020-04-30-htb-solidstate.md
# _posts/2020-05-19-htb-arctic.md
# _posts/2020-06-08-endgame-poo.md
# _posts/2020-06-30-htb-blocky.md
# _posts/2020-08-08-htb-fatty.md
# _posts/2020-08-08-jar-files-analysis-and-modifications.md
# _posts/2020-08-29-htb-quick.md
# _posts/2020-10-24-htb-dyplesher.md
# _posts/2020-11-07-htb-tabby.md
# _posts/2020-11-21-htb-buff.md
# _posts/2020-12-19-htb-laser.md
# _posts/2021-01-01-hackvent-leet.md
# _posts/2021-01-09-htb-omni.md
# _posts/2021-01-12-holidayhack-03-pos.md
# _posts/2021-02-13-htb-jewel.md
# _posts/2021-02-20-htb-feline.md
# _posts/2021-04-03-htb-time.md
# _posts/2021-04-24-htb-bucket.md
# _posts/2021-05-19-htb-kotarak.md
# _posts/2021-07-03-htb-ophiuchi.md
# _posts/2021-10-09-htb-monitors.md
# _posts/2021-11-13-htb-seal.md

