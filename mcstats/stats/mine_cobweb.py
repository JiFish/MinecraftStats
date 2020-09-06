from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_cobweb',
        {
            'title': 'Web Remover',
            'desc': 'Cobweb removed',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:mined','minecraft:cobweb'])
    ))
