from mcstats import mcstats
mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_flower',
        {
            'title': 'Flower Picker',
            'desc': 'Flowers picked',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:mined'],
            ['minecraft:dandelion',
             'minecraft:poppy',
             'minecraft:blue_orchid',
             'minecraft:allium',
             'minecraft:azure_bluet',
             'minecraft:red_tulip',
             'minecraft:orange_tulip',
             'minecraft:white_tulip',
             'minecraft:pink_tulip',
             'minecraft:oxeye_daisy',
             'minecraft:cornflower',
             'minecraft:lily_of_the_valley',
             'minecraft:wither_rose',
             'minecraft:sunflower',
             'minecraft:lilac',
             'minecraft:rose_bush',
             'minecraft:peony']),
    ))
