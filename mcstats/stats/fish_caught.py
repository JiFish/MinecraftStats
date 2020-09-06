from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'fish_caught',
        {
            'title': 'Fisherman',
            'desc': 'Fish caught',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:fish_caught']),
        1912 # Not sure when this stat was introduced
    ))
