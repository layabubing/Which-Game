import requests
from bs4 import BeautifulSoup
import headers

# Choose a header
header = headers.headers
# Get the tables
page = requests.get(url, headers=header)
page = page.text                  # Change the variable of the response attribute to a string attribute
soup = BeautifulSoup(page, "html.parser")   # bs4.BeautifulSoup
table = soup.find(class_="tc_center_table")         # bs4.element.Tag
score_tables = table.find_all(class_="score")
teams = table.find_all(align="right")

links, scores = [], []
for score in score_tables:
    link = score.find('a').get('href')
    matches_score = score.text
    links.append(link)          # Reserve in advance for future functions(2024.8.5)
    scores.append(matches_score)

rows = map(str, table.find_all('tr'))
rows_split = []

for row in rows:
    row.split("\n")
    rows_split.append(row.split("\n"))

goals = [i[6][15:-5] for i in rows_split[2:]]
goals_subscript = []
j = 0

for goal in gaals:
    if goal != 0:
        goals_subscript.append(j)
    j += 1

teams_temp = []
for team in teams:
    teams_temp.append(team.text)
teams = teams_temp

team_dictionary = {"home":[], "visit":[]}
for i in range(1, int((len(teams_temp))/2)+1):
    team_dictionary["home"].append(teams[2 * i - 2])
    team_dictionary["visit"].append(teams[2 * i - 1])

print(team_dictionary)
