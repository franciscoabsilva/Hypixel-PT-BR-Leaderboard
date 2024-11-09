import json, requests
from discord import colour
from math import *
import discord, asyncio, datetime
from discord.ext import commands, tasks
from itertools import zip_longest

api_key = ""
bot_token = ''

stat_title = {
    "playerLevel": "Network Level",
    "playerAp": "Achievement Points",
    "playerQuests": "Quests",
    "playerKarma": "Karma",
    "playerGiftsSent": "Gifts Sent",
    "playerGiftsRecieved": "Gifts Recieved",
    "playerRanksGifted": "Ranks Gifted",
    "arcadeWins": "Arcade Wins",
    "bedwarsWins": "Bedwars Wins",
    "blitzWins": "Blitz Wins",
    "buildbattleWins": "Build Battle Wins",
    "classicWins": "Classic Games Wins",
    "vampirezWins": "VampireZ Wins",
    "quakeWins": "Quakecraft Wins",
    "paintballWins": "Paintball Warfare Wins",
    "arenaWins": "Arena Brawl Wins",
    "wallsWins": "The Walls Wins",
    "tkrWins": "Turbo Kart Racers Wins",
    "cvcWins": "Cops vs Crims Wins",
    "duelsWins": "Duels Wins",
    "megawallsWins": "Mega Walls Wins",
    "murderWins": "Murder Mystery Wins",
    "skywarsWins": "Skywars Wins",
    "smashWins": "Smash Heroes Wins",
    "speeduhcWins": "Speed UHC Wins",
    "pitPrestige": "The Pit Prestige",
    "tntWins": "TNT Games Wins",
    "uhcWins": "UHC Wins",
    "warlordsWins": "Warlords Wins",
    "woolwarsWins": "Wool Wars Wins"
}

stat_arcade = {
    "arcadeWins": "Arcade Wins",
    "arcadeCoins": "Arcade Coins",
    "hitwWins": "Hole in the Wall Wins",
    "soccerWins": "Football Wins",
    "bhWins": "Bounty Hunters Wins",
    "ppWins": "Pixel Painters Wins",
    "ctwWools": "Capture the Wool Wools",
    "dwWins": "Dragon Wars Wins",
    "esWins": "Ender Spleef Wins",
    "gwWins": "Galaxy Wars Wins",
    "toWins": "Throw Out Wins",
    "caWave": "Creeper Attack Waves",
    "fhWins": "Farm Hunt Wins",
    "pgWins": "Party Games Wins",
    "zombiesWins": "Zombies Wins",
    "hnspartypooperWins": "Hide n' Seek Party Pooper Wins",
    "hnsprophuntWins": "Hide n' Seek Prop Hunt Wins",
    "hsWins": "Hypixel Says Wins",
    "mwWins": "Mini Walls Wins",
    "bdWins": "Blocking Dead Wins",
    "easterWins": "Easter Simulator Wins",
    "scubaWins": "Scuba Simulator Wins",
    "grinchWins": "Grinch Simulator Wins",
    "halloweenWins": "Halloween Simulator Wins"
}

stat_bedwars = {
    "bedwarsWins": "Bedwars Wins",
    "bedwarsLevel": "Bedwars Level",
    "bedwarsKills": "Bedwars Kills",
    "bedwarsBedsBroken": "Beds Broken",
    "bedwarsFinals": "Bedwars Final Kills",
    "bedwarssoloWins": "Bedwars Solo Wins",
    "bedwars2sWins": "Bedwars Doubles Wins",
    "bedwars3sWins": "Bedwars Trios Wins",
    "bedwars4sWins": "Bedwars Fours Wins",
    "bedwars4v4Wins": "Bedwars 4v4 Wins"
}

stat_blitz = {
    "blitzWins": "Blitz Wins",
    "blitzKills": "Blitz Kills",
    "blitzStarUses": "Blitz Stars Used",
    "blitzMobs": "Blitz Mobs Spawned",
    "soloblitzWins": "Blitz Solo Wins",
    "blitzSoloKills": "Blitz Solo Kills",
    "teamsblitzWins": "Blitz Teams Wins",
    "blitzTeamsKills": "Blitz Teams Kills",
    "blitzRandomWins": "Blitz Random Kit Wins",
    "blitzTauntKills": "Blitz Taunt Kills",
    "blitzRamboWins": "Blitz Rambo Kit Wins"
}

stat_buildbattle = {
    "buildbattleWins": "Build Battle Wins",
    "buildbattleScore": "Build Battle Score",
    "buildbattleCoins": "Build Battle Coins",
    "buildbattlesoloWins": "Build Battle Solo Wins",
    "buildbattleteamsWins": "Build Battle Teams Wins",
    "buildbattleTotalvotes": "Build Battle Total Votes",
    "buildbattlegtbWins": "Guess the Build Wins",
    "buildbattleCorrectguesses": "Guess the Build Correct Guesses"
}

stat_duels = {
    "duelsWins": "Duels Wins",
    "duelsKills": "Duels Kills",
    "duelsBestWs": "Duels Best Winstreak",
    "duelsBowWins": "Bow Duel Wins",
    "duelsClassicWins": "Classic Duel Wins",
    "duelsOpWins": "OP Duel Wins",
    "duelsUhcWins": "UHC Duel Wins",
    "duelsNodebuffWins": "NoDebuff Duel Wins",
    "duelsMwWins": "Mega Walls Duel Wins",
    "duelsBlitzWins": "Blitz Duel Wins",
    "duelsSwWins": "Skywars Duel Wins",
    "duelsComboWins": "Combo Duel Wins",
    "duelsBsWins": "Bow Spleef Duel Wins",
    "duelsSumoWins": "Sumo Duel Wins",
    "duelsBoxingWins": "Boxing Duel Wins",
    "duelsBridgeWins": "Bridge Duel Wins",
    "duelsUhcdmWins": "UHC Deathmatch Duel Wins",
    "duelsParkourWins": "Parkour Duel Wins",
    "duelsArenaWins": "Arena Duel Wins"
}

stat_megawalls = {
    "megawallsWins": "Wins",
    "megawallsKills": "Kills",
    "megawallsAssists": "Assists",
    "megawallsFK": "Final Kills",
    "megawallsFA": "Final Assists",
    "megawallsDefensiveKills": "Defensive Kills",
    "megawallsWitherDamage": "Wither Damage",
    "megawallsCoins": "Coins",
    "megawallsMythicFavor": "Mythic Favor",
    "megawallsPrestiges": "Prestiges",
    "megawallsTreasures": "Chests Found",
    "megawallsCakes": "Cakes Found",
    "megawallsWinsStandard": "Wins Standard",
    "megawallsFaceOff": "Wins Face Off",
    "megawallscowWins": "Cow Wins",
    "megawallscowFK": "Cow Final Kills",
    "megawallshunterWins": "Hunter Wins",
    "megawallshunterFK": "Hunter Final Kills",
    "megawallssharkWins": "Shark Wins",
    "megawallssharkFK": "Shark Final Kills",
    "megawallsdreadlordWins": "Dreadlord Wins",
    "megawallsdreadlordFK": "Dreadlord Final Kills",
    "megawallshunterWins": "Hunter Wins",
    "megawallshunterFK": "Hunter Final Kills",
    "megawallsherobrineWins": "Herobrine Wins",
    "megawallsherobrineFK": "Herobrine Final Kills",
    "megawallspigmanWins": "Pigman Wins",
    "megawallspigmanFK": "Pigman Final Kills",
    "megawallszombieWins": "Zombie Wins",
    "megawallszombieFK": "Zombie Final Kills",
    "megawallsarcanistWins": "Arcanist Wins",
    "megawallsarcanistFK": "Arcanist Final Kills",
    "megawallsshamanWins": "Shaman Wins",
    "megawallsshamanFK": "Shaman Final Kills",
    "megawallssquidWins": "Squid Wins",
    "megawallssquidFK": "Squid Final Kills",
    "megawallsendermanWins": "Enderman Wins",
    "megawallsendermanFK": "Enderman Final Kills",
    "megawallsblazeWins": "Blaze Wins",
    "megawallsblazeFK": "Blaze Final Kills",
    "megawallsskeletonWins": "Skeleton Wins",
    "megawallsskeletonFK": "Skeleton Final Kills",
    "megawallsspiderWins": "Spider Wins",
    "megawallsspiderFK": "Spider Final Kills",
    "megawallspirateWins": "Pirate Wins",
    "megawallspirateFK": "Pirate Final Kills",
    "megawallscreeperWins": "Creeper Wins",
    "megawallscreeperFK": "Creeper Final Kills",
    "megawallsassassinWins": "Assassin Wins",
    "megawallsassassinFK": "Assassin Final Kills",
    "megawallswerewolfWins": "Werewolf Wins",
    "megawallswerewolfFK": "Werewolf Final Kills",
    "megawallsphoenixWins": "Phoenix Wins",
    "megawallsphoenixFK": "Phoenix Final Kills",
    "megawallsautomatonWins": "Automaton Wins",
    "megawallsautomatonFK": "Automaton Final Kills",
    "megawallsmolemanWins": "Moleman Wins",
    "megawallsmolemanFK": "Moleman Final Kills",
    "megawallsrenegadeWins": "Renegade Wins",
    "megawallsrenegadeFK": "Renegade Final Kills",
    "megawallssnowmanWins": "Snowman Wins",
    "megawallssnowmanFK": "Snowman Final Kills"
}

stat_murder = {
    "murderWins": "Wins",
    "murderKills": "Kills",
    "murderGamesPlayed": "Games Played",
    "murderCoins": "Coins",
    "murderGoldCaught": "Gold Collected",
    "murderMurderWins": "Wins as Murder",
    "murderMurderKills": "Kills as Murder",
    "murderDetectiveWins": "Wins as Detective",
    "murderHero": "Hero Wins",
    "murderKnifeKills": "Knife Kills",
    "murderBowKills": "Bow Kills",
    "murderTrapKills": "Trap Kills",
    "murderWinsClassic": "Wins Murder Classic",
    "murderKillsClassic": "Kills Murder Classic",
    "murderWinsDouble": "Wins Murder Double Up",
    "murderKillsDouble": "Kills Murder Double Up",
    "murderWinsAssassins": "Wins Assassins",
    "murderKillsAssassins": "Kills Assassins",
    "murderWinsShowdown": "Wins Showdown",
    "murderKillsShowdown": "Kills Showdown",
    "murderWinsInfections": "Wins Infections",
    "murderPlayersInfected": "Players Infected",
    "murderKillsAsSurvivor": "Kills as Survivor",
    "murderTimeSurvivedMinutes": "Infections Time Survived (Minutes)"
}

stat_skywars = {
    "skywarsWins": "Skywars Wins",
    "skywarsKills": "Skywars Kills",
    "starssw": "Skywars Stars",
    "skywarsHeads": "Skywars Heads",
    "swsoloWins": "Solo Skywars Wins",
    "swteamsWins": "Teams Skywars Wins",
    "swsolonormalWins": "Solo Normal Wins",
    "swsoloinsaneWins": "Solo Insane Wins",
    "swteamsnormalWins": "Teams Normal Wins",
    "swteamsinsaneWins": "Teams Insane Wins",
    "megaswWins": "Mega Skywars Wins",
    "megadoublesswWins": "Mega Doubles Wins",
    "rskywarsWins": "Ranked Skywars Wins",
    "labskywarsWins": "Skywars Laboratory Wins"
}

