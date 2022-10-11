import pandas as pd
import random
from datetime import date

today = date.today()
print("Today's date:", today)


dfb = pd.read_csv(r'../101-AI-Prevision-Qatar-2022/data/raw/fifa_ranking-2022-10-06.csv')
dfb = dfb[['country_abrv','total_points', 'rank_date']]
print(dfb.info())
dfb['rank_date'] = pd.to_datetime(dfb['rank_date'])

selecao = (dfb['rank_date'] >= '2018-01-01') & (dfb['rank_date'] <= '2019-02-10')
df_filtrado = dfb[selecao]

print(df_filtrado)
print(dfb.info())
print(dfb.head())



#country_abrv
#total_points

df = pd.read_csv('https://raw.githubusercontent.com/digitalinnovationone/live-coding-evitando-o-7x1-com-python-e-sql/main/data.csv')
print(df.head())

print('*' *30)

class Team:
    best_score = 1837.6 #BRA
    poor_score = 1393.5 #GAN

    def __init__(self, cellData):
        teamData = cellData.split('|')
        self.name = str(teamData[0])
        self.score = float(teamData[1])

    def motivate(self):
        self.lastMotivation = random.uniform(70, (self.score * 100) / Team.best_score)
        return self.lastMotivation

bestTeamByGroup = {}

for label, content in df.items():
    #    print(label)
    #    print(content)
    team1 = Team(content[0])
    team2 = Team(content[1])
    team3 = Team(content[2])
    team4 = Team(content[3])

    bestTeamByGroup[label] = sorted([team1, team2, team3, team4], key=Team.motivate, reverse=True)

for grupo, motivatedTeams in bestTeamByGroup.items():
    print(f'Grupo {grupo}: ', end="")
    for team in motivatedTeams:
        print(f'{team.name} ({team.lastMotivation:.2f}) ', end="")
    print()

print('*' *30)

team1A = bestTeamByGroup['A'][0]
team2A = bestTeamByGroup['A'][1]
team1B = bestTeamByGroup['B'][0]
team2B = bestTeamByGroup['B'][1]
team1C = bestTeamByGroup['C'][0]
team2C = bestTeamByGroup['C'][1]
team1D = bestTeamByGroup['D'][0]
team2D = bestTeamByGroup['D'][1]
team1E = bestTeamByGroup['E'][0]
team2E = bestTeamByGroup['E'][1]
team1F = bestTeamByGroup['F'][0]
team2F = bestTeamByGroup['F'][1]
team1G = bestTeamByGroup['G'][0]
team2G = bestTeamByGroup['G'][1]
team1H = bestTeamByGroup['H'][0]
team2H = bestTeamByGroup['H'][1]

oitava1 = team1A if team1A.motivate() > team2B.motivate() else team2B
oitava2 = team1C if team1C.motivate() > team2D.motivate() else team2D
oitava3 = team1E if team1E.motivate() > team2F.motivate() else team2F
oitava4 = team1G if team1G.motivate() > team2H.motivate() else team2H
oitava5 = team1B if team1B.motivate() > team2A.motivate() else team2A
oitava6 = team1D if team1D.motivate() > team2C.motivate() else team2C
oitava7 = team1F if team1F.motivate() > team2E.motivate() else team2E
oitava8 = team1H if team1H.motivate() > team2G.motivate() else team2G

print(f'{team1A.name} ({team1A.lastMotivation:.2f}) x {team2B.name} ({team2B.lastMotivation:.2f})')
print(f'{team1C.name} ({team1C.lastMotivation:.2f}) x {team2D.name} ({team2D.lastMotivation:.2f})')
print(f'{team1E.name} ({team1E.lastMotivation:.2f}) x {team2F.name} ({team2F.lastMotivation:.2f})')
print(f'{team1G.name} ({team1G.lastMotivation:.2f}) x {team2H.name} ({team2H.lastMotivation:.2f})')
print(f'{team1B.name} ({team1B.lastMotivation:.2f}) x {team2A.name} ({team2A.lastMotivation:.2f})')
print(f'{team1D.name} ({team1D.lastMotivation:.2f}) x {team2C.name} ({team2C.lastMotivation:.2f})')
print(f'{team1F.name} ({team1F.lastMotivation:.2f}) x {team2E.name} ({team2E.lastMotivation:.2f})')
print(f'{team1H.name} ({team1H.lastMotivation:.2f}) x {team2G.name} ({team2G.lastMotivation:.2f})')

print('*' *30)

quarta1 = oitava1 if oitava1.motivate() > oitava2.motivate() else oitava2
quarta2 = oitava3 if oitava3.motivate() > oitava4.motivate() else oitava4
quarta3 = oitava5 if oitava5.motivate() > oitava6.motivate() else oitava6
quarta4 = oitava7 if oitava7.motivate() > oitava8.motivate() else oitava8

print(f'{oitava1.name} ({oitava1.lastMotivation:.2f}) x {oitava2.name} ({oitava2.lastMotivation:.2f})')
print(f'{oitava3.name} ({oitava3.lastMotivation:.2f}) x {oitava4.name} ({oitava4.lastMotivation:.2f})')
print(f'{oitava5.name} ({oitava5.lastMotivation:.2f}) x {oitava6.name} ({oitava6.lastMotivation:.2f})')
print(f'{oitava7.name} ({oitava7.lastMotivation:.2f}) x {oitava8.name} ({oitava8.lastMotivation:.2f})')

print('*' *30)

semi1 = quarta1 if quarta1.motivate() > quarta2.motivate() else quarta2
semi2 = quarta3 if quarta3.motivate() > quarta4.motivate() else quarta4

print(f'{quarta1.name} ({quarta1.lastMotivation:.2f}) x {quarta2.name} ({quarta2.lastMotivation:.2f})')
print(f'{quarta3.name} ({quarta3.lastMotivation:.2f}) x {quarta4.name} ({quarta4.lastMotivation:.2f})')

print('*' *30)

final1 = semi1 if semi1.motivate() > semi2.motivate() else semi2
final2 = semi2 if semi2.motivate() < semi1.motivate() else semi1

print(f'Disputa Ouro: {semi1.name} ({semi1.lastMotivation:.2f}) x {semi2.name} ({semi2.lastMotivation:.2f})')