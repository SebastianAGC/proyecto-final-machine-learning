# Proyecto Final
# Sebastián Galindo
# Carné 15452
# Data Mining y Machine Learning

# Managing imports
import pandas as pd
import numpy


def normalize_data(data):
    #removed gameid
    #removes first blood
    #removed kda
    #removed elite monsters
    #removed total gold
    #removed avglvl
    #removed total experience
    #removed gold diff
    #removed experience diff
    #removed cs per min
    #removed gold per min
    max_win = max(data["Win"])
    max_wards_placed = max(data["WardsPlaced"])
    max_wards_destroyed = max(data["WardsDestroyed"])
    #max_kills = max(data["blueKills"])
    #max_deaths = max(data["blueDeaths"])
    #max_assists = max(data["blueAssists"])
    max_dragons = max(data["Dragons"])
    max_heralds = max(data["Heralds"])
    max_towers_destroyed = max(data["TowersDestroyed"])
    max_minions_killed = max(data["TotalMinionsKilled"])
    max_jg_minions_killed = max(data["TotalJungleMinionsKilled"])
    #max_cs_per_min = max(data["blueCSPerMin"])

    data["Win"] = data["Win"] / max_win
    data["WardsPlaced"] = data["WardsPlaced"] / max_wards_placed
    data["WardsDestroyed"] = data["WardsDestroyed"] / max_wards_destroyed
    data["Dragons"] = data["Dragons"] / max_dragons
    data["Heralds"] = data["Heralds"] / max_heralds
    data["TowersDestroyed"] = data["TowersDestroyed"] / max_towers_destroyed
    data["TotalMinionsKilled"] = data["TotalMinionsKilled"] / max_minions_killed
    data["TotalJungleMinionsKilled"] = data["TotalJungleMinionsKilled"] / max_jg_minions_killed
    return data


# -------------------------------------------------------------------------------------#
# -------------------------------------------------------------------------------------#
# -----------------------------PROGRAM STARTS HERE-------------------------------------#
# -------------------------------------------------------------------------------------#
# -------------------------------------------------------------------------------------#

# Inputs
print("Reading inputs...")
input_file = pd.read_csv("high_diamond_ranked_10min.csv")
output_training_size = 1000
output_test_size = 300

# Normalize data
print("Normalizing data...")
input_file_data = normalize_data(input_file)

# Shuffle training data
input_file_data = input_file_data.sample(frac=1)


# CODE USED WHEN DATA FILE WAS ONLY ONE FILE
input_data_training = input_file_data.sample(frac=0.7)
input_data_test = input_file_data.drop(input_data_training.index)

# CODE USED TO GENERATE TRAINING AND TEST FILES
input_data_training.to_csv('league-rankeds-training.csv', index=False)
input_data_test.to_csv('league-rankeds-test.csv', index=False)


#input_training_file = pd.read_csv("winequality-training.csv")  # CHANGE PATH HERE
#input_test_file = pd.read_csv("winequality-test.csv")  # CHANGE PATH HERE
#input_iterations = 10000
#input_alpha = 0.1
#input_threshold = 0.5
#input_weights = numpy.zeros(input_training_file.shape[1])
#input_folds = 10