stat_such = {
    "speeduhcWins": "Speed UHC Wins",
    "speeduhcKills": "Speed UHC Kills",
    "speeduhcScore": "Speed UHC Score",
    "speeduhcCoins": "Speed UHC Coins",
    "speeduhcSalt": "Speed UHC Salt",
    "speeduhcTears": "Speed UHC Tears",
    "speeduhcSoloWins": "Solo Wins",
    "speeduhcSoloKills": "Solo Kills",
    "speeduhcTeamsWins": "Teams Wins",
    "speeduhcTeamsKills": "Teams Kills",
    "speeduhcAssists": "Speed UHC Assists",
    "speeduhcSurvivedPlayers": "Total Players Survived",
    "speeduhcKillstreak": "Best Killstreak",
    "speeduhcWinstreak": "Best Winstreak"
}

stat_tnt = {
    "tntWins": "TNT Games Wins",
    "tntrunWins": "TNT Run Wins",
    "pvprunWins": "PVP Run Wins",
    "pvprunKills": "PVP Run Kills",
    "bowspleefWins": "Bow Spleef Wins",
    "tnttagWins": "TNT Tag Wins",
    "wizardWins": "Wizards Wins",
    "wizardsKills": "Wizards Kills",
    "wizardsCaptures": "Wizards Points Captured"
}

stat_warlords = {
    "warlordsWins": "Warlords Wins",
    "warlordsKills": "Warlords Kills",
    "warlordsAssists": "Warlords Assists",
    "warlordsctfWins": "Capture the Flag Wins",
    "warlordsdomWins": "Domination Wins",
    "warlordstdmWins": "Team Deathmatch Wins"
}

stat_woolwars = {
    "woolwarsWins": "Wool Wars Wins",
    "woolwarsStars": "Wool Wars Stars",
    "woolwarsKills": "Wool Wars Kills",
    "woolwarsAssists": "Wool Wars Assists",
    "woolwarsBlocksPlaced": "Blocks Placed",
    "woolwarsBlocksBroken": "Blocks Broken",
    "woolwarsPowerups": "Total Powerups",
    "woolwarsWool": "Total Wool",
    "woolwarsGames": "Games Played"
}

def xp_to_star(woolwarsXP):
    stars = [0, 1000, 2000, 3000, 4000] + ([5000] * 95)
    xp_per_prestige, summed_star_xp = sum(stars), 0
    for star, star_xp in enumerate(stars):
        summed_star_xp += star_xp
        if woolwarsXP % xp_per_prestige < summed_star_xp:
            return round(float(f"{int(woolwarsXP // xp_per_prestige)}{str(star).zfill(2)}"))

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix = "$", intents = intents)

