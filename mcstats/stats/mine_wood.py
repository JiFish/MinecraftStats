from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_wood',
        {
            'title': 'Lumberjack',
            'desc': 'Wood blocks cut',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:mined'],['minecraft:.+_log', 'minecraft:.+_stem'])
    ))
