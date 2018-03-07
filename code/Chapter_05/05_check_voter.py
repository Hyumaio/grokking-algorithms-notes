voted = {}


def check_voter(name):
    if voted.get(name):
        print('Already voted, invalidate this vote...')
    else:
        voted[name] = True
        print('Thanks for your vote...')


check_voter('fiona')  # OUT: Thanks for your vote...
check_voter('lip')  # OUT: Thanks for your vote...
check_voter('fiona')  # OUT: Already voted, invalidate this vote...
