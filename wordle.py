from collections import namedtuple, defaultdict
import copy
import json
import string
from enum import Enum

from tqdm import tqdm

with open('wordle_words_part_1.txt', 'r') as fp:
    wordsPart1 = json.load(fp)

with open('wordle_words_part_2.txt', 'r') as fp:
    wordsPart2 = json.load(fp)

words = wordsPart1 + wordsPart2
letters = string.ascii_lowercase
len(words)

pastGoals = [
    'tapir',
    'troll',
    'unify',
    'rebus',
    'boost',
    'truss',
    'siege',
]
[g in wordsPart1 for g in pastGoals]

max([max({l: word.count(l) for l in letters}.values()) for word in words])

class Color(Enum):
    GREEN = '🟩'
    YELLOW = '🟨'
    BLACK = '⬛'
    DONE = '❌'
    UNDEFINED = ' '

    def __str__(self):
        return self.value

CORRECT = '🟩🟩🟩🟩🟩'

PuzzleInfo = namedtuple(
    'PuzzleInfo', ['requiredLetters', 'letterRestrictions', 'maxOccurences', 'minOccurences'])
NoInfo = PuzzleInfo(
    ['' for _ in range(5)],
    [set() for _ in range(5)],
    {l: 5 for l in letters},
    {l: 0 for l in letters},
)# yapf: disable

def checkWord(guess: str, goal: str):
    return guess == goal

def scoreWord(guess: str, goal: str):
    goalLetterCounts = {l: goal.count(l) for l in letters}

    score = [Color.UNDEFINED] * 5
    for i, (guessLetter, goalLetter) in enumerate(zip(guess, goal)):
        if guessLetter == goalLetter:
            score[i] = Color.GREEN
            goalLetterCounts[guessLetter] -= 1

    for i, guessLetter in enumerate(guess):
        if score[i] != Color.GREEN:
            if goalLetterCounts[guessLetter] > 0:
                goalLetterCounts[guessLetter] -= 1
                score[i] = Color.YELLOW
            else:
                score[i] = Color.BLACK
    return score

def score2str(score: list):
    return ''.join(map(str, score))

def str2score(scoreStr: str):
    return list(map(Color, scoreStr))

def test_scoring():
    for guess, goal, score in [
            #193
        ('loser', 'tapir', '⬛⬛⬛⬛🟩'),
        ('chair', 'tapir', '⬛⬛🟨🟩🟩'),
        ('nadir', 'tapir', '⬛🟩⬛🟩🟩'),
        ('tapir', 'tapir', '🟩🟩🟩🟩🟩'),
            #194
        ('laser', 'troll', '🟨⬛⬛⬛🟨'),
        ('broil', 'troll', '⬛🟩🟩⬛🟩'),
        ('troll', 'troll', '🟩🟩🟩🟩🟩'),
            #195
        ('laser', 'unify', '⬛⬛⬛⬛⬛'),
        ('point', 'unify', '⬛⬛🟩🟨⬛'),
        ('unify', 'unify', '🟩🟩🟩🟩🟩'),
            #196
        ('laser', 'rebus', '⬛⬛🟨🟨🟨'),
        ('store', 'rebus', '🟨⬛⬛🟨🟨'),
        ('rends', 'rebus', '🟩🟩⬛⬛🟩'),
        ('reefs', 'rebus', '🟩🟩⬛⬛🟩'),
        ('rebus', 'rebus', '🟩🟩🟩🟩🟩'),
            #197
        ('laser', 'boost', '⬛⬛🟨⬛⬛'),
        ('pouts', 'boost', '⬛🟩⬛🟨🟨'),
        ('hoist', 'boost', '⬛🟩⬛🟩🟩'),
        ('boost', 'boost', '🟩🟩🟩🟩🟩'),
            #198
        ('laser', 'truss', '⬛⬛🟨⬛🟨'),
        ('sours', 'truss', '🟨⬛🟩🟨🟩'),
        ('truss', 'truss', '🟩🟩🟩🟩🟩'),
            #199
        ('laser', 'siege', '⬛⬛🟨🟨⬛'),
        ('shine', 'siege', '🟩⬛🟨⬛🟩'),
        ('suite', 'siege', '🟩⬛🟨⬛🟩'),
        ('sieve', 'siege', '🟩🟩🟩⬛🟩'),
        ('siege', 'siege', '🟩🟩🟩🟩🟩'),
            # other tests
        ('bunty', 'unify', '⬛🟨🟨⬛🟩'),
        ('palay', 'unify', '⬛⬛⬛⬛🟩'),
        ('sores', 'boost', '🟨🟩⬛⬛⬛'),
        ('sores', 'truss', '🟨⬛🟨⬛🟩'),
        ('arars', 'truss', '⬛🟩⬛⬛🟩'),
        ('rears', 'truss', '🟨⬛⬛⬛🟩'),
        ('sassy', 'isles', '🟨⬛🟨⬛⬛'),
    ]:
        assert score2str(scoreWord(
            guess, goal)) == score, "guess '{}' for goal '{}' scored {} != {} expected".format(
                guess, goal, score2str(scoreWord(guess, goal)), score)

