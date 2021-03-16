import tui

years_list = 9
medal_list = 14
team_list = 6

def list_years(data):
    tui.started("List Years")
    years = set()
    for record in data:
        year = record[years_list]
        years.add(year)
    tui.display_years(years)
    tui.completed()


def tally_medals(data):
    tui.started("Tally Medals")
    medal_tally = {"Gold": 0, "Silver": 0, "Bronze": 0}
    for record in data:
        medal = record[medal_list]
        if medal in ("Gold", "Silver", "Bronze"):
            medal_tally[medal] += 1
    tui.display_medal_tally(medal_tally)
    tui.completed()


def tally_team_medals(data):
    tui.started("Tally Medals for each team")
    team_medals = {}
    for record in data:
        team = record[team_list]
        medal = record[medal_list]

        if medal not in ("Gold", "Silver", "Bronze"):
            continue

        if team in team_medals:
            team_medals[team][medal] += 1
        else:
            team_medals[team] = {"Gold": 0, "Silver": 0, "Bronze": 0}
            team_medals[team][medal] += 1

    tui.display_team_medal_tally(team_medals)
    tui.completed()

