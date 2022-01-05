nextWord = {
    '⬛⬛⬛⬛⬛': 'phony',
    '⬛⬛⬛⬛🟨': 'linty',
    '⬛⬛⬛⬛🟩': 'globi',
    '⬛⬛⬛🟨⬛': 'nyala',
    '⬛⬛⬛🟨🟨': 'mania',
    '⬛⬛⬛🟨🟩': 'lathi',
    '⬛⬛⬛🟩⬛': 'canal',
    '⬛⬛⬛🟩🟨': 'nidal',
    '⬛⬛⬛🟩🟩': 'litai',
    '⬛⬛🟨⬛⬛': 'croon',
    '⬛⬛🟨⬛🟨': 'print',
    '⬛⬛🟨⬛🟩': 'briki',
    '⬛⬛🟨🟨⬛': 'orant',
    '⬛⬛🟨🟨🟨': 'drain',
    '⬛⬛🟨🟨🟩': 'cauri',
    '⬛⬛🟨🟩⬛': 'altar',
    '⬛⬛🟨🟩🟨': 'cimar',
    '⬛⬛🟨🟩🟩': 'braai',
    '⬛⬛🟩⬛⬛': 'rorty',
    '⬛⬛🟩⬛🟨': 'lirot',
    '⬛⬛🟩⬛🟩': 'cirri',
    '⬛⬛🟩🟨⬛': 'carry',
    '⬛⬛🟩🟨🟨': 'atria',
    '⬛⬛🟩🟨🟩': 'carpi',
    '⬛⬛🟩🟩⬛': 'aural',
    '⬛⬛🟩🟩🟨': 'diram',
    '⬛⬛🟩🟩🟩': 'korai',
    '⬛🟨⬛⬛⬛': 'dolce',
    '⬛🟨⬛⬛🟨': 'lined',
    '⬛🟨⬛⬛🟩': 'enoki',
    '⬛🟨⬛🟨⬛': 'lawed',
    '⬛🟨⬛🟨🟨': 'maile',
    '⬛🟨⬛🟨🟩': 'aurei',
    '⬛🟨⬛🟩⬛': 'clean',
    '⬛🟨⬛🟩🟨': 'eliad',
    '⬛🟨🟨⬛⬛': 'ormer',
    '⬛🟨🟨⬛🟨': 'rivet',
    '⬛🟨🟨⬛🟩': 'aurei',
    '⬛🟨🟨🟨⬛': 'alter',
    '⬛🟨🟨🟨🟨': 'afire',
    '⬛🟨🟨🟨🟩': 'aurei',
    '⬛🟨🟨🟩⬛': 'aread',
    '⬛🟨🟨🟩🟨': 'perai',
    '⬛🟨🟩⬛⬛': 'borde',
    '⬛🟨🟩⬛🟨': 'direr',
    '⬛🟨🟩🟨⬛': 'carer',
    '⬛🟨🟩🟨🟨': 'aired',
    '⬛🟨🟩🟨🟩': 'aurei',
    '⬛🟨🟩🟩⬛': 'marae',
    '⬛🟩⬛⬛⬛': 'yente',
    '⬛🟩⬛⬛🟨': 'teind',
    '⬛🟩⬛⬛🟩': 'lenti',
    '⬛🟩⬛🟨⬛': 'beaty',
    '⬛🟩⬛🟨🟨': 'tenia',
    '⬛🟩⬛🟩⬛': 'decal',
    '⬛🟩🟨⬛⬛': 'deter',
    '⬛🟩🟨⬛🟨': 'relit',
    '⬛🟩🟨⬛🟩': 'petri',
    '⬛🟩🟨🟨⬛': 'deare',
    '⬛🟩🟨🟨🟨': 'deair',
    '⬛🟩🟨🟩⬛': 'renal',
    '⬛🟩🟩⬛⬛': 'herye',
    '⬛🟩🟩⬛🟨': 'derig',
    '⬛🟩🟩⬛🟩': 'cerci',
    '⬛🟩🟩🟨⬛': 'derat',
    '⬛🟩🟩🟨🟨': 'ceria',
    '⬛🟩🟩🟩⬛': 'deray',
    '⬛🟩🟩🟩🟩': 'perai',
    '🟨⬛⬛⬛⬛': 'loons',
    '🟨⬛⬛⬛🟨': 'lints',
    '🟨⬛⬛⬛🟩': 'sushi',
    '🟨⬛⬛🟨⬛': 'lants',
    '🟨⬛⬛🟨🟨': 'kalis',
    '🟨⬛⬛🟨🟩': 'tarsi',
    '🟨⬛⬛🟩⬛': 'almas',
    '🟨⬛⬛🟩🟨': 'pimas',
    '🟨⬛⬛🟩🟩': 'assai',
    '🟨⬛🟨⬛⬛': 'prost',
    '🟨⬛🟨⬛🟨': 'brits',
    '🟨⬛🟨⬛🟩': 'rishi',
    '🟨⬛🟨🟨⬛': 'brast',
    '🟨⬛🟨🟨🟨': 'amirs',
    '🟨⬛🟨🟩⬛': 'arnas',
    '🟨⬛🟨🟩🟨': 'ribas',
    '🟨⬛🟩⬛⬛': 'borts',
    '🟨⬛🟩⬛🟨': 'lirks',
    '🟨⬛🟩⬛🟩': 'cursi',
    '🟨⬛🟩🟨⬛': 'darks',
    '🟨⬛🟩🟨🟨': 'airns',
    '🟨⬛🟩🟨🟩': 'tarsi',
    '🟨⬛🟩🟩⬛': 'auras',
    '🟨⬛🟩🟩🟨': 'liras',
    '🟨🟨⬛⬛⬛': 'losen',
    '🟨🟨⬛⬛🟨': 'nites',
    '🟨🟨⬛⬛🟩': 'issei',
    '🟨🟨⬛🟨⬛': 'mased',
    '🟨🟨⬛🟨🟨': 'maise',
    '🟨🟨⬛🟩⬛': 'ephas',
    '🟨🟨⬛🟩🟨': 'ideas',
    '🟨🟨🟨⬛⬛': 'trees',
    '🟨🟨🟨⬛🟨': 'risen',
    '🟨🟨🟨🟨⬛': 'arets',
    '🟨🟨🟨🟨🟨': 'arise',
    '🟨🟨🟨🟩⬛': 'shear',
    '🟨🟨🟩⬛⬛': 'bores',
    '🟨🟨🟩⬛🟨': 'cires',
    '🟨🟨🟩🟨⬛': 'acres',
    '🟨🟨🟩🟩⬛': 'eyras',
    '🟨🟩⬛⬛⬛': 'leets',
    '🟨🟩⬛⬛🟨': 'denis',
    '🟨🟩⬛⬛🟩': 'besti',
    '🟨🟩⬛🟨⬛': 'least',
    '🟨🟩⬛🟨🟨': 'sepia',
    '🟨🟩⬛🟩⬛': 'besat',
    '🟨🟩🟨⬛⬛': 'reset',
    '🟨🟩🟨⬛🟨': 'heirs',
    '🟨🟩🟨🟨⬛': 'reads',
    '🟨🟩🟨🟨🟨': 'aesir',
    '🟨🟩🟨🟩⬛': 'resat',
    '🟨🟩🟩⬛⬛': 'merks',
    '🟨🟩🟩⬛🟨': 'meris',
    '🟨🟩🟩🟨⬛': 'aeros',
    '🟨🟩🟩🟩⬛': 'serac',
    '🟩⬛⬛⬛⬛': 'slots',
    '🟩⬛⬛⬛🟨': 'skits',
    '🟩⬛⬛⬛🟩': 'sushi',
    '🟩⬛⬛🟨⬛': 'slats',
    '🟩⬛⬛🟨🟨': 'satin',
    '🟩⬛⬛🟨🟩': 'sampi',
    '🟩⬛⬛🟩⬛': 'solas',
    '🟩⬛⬛🟩🟨': 'sidas',
    '🟩⬛⬛🟩🟩': 'satai',
    '🟩⬛🟨⬛⬛': 'sport',
    '🟩⬛🟨⬛🟨': 'skirt',
    '🟩⬛🟨🟨⬛': 'starn',
    '🟩⬛🟨🟨🟨': 'stair',
    '🟩⬛🟨🟩⬛': 'solar',
    '🟩⬛🟨🟩🟨': 'simar',
    '🟩⬛🟩⬛⬛': 'stroy',
    '🟩⬛🟩⬛🟨': 'strip',
    '🟩⬛🟩🟨⬛': 'sards',
    '🟩⬛🟩🟨🟨': 'sarin',
    '🟩⬛🟩🟩⬛': 'scrat',
    '🟩🟨⬛⬛⬛': 'sleet',
    '🟩🟨⬛⬛🟨': 'spiel',
    '🟩🟨⬛⬛🟩': 'segni',
    '🟩🟨⬛🟨⬛': 'slade',
    '🟩🟨⬛🟨🟨': 'saice',
    '🟩🟨⬛🟩⬛': 'stean',
    '🟩🟨🟨⬛⬛': 'shero',
    '🟩🟨🟨⬛🟨': 'skier',
    '🟩🟨🟨🟨⬛': 'safer',
    '🟩🟨🟨🟩⬛': 'smear',
    '🟩🟨🟩⬛⬛': 'sored',
    '🟩🟨🟩⬛🟨': 'siren',
    '🟩🟨🟩🟨⬛': 'sared',
    '🟩🟨🟩🟩⬛': 'scrae',
    '🟩🟩⬛⬛⬛': 'sense',
    '🟩🟩⬛⬛🟨': 'seise',
    '🟩🟩⬛⬛🟩': 'segni',
    '🟩🟩⬛🟨⬛': 'seals',
    '🟩🟩⬛🟨🟨': 'sepia',
    '🟩🟩⬛🟩⬛': 'sedan',
    '🟩🟩🟨⬛⬛': 'sever',
    '🟩🟩🟨⬛🟨': 'serif',
    '🟩🟩🟨⬛🟩': 'sehri',
    '🟩🟩🟨🟨⬛': 'seare',
    '🟩🟩🟨🟩⬛': 'segar',
    '🟩🟩🟩⬛⬛': 'seres',
    '🟩🟩🟩⬛🟨': 'serif',
    '🟩🟩🟩🟨⬛': 'serac',
    '🟩🟩🟩🟩⬛': 'serac',
}
