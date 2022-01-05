import glob
import json
from tqdm import tqdm

nextWord = {}
file_pattern = 'next-results/*'
filepaths = sorted(glob.glob(file_pattern))
len(filepaths)
for filepath in tqdm(filepaths):
    with open(filepath, 'r') as fp:
        results = json.load(fp)
    nextWord.update(results)

nextWord