# guess = 'sassy'
# score = str2score('🟨⬛🟨⬛⬛')
#
# guess = 'rears'
# score = str2score('🟨⬛⬛⬛🟩')
#
# guess = 'cigar'
# score = str2score('⬛⬛🟨🟩🟩')

def interpretScore(guess: str, score: list):
    letterColors = {
        l: [color for (letter, color) in zip(guess, score) if letter == l]
        for l in guess
    }
    nOccurences = {l: guess.count(l) for l in guess}
    nBlack = {l: letterColors[l].count(Color.BLACK) for (l, colors) in zip(guess, score)}
    nYellow = {l: letterColors[l].count(Color.YELLOW) for (l, colors) in zip(guess, score)}

    requiredLetters = [
        letter if color == Color.GREEN else '' for (letter, color) in zip(guess, score)
    ]

    letterRestrictions = [set() for _ in range(5)]
    for i, (letter, color) in enumerate(zip(guess, score)):
        if color != Color.GREEN:
            letterRestrictions[i].add(letter)
            for guessed_letter in guess:
                if guessed_letter != letter and nBlack[guessed_letter] > 0 and nYellow[
                        guessed_letter] == 0:
                    letterRestrictions[i].add(guessed_letter)

    maxOccurences = {l: 5 if nBlack[l] == 0 else nOccurences[l] - nBlack[l] for l in guess}
    minOccurences = {l: 0 if nOccurences[l] == 0 else nOccurences[l] - nBlack[l] for l in guess}

    info = PuzzleInfo(requiredLetters, letterRestrictions, maxOccurences, minOccurences)
    return info

def isWordAllowed(word: str, wordList: list, info: PuzzleInfo, hardMode: bool = True):
    if word not in wordList:
        return False

    if hardMode:
        for i, letter in enumerate(word):
            if info.requiredLetters[i] and letter != info.requiredLetters[i]:
                # print('{} required at position {}'.format(info.requiredLetters[i], i))
                return False
        # only compute/check nOccurences if necessary
        nOccurences = defaultdict(int, {letter: word.count(letter) for letter in word})
        for letter, minOccurences in info.minOccurences.items():
            if minOccurences > 0 and letter not in word or nOccurences[letter] < minOccurences:
                # print("'{}' must occur at least {} times".format(letter, minOccurences))
                return False
    return True

def isWordCompatibleWithInfo(word: str, info: PuzzleInfo, hardMode: bool = True):
    for i, letter in enumerate(word):
        if info.requiredLetters[i] and letter != info.requiredLetters[i]:
            # print('{} required at position {}'.format(info.requiredLetters[i], i))
            return False
        if info.letterRestrictions[i] and letter in info.letterRestrictions[i]:
            # print('{} forbidden at position {}'.format(info.requiredLetters[i], i))
            if hardMode:
                return False
    # only compute/check nOccurences if necessary
    nOccurences = defaultdict(int, {letter: word.count(letter) for letter in word})
    for letter, maxOccurences in info.maxOccurences.items():
        if letter in word and nOccurences[letter] > maxOccurences:
            # print("'{}' must occur at most {} times".format(letter, maxOccurences))
            return False
    for letter, minOccurences in info.minOccurences.items():
        if minOccurences > 0 and letter not in word or nOccurences[letter] < minOccurences:
            # print("'{}' must occur at least {} times".format(letter, minOccurences))
            return False
    return True

def test_compatibility():
    # all words should be compatible when no info has been given yet
    for word in words:
        assert isWordCompatibleWithInfo(word, NoInfo)

def restrictValidWords(validWords: list, info: PuzzleInfo):
    newValidWords = [word for word in validWords if isWordCompatibleWithInfo(word, info)]
    return newValidWords

