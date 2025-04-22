from enum import IntEnum

class AnixartComment(IntEnum):
    DISLIKE = 1
    LIKE = 2

class AnixartProfileVotedSort(IntEnum):
    LAST_FIRST = 1
    OLD_FIRST = 2
    STAR_5 = 3
    STAR_4 = 4
    STAR_3 = 5
    STAR_2 = 6
    STAR_1 = 7

class AnixartLists(IntEnum):
    WATCHING = 1
    IN_PLANS = 2
    WATCHED = 3
    POSTPONED = 4
    DROPPED = 5

class AnixartReleaseStatus(IntEnum):
    FINISHED = 1,
    ONGOING = 2,
    UPCOMING = 3

class AnixartReleaseCategory(IntEnum):
    SERIES = 1,
    MOVIES = 2,
    OVA = 3

class AnixartReleaseAgeRating(IntEnum):
    G = 1, # 0+
    PG6 = 2 # 6+
    PG12 = 3, # 12+
    R16 = 4 # 16+
    R18 = 5 # 18+

class AnixartReleaseSeason(IntEnum):
    WINTER = 1,
    SPRING = 2
    SUMMER = 3
    FALL = 4