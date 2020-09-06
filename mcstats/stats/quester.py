from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'quester',
        {
            'title': 'Secret of Zephyros',
            'desc': 'Advancements Made',
            'unit': 'int',
        },
        mcstats.StatCountAdvancementGroup(
            [['quest:'],
            ['quest:day_','quest:birthday_','quest:pirate','quest:puzzle','quest:tree','quest:redo','quest:time','quest:recipies','quest:root','quest:advent_root']])
    ))
