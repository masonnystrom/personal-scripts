# data_wrangling/teams.py

#example class 

class Team():
    def __init__(self, name, city, sport=None, roster=[]):
        self.name = name
        self.city = city
        self.sport = sport 
        self.roster = roster 

    # this is a property
    @property
    def full_name(self):
        # return team['city'] + " " + team['name']
        return f"{team.city} {team.name}"
    
    # this is a method
    def advertise(self):
        # return team['city'] + " " + team['name']
        print("Pease come to ", self.city, "to see us play")

if __name__ == "__main__":

    teams = [
    {"name": "Yankees", "city": "New York"},
    {"name": "Mets", "city": "New York"},
    {"name": "Nationals", "city": "Washington"}
    ]

    for d in teams:
        team = Team(d['name'], d['city'])
        print(team.name)
        print(team.full_name) # deocration @property lets us invoke the function without ()
        print(team.advertise()) # this is a method