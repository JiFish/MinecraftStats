from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'eat_all',
        {
            'title': 'Wafer Thin Mint',
            'desc': 'Total food eaten',
            'unit': 'int',
        },
        mcstats.StatSumReader([
            mcstats.StatReader(['minecraft:used','minecraft:rotten_flesh']),
            mcstats.StatReader(['minecraft:used','minecraft:spider_eye']),
            mcstats.StatReader(['minecraft:used','minecraft:poisonous_potato']),
            mcstats.StatReader(['minecraft:used','minecraft:cooked_porkchop']),
            mcstats.StatReader(['minecraft:used','minecraft:cooked_beef']),
            mcstats.StatReader(['minecraft:used','minecraft:cooked_chicken']),
            mcstats.StatReader(['minecraft:used','minecraft:cooked_mutton']),
            mcstats.StatReader(['minecraft:used','minecraft:cooked_rabbit']),
            mcstats.StatReader(['minecraft:used','minecraft:porkchop']),
            mcstats.StatReader(['minecraft:used','minecraft:beef']),
            mcstats.StatReader(['minecraft:used','minecraft:chicken']),
            mcstats.StatReader(['minecraft:used','minecraft:mutton']),
            mcstats.StatReader(['minecraft:used','minecraft:rabbit']),
            mcstats.StatReader(['minecraft:used','minecraft:rabbit_stew']),
            mcstats.StatReader(['minecraft:used','minecraft:mushroom_stew']),
            mcstats.StatReader(['minecraft:used','minecraft:beetroot_soup']),
            mcstats.StatReader(['minecraft:used','minecraft:suspicious_stew']),
            mcstats.StatReader(['minecraft:used','minecraft:golden_carrot']),
            mcstats.StatReader(['minecraft:used','minecraft:golden_apple']),
            mcstats.StatReader(['minecraft:used','minecraft:carrot']),
            mcstats.StatReader(['minecraft:used','minecraft:potato']),
            mcstats.StatReader(['minecraft:used','minecraft:baked_potato']),
            mcstats.StatReader(['minecraft:used','minecraft:beetroot']),
            mcstats.StatReader(['minecraft:used','minecraft:apple']),
            mcstats.StatReader(['minecraft:used','minecraft:pumpkin_pie']),
            mcstats.StatReader(['minecraft:used','minecraft:chorus_fruit']),
            mcstats.StatReader(['minecraft:used','minecraft:melon_slice']),
            mcstats.StatReader(['minecraft:used','minecraft:cookie']),
            mcstats.StatReader(['minecraft:used','minecraft:cake']),
            mcstats.StatReader(['minecraft:used','minecraft:bread']),
            mcstats.StatReader(['minecraft:used','minecraft:sweet_berries']),
            mcstats.StatReader(['minecraft:used','minecraft:dried_kelp']),
            mcstats.StatReader(['minecraft:used','minecraft:cookie']),
            mcstats.StatReader(['minecraft:used','minecraft:cooked_salmon']),
            mcstats.StatReader(['minecraft:used','minecraft:cooked_cod']),
            mcstats.StatReader(['minecraft:used','minecraft:salmon']),
            mcstats.StatReader(['minecraft:used','minecraft:cod']),
            mcstats.StatReader(['minecraft:used','minecraft:clownfish']),
            mcstats.StatReader(['minecraft:used','minecraft:tropical_fish']),
            mcstats.StatReader(['minecraft:used','minecraft:honey_bottle']),
        ])
    ))