@tasks.loop(minutes = 10)
async def renew():
    global rankings, last_update_time, all_players_stats, embed_colour, rankings_arcade, all_players_arcade_stats, rankings_bedwars, all_players_bedwars_stats, rankings_blitz, all_players_blitz_stats, rankings_buildbattle, all_players_buildbattle_stats, rankings_duels, all_players_duels_stats, rankings_megawalls, all_players_megawalls_stats, rankings_murder, all_players_murder_stats, rankings_skywars, all_players_skywars_stats, rankings_such, all_players_such_stats, rankings_tnt, all_players_tnt_stats, rankings_warlords, all_players_warlords_stats, rankings_woolwars, all_players_woolwars_stats
    with open("UUID.txt") as f:
        uid_list = f.read().splitlines()

    all_players_stats = []
    all_players_arcade_stats = []
    all_players_bedwars_stats = []
    all_players_blitz_stats = []
    all_players_buildbattle_stats = []
    all_players_duels_stats = []
    all_players_megawalls_stats = []
    all_players_murder_stats = []
    all_players_skywars_stats = []
    all_players_such_stats = []
    all_players_tnt_stats = []
    all_players_warlords_stats = []
    all_players_woolwars_stats = []
    print('Coletando dados da API...')
    for x, uuid in enumerate(uid_list):
        playerInfo = requests.get(f"https://api.hypixel.net/player?key={api_key}&uuid={uuid}").json()["player"]
        # IGN
        playerName = playerInfo["displayname"]

        # Network Level
        try: exp = playerInfo["networkExp"]
        except KeyError: exp = 0
        playerLevel = round(1 + -3.5 + sqrt(12.25 + 0.0008 * exp), 2)

        # Achievement Points
        try: playerAp = playerInfo["achievementPoints"]
        except KeyError: playerAp = 0

        # Quests
        playerQuests = 0
        try:
            all_modes_quests = list(playerInfo["quests"].keys())
            for mode in all_modes_quests:
                try: mode_quests = len(playerInfo["quests"][mode]["completions"])
                except KeyError: continue
                playerQuests += mode_quests
        except KeyError:
            pass

        # Karma
        try: playerKarma = playerInfo["karma"]
        except KeyError: playerKarma = 0

        # Gifts Sent
        try: playerGiftsSent = playerInfo["giftingMeta"]["bundlesGiven"]
        except KeyError: playerGiftsSent = 0

        # Gifts Recieved
        try: playerGiftsRecieved = playerInfo["giftingMeta"]["bundlesReceived"]
        except KeyError: playerGiftsRecieved = 0

        # Ranks Given
        try: playerRanksGifted = playerInfo["giftingMeta"]["ranksGiven"]
        except KeyError: playerRanksGifted = 0

        # Arcade Games
        try: arcadeCoins = playerInfo["stats"]["Arcade"]["coins"]
        except KeyError: arcadeCoins = 0
        arcadeCoins = int(arcadeCoins)

        try: hitwWins = playerInfo["stats"]["Arcade"]["wins_hole_in_the_wall"]
        except KeyError: hitwWins = 0

        try: soccerWins = playerInfo["stats"]["Arcade"]["wins_soccer"]
        except KeyError: soccerWins = 0

        try: bhWins = playerInfo["stats"]["Arcade"]["wins_oneinthequiver"]
        except KeyError: bhWins = 0

        try: ppWins = playerInfo["stats"]["Arcade"]["wins_draw_their_thing"]
        except KeyError: ppWins = 0

        try: ctwWools = playerInfo["achievements"]["arcade_ctw_oh_sheep"]
        except KeyError: ctwWools = 0

        try: dwWins = playerInfo["stats"]["Arcade"]["wins_dragonwars2"]
        except KeyError: dwWins = 0

        try: esWins = playerInfo["stats"]["Arcade"]["wins_ender"]
        except KeyError: esWins = 0

        try: gwWins = playerInfo["stats"]["Arcade"]["sw_game_wins"]
        except KeyError: gwWins = 0

        try: toWins = playerInfo["stats"]["Arcade"]["wins_throw_out"]
        except KeyError: toWins = 0

        try: caWave = playerInfo["stats"]["Arcade"]["max_wave"]
        except KeyError: caWave = 0

        try: fhWins = playerInfo["stats"]["Arcade"]["wins_farm_hunt"]
        except KeyError: fhWins = 0

        try: pg3Wins = playerInfo["stats"]["Arcade"]["wins_party_3"]
        except KeyError: pg3Wins = 0

        try: pg1Wins = playerInfo["stats"]["Arcade"]["wins_party"]
        except KeyError: pg1Wins = 0

        pgWins = int(pg1Wins + pg3Wins)
        try: zombiesWins = playerInfo["stats"]["Arcade"]["wins_zombies"]
        except KeyError: zombiesWins = 0

        try: hnsseekerWins = playerInfo["stats"]["Arcade"]["party_pooper_seeker_wins_hide_and_seek"]
        except KeyError: hnsseekerWins = 0

        try: hnshiderWins = playerInfo["stats"]["Arcade"]["party_pooper_hider_wins_hide_and_seek"]
        except KeyError: hnshiderWins = 0

        hnspartypooperWins = int(hnsseekerWins + hnshiderWins)
        try: hns2seekerWins = playerInfo["stats"]["Arcade"]["prop_hunt_hider_wins_hide_and_seek"]
        except KeyError: hns2seekerWins = 0

        try: hns2hiderWins = playerInfo["stats"]["Arcade"]["prop_hunt_seeker_wins_hide_and_seek"]
        except KeyError: hns2hiderWins = 0

        hnsprophuntWins = int(hns2seekerWins + hns2hiderWins)
        try: hsWins = playerInfo["stats"]["Arcade"]["wins_simon_says"]
        except KeyError: hsWins = 0

        try: mwWins = playerInfo["stats"]["Arcade"]["wins_mini_walls"]
        except KeyError: mwWins = 0

        try: bdWins = playerInfo["stats"]["Arcade"]["wins_dayone"]
        except KeyError: bdWins = 0

        try: easterWins = playerInfo["stats"]["Arcade"]["wins_easter_simulator"]
        except KeyError: easterWins = 0

        try: scubaWins = playerInfo["stats"]["Arcade"]["wins_scuba_simulator"]
        except KeyError: scubaWins = 0

        try: grinchWins = playerInfo["stats"]["Arcade"]["wins_grinch_simulator_v2"]
        except KeyError: grinchWins = 0

        try: halloweenWins = playerInfo["stats"]["Arcade"]["wins_halloween_simulator"]
        except KeyError: halloweenWins = 0

        arcadeWins = int(hitwWins + soccerWins + bhWins + ppWins + ctwWools + dwWins + esWins + gwWins + toWins + caWave + fhWins + pgWins + zombiesWins + hnspartypooperWins + hnsprophuntWins + hsWins + mwWins + bdWins + easterWins + scubaWins + grinchWins + halloweenWins)

        # Bedwars
        try: bedwarsWins = playerInfo["stats"]["Bedwars"]["wins_bedwars"]
        except KeyError: bedwarsWins = 0

        try: bedwarsLevel = playerInfo["achievements"]["bedwars_level"]
        except KeyError: bedwarsLevel = 0

        try: bedwarsKills = playerInfo["stats"]["Bedwars"]["kills_bedwars"]
        except KeyError: bedwarsKills = 0

        try: bedwarsBedsBroken = playerInfo["stats"]["Bedwars"]["beds_broken_bedwars"]
        except KeyError: bedwarsBedsBroken = 0

        try: bedwarsFinals = playerInfo["stats"]["Bedwars"]["final_kills_bedwars"]
        except KeyError: bedwarsFinals = 0

        try: bedwarssoloWins = playerInfo["stats"]["Bedwars"]["eight_one_wins_bedwars"]
        except KeyError: bedwarssoloWins = 0

        try: bedwars2sWins = playerInfo["stats"]["Bedwars"]["eight_two_wins_bedwars"]
        except KeyError: bedwars2sWins = 0

        try: bedwars3sWins = playerInfo["stats"]["Bedwars"]["four_three_wins_bedwars"]
        except KeyError: bedwars3sWins = 0

        try: bedwars4sWins = playerInfo["stats"]["Bedwars"]["four_four_wins_bedwars"]
        except KeyError: bedwars4sWins = 0

        try: bedwars4v4Wins = playerInfo["stats"]["Bedwars"]["two_four_wins_bedwars"]
        except KeyError: bedwars4v4Wins = 0

        # Blitz
        try: soloblitzWins = playerInfo["stats"]["HungerGames"]["wins"]
        except KeyError: soloblitzWins = 0

        try: teamsblitzWins = playerInfo["stats"]["HungerGames"]["wins_teams"]
        except KeyError: teamsblitzWins = 0

        blitzWins = int(soloblitzWins + teamsblitzWins)

        try: blitzKills = playerInfo["stats"]["HungerGames"]["kills"]
        except KeyError: blitzKills = 0

        try: blitzMobs = playerInfo["stats"]["HungerGames"]["mobs_spawned"]
        except KeyError: blitzMobs = 0

        try: blitzRandomWins = playerInfo["stats"]["HungerGames"]["random_wins"]
        except KeyError: blitzRandomWins = 0

        try: blitzStarUses = playerInfo["stats"]["HungerGames"]["blitz_uses"]
        except KeyError: blitzStarUses = 0

        try: blitzTauntKills = playerInfo["stats"]["HungerGames"]["taunt_kills"]
        except KeyError: blitzTauntKills = 0

        try: blitzSoloKills = playerInfo["stats"]["HungerGames"]["kills_solo_normal"]
        except KeyError: blitzSoloKills = 0

        try: blitzTeamsKills = playerInfo["stats"]["HungerGames"]["kills_teams_normal"]
        except KeyError: blitzTeamsKills = 0

        try: blitzRamboWins = playerInfo["stats"]["HungerGames"]["rambo_wins"]
        except KeyError: blitzRamboWins = 0

        # Build Battle
        try: buildbattleWins = playerInfo["stats"]["BuildBattle"]["wins"]
        except KeyError: buildbattleWins = 0

        try: buildbattleScore = playerInfo["stats"]["BuildBattle"]["score"]
        except KeyError: buildbattleScore = 0

        try: buildbattleCoins = playerInfo["stats"]["BuildBattle"]["coins"]
        except KeyError: buildbattleCoins = 0

        try: buildbattlesoloWins = playerInfo["stats"]["BuildBattle"]["wins_solo_normal"]
        except KeyError: buildbattlesoloWins = 0

        try: buildbattleteamsWins = playerInfo["stats"]["BuildBattle"]["wins_teams_normal"]
        except KeyError: buildbattleteamsWins = 0

        try: buildbattleTotalvotes = playerInfo["stats"]["BuildBattle"]["total_votes"]
        except KeyError: buildbattleTotalvotes = 0

        try: buildbattlegtbWins = playerInfo["stats"]["BuildBattle"]["wins_guess_the_build"]
        except KeyError: buildbattlegtbWins = 0

        try: buildbattleCorrectguesses = playerInfo["stats"]["BuildBattle"]["correct_guesses"]
        except KeyError: buildbattleCorrectguesses = 0

        # Classic
        try: hvampirezWins = playerInfo["stats"]["VampireZ"]["human_wins"]
        except KeyError: hvampirezWins = 0

        try: vvampirezWins = playerInfo["stats"]["VampireZ"]["vampire_wins"]
        except KeyError: vvampirezWins = 0

        try: soloquakeWins = playerInfo["stats"]["Quake"]["wins"]
        except KeyError: soloquakeWins = 0

        try: teamsquakeWins = playerInfo["stats"]["Quake"]["wins_teams"]
        except KeyError: teamsquakeWins = 0

        try:paintballWins = playerInfo["stats"]["Paintball"]["wins"]
        except KeyError: paintballWins = 0

        try: arenaWins = playerInfo["stats"]["Arena"]["wins"]
        except KeyError: arenaWins = 0

        try: wallsWins = playerInfo["stats"]["Walls"]["wins"]
        except KeyError: wallsWins = 0

        try: tkrWins = playerInfo["stats"]["GingerBread"]["gold_trophy"]
        except KeyError: tkrWins = 0

        vampirezWins = int(hvampirezWins + vvampirezWins)

        quakeWins = int(soloquakeWins + teamsquakeWins)

        classicWins = int(vampirezWins + quakeWins + paintballWins + arenaWins + wallsWins + tkrWins)

        # Cops And Crims
        try: cvcdefWins = playerInfo["stats"]["MCGO"]["game_wins"]
        except KeyError: cvcdefWins = 0

        try: cvctdmWins = playerInfo["stats"]["MCGO"]["game_wins_deathmatch"]
        except KeyError: cvctdmWins = 0

        cvcWins = int(cvcdefWins + cvctdmWins)

        # Duels
        try: duelsWins = playerInfo["stats"]["Duels"]["wins"]
        except KeyError: duelsWins = 0

        try: duelsKills = playerInfo["stats"]["Duels"]["kills"]
        except KeyError: duelsKills = 0

        try: duelsBestWs = playerInfo["stats"]["Duels"]["best_overall_winstreak"]
        except KeyError: duelsBestWs = 0

        try: duelsBowWins = playerInfo["stats"]["Duels"]["bow_duel_wins"]
        except KeyError: duelsBowWins = 0

        try: duelsClassicWins = playerInfo["stats"]["Duels"]["classic_duel_wins"]
        except KeyError: duelsClassicWins = 0

        try: duelsOpSWins = playerInfo["stats"]["Duels"]["op_duel_wins"]
        except KeyError: duelsOpSWins = 0

        try: duelsOpDWins = playerInfo["stats"]["Duels"]["op_doubles_wins"]
        except KeyError: duelsOpDWins = 0

        duelsOpWins = int(duelsOpSWins + duelsOpDWins)

        try: duelsUhcSWins = playerInfo["stats"]["Duels"]["uhc_duel_wins"]
        except KeyError: duelsUhcSWins = 0

        try: duelsUhcDWins = playerInfo["stats"]["Duels"]["uhc_doubles_wins"]
        except KeyError: duelsUhcDWins = 0

        try: duelsUhcFwins = playerInfo["stats"]["Duels"]["uhc_four_wins"]
        except KeyError: duelsUhcFwins = 0

        duelsUhcWins = int(duelsUhcSWins + duelsUhcDWins + duelsUhcFwins)

        try: duelsNodebuffWins = playerInfo["stats"]["Duels"]["potion_duel_wins"]
        except KeyError: duelsNodebuffWins = 0

        try: duelsMwSWins = playerInfo["stats"]["Duels"]["mw_duel_wins"]
        except KeyError: duelsMwSWins = 0

        try: duelsMwDWins = playerInfo["stats"]["Duels"]["mw_doubles_wins"]
        except KeyError: duelsMwDWins = 0

        duelsMwWins = int(duelsMwSWins + duelsMwDWins)

        try: duelsBlitzWins = playerInfo["stats"]["Duels"]["blitz_duel_wins"]
        except KeyError: duelsBlitzWins = 0

        try: duelsSwSWins = playerInfo["stats"]["Duels"]["sw_duel_wins"]
        except KeyError: duelsSwWins = 0

        try: duelsSwDWins = playerInfo["stats"]["Duels"]["sw_doubles_wins"]
        except KeyError: duelsSwWins = 0

        duelsSwWins = int(duelsSwSWins + duelsSwDWins)

        try: duelsComboWins = playerInfo["stats"]["Duels"]["combo_duel_wins"]
        except KeyError: duelsComboWins = 0

        try: duelsBsWins = playerInfo["stats"]["Duels"]["bowspleef_duel_wins"]
        except KeyError: duelsBsWins = 0

        try: duelsSumoWins = playerInfo["stats"]["Duels"]["sumo_duel_wins"]
        except KeyError: duelsSumoWins = 0

        try: duelsBoxingWins = playerInfo["stats"]["Duels"]["boxing_duel_wins"]
        except KeyError: duelsBoxingWins = 0

        try: duelsBridgeSWins = playerInfo["stats"]["Duels"]["bridge_duel_wins"]
        except KeyError: duelsBridgeSWins = 0

        try: duelsBridgeDWins = playerInfo["stats"]["Duels"]["bridge_doubles_wins"]
        except KeyError: duelsBridgeDWins = 0

        try: duelsBridgeTWins = playerInfo["stats"]["Duels"]["bridge_threes_wins"]
        except KeyError: duelsBridgeTWins = 0

        try: duelsBridgeFWins = playerInfo["stats"]["Duels"]["bridge_four_wins"]
        except KeyError: duelsBridgeFWins = 0

        try: duelsBridge4DWins = playerInfo["stats"]["Duels"]["bridge_2v2v2v2_wins"]
        except KeyError: duelsBridge4DWins = 0

        try: duelsBridge4TWins = playerInfo["stats"]["Duels"]["bridge_3v3v3v3_wins"]
        except KeyError: duelsBridge4TWins = 0

        try: duelsBridgeCtfWins = playerInfo["stats"]["Duels"]["capture_threes_wins"]
        except KeyError: duelsBridgeCtfWins = 0

        duelsBridgeWins = int(duelsBridgeSWins + duelsBridgeDWins + duelsBridgeTWins + duelsBridgeFWins + duelsBridge4DWins + duelsBridge4TWins + duelsBridgeCtfWins)

        try: duelsUhcdmWins = playerInfo["stats"]["Duels"]["uhc_meetup_wins"]
        except KeyError: duelsUhcdmWins = 0

        try: duelsParkourWins = playerInfo["stats"]["Duels"]["parkour_eight_wins"]
        except KeyError: duelsParkourWins = 0

        try: duelsArenaWins = playerInfo["stats"]["Duels"]["duel_arena_wins"]
        except KeyError: duelsArenaWins = 0

        # Mega Walls
        try: megawallsWins = playerInfo["stats"]["Walls3"]["wins"]
        except KeyError: megawallsWins = 0

        try: megawallsKills = playerInfo["stats"]["Walls3"]["kills"]
        except KeyError: megawallsKills = 0

        try: megawallsAssists = playerInfo["stats"]["Walls3"]["assists"]
        except KeyError: megawallsAssists = 0

        try: megawallsFK = playerInfo["stats"]["Walls3"]["final_kills"]
        except KeyError: megawallsFK = 0

        try: megawallsFA = playerInfo["stats"]["Walls3"]["final_assists"]
        except KeyError: megawallsFA = 0

        try: megawallsDefensiveKills = playerInfo["stats"]["Walls3"]["walls3_guardian"]
        except KeyError: megawallsDefensiveKills = 0

        try: megawallsWitherDamage = playerInfo["achievements"]["walls3_rusher"]
        except KeyError: megawallsWitherDamage = 0

        try: megawallsWinsStandard = playerInfo["stats"]["Walls3"]["wins_standard"]
        except KeyError: megawallsWinsStandard = 0

        try: megawallsFaceOff = playerInfo["stats"]["Walls3"]["wins_face_off"]
        except KeyError: megawallsFaceOff = 0

        try: megawallsCoins = playerInfo["stats"]["Walls3"]["coins"]
        except KeyError: megawallsCoins = 0

        try: megawallsMythicFavor = playerInfo["stats"]["Walls3"]["mythic_favor"]
        except KeyError: megawallsMythicFavor = 0

        try: megawallsPrestiges = playerInfo["achievements"]["walls3_moctezuma"]
        except KeyError: megawallsPrestiges = 0

        try: megawallsTreasures = playerInfo["stats"]["Walls3"]["treasures_found"]
        except KeyError: megawallsTreasures = 0

        try: megawallsCakes = playerInfo["stats"]["Walls3"]["cakes_found"]
        except KeyError: megawallsCakes = 0

        try: megawallscowWins = playerInfo["stats"]["Walls3"]["cow_wins"]
        except KeyError: megawallscowWins = 0

        try: megawallscowFK = playerInfo["stats"]["Walls3"]["cow_final_kills"]
        except KeyError: megawallscowFK = 0

        try: megawallshunterWins = playerInfo["stats"]["Walls3"]["hunter_wins"]
        except KeyError: megawallshunterWins = 0

        try: megawallshunterFK = playerInfo["stats"]["Walls3"]["hunter_final_kills"]
        except KeyError: megawallshunterFK = 0

        try: megawallssharkWins = playerInfo["stats"]["Walls3"]["shark_wins"]
        except KeyError: megawallssharkWins = 0

        try: megawallssharkFK = playerInfo["stats"]["Walls3"]["shark_final_kills"]
        except KeyError: megawallssharkFK = 0

        try: megawallsdreadlordWins = playerInfo["stats"]["Walls3"]["dreadlord_wins"]
        except KeyError: megawallsdreadlordWins = 0

        try: megawallsdreadlordFK = playerInfo["stats"]["Walls3"]["dreadlord_final_kills"]
        except KeyError: megawallsdreadlordFK = 0

        try: megawallshunterWins = playerInfo["stats"]["Walls3"]["hunter_wins"]
        except KeyError: megawallshunterWins = 0

        try: megawallshunterFK = playerInfo["stats"]["Walls3"]["hunter_final_kills"]
        except KeyError: megawallshunterFK = 0

        try: megawallsherobrineWins = playerInfo["stats"]["Walls3"]["herobrine_wins"]
        except KeyError: megawallsherobrineWins = 0

        try: megawallsherobrineFK = playerInfo["stats"]["Walls3"]["herobrine_final_kills"]
        except KeyError: megawallsherobrineFK = 0

        try: megawallspigmanWins = playerInfo["stats"]["Walls3"]["pigman_wins"]
        except KeyError: megawallspigmanWins = 0

        try: megawallspigmanFK = playerInfo["stats"]["Walls3"]["pigman_final_kills"]
        except KeyError: megawallspigmanFK = 0

        try: megawallszombieWins = playerInfo["stats"]["Walls3"]["zombie_wins"]
        except KeyError: megawallszombieWins = 0

        try: megawallszombieFK = playerInfo["stats"]["Walls3"]["zombie_final_kills"]
        except KeyError: megawallszombieFK = 0

        try: megawallsarcanistWins = playerInfo["stats"]["Walls3"]["arcanist_wins"]
        except KeyError: megawallsarcanistWins = 0

        try: megawallsarcanistFK = playerInfo["stats"]["Walls3"]["arcanist_final_kills"]
        except KeyError: megawallsarcanistFK = 0

        try: megawallsshamanWins = playerInfo["stats"]["Walls3"]["shaman_wins"]
        except KeyError: megawallsshamanWins = 0

        try: megawallsshamanFK = playerInfo["stats"]["Walls3"]["shaman_final_kills"]
        except KeyError: megawallsshamanFK = 0

        try: megawallssquidWins = playerInfo["stats"]["Walls3"]["squid_wins"]
        except KeyError: megawallssquidWins = 0

        try: megawallssquidFK = playerInfo["stats"]["Walls3"]["squid_final_kills"]
        except KeyError: megawallssquidFK = 0

        try: megawallsendermanWins = playerInfo["stats"]["Walls3"]["enderman_wins"]
        except KeyError: megawallsendermanWins = 0

        try: megawallsendermanFK = playerInfo["stats"]["Walls3"]["enderman_final_kills"]
        except KeyError: megawallsendermanFK = 0

        try: megawallsblazeWins = playerInfo["stats"]["Walls3"]["blaze_wins"]
        except KeyError: megawallsblazeWins = 0

        try: megawallsblazeFK = playerInfo["stats"]["Walls3"]["blaze_final_kills"]
        except KeyError: megawallsblazeFK = 0

        try: megawallsskeletonWins = playerInfo["stats"]["Walls3"]["skeleton_wins"]
        except KeyError: megawallsskeletonWins = 0

        try: megawallsskeletonFK = playerInfo["stats"]["Walls3"]["skeleton_final_kills"]
        except KeyError: megawallsskeletonFK = 0

        try: megawallsspiderWins = playerInfo["stats"]["Walls3"]["spider_wins"]
        except KeyError: megawallsspiderWins = 0

        try: megawallsspiderFK = playerInfo["stats"]["Walls3"]["spider_final_kills"]
        except KeyError: megawallsspiderFK = 0

        try: megawallspirateWins = playerInfo["stats"]["Walls3"]["pirate_wins"]
        except KeyError: megawallspirateWins = 0

        try: megawallspirateFK = playerInfo["stats"]["Walls3"]["pirate_final_kills"]
        except KeyError: megawallspirateFK = 0

        try: megawallscreeperWins = playerInfo["stats"]["Walls3"]["creeper_wins"]
        except KeyError: megawallscreeperWins = 0

        try: megawallscreeperFK = playerInfo["stats"]["Walls3"]["creeper_final_kills"]
        except KeyError: megawallscreeperFK = 0

        try: megawallsassassinWins = playerInfo["stats"]["Walls3"]["assassin_wins"]
        except KeyError: megawallsassassinWins = 0

        try: megawallsassassinFK = playerInfo["stats"]["Walls3"]["assassin_final_kills"]
        except KeyError: megawallsassassinFK = 0

        try: megawallswerewolfWins = playerInfo["stats"]["Walls3"]["werewolf_wins"]
        except KeyError: megawallswerewolfWins = 0

        try: megawallswerewolfFK = playerInfo["stats"]["Walls3"]["werewolf_final_kills"]
        except KeyError: megawallswerewolfFK = 0

        try: megawallsphoenixWins = playerInfo["stats"]["Walls3"]["phoenix_wins"]
        except KeyError: megawallsphoenixWins = 0

        try: megawallsphoenixFK = playerInfo["stats"]["Walls3"]["phoenix_final_kills"]
        except KeyError: megawallsphoenixFK = 0

        try: megawallsautomatonWins = playerInfo["stats"]["Walls3"]["automaton_wins"]
        except KeyError: megawallsautomatonWins = 0

        try: megawallsautomatonFK = playerInfo["stats"]["Walls3"]["automaton_final_kills"]
        except KeyError: megawallsautomatonFK = 0

        try: megawallsmolemanWins = playerInfo["stats"]["Walls3"]["moleman_wins"]
        except KeyError: megawallsmolemanWins = 0

        try: megawallsmolemanFK = playerInfo["stats"]["Walls3"]["moleman_final_kills"]
        except KeyError: megawallsmolemanFK = 0

        try: megawallsrenegadeWins = playerInfo["stats"]["Walls3"]["renegade_wins"]
        except KeyError: megawallsrenegadeWins = 0

        try: megawallsrenegadeFK = playerInfo["stats"]["Walls3"]["renegade_final_kills"]
        except KeyError: megawallsrenegadeFK = 0

        try: megawallssnowmanWins = playerInfo["stats"]["Walls3"]["snowman_wins"]
        except KeyError: megawallssnowmanWins = 0

        try: megawallssnowmanFK = playerInfo["stats"]["Walls3"]["snowman_final_kills"]
        except KeyError: megawallssnowmanFK = 0

        # Murder
        try: murderWins = playerInfo["stats"]["MurderMystery"]["wins"]
        except KeyError: murderWins = 0

        try: murderKills = playerInfo["stats"]["MurderMystery"]["kills"]
        except KeyError: murderKills = 0

        try: murderGamesPlayed = playerInfo["stats"]["MurderMystery"]["games"]
        except KeyError: murderGamesPlayed = 0

        try: murderCoins = playerInfo["stats"]["MurderMystery"]["coins"]
        except KeyError: murderCoins = 0

        try: murderGoldCaught = playerInfo["achievements"]["murdermystery_hoarder"]
        except KeyError: murderGoldCaught = 0

        try: murderMurderWins = playerInfo["stats"]["MurderMystery"]["murderer_wins"]
        except KeyError: murderMurderWins = 0

        try: murderMurderKills = playerInfo["stats"]["MurderMystery"]["kills_as_murderer"]
        except KeyError: murderMurderKills = 0

        try: murderDetectiveWins = playerInfo["stats"]["MurderMystery"]["detective_wins"]
        except KeyError: murderDetectiveWins = 0

        try: murderHero = playerInfo["stats"]["MurderMystery"]["was_hero"]
        except KeyError: murderHero = 0

        try: murderKnifeKills = playerInfo["stats"]["MurderMystery"]["knife_kills"]
        except KeyError: murderKnifeKills = 0

        try: murderBowKills = playerInfo["stats"]["MurderMystery"]["bow_kills"]
        except KeyError: murderBowKills = 0

        try: murderTrapKills = playerInfo["stats"]["MurderMystery"]["trap_kills"]
        except KeyError: murderTrapKills = 0

        try: murderWinsClassic = playerInfo["stats"]["MurderMystery"]["wins_MURDER_CLASSIC"]
        except KeyError: murderWinsClassic = 0

        try: murderKillsClassic = playerInfo["stats"]["MurderMystery"]["kills_MURDER_CLASSIC"]
        except KeyError: murderKillsClassic = 0

        try: murderWinsDouble = playerInfo["stats"]["MurderMystery"]["wins_MURDER_DOUBLE_UP"]
        except KeyError: murderWinsDouble = 0

        try: murderKillsDouble = playerInfo["stats"]["MurderMystery"]["kills_MURDER_DOUBLE_UP"]
        except KeyError: murderKillsDouble = 0

        try: murderWinsAssassins = playerInfo["stats"]["MurderMystery"]["wins_MURDER_ASSASSINS"]
        except KeyError: murderWinsAssassins = 0

        try: murderKillsAssassins = playerInfo["achievements"]["murdermystery_hitman"]
        except KeyError: murderKillsAssassins = 0

        try: murderWinsShowdown = playerInfo["stats"]["MurderMystery"]["wins_MURDER_SHOWDOWN"]
        except KeyError: murderWinsShowdown = 0

        try: murderKillsShowdown = playerInfo["stats"]["MurderMystery"]["kills_MURDER_SHOWDOWN"]
        except KeyError: murderKillsShowdown = 0

        try: murderWinsInfections = playerInfo["stats"]["MurderMystery"]["wins_MURDER_INFECTION"]
        except KeyError: murderWinsInfections = 0

        try: murderPlayersInfected = playerInfo["stats"]["MurderMystery"]["kills_as_infected_MURDER_INFECTION"]
        except KeyError: murderPlayersInfected = 0

        try: murderKillsAsSurvivor = playerInfo["stats"]["MurderMystery"]["kills_as_survivor_MURDER_INFECTION"]
        except KeyError: murderKillsAsSurvivor = 0

        try: murderTimeSurvivedSeconds = playerInfo["stats"]["MurderMystery"]["total_time_survived_seconds"]
        except KeyError: murderTimeSurvivedSeconds = 0

        murderTimeSurvivedMinutes = round(murderTimeSurvivedSeconds / 60)

        # Skywars
        try: skywarsWins = playerInfo["stats"]["SkyWars"]["wins"]
        except KeyError: skywarsWins = 0

        try: skywarsKills = playerInfo["stats"]["SkyWars"]["kills"]
        except KeyError: skywarsKills = 0

        try: starsxp = playerInfo["stats"]["SkyWars"]["skywars_experience"]
        except KeyError: starsxp = 0

        xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
        if starsxp >= 15000:
            starssw = round(((starsxp - 15000) / 10000. + 12), 2)
        else:
            try:
                for i in range(len(xps)):
                    if starsxp < xps[i]:
                        starssw = 1 + i + float(starsxp - xps[i-1]) / (xps[i] - xps[i-1])
            except NameError:
                starssw = 0

        try: skywarsHeads = playerInfo["stats"]["SkyWars"]["heads"]
        except KeyError: skywarsHeads = 0

        try: swsoloWins = playerInfo["stats"]["SkyWars"]["wins_solo"]
        except KeyError: swsoloWins = 0

        try: swteamsWins = playerInfo["stats"]["SkyWars"]["wins_team"]
        except KeyError: swteamsWins = 0

        try: swsolonormalWins = playerInfo["stats"]["SkyWars"]["wins_solo_normal"]
        except KeyError: swsolonormalWins = 0

        try: swsoloinsaneWins = playerInfo["stats"]["SkyWars"]["wins_solo_insane"]
        except KeyError: swsoloinsaneWins = 0

        try: swteamsnormalWins = playerInfo["stats"]["SkyWars"]["wins_team_normal"]
        except KeyError: swteamsnormalWins = 0

        try: swteamsinsaneWins = playerInfo["stats"]["SkyWars"]["wins_team_insane"]
        except KeyError: swteamsinsaneWins = 0

        try: megaswWins = playerInfo["stats"]["SkyWars"]["wins_mega"]
        except KeyError: megaswWins = 0

        try: megadoublesswWins = playerInfo["stats"]["SkyWars"]["wins_mega_doubles"]
        except KeyError: megadoublesswWins = 0

        try: rskywarsWins = playerInfo["stats"]["SkyWars"]["wins_ranked_normal"]
        except KeyError: rskywarsWins = 0

        try: labskywarsWins = playerInfo["stats"]["SkyWars"]["wins_lab"]
        except KeyError: labskywarsWins = 0

        # Smash Heroes
        try: smashWins = playerInfo["stats"]["SuperSmash"]["wins"]
        except KeyError: smashWins = 0

        # Speed UHC
        try: speeduhcWins = playerInfo["stats"]["SpeedUHC"]["wins"]
        except KeyError: speeduhcWins = 0

        try: speeduhcKills = playerInfo["stats"]["SpeedUHC"]["kills"]
        except KeyError: speeduhcKills = 0

        try: speeduhcScore = playerInfo["stats"]["SpeedUHC"]["score"]
        except KeyError: speeduhcScore = 0

        try: speeduhcCoins = playerInfo["stats"]["SpeedUHC"]["coins"]
        except KeyError: speeduhcCoins = 0

        try: speeduhcSalt = playerInfo["stats"]["SpeedUHC"]["salt"]
        except KeyError: speeduhcSalt = 0

        try: speeduhcTears = playerInfo["stats"]["SpeedUHC"]["tears_gathered"]
        except KeyError: speeduhcTears = 0

        try: speeduhcSoloWins = playerInfo["stats"]["SpeedUHC"]["wins_solo"]
        except KeyError: speeduhcSoloWins = 0

        try: speeduhcSoloKills = playerInfo["stats"]["SpeedUHC"]["kills_solo"]
        except KeyError: speeduhcSoloKills = 0

        try: speeduhcTeamsWins = playerInfo["stats"]["SpeedUHC"]["wins_team"]
        except KeyError: speeduhcTeamsWins = 0

        try: speeduhcTeamsKills = playerInfo["stats"]["SpeedUHC"]["kills_team"]
        except KeyError: speeduhcTeamsKills = 0

        try: speeduhcAssists = playerInfo["stats"]["SpeedUHC"]["assists"]
        except KeyError: speeduhcAssists = 0

        try: speeduhcSurvivedPlayers = playerInfo["stats"]["SpeedUHC"]["survived_players"]
        except KeyError: speeduhcSurvivedPlayers = 0

        try: speeduhcKillstreak = playerInfo["stats"]["SpeedUHC"]["highestKillstreak"]
        except KeyError: speeduhcKillstreak = 0

        try: speeduhcWinstreak = playerInfo["stats"]["SpeedUHC"]["highestWinstreak"]
        except KeyError: speeduhcWinstreak = 0

        # The Pit
        try: pitPrestige = playerInfo["achievements"]["pit_prestiges"]
        except KeyError: pitPrestige = 0

        # TNT Games
        try: tntrunWins = playerInfo["stats"]["TNTGames"]["wins_tntrun"]
        except KeyError: tntrunWins = 0

        try: pvprunWins = playerInfo["stats"]["TNTGames"]["wins_pvprun"]
        except KeyError: pvprunWins = 0

        try: pvprunKills = playerInfo["stats"]["TNTGames"]["kills_pvprun"]
        except KeyError: pvprunKills = 0

        try: bowspleefWins = playerInfo["stats"]["TNTGames"]["wins_bowspleef"]
        except KeyError: bowspleefWins = 0

        try: tnttagWins = playerInfo["stats"]["TNTGames"]["wins_tntag"]
        except KeyError: tnttagWins = 0

        try: wizardsWins = playerInfo["stats"]["TNTGames"]["wins_capture"]
        except KeyError: wizardsWins = 0

        try: wizardsKills = playerInfo["stats"]["TNTGames"]["kills_capture"]
        except KeyError: wizardsKills = 0

        try: wizardsCaptures = playerInfo["stats"]["TNTGames"]["points_capture"]
        except KeyError: wizardsCaptures = 0

        tntWins = int(tntrunWins + pvprunWins + bowspleefWins + tnttagWins + wizardsWins)

        # UHC
        try: solouhcWins = playerInfo["stats"]["UHC"]["wins_solo"]
        except KeyError: solouhcWins = 0

        try: teamsuhcWins = playerInfo["stats"]["UHC"]["wins"]
        except KeyError: teamsuhcWins = 0

        try: duobrawluhcWins = playerInfo["stats"]["UHC"]["wins_duo_brawl"]
        except KeyError: duobrawluhcWins = 0

        uhcWins = int(solouhcWins + teamsuhcWins + duobrawluhcWins)

        # Warlords
        try: warlordsWins = playerInfo["stats"]["Battleground"]["wins"]
        except KeyError: warlordsWins = 0

        try: warlordsKills = playerInfo["stats"]["Battleground"]["kills"]
        except KeyError: warlordsKills = 0

        try: warlordsAssists = playerInfo["stats"]["Battleground"]["assists"]
        except KeyError: warlordsAssists = 0

        try: warlordsctfWins = playerInfo["stats"]["Battleground"]["wins_capturetheflag"]
        except KeyError: warlordsctfWins = 0

        try: warlordsdomWins = playerInfo["stats"]["Battleground"]["wins_domination"]
        except KeyError: warlordsdomWins = 0

        try: warlordstdmWins = playerInfo["stats"]["Battleground"]["wins_teamdeathmatch"]
        except KeyError: warlordstdmWins = 0

        # WoolWars
        try: woolwarsWins = playerInfo["stats"]["WoolGames"]["wool_wars"]["stats"]["wins"]
        except KeyError: woolwarsWins = 0

        try: woolwarsXP = playerInfo["stats"]["WoolGames"]["progression"]["experience"]
        except KeyError: woolwarsXP = 0

        woolwarsStars = xp_to_star(woolwarsXP)

        try: woolwarsKills = playerInfo["stats"]["WoolGames"]["wool_wars"]["stats"]["kills"]
        except KeyError: woolwarsKills = 0

        try: woolwarsAssists = playerInfo["stats"]["WoolGames"]["wool_wars"]["stats"]["assists"]
        except KeyError: woolwarsAssists = 0

        try: woolwarsBlocksPlaced = playerInfo["stats"]["WoolGames"]["wool_wars"]["stats"]["wool_placed"]
        except KeyError: woolwarsBlocksPlaced = 0

        try: woolwarsBlocksBroken = playerInfo["stats"]["WoolGames"]["wool_wars"]["stats"]["blocks_broken"]
        except KeyError: woolwarsBlocksBroken = 0

        try: woolwarsPowerups = playerInfo["stats"]["WoolGames"]["wool_wars"]["stats"]["powerups_gotten"]
        except KeyError: woolwarsPowerups = 0

        try: woolwarsWool = playerInfo["stats"]["WoolGames"]["coins"]
        except KeyError: woolwarsWool = 0

        try: woolwarsGames = playerInfo["stats"]["WoolGames"]["wool_wars"]["stats"]["games_played"]
        except KeyError: woolwarsGames = 0


        player_stats = {
            "playerName": playerName,
            "playerLevel": playerLevel,
            "playerAp": playerAp,
            "playerQuests": playerQuests,
            "playerKarma": playerKarma,
            "playerGiftsSent": playerGiftsSent,
            "playerGiftsRecieved": playerGiftsRecieved,
            "playerRanksGifted": playerRanksGifted,
            "arcadeWins": arcadeWins,
            "classicWins": classicWins,
            "bedwarsWins": bedwarsWins,
            "blitzWins": blitzWins,
            "buildbattleWins": buildbattleWins,
            "classicWins": classicWins,
            "vampirezWins": vampirezWins,
            "quakeWins": quakeWins,
            "paintballWins": paintballWins,
            "arenaWins": arenaWins,
            "wallsWins": wallsWins,
            "tkrWins": tkrWins,
            "cvcWins": cvcWins,
            "duelsWins": duelsWins,
            "megawallsWins": megawallsWins,
            "murderWins": murderWins,
            "skywarsWins": skywarsWins,
            "smashWins": smashWins,
            "speeduhcWins": speeduhcWins,
            "pitPrestige": pitPrestige,
            "tntWins": tntWins,
            "uhcWins": uhcWins,
            "warlordsWins": warlordsWins,
            "woolwarsWins": woolwarsWins
        }
        all_players_stats.append(player_stats)

        arcade_stats = {
            "playerName": playerName,
            "arcadeWins": arcadeWins,
            "arcadeCoins": arcadeCoins,
            "hitwWins": hitwWins,
            "soccerWins": soccerWins,
            "bhWins": bhWins,
            "ppWins": ppWins,
            "ctwWools": ctwWools,
            "dwWins": dwWins,
            "esWins": esWins,
            "gwWins": gwWins,
            "toWins": toWins,
            "caWave": caWave,
            "fhWins": fhWins,
            "pgWins": pgWins,
            "zombiesWins": zombiesWins,
            "hnspartypooperWins": hnspartypooperWins,
            "hnsprophuntWins": hnsprophuntWins,
            "hsWins": hsWins,
            "mwWins": mwWins,
            "bdWins": bdWins,
            "easterWins": easterWins,
            "scubaWins": scubaWins,
            "grinchWins": grinchWins,
            "halloweenWins": halloweenWins
        }
        all_players_arcade_stats.append(arcade_stats)

        bedwars_stats = {
            "playerName": playerName,
            "bedwarsWins": bedwarsWins,
            "bedwarsLevel": bedwarsLevel,
            "bedwarsLevel": bedwarsLevel,
            "bedwarsBedsBroken": bedwarsBedsBroken,
            "bedwarsFinals": bedwarsFinals,
            "bedwarssoloWins": bedwarssoloWins,
            "bedwars2sWins": bedwars2sWins,
            "bedwars3sWins": bedwars3sWins,
            "bedwars4sWins": bedwars4sWins,
            "bedwars4v4Wins": bedwars4v4Wins
        }
        all_players_bedwars_stats.append(bedwars_stats)

        blitz_stats = {
            "playerName": playerName,
            "blitzWins": blitzWins,
            "blitzKills": blitzKills,
            "blitzStarUses": blitzStarUses,
            "blitzMobs": blitzMobs,
            "soloblitzWins": soloblitzWins,
            "blitzSoloKills": blitzSoloKills,
            "teamsblitzWins": teamsblitzWins,
            "blitzTeamsKills": blitzTeamsKills,
            "blitzRandomWins": blitzRandomWins,
            "blitzTauntKills": blitzTauntKills,
            "blitzRamboWins": blitzRamboWins
        }
        all_players_blitz_stats.append(blitz_stats)

        buildbattle_stats = {
            "playerName": playerName,
            "buildbattleWins": buildbattleWins,
            "buildbattleScore": buildbattleScore,
            "buildbattleCoins": buildbattleCoins,
            "buildbattlesoloWins": buildbattlesoloWins,
            "buildbattleteamsWins": buildbattleteamsWins,
            "buildbattleTotalvotes": buildbattleTotalvotes,
            "buildbattlegtbWins": buildbattlegtbWins,
            "buildbattleCorrectguesses": buildbattleCorrectguesses
        }
        all_players_buildbattle_stats.append(buildbattle_stats)

        duels_stats = {
            "playerName": playerName,
            "duelsWins": duelsWins,
            "duelsKills": duelsKills,
            "duelsBestWs": duelsBestWs,
            "duelsBowWins": duelsBowWins,
            "duelsClassicWins": duelsClassicWins,
            "duelsOpWins": duelsOpWins,
            "duelsUhcWins": duelsUhcWins,
            "duelsNodebuffWins": duelsNodebuffWins,
            "duelsMwWins": duelsMwWins,
            "duelsBlitzWins": duelsBlitzWins,
            "duelsSwWins": duelsSwWins,
            "duelsComboWins": duelsComboWins,
            "duelsBsWins": duelsBsWins,
            "duelsSumoWins": duelsSumoWins,
            "duelsBoxingWins": duelsBoxingWins,
            "duelsBridgeWins": duelsBridgeWins,
            "duelsUhcdmWins": duelsUhcdmWins,
            "duelsParkourWins": duelsParkourWins,
            "duelsArenaWins": duelsArenaWins
        }
        all_players_duels_stats.append(duels_stats)

        megawalls_stats = {
            "playerName": playerName,
            "megawallsWins": megawallsWins,
            "megawallsKills": megawallsKills,
            "megawallsAssists": megawallsAssists,
            "megawallsFK": megawallsFK,
            "megawallsFA": megawallsFA,
            "megawallsDefensiveKills": megawallsDefensiveKills,
            "megawallsWitherDamage": megawallsWitherDamage,
            "megawallsCoins": megawallsCoins,
            "megawallsMythicFavor": megawallsMythicFavor,
            "megawallsPrestiges": megawallsPrestiges,
            "megawallsTreasures": megawallsTreasures,
            "megawallsCakes": megawallsCakes,
            "megawallsWinsStandard": megawallsWinsStandard,
            "megawallsFaceOff": megawallsFaceOff,
            "megawallscowWins": megawallscowWins,
            "megawallscowFK": megawallscowFK,
            "megawallshunterWins": megawallshunterWins,
            "megawallshunterFK": megawallshunterFK,
            "megawallssharkWins": megawallssharkWins,
            "megawallssharkFK": megawallssharkFK,
            "megawallsdreadlordWins": megawallsdreadlordWins,
            "megawallsdreadlordFK": megawallsdreadlordFK,
            "megawallshunterWins": megawallshunterWins,
            "megawallshunterFK": megawallshunterFK,
            "megawallsherobrineWins": megawallsherobrineWins,
            "megawallsherobrineFK": megawallsherobrineFK,
            "megawallspigmanWins": megawallspigmanWins,
            "megawallspigmanFK": megawallspigmanFK,
            "megawallszombieWins": megawallszombieWins,
            "megawallszombieFK": megawallszombieFK,
            "megawallsarcanistWins": megawallsarcanistWins,
            "megawallsarcanistFK": megawallsarcanistFK,
            "megawallsshamanWins": megawallsshamanWins,
            "megawallsshamanFK": megawallsshamanFK,
            "megawallssquidWins": megawallssquidWins,
            "megawallssquidFK": megawallssquidFK,
            "megawallsendermanWins": megawallsendermanWins,
            "megawallsendermanFK": megawallsendermanFK,
            "megawallsblazeWins": megawallsblazeWins,
            "megawallsblazeFK": megawallsblazeFK,
            "megawallsskeletonWins": megawallsskeletonWins,
            "megawallsskeletonFK": megawallsskeletonFK,
            "megawallsspiderWins": megawallsspiderWins,
            "megawallsspiderFK": megawallsspiderFK,
            "megawallspirateWins": megawallspirateWins,
            "megawallspirateFK": megawallspirateFK,
            "megawallscreeperWins": megawallscreeperWins,
            "megawallscreeperFK": megawallscreeperFK,
            "megawallsassassinWins": megawallsassassinWins,
            "megawallsassassinFK": megawallsassassinFK,
            "megawallswerewolfWins": megawallswerewolfWins,
            "megawallswerewolfFK": megawallswerewolfFK,
            "megawallsphoenixWins": megawallsphoenixWins,
            "megawallsphoenixFK": megawallsphoenixFK,
            "megawallsautomatonWins": megawallsautomatonWins,
            "megawallsautomatonFK": megawallsautomatonFK,
            "megawallsmolemanWins": megawallsmolemanWins,
            "megawallsmolemanFK": megawallsmolemanFK,
            "megawallsrenegadeWins": megawallsrenegadeWins,
            "megawallsrenegadeFK": megawallsrenegadeFK,
            "megawallssnowmanWins": megawallssnowmanWins,
            "megawallssnowmanFK": megawallssnowmanFK
        }
        all_players_megawalls_stats.append(megawalls_stats)

        murder_stats = {
            "playerName": playerName,
            "murderWins": murderWins,
            "murderKills": murderKills,
            "murderGamesPlayed": murderGamesPlayed,
            "murderCoins": murderCoins,
            "murderGoldCaught": murderGoldCaught,
            "murderMurderWins": murderMurderWins,
            "murderMurderKills": murderMurderKills,
            "murderDetectiveWins": murderDetectiveWins,
            "murderHero": murderHero,
            "murderKnifeKills": murderKnifeKills,
            "murderBowKills": murderBowKills,
            "murderTrapKills": murderTrapKills,
            "murderWinsClassic": murderWinsClassic,
            "murderKillsClassic": murderKillsClassic,
            "murderWinsDouble": murderWinsDouble,
            "murderKillsDouble": murderKillsDouble,
            "murderWinsAssassins": murderWinsAssassins,
            "murderKillsAssassins": murderKillsAssassins,
            "murderWinsShowdown": murderWinsShowdown,
            "murderKillsShowdown": murderKillsShowdown,
            "murderWinsInfections": murderWinsInfections,
            "murderPlayersInfected": murderPlayersInfected,
            "murderKillsAsSurvivor": murderKillsAsSurvivor,
            "murderTimeSurvivedMinutes": murderTimeSurvivedMinutes
        }
        all_players_murder_stats.append(murder_stats)



        skywars_stats = {
            "playerName": playerName,
            "skywarsWins": skywarsWins,
            "skywarsKills": skywarsKills,
            "starssw": starssw,
            "skywarsWins": skywarsWins,
            "skywarsKills": skywarsKills,
            "starssw": starssw,
            "skywarsHeads": skywarsHeads,
            "swsoloWins": swsoloWins,
            "swteamsWins": swteamsWins,
            "swsolonormalWins": swsolonormalWins,
            "swsoloinsaneWins": swsoloinsaneWins,
            "swteamsnormalWins": swteamsnormalWins,
            "swteamsinsaneWins": swteamsinsaneWins,
            "megaswWins": megaswWins,
            "megadoublesswWins": megadoublesswWins,
            "rskywarsWins": rskywarsWins,
            "labskywarsWins": labskywarsWins
        }
        all_players_skywars_stats.append(skywars_stats)

        such_stats = {
            "playerName": playerName,
            "speeduhcWins": speeduhcWins,
            "speeduhcKills": speeduhcKills,
            "speeduhcScore": speeduhcScore,
            "speeduhcCoins": speeduhcCoins,
            "speeduhcSalt": speeduhcSalt,
            "speeduhcTears": speeduhcTears,
            "speeduhcSoloWins": speeduhcSoloWins,
            "speeduhcSoloKills": speeduhcSoloKills,
            "speeduhcTeamsWins": speeduhcTeamsWins,
            "speeduhcTeamsKills": speeduhcTeamsKills,
            "speeduhcAssists": speeduhcAssists,
            "speeduhcSurvivedPlayers": speeduhcSurvivedPlayers,
            "speeduhcKillstreak": speeduhcKillstreak,
            "speeduhcWinstreak": speeduhcWinstreak
        }
        all_players_such_stats.append(such_stats)

        tnt_stats = {
            "playerName": playerName,
            "tntWins": tntWins,
            "tntrunWins": tntrunWins,
            "pvprunWins": pvprunWins,
            "pvprunKills": pvprunKills,
            "bowspleefWins": bowspleefWins,
            "tnttagWins": tnttagWins,
            "wizardWins": wizardsWins,
            "wizardsKills": wizardsKills,
            "wizardsCaptures": wizardsCaptures
        }
        all_players_tnt_stats.append(tnt_stats)

        warlords_stats = {
            "playerName": playerName,
            "warlordsWins": warlordsWins,
            "warlordsKills": warlordsKills,
            "warlordsAssists": warlordsAssists,
            "warlordsctfWins": warlordsctfWins,
            "warlordsdomWins": warlordsdomWins,
            "warlordstdmWins": warlordstdmWins
        }
        all_players_warlords_stats.append(warlords_stats)

        woolwars_stats = {
            "playerName": playerName,
            "woolwarsWins": woolwarsWins,
            "woolwarsStars": woolwarsStars,
            "woolwarsKills": woolwarsKills,
            "woolwarsAssists": woolwarsAssists,
            "woolwarsBlocksPlaced": woolwarsBlocksPlaced,
            "woolwarsBlocksBroken": woolwarsBlocksBroken,
            "woolwarsPowerups": woolwarsPowerups,
            "woolwarsWool": woolwarsWool,
            "woolwarsGames": woolwarsGames
        }
        all_players_woolwars_stats.append(woolwars_stats)


        print(f'[{x+1}/{len(uid_list)}] Fetching data: {playerName}')
        await asyncio.sleep(1)


    embed_colour = discord.Colour.random()

    now = datetime.datetime.now()
    last_update_time = now.strftime("%d/%m/%Y %H:%M:%S")

    print('Formando os rankings...')

    rankings = {}
    for stat in player_stats:
        if stat != "playerName":
            sorting = sorted(all_players_stats, key = lambda d: d[stat], reverse = True)
            ranking = [{"playerName": el["playerName"], stat: el[stat]} for el in sorting[0:10]]
            rankings[f"{stat}Ranking"] = ranking

    rankings_arcade = {}
    for stat in arcade_stats:
        if stat != "playerName":
            sorting = sorted(all_players_arcade_stats, key = lambda d: d[stat], reverse = True)
            ranking_arcade = [{"playerName": el["playerName"], stat: el[stat]} for el in sorting[0:10]]
            rankings_arcade[f"{stat}Ranking"] = ranking_arcade

    rankings_bedwars = {}
    for stat in bedwars_stats:
        if stat != "playerName":
            sorting = sorted(all_players_bedwars_stats, key = lambda d: d[stat], reverse = True)
            ranking_bedwars = [{"playerName": el["playerName"], stat: el[stat]} for el in sorting[0:10]]
            rankings_bedwars[f"{stat}Ranking"] = ranking_bedwars

    rankings_blitz = {}
    for stat in blitz_stats:
        if stat != "playerName":
            sorting = sorted(all_players_blitz_stats, key = lambda d: d[stat], reverse = True)
            ranking_blitz = [{"playerName": el["playerName"], stat: el[stat]} for el in sorting[0:10]]
            rankings_blitz[f"{stat}Ranking"] = ranking_blitz

    rankings_buildbattle = {}
    for stat in buildbattle_stats:
        if stat != "playerName":
            sorting = sorted(all_players_buildbattle_stats, key = lambda d: d[stat], reverse = True)
            ranking_buildbattle = [{"playerName": el["playerName"], stat: el[stat]} for el in sorting[0:10]]
            rankings_buildbattle[f"{stat}Ranking"] = ranking_buildbattle

    rankings_duels = {}
    for stat in duels_stats:
        if stat != "playerName":
            sorting = sorted(all_players_duels_stats, key = lambda d: d[stat], reverse = True)
            ranking_duels = [{"playerName": el["playerName"], stat: el[stat]} for el in sorting[0:10]]
            rankings_duels[f"{stat}Ranking"] = ranking_duels

    rankings_megawalls = {}
    for stat in megawalls_stats:
        if stat != "playerName":
            sorting = sorted(all_players_megawalls_stats, key = lambda d: d[stat], reverse = True)
            ranking_megawalls = [{"playerName": el["playerName"], stat: el[stat]} for el in sorting[0:10]]
            rankings_megawalls[f"{stat}Ranking"] = ranking_megawalls

    rankings_murder = {}
    for stat in murder_stats:
        if stat != "playerName":
            sorting = sorted(all_players_murder_stats, key = lambda d: d[stat], reverse = True)
            ranking_murder = [{"playerName": el["playerName"], stat: el[stat]} for el in sorting[0:10]]
            rankings_murder[f"{stat}Ranking"] = ranking_murder

    rankings_skywars = {}
    for stat in skywars_stats:
        if stat != "playerName":
            sorting = sorted(all_players_skywars_stats, key = lambda d: d[stat], reverse = True)
            ranking_skywars = [{"playerName": el["playerName"], stat: el[stat]} for el in sorting[0:10]]
            rankings_skywars[f"{stat}Ranking"] = ranking_skywars

    rankings_such = {}
    for stat in such_stats:
        if stat != "playerName":
            sorting = sorted(all_players_such_stats, key = lambda d: d[stat], reverse = True)
            ranking_such = [{"playerName": el["playerName"], stat: el[stat]} for el in sorting[0:10]]
            rankings_such[f"{stat}Ranking"] = ranking_such

    rankings_tnt = {}
    for stat in tnt_stats:
        if stat != "playerName":
            sorting = sorted(all_players_tnt_stats, key = lambda d: d[stat], reverse = True)
            ranking_tnt = [{"playerName": el["playerName"], stat: el[stat]} for el in sorting[0:10]]
            rankings_tnt[f"{stat}Ranking"] = ranking_tnt

    rankings_warlords = {}
    for stat in warlords_stats:
        if stat != "playerName":
            sorting = sorted(all_players_warlords_stats, key = lambda d: d[stat], reverse = True)
            ranking_warlords = [{"playerName": el["playerName"], stat: el[stat]} for el in sorting[0:10]]
            rankings_warlords[f"{stat}Ranking"] = ranking_warlords

    rankings_woolwars = {}
    for stat in woolwars_stats:
        if stat != "playerName":
            sorting = sorted(all_players_woolwars_stats, key = lambda d: d[stat], reverse = True)
            ranking_woolwars = [{"playerName": el["playerName"], stat: el[stat]} for el in sorting[0:10]]
            rankings_woolwars[f"{stat}Ranking"] = ranking_woolwars

    print('Rankings atualizados com sucesso!')
    print(f'Ultima atualização: {last_update_time}')

