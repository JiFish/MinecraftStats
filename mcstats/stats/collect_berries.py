from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'collect_berries',
        {
            'title': 'Berry Collector',
            'desc': 'Sweet berries collected',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:picked_up','minecraft:sweet_berries']),
        1916 # berries introduced in 18w49a
    ))
