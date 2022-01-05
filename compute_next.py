import argparse
from collections import namedtuple, defaultdict
import copy
import json
import os
import string
from enum import Enum

from tqdm import tqdm

from wordle import words, computeGreedyBestWord, scoreWord, score2str, str2score, interpretScore, restrictValidWords, restrictAllowedWords


def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--easy-mode', action='store_true',
                        help="Disable hard mode; guesses don't need to meet additional requirements")
    parser.add_argument('-s','--seed', type=int, default=0,
                        help='Random seed')
    parser.add_argument("-f", "--fool_ipython", help="Dummy arg to fool ipython", default="1")
    args = parser.parse_args()

    guess = 'serai'
    validWords = words
    allowedWords = words
    possibleScores = defaultdict(list)
    for potential_goal in words:
        if potential_goal == 'serai':
            continue
        hypotheticalScore = scoreWord(guess, potential_goal)
        possibleScores[score2str(hypotheticalScore)].append(potential_goal)

    len(possibleScores)
    assert 0 <= args.seed < len(possibleScores)

    hypotheticalScore = sorted(possibleScores.items())[args.seed][0]
    hypothetical_info = interpretScore(guess, str2score(hypotheticalScore))
    hypothetical_validWords = restrictValidWords(validWords, hypothetical_info)
    hypothetical_allowedWords = restrictAllowedWords(allowedWords=words,
                                        wordList=words,
                                        info=hypothetical_info,
                                        lastWord=guess,
                                        hardMode=(not args.easy_mode))

    bestWord, worstCaseValidSetSize, worstCaseScore = computeGreedyBestWord(
            validWords=hypothetical_validWords,
            allowedWords=hypothetical_allowedWords,
            info=hypothetical_info,
            hardMode=(not args.easy_mode),
            outputCalculations=True,
    )

    result = {hypotheticalScore: bestWord}

    results_dir = 'next-results'
    os.makedirs(results_dir, exist_ok=True)
    filename = 'outcome-{:03d}.json'.format(args.seed)
    output_file = os.path.join(results_dir, filename)
    with open(output_file, 'w') as fp:
        json.dump(result, fp)

main()
