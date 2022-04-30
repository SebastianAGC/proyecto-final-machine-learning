# Proyecto Final
# Sebastián Galindo
# Carné 15452
# Data Mining y Machine Learning

# Managing imports
import pandas as pd


def normalize_dataset1(data):

    max_wards_placed = max(data["WardsPlaced"])
    max_wards_destroyed = max(data["WardsDestroyed"])
    max_dragons = max(data["Dragons"])
    max_heralds = max(data["Heralds"])
    max_towers_destroyed = max(data["TowersDestroyed"])
    max_minions_killed = max(data["TotalMinionsKilled"])
    max_jg_minions_killed = max(data["TotalJungleMinionsKilled"])

    data["WardsPlaced"] = data["WardsPlaced"] / max_wards_placed
    data["WardsDestroyed"] = data["WardsDestroyed"] / max_wards_destroyed
    data["Dragons"] = data["Dragons"] / max_dragons
    data["Heralds"] = data["Heralds"] / max_heralds
    data["TowersDestroyed"] = data["TowersDestroyed"] / max_towers_destroyed
    data["TotalMinionsKilled"] = data["TotalMinionsKilled"] / max_minions_killed
    data["TotalJungleMinionsKilled"] = data["TotalJungleMinionsKilled"] / max_jg_minions_killed
    return data


def normalize_dataset2(data):
    max_wards_placed = max(data["WardsPlaced"])
    max_wards_destroyed = max(data["WardsDestroyed"])
    max_kills = max(data["Kills"])
    max_deaths = max(data["Deaths"])
    max_assists = max(data["Assists"])
    max_dragons = max(data["Dragons"])
    max_heralds = max(data["Heralds"])
    max_towers_destroyed = max(data["TowersDestroyed"])
    max_minions_killed = max(data["TotalMinionsKilled"])
    max_jg_minions_killed = max(data["TotalJungleMinionsKilled"])

    data["WardsPlaced"] = data["WardsPlaced"] / max_wards_placed
    data["WardsDestroyed"] = data["WardsDestroyed"] / max_wards_destroyed
    data["Kills"] = data["Kills"] / max_kills
    data["Deaths"] = data["Deaths"] / max_deaths
    data["Assists"] = data["Assists"] / max_assists
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
input_file_dataset1 = pd.read_csv("high_diamond_ranked_10min_wo_kills.csv")
input_file_dataset2 = pd.read_csv("high_diamond_ranked_10min_w_kills.csv")
input_file_dataset3 = pd.read_csv("high_diamond_ranked_10min_diff_parsed.csv")
output_training_size = 1000
output_test_size = 300

# Normalize data
print("Normalizing data...")
data_dataset1 = normalize_dataset1(input_file_dataset1)
data_dataset2 = normalize_dataset2(input_file_dataset2)
data_dataset3 = input_file_dataset3

# Shuffle training data
data_dataset1 = data_dataset1.sample(frac=1)
data_dataset2 = data_dataset2.sample(frac=1)
data_dataset3 = data_dataset3.sample(frac=1)

# CODE USED WHEN DATA FILE WAS ONLY ONE FILE
dataset1_training = data_dataset1.sample(frac=0.7)
dataset1_test = data_dataset1.drop(dataset1_training.index)
dataset1_training2 = dataset1_training.sample(frac=0.7)
dataset1_validation = dataset1_training.drop(dataset1_training2.index)

dataset2_training = data_dataset2.sample(frac=0.7)
dataset2_test = data_dataset2.drop(dataset2_training.index)
dataset2_training2 = dataset2_training.sample(frac=0.7)
dataset2_validation = dataset2_training.drop(dataset2_training2.index)

dataset3_training = data_dataset3.sample(frac=0.7)
dataset3_test = data_dataset3.drop(dataset3_training.index)
dataset3_training2 = dataset3_training.sample(frac=0.7)
dataset3_validation = dataset3_training.drop(dataset3_training2.index)

# CODE USED TO GENERATE TRAINING AND TEST FILES
dataset1_training2.to_csv('league-rankeds-dataset1-training.csv', index=False)
dataset1_validation.to_csv('league-rankeds-dataset1-validation.csv', index=False)
dataset1_test.to_csv('league-rankeds-dataset1-test.csv', index=False)

dataset2_training2.to_csv('league-rankeds-dataset2-training.csv', index=False)
dataset2_validation.to_csv('league-rankeds-dataset2-validation.csv', index=False)
dataset2_test.to_csv('league-rankeds-dataset2-test.csv', index=False)

dataset3_training2.to_csv('league-rankeds-dataset3-training.csv', index=False)
dataset3_validation.to_csv('league-rankeds-dataset3-validation.csv', index=False)
dataset3_test.to_csv('league-rankeds-dataset3-test.csv', index=False)