# sor activites based on finish time
# select first activity from sorted array and print it.
# For all remain activites
#   if the start time of this activity is greater than or equal to the finish time
#   of previous selected activity then select this activity and print it.

activities = [
    ["A1", 0, 6],
    ["A2", 3, 4],
    ["A3", 1, 2],
    ["A4", 5, 8],
    ["A5", 5, 7],
    ["A6", 8, 9]
]


def get_max_activity(activities):
    activities.sort(key=lambda x: x[2])
    i = 0
    first_A = activities[i][0]
    print(first_A)
    for j in range(len(activities)):
        if activities[j][1] > activities[i][2]:
            print(activities[j][0])
            i = j


get_max_activity(activities)
