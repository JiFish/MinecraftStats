from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'guild',
        {
            'title': 'Adventurer\'s Guild',
            'desc': 'Advancements Made',
            'unit': 'int',
        },
        mcstats.StatCountAdvancementGroup(
            [['quest:pirate','quest:puzzle','quest:tree','quest:redo','quest:time'],
            []])
    ))