def restrictAllowedWords(allowedWords: list,
                         wordList: list = None,
                         info: PuzzleInfo = NoInfo,
                         lastWord: str = None,
                         hardMode: bool = True):
    if wordList is None:
        wordList = words
    newAllowedWords = [
        word for word in allowedWords
        if isWordAllowed(word, wordList, info, hardMode=hardMode) and word != lastWord
    ]
    return newAllowedWords

def updateInfo(oldInfo: PuzzleInfo, newInfo: PuzzleInfo):
    updatedInfo = copy.deepcopy(oldInfo)
    for i in range(5):
        if not updatedInfo.requiredLetters[i]:
            updatedInfo.requiredLetters[i] = newInfo.requiredLetters[i]
        updatedInfo.letterRestrictions[i] = updatedInfo.letterRestrictions[i].union(
            newInfo.letterRestrictions[i])
    for letter, maxOccurences in updatedInfo.maxOccurences.items():
        if letter in newInfo.maxOccurences and newInfo.maxOccurences[letter] < maxOccurences:
            updatedInfo.maxOccurences[letter] = newInfo.maxOccurences[letter]
    for letter, minOccurences in updatedInfo.minOccurences.items():
        if letter in newInfo.minOccurences and newInfo.minOccurences[letter] > minOccurences:
            updatedInfo.minOccurences[letter] = newInfo.minOccurences[letter]
    return updatedInfo

def test_valid_solves():
    for solve in [
        [
            #193
            ('loser', 'tapir', '⬛⬛⬛⬛🟩'),
            ('chair', 'tapir', '⬛⬛🟨🟩🟩'),
            ('nadir', 'tapir', '⬛🟩⬛🟩🟩'),
            ('tapir', 'tapir', '🟩🟩🟩🟩🟩'),
        ],
        [
            #194
            ('laser', 'troll', '🟨⬛⬛⬛🟨'),
            ('broil', 'troll', '⬛🟩🟩⬛🟩'),
            ('troll', 'troll', '🟩🟩🟩🟩🟩'),
        ],
        [
            #195
            ('laser', 'unify', '⬛⬛⬛⬛⬛'),
            ('point', 'unify', '⬛⬛🟩🟨⬛'),
            ('unify', 'unify', '🟩🟩🟩🟩🟩'),
        ],
        [
            #196
            ('laser', 'rebus', '⬛⬛🟨🟨🟨'),
            ('store', 'rebus', '🟨⬛⬛🟨🟨'),
            ('rends', 'rebus', '🟩🟩⬛⬛🟩'),
            ('reefs', 'rebus', '🟩🟩⬛⬛🟩'),
            ('rebus', 'rebus', '🟩🟩🟩🟩🟩'),
        ],
        [
            #197
            ('laser', 'boost', '⬛⬛🟨⬛⬛'),
            ('pouts', 'boost', '⬛🟩⬛🟨🟨'),
            ('hoist', 'boost', '⬛🟩⬛🟩🟩'),
            ('boost', 'boost', '🟩🟩🟩🟩🟩'),
        ],
        [
            #198
            ('laser', 'truss', '⬛⬛🟨⬛🟨'),
            ('sours', 'truss', '🟨⬛🟩🟨🟩'),
            ('truss', 'truss', '🟩🟩🟩🟩🟩'),
        ],
        [
            #199
            ('laser', 'siege', '⬛⬛🟨🟨⬛'),
            ('shine', 'siege', '🟩⬛🟨⬛🟩'),
            ('sieve', 'siege', '🟩🟩🟩⬛🟩'),
            ('siege', 'siege', '🟩🟩🟩🟩🟩'),
        ]
    ]:
        info = NoInfo
        validWords = words
        goal = solve[-1][1]
        it = iter(solve)
        step = next(it)
        for step in solve:
            guess, _, observedScore = step
            print('guess: {}'.format(guess), end='   ')
            assert isWordAllowed(guess, words, info,
                                 hardMode=False), "'{}' is not in the word list".format(guess)
            assert isWordAllowed(guess, words, info,
                                 hardMode=True), "'{}' violates hard mode".format(guess)
            assert guess in validWords, "'{}' not compatible with all known information".format(
                guess)
            score = scoreWord(guess, goal)
            print('score: {}'.format(score2str(score)))
            assert score2str(score) == observedScore
            new_info = interpretScore(guess, score)
            validWords = restrictValidWords(validWords, new_info)
            info = updateInfo(info, new_info)
        print()
        assert score2str(score) == CORRECT

