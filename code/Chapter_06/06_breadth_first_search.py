import collections as cl

GRAPH = {"you": ["alice", "bob", "claire"], "bob": ["anuj", "peggy"], "alice": ["peggy"], "claire": ["thom", "jonny"], "anuj": [], "peggy": [], "thom": [], "jonny": []}


def is_mango_seller(person):
    return True if person == 'jonny' else False


def breadth_first_search(name):
    search_queue = cl.deque()  # double-ended queue
    search_queue += GRAPH[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if is_mango_seller(person):
                return 'BINGO!!! {} is a mango seller!!!'.format(person)
            else:
                print('{} is not a mango seller...'.format(person))
                search_queue += GRAPH[person]
                searched.append(person)
    return "Can't find a mango seller..."


if __name__ == '__main__':
    print(breadth_first_search("you"))
