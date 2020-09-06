from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_honey_bottle',
        {
            'title': 'Honey Monster',
            'desc': 'Honey bottles drunk',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:honey_bottle']),
        2200 # honey added in 19w34a
    ))
