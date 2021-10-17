T = (1, 2, 3, 4)
len(T)
T + (5, 6)  # (1, 2, 3, 4, 5, 6)
T  # (1, 2, 3, 4)

T.index(4)  # 4 appears at 3rd index location. Index starts at 0
T.count(3)  # 1. Number of entries.

# Making a new tuple
T = (2,) + T[1:]
T  # (2, 2, 3, 4)

# multiple data types in a tuple
T = 'spam', 3.0, [11, 12, 13]
type(T)  # <class 'tuple'>
T[1]  # 3.0. Navigating as usual.