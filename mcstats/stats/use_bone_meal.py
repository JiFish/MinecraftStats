from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'use_bone_meal',
        {
            'title': 'Green Thumb',
            'desc': 'Bone Meal Used',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:used','minecraft:bone_meal'])
    ))
