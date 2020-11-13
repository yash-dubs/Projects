"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    counter = 0
    for x in paragraphs:
        if counter == k and select(x):
            counter = counter + 1
            return x
        if select(x):
            counter = counter + 1
    return ''
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    def helper(paragraphs):
        paragraph = split(remove_punctuation(lower(paragraphs)))
        for x in topic:
            for y in paragraph:
                if x == y:
                    return True
        return False

    return helper
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """

    # BEGIN PROBLEM 3
    #break

    typed_words = split(typed)
    reference_words = split(reference)

    total = 0
    if len(reference_words) == 0 or len(typed_words) == 0:
        return 0.0
    for i in range(min(len(typed_words),len(reference_words))):
        if typed_words[i] == reference_words[i]:
            total += 1
    return (total/len(typed_words)) * 100

    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    typed1_len = len(typed)
    return (typed1_len/5) / (elapsed/ 60)



    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    minimum = 100
    corrected_word = 0
    if user_word in valid_words:
        return user_word
    for y in valid_words:
        if user_word == y:
            return user_word
        else:
            m = diff_function(user_word, y, limit)
            if m < minimum:
                minimum = m
                corrected_word = y
    if minimum > limit:
        return user_word
    return corrected_word

    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6

    def helper(start, goal, limit, counter):
        if len(start) == 0 and len(goal) != 0:
            counter = counter + len(goal)
            return counter
        if len(goal) == 0 and len(start) != 0:
            counter = counter + len(start)
            return counter
        elif len(start) == 0 or len(goal) == 0:
            return counter
        elif counter > limit:
            return counter
        elif start[0] != goal[0]:
            return helper(start[1:], goal[1:], limit, counter + 1)
        else:
            return helper(start[1:], goal[1:], limit, counter)
    return helper(start, goal, limit, 0)


    # END PROBLEM 6


def meowstake_matches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""

    if start == goal or limit < 0: # Fill in the condition
        # BEGIN
        return 0
        # END

    elif len(start) == 0 or len(goal) == 0: # Feel free to remove or add additional cases
        # BEGIN
        return max(len(start), len(goal))
        # END

    else:
        add_diff = meowstake_matches(start, goal[1:], limit - 1) # remove goal
        remove_diff = meowstake_matches(start[1:], goal, limit - 1) # remove start
        if start[0] == goal[0]:
            substitute_diff = meowstake_matches(start[1:], goal[1:], limit) - 1
        else:
            substitute_diff = meowstake_matches(start[1:], goal[1:], limit - 1)
        # BEGIN

        return 1 + min(add_diff, remove_diff, substitute_diff)
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
     # send dictionary, return #
    z = 0
    correct_so_far = 0
    index = 0
    while index < len(typed):
        if typed[index] == prompt[index]:
            correct_so_far = correct_so_far + 1
        else:
            index = len(typed)
        index = index + 1

    z = correct_so_far / len(prompt)
    send({"id": id, "progress": z})
    return z




    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9

    times = [[abs(x[index] - x[index + 1]) for index in range(len(x) - 1)] for x in times_per_player]
    return game(words, times)
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    players = range(len(all_times(game)))  # An index for each player
    words = range(len(all_words(game)))    # An index for each word
    # BEGIN PROBLEM 10
    list = [['a'] for x in players]
    for w in words:
        index = 0
        word_ats = word_at(game, w)
        times = time(game, index, w)
        for p in players[1:]:
            times1 = time(game, p, w)
            if times > times1:
                times = times1
                index = p
        list[index].append(word_ats)
    return [lst[1:] for lst in list]


    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you

##########################
# Extra Credit #
##########################

key_distance = get_key_distances()
def key_distance_diff(start, goal, limit):
    """ A diff function that takes into account the distances between keys when
    computing the difference score."""

    start = start.lower() #converts the string to lowercase
    goal = goal.lower() #converts the string to lowercase

    # BEGIN PROBLEM EC1


    if start == goal: # Fill in the condition
        return 0
    elif goal in start or start in goal:
        return abs(len(start) - len(goal))
    elif limit < 1:
        return float('inf')
    elif len(start) == 0 or len(goal) == 0: # Feel free to remove or add additional cases
        return max(len(start), len(goal))

    else:



        while start[0] == goal[0]:
            start = start[1:]
            goal = goal[1:]
        add_diff = 1 + key_distance_diff(start, goal[1:], limit - 1)  # remove goal
        remove_diff = 1 + key_distance_diff(start[1:], goal, limit - 1)  # remove start
        substitute_diff = key_distance_diff(start[1:], goal[1:], limit - key_distance[start[0], goal[0]]) + key_distance[start[0], goal[0]]
        if start[0] == goal[0]:
            return key_distance[start[0], goal[0]]
        if add_diff < 1:
            r = add_diff
            return r
        if substitute_diff < 1:
            r = substitute_diff
            return r
        if remove_diff < 1:
            r = remove_diff
            return r




        r = min(add_diff, remove_diff, substitute_diff)
        return r
    # END PROBLEM EC1

def memo(f):
    """A memoization function as seen in John Denero's lecture on Growth"""

    cache = {}
    def memoized(*args):
        list = []
        for arg in args:
            if type(arg) == list:
                arg = tuple(arg)
            list.append(arg)
        args = tuple(list)
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return memoized


key_distance_diff = memo(key_distance_diff)
key_distance_diff = count(key_distance_diff)

def faster_autocorrect(user_word, valid_words, diff_function, limit):
    """A memoized version of the autocorrect function implemented above."""

    # BEGIN PROBLEM EC2

    return autocorrect(user_word, tuple(valid_words), memo(diff_function), limit)
    # END PROBLEM EC2


faster_autocorrect = memo(faster_autocorrect)
meowstake_matches = memo(meowstake_matches)
##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)