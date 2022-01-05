import argparse
import copy
import json
import os

from wordle import words, computeGreedyBestWord

def splitIntoChunks(lst, chunkSize):
    for i in range(0, len(lst), chunkSize):
        yield lst[i : i + chunkSize]

def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--easy-mode', action='store_true',
                        help="Disable hard mode; guesses don't need to meet additional requirements")
    parser.add_argument('-s','--seed', type=int, default=0,
                        help='Random seed')
    parser.add_argument('-c','--chunk-size', type=int, default=10,
                        help='Number of words to process per job')
    parser.add_argument("-f", "--fool_ipython", help="Dummy arg to fool ipython", default="1")
    args = parser.parse_args()

    validWords = copy.deepcopy(words)

    chunks = list(splitIntoChunks(words, args.chunk_size))
    assert 0 <= args.seed < len(chunks)
    allowedWords = chunks[args.seed]

    bestWord, worstCaseValidSetSize, worstCaseScore = computeGreedyBestWord(validWords=words, allowedWords=allowedWords, hardMode=(not args.easy_mode), outputCalculations=True, shortCircuit=False)

    results = {word: (worstCaseValidSetSize[word], worstCaseScore[word]) for word in allowedWords}
    results_dir = 'results'
    os.makedirs(results_dir, exist_ok=True)
    filename = 'words-{:05d}-to-{:05d}.json'.format(args.seed * args.chunk_size, (args.seed + 1) * args.chunk_size - 1)
    output_file = os.path.join(results_dir, filename)
    with open(output_file, 'w') as fp:
        json.dump(results, fp)

main()