@bot.event
async def on_ready():
    print('Iniciado')
    renew.start()

@bot.command()
async def players(ctx):
    players_embed = discord.Embed(title = "Players included in the ranking", color = embed_colour)
    for ten_players in list(zip_longest(all_players_stats[::10], all_players_stats[1::10], all_players_stats[2::10], all_players_stats[3::10], all_players_stats[4::10], all_players_stats[5::10], all_players_stats[6::10], all_players_stats[7::10], all_players_stats[8::10], all_players_stats[9::10])):
        players_embed.add_field(name = "\u200b", value = '\n'.join([f'``{player["playerName"]}``' for player in ten_players if player is not None]), inline = True)
    players_embed.set_footer(text = f"Players amount: {len(all_players_stats)}")
    await ctx.reply(f"Last update: {last_update_time}", embed = players_embed, mention_author = False)

@bot.command()
async def lb(ctx, mode = None):
    if mode:
        if mode == 'arcade':
            keys_arcade = list(rankings_arcade.keys())
            for fifteen_ranks_arcade in list(zip_longest(keys_arcade[::21], keys_arcade[1::21], keys_arcade[2::21], keys_arcade[3::21], keys_arcade[4::21], keys_arcade[5::21], keys_arcade[6::21], keys_arcade[7::21], keys_arcade[8::21], keys_arcade[9::21], keys_arcade[10::21], keys_arcade[11::21], keys_arcade[12::21], keys_arcade[13::21], keys_arcade[14::21], keys_arcade[15::21], keys_arcade[16::21], keys_arcade[17::21], keys_arcade[18::21], keys_arcade[19::21], keys_arcade[20::21])):
                embed = discord.Embed(title = "Hypixel Arcade Leaderboard PT/BR", description = f"Last update: {last_update_time}", color = embed_colour, timestamp = datetime.datetime.utcnow())
                for rank in fifteen_ranks_arcade:
                    if rank is not None:
                        embed.add_field(name = stat_arcade[rank.removesuffix("Ranking")], value = '\n'.join([f'{x+1}. **{player["playerName"]}:** {player[rank.removesuffix("Ranking")]}' for x, player in enumerate(rankings_arcade[rank])]), inline = True)
                await ctx.send(embed = embed)
                await asyncio.sleep(1)
        elif mode == 'bedwars':
            keys_bedwars = list(rankings_bedwars.keys())
            for fifteen_ranks_bedwars in list(zip_longest(keys_bedwars[::21], keys_bedwars[1::21], keys_bedwars[2::21], keys_bedwars[3::21], keys_bedwars[4::21], keys_bedwars[5::21], keys_bedwars[6::21], keys_bedwars[7::21], keys_bedwars[8::21], keys_bedwars[9::21], keys_bedwars[10::21], keys_bedwars[11::21], keys_bedwars[12::21], keys_bedwars[13::21], keys_bedwars[14::21], keys_bedwars[15::21], keys_bedwars[16::21], keys_bedwars[17::21], keys_bedwars[18::21], keys_bedwars[19::21], keys_bedwars[20::21])):
                embed = discord.Embed(title = "Hypixel Bedwars Leaderboard PT/BR", description = f"Last update: {last_update_time}", color = embed_colour, timestamp = datetime.datetime.utcnow())
                for rank in fifteen_ranks_bedwars:
                    if rank is not None:
                        embed.add_field(name = stat_bedwars[rank.removesuffix("Ranking")], value = '\n'.join([f'{x+1}. **{player["playerName"]}:** {player[rank.removesuffix("Ranking")]}' for x, player in enumerate(rankings_bedwars[rank])]), inline = True)
                await ctx.send(embed = embed)
                await asyncio.sleep(1)
        elif mode == 'blitz':
            keys_blitz = list(rankings_blitz.keys())
            for fifteen_ranks_blitz in list(zip_longest(keys_blitz[::21], keys_blitz[1::21], keys_blitz[2::21], keys_blitz[3::21], keys_blitz[4::21], keys_blitz[5::21], keys_blitz[6::21], keys_blitz[7::21], keys_blitz[8::21], keys_blitz[9::21], keys_blitz[10::21], keys_blitz[11::21], keys_blitz[12::21], keys_blitz[13::21], keys_blitz[14::21], keys_blitz[15::21], keys_blitz[16::21], keys_blitz[17::21], keys_blitz[18::21], keys_blitz[19::21], keys_blitz[20::21])):
                embed = discord.Embed(title = "Hypixel Blitz Leaderboard PT/BR", description = f"Last update: {last_update_time}", color = embed_colour, timestamp = datetime.datetime.utcnow())
                for rank in fifteen_ranks_blitz:
                    if rank is not None:
                        embed.add_field(name = stat_blitz[rank.removesuffix("Ranking")], value = '\n'.join([f'{x+1}. **{player["playerName"]}:** {player[rank.removesuffix("Ranking")]}' for x, player in enumerate(rankings_blitz[rank])]), inline = True)
                await ctx.send(embed = embed)
                await asyncio.sleep(1)
        elif mode == 'buildbattle':
            keys_buildbattle = list(rankings_buildbattle.keys())
            for fifteen_ranks_buildbattle in list(zip_longest(keys_buildbattle[::21], keys_buildbattle[1::21], keys_buildbattle[2::21], keys_buildbattle[3::21], keys_buildbattle[4::21], keys_buildbattle[5::21], keys_buildbattle[6::21], keys_buildbattle[7::21], keys_buildbattle[8::21], keys_buildbattle[9::21], keys_buildbattle[10::21], keys_buildbattle[11::21], keys_buildbattle[12::21], keys_buildbattle[13::21], keys_buildbattle[14::21], keys_buildbattle[15::21], keys_buildbattle[16::21], keys_buildbattle[17::21], keys_buildbattle[18::21], keys_buildbattle[19::21], keys_buildbattle[20::21])):
                embed = discord.Embed(title = "Hypixel Build Battle Leaderboard PT/BR", description = f"Last update: {last_update_time}", color = embed_colour, timestamp = datetime.datetime.utcnow())
                for rank in fifteen_ranks_buildbattle:
                    if rank is not None:
                        embed.add_field(name = stat_buildbattle[rank.removesuffix("Ranking")], value = '\n'.join([f'{x+1}. **{player["playerName"]}:** {player[rank.removesuffix("Ranking")]}' for x, player in enumerate(rankings_buildbattle[rank])]), inline = True)
                await ctx.send(embed = embed)
                await asyncio.sleep(1)
        elif mode == 'duels':
            keys_duels = list(rankings_duels.keys())
            for fifteen_ranks_duels in list(zip_longest(keys_duels[::21], keys_duels[1::21], keys_duels[2::21], keys_duels[3::21], keys_duels[4::21], keys_duels[5::21], keys_duels[6::21], keys_duels[7::21], keys_duels[8::21], keys_duels[9::21], keys_duels[10::21], keys_duels[11::21], keys_duels[12::21], keys_duels[13::21], keys_duels[14::21], keys_duels[15::21], keys_duels[16::21], keys_duels[17::21], keys_duels[18::21], keys_duels[19::21], keys_duels[20::21])):
                embed = discord.Embed(title = "Hypixel Duels Leaderboard PT/BR", description = f"Last update: {last_update_time}", color = embed_colour, timestamp = datetime.datetime.utcnow())
                for rank in fifteen_ranks_duels:
                    if rank is not None:
                        embed.add_field(name = stat_duels[rank.removesuffix("Ranking")], value = '\n'.join([f'{x+1}. **{player["playerName"]}:** {player[rank.removesuffix("Ranking")]}' for x, player in enumerate(rankings_duels[rank])]), inline = True)
                await ctx.send(embed = embed)
                await asyncio.sleep(1)
        elif mode == 'megawalls':
            keys_megawalls = list(rankings_megawalls.keys())
            for fifteen_ranks_megawalls in list(zip_longest(keys_megawalls[::21], keys_megawalls[1::21], keys_megawalls[2::21], keys_megawalls[3::21], keys_megawalls[4::21], keys_megawalls[5::21], keys_megawalls[6::21], keys_megawalls[7::21], keys_megawalls[8::21], keys_megawalls[9::21], keys_megawalls[10::21], keys_megawalls[11::21], keys_megawalls[12::21], keys_megawalls[13::21], keys_megawalls[14::21], keys_megawalls[15::21], keys_megawalls[16::21], keys_megawalls[17::21], keys_megawalls[18::21], keys_megawalls[19::21], keys_megawalls[20::21])):
                embed = discord.Embed(title = "Hypixel Mega Walls Leaderboard PT/BR", description = f"Last update: {last_update_time}", color = embed_colour, timestamp = datetime.datetime.utcnow())
                for rank in fifteen_ranks_megawalls:
                    if rank is not None:
                        embed.add_field(name = stat_megawalls[rank.removesuffix("Ranking")], value = '\n'.join([f'{x+1}. **{player["playerName"]}:** {player[rank.removesuffix("Ranking")]}' for x, player in enumerate(rankings_megawalls[rank])]), inline = True)
                await ctx.send(embed = embed)
                await asyncio.sleep(1)
        elif mode == 'murder':
            keys_murder = list(rankings_murder.keys())
            for fifteen_ranks_murder in list(zip_longest(keys_murder[::21], keys_murder[1::21], keys_murder[2::21], keys_murder[3::21], keys_murder[4::21], keys_murder[5::21], keys_murder[6::21], keys_murder[7::21], keys_murder[8::21], keys_murder[9::21], keys_murder[10::21], keys_murder[11::21], keys_murder[12::21], keys_murder[13::21], keys_murder[14::21], keys_murder[15::21], keys_murder[16::21], keys_murder[17::21], keys_murder[18::21], keys_murder[19::21], keys_murder[20::21])):
                embed = discord.Embed(title = "Hypixel Murder Leaderboard PT/BR", description = f"Last update: {last_update_time}", color = embed_colour, timestamp = datetime.datetime.utcnow())
                for rank in fifteen_ranks_murder:
                    if rank is not None:
                        embed.add_field(name = stat_murder[rank.removesuffix("Ranking")], value = '\n'.join([f'{x+1}. **{player["playerName"]}:** {player[rank.removesuffix("Ranking")]}' for x, player in enumerate(rankings_murder[rank])]), inline = True)
                await ctx.send(embed = embed)
                await asyncio.sleep(1)
        elif mode == 'skywars':
            keys_skywars = list(rankings_skywars.keys())
            for fifteen_ranks_skywars in list(zip_longest(keys_skywars[::21], keys_skywars[1::21], keys_skywars[2::21], keys_skywars[3::21], keys_skywars[4::21], keys_skywars[5::21], keys_skywars[6::21], keys_skywars[7::21], keys_skywars[8::21], keys_skywars[9::21], keys_skywars[10::21], keys_skywars[11::21], keys_skywars[12::21], keys_skywars[13::21], keys_skywars[14::21], keys_skywars[15::21], keys_skywars[16::21], keys_skywars[17::21], keys_skywars[18::21], keys_skywars[19::21], keys_skywars[20::21])):
                embed = discord.Embed(title = "Hypixel Skywars Leaderboard PT/BR", description = f"Last update: {last_update_time}", color = embed_colour, timestamp = datetime.datetime.utcnow())
                for rank in fifteen_ranks_skywars:
                    if rank is not None:
                        embed.add_field(name = stat_skywars[rank.removesuffix("Ranking")], value = '\n'.join([f'{x+1}. **{player["playerName"]}:** {player[rank.removesuffix("Ranking")]}' for x, player in enumerate(rankings_skywars[rank])]), inline = True)
                await ctx.send(embed = embed)
                await asyncio.sleep(1)
        elif mode == 'speeduhc':
            keys_such = list(rankings_such.keys())
            for fifteen_ranks_such in list(zip_longest(keys_such[::21], keys_such[1::21], keys_such[2::21], keys_such[3::21], keys_such[4::21], keys_such[5::21], keys_such[6::21], keys_such[7::21], keys_such[8::21], keys_such[9::21], keys_such[10::21], keys_such[11::21], keys_such[12::21], keys_such[13::21], keys_such[14::21], keys_such[15::21], keys_such[16::21], keys_such[17::21], keys_such[18::21], keys_such[19::21], keys_such[20::21])):
                embed = discord.Embed(title = "Hypixel Speed UHC Leaderboard PT/BR", description = f"Last update: {last_update_time}", color = embed_colour, timestamp = datetime.datetime.utcnow())
                for rank in fifteen_ranks_such:
                    if rank is not None:
                        embed.add_field(name = stat_such[rank.removesuffix("Ranking")], value = '\n'.join([f'{x+1}. **{player["playerName"]}:** {player[rank.removesuffix("Ranking")]}' for x, player in enumerate(rankings_such[rank])]), inline = True)
                await ctx.send(embed = embed)
                await asyncio.sleep(1)
        elif mode == 'tnt':
            keys_tnt = list(rankings_tnt.keys())
            for fifteen_ranks_tnt in list(zip_longest(keys_tnt[::21], keys_tnt[1::21], keys_tnt[2::21], keys_tnt[3::21], keys_tnt[4::21], keys_tnt[5::21], keys_tnt[6::21], keys_tnt[7::21], keys_tnt[8::21], keys_tnt[9::21], keys_tnt[10::21], keys_tnt[11::21], keys_tnt[12::21], keys_tnt[13::21], keys_tnt[14::21], keys_tnt[15::21], keys_tnt[16::21], keys_tnt[17::21], keys_tnt[18::21], keys_tnt[19::21], keys_tnt[20::21])):
                embed = discord.Embed(title = "Hypixel TNT Games Leaderboard PT/BR", description = f"Last update: {last_update_time}", color = embed_colour, timestamp = datetime.datetime.utcnow())
                for rank in fifteen_ranks_tnt:
                    if rank is not None:
                        embed.add_field(name = stat_tnt[rank.removesuffix("Ranking")], value = '\n'.join([f'{x+1}. **{player["playerName"]}:** {player[rank.removesuffix("Ranking")]}' for x, player in enumerate(rankings_tnt[rank])]), inline = True)
                await ctx.send(embed = embed)
                await asyncio.sleep(1)
        elif mode == 'warlords':
            keys_warlords = list(rankings_warlords.keys())
            for fifteen_ranks_warlords in list(zip_longest(keys_warlords[::21], keys_warlords[1::21], keys_warlords[2::21], keys_warlords[3::21], keys_warlords[4::21], keys_warlords[5::21], keys_warlords[6::21], keys_warlords[7::21], keys_warlords[8::21], keys_warlords[9::21], keys_warlords[10::21], keys_warlords[11::21], keys_warlords[12::21], keys_warlords[13::21], keys_warlords[14::21], keys_warlords[15::21], keys_warlords[16::21], keys_warlords[17::21], keys_warlords[18::21], keys_warlords[19::21], keys_warlords[20::21])):
                embed = discord.Embed(title = "Hypixel Warlords Leaderboard PT/BR", description = f"Last update: {last_update_time}", color = embed_colour, timestamp = datetime.datetime.utcnow())
                for rank in fifteen_ranks_warlords:
                    if rank is not None:
                        embed.add_field(name = stat_warlords[rank.removesuffix("Ranking")], value = '\n'.join([f'{x+1}. **{player["playerName"]}:** {player[rank.removesuffix("Ranking")]}' for x, player in enumerate(rankings_warlords[rank])]), inline = True)
                await ctx.send(embed = embed)
                await asyncio.sleep(1)
        elif mode == 'woolwars':
            keys_woolwars = list(rankings_woolwars.keys())
            for fifteen_ranks_woolwars in list(zip_longest(keys_woolwars[::21], keys_woolwars[1::21], keys_woolwars[2::21], keys_woolwars[3::21], keys_woolwars[4::21], keys_woolwars[5::21], keys_woolwars[6::21], keys_woolwars[7::21], keys_woolwars[8::21], keys_woolwars[9::21], keys_woolwars[10::21], keys_woolwars[11::21], keys_woolwars[12::21], keys_woolwars[13::21], keys_woolwars[14::21], keys_woolwars[15::21], keys_woolwars[16::21], keys_woolwars[17::21], keys_woolwars[18::21], keys_woolwars[19::21], keys_woolwars[20::21])):
                embed = discord.Embed(title = "Hypixel Wool Wars Leaderboard PT/BR", description = f"Last update: {last_update_time}", color = embed_colour, timestamp = datetime.datetime.utcnow())
                for rank in fifteen_ranks_woolwars:
                    if rank is not None:
                        embed.add_field(name = stat_woolwars[rank.removesuffix("Ranking")], value = '\n'.join([f'{x+1}. **{player["playerName"]}:** {player[rank.removesuffix("Ranking")]}' for x, player in enumerate(rankings_woolwars[rank])]), inline = True)
                await ctx.send(embed = embed)
                await asyncio.sleep(1)
        else:
            embed = discord.Embed(title = "Invalid argument", description = "You've entered a gamemode that is invalid or has not been included in the rankings yet. Currently supported gamemodes: ``arcade``, ``bedwars``, ``blitz``, ``buildbattle``, ``duels``, ``murder``, ``skywars``, ``speeduhc``, ``tnt``, ``warlords``, ``woolwars``.", color =  discord.Color.red())
            await ctx.reply(embed = embed, mention_author = False)
    else:
        keys = list(rankings.keys())
        for fifteen_ranks in list(zip_longest(keys[::21], keys[1::21], keys[2::21], keys[3::21], keys[4::21], keys[5::21], keys[6::21], keys[7::21], keys[8::21], keys[9::21], keys[10::21], keys[11::21], keys[12::21], keys[13::21], keys[14::21], keys[15::21], keys[16::21], keys[17::21], keys[18::21], keys[19::21], keys[20::21])):
            embed = discord.Embed(title = "Hypixel General Leaderboard PT/BR", description = f"Last update: {last_update_time}\nFor mode-specific leaderboards, use $lb [mode]\nCurrently supported gamemodes: ``arcade``, ``bedwars``, ``blitz``,  ``buildbattle``, ``duels``, ``mega walls``, ``murder``, ``skywars``, ``speeduhc``, ``tnt``, ``warlords``, ``woolwars``.", color = embed_colour, timestamp = datetime.datetime.utcnow())
            for rank in fifteen_ranks:
                if rank is not None:
                    embed.add_field(name = stat_title[rank.removesuffix("Ranking")], value = '\n'.join([f'{x+1}. **{player["playerName"]}:** {player[rank.removesuffix("Ranking")]}' for x, player in enumerate(rankings[rank])]), inline = True)
            await ctx.send(embed = embed)
            await asyncio.sleep(1)

bot.run(bot_token)