def test_suboptimal_solve():
    for solve in [[
            #199
        ('laser', 'siege', '⬛⬛🟨🟨⬛'),
        ('shine', 'siege', '🟩⬛🟨⬛🟩'),
        ('suite', 'siege', '🟩⬛🟨⬛🟩'),
        ('sieve', 'siege', '🟩🟩🟩⬛🟩'),
        ('siege', 'siege', '🟩🟩🟩🟩🟩'),
    ]]:
        info = NoInfo
        validWords = words
        goal = solve[-1][1]
        it = iter(solve)
        step = next(it)
        for step in solve:
            guess, _, observedScore = step
            print('guess: {}'.format(guess), end='   ')
            assert isWordAllowed(guess, words, info,
                                 hardMode=False), "'{}' is not in the word list".format(guess)
            assert isWordAllowed(guess, words, info,
                                 hardMode=True), "'{}' violates hard mode".format(guess)
            if guess == 'suite':
                assert guess not in validWords, "'{}' not supposed to be compatible with known information".format(
                    guess)
            score = scoreWord(guess, goal)
            print('score: {}'.format(score2str(score)))
            assert score2str(score) == observedScore
            new_info = interpretScore(guess, score)
            validWords = restrictValidWords(validWords, new_info)
            info = updateInfo(info, new_info)
        print()
        assert score2str(score) == '🟩🟩🟩🟩🟩'

def computeGreedyBestWord(validWords: list,
                          allowedWords: list = None,
                          info: PuzzleInfo = NoInfo,
                          hardMode: bool = True,
                          outputCalculations: bool = False):
    if allowedWords is None:
        allowedWords = words

    worstCaseSizeForBestWordSoFar = len(validWords)

    worstCaseValidSetSize = defaultdict(int)
    # it = iter(allowedWords)
    # word = next(it)
    for word in tqdm(allowedWords):
        possibleScores = set()
        for potential_goal in validWords:
            hypotheticalScore = scoreWord(word, potential_goal)
            possibleScores.add(score2str(hypotheticalScore))
        # it2 = iter(possibleScores)
        # hypotheticalScore = next(it2)
        for hypotheticalScore in possibleScores:
            hypothetical_info = interpretScore(word, str2score(hypotheticalScore))
            newValidWords = restrictValidWords(validWords, hypothetical_info)
            worstCaseValidSetSize[word] = max(worstCaseValidSetSize[word], len(newValidWords))
            if worstCaseValidSetSize[word] > worstCaseSizeForBestWordSoFar:
                break

        bestWord = min(worstCaseValidSetSize, key=worstCaseValidSetSize.get)
        worstCaseSizeForBestWordSoFar = worstCaseValidSetSize[bestWord]

    if outputCalculations:
        result = bestWord, worstCaseValidSetSize
    else:
        result = bestWord

    return result

def solve():
    goal = 'tapir'
    hardMode = True
    validWords = copy.deepcopy(words)
    allowedWords = copy.deepcopy(words)
    info = NoInfo

    guess = computeGreedyBestWord(validWords, hardMode=True, outputCalculations=True)
    print('guess: {}'.format(guess), end='   ')
    score = scoreWord(guess, goal)
    print(score2str(score))
    info = interpretScore(guess, score)
    validWords = restrictValidWords(validWords, info)
    allowedWords = restrictAllowedWords(allowedWords=words,
                                        wordList=words,
                                        info=info,
                                        lastWord=guess,
                                        hardMode=hardMode)
    len(allowedWords)

    while score2str(score) != CORRECT:
        guess, calcs = computeGreedyBestWord(validWords,
                                             allowedWords,
                                             info,
                                             hardMode=True,
                                             outputCalculations=True)
        print('guess: {}'.format(guess), end='   ')
        score = scoreWord(guess, goal)
        print(score2str(score))
        new_info = interpretScore(guess, score)
        validWords = restrictValidWords(validWords, new_info)
        allowedWords = restrictAllowedWords(allowedWords,
                                            info=new_info,
                                            lastWord=guess,
                                            hardMode=hardMode)
        len(allowedWords)
        info = updateInfo(info, new_info)

def test():
    test_scoring()
    test_compatibility()
    test_valid_solves()
    test_suboptimal_solve()
    print('All tests passed.')

# solve()
