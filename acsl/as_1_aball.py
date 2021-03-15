#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:54:09 2021

@author: mac
"""

from collections import namedtuple

player = namedtuple("Player", "name team point1 point2 point3")

def get_data(the_file = "as_1_aball_sample.txt"):
    lineup = [ ]
    with open(the_file, "r") as f:
        for idx, line in enumerate(f, start=1):
            team = "Jets" if idx <= 4 else "Sharks"
            name, point1, point2, point3 = line.split(",")
            lineup.append(player(name, team, 
                                 int(point1), int(point2), int(point3)))
    return lineup

def three_pointers(player_data):
    return sum([p.point3 for p in player_data])

def most_goals(player_data):
    num_goals = []
    for p in player_data:
        num_goals.append((p.point1 + p.point2 + p.point3, p.name))
    return sorted(num_goals)

def sorted_score(player_data, team=None):
    """
    Optionally filter by team
    return [(points, name)...] list
    """
    num_points = []
    for p in player_data:
        if team and (team != p.team):
            continue
        num_points.append((1*p.point1 + 
                           2*p.point2 + 
                           3*p.point3, p.name))
    return sorted(num_points)
        
def highest_team(player_data):
    """
    returns something like (("Jets", "Sharks"), 30)
    i.e. team order (winner first), winner's score
    """
    num_points = []
    for p in player_data:
        num_points.append((1*p.point1 + 
                           2*p.point2 + 
                           3*p.point3, p.team))
        
    jets = sum([p[0] for p in num_points if p[1] == "Jets"])
    sharks = sum([p[0] for p in num_points if p[1] == "Sharks"])
    win_score = max(jets, sharks)
    team_order = ("Jets", "Sharks") if jets > sharks else ("Sharks", "Jets")
    return team_order, win_score

def main(input_file, output_file=None):
    """
    input_file = as_1_aball_sample.txt or as_1_aball_test.txt
    output_file = None or any string, output to console if None
    """
    the_data = get_data(input_file) # None or "as_1_aball_test.txt"
    # three pointers
    three = three_pointers(the_data)
    # most goals
    most = most_goals(the_data)[-1][1]
    # highest score
    highest = sorted_score(the_data)[-1][1]
    # winning score
    team_order, winning_score = highest_team(the_data)
    # losing team, 2nd highest
    second_highest = sorted_score(the_data, team=team_order[1])[-2][1]
    
    if output_file:
        f =  open(output_file, "w")
    else:
        f = None
        
    print(three, file=f)
    print(most, file=f)
    print(highest, file=f)
    print(winning_score, file=f)
    print(second_highest, end=None, file=f) # losing team
    
    if f:
        f.close()
    
if __name__ == "__main__":
    main("as_1_aball_sample.txt")
    main("as_1_aball_test.txt")