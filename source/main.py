# パス操作ライブラリにosかpathlibどちらを採用するか検討
import csv
import pathlib
import matplotlib.pyplot as plt

#  ディレクトリ名
_directory_name = "dataset"

# csvファイル名
_pokemon_status_file_name = "pokemon_status.csv"

# 列名 ポケモン名
COLUMN_NAME_POKEMON_NAME = 1

# 列名 タイプ1
COLUMN_NAME_POKEMON_TYPE1 = 2

# 列名 タイプ2
COLUMN_NAME_POKEMON_TYPE2 = 3

# 列名 合計
COLUMN_NAME_NUM = 13

# インスタンス生成
pureWindowsPath = pathlib.PureWindowsPath(__file__)
current_directory = pureWindowsPath.parent
parent_directory = current_directory.parent
csv_file_path = parent_directory.joinpath(_directory_name, _pokemon_status_file_name)

pokemon_dictionary = {}
pokemon_name_list = []
pokemon_num_list = []
pokemon_type_list = []
with open(csv_file_path) as csv_file_path:
    # ヘッダーを削除
    next(csv.reader(csv_file_path))

    for row in csv.reader(csv_file_path):

        name = row[COLUMN_NAME_POKEMON_NAME]
        num = row[COLUMN_NAME_NUM]
        type1 = row[COLUMN_NAME_POKEMON_TYPE1]
        type2 = row[COLUMN_NAME_POKEMON_TYPE2]

        pokemon_name_list.append(name)
        pokemon_num_list.append(num)
        pokemon_type_list.append(type1)
        pokemon_type_list.append(type2)

pokemon_dictionary = dict(zip(pokemon_name_list, pokemon_num_list))

max_num_pokemon = {}
min_num_pokemon = {}
max_value = 0
for key, value in pokemon_dictionary.items():

    if value == max(pokemon_dictionary.values()):
        max_num_pokemon[key] = value

    if value == min(pokemon_dictionary.values()):
        min_num_pokemon[key] = value

print("一番高いポケモン" + max_num_pokemon.__str__())
print("一番低いポケモン" + min_num_pokemon.__str__())

pokemon_type_count_dictionary = {}
nomal_count = pokemon_type_list.count("ノーマル")
pokemon_type_count_dictionary["ノーマル"] = nomal_count

fire_count = pokemon_type_list.count("ほのお")
pokemon_type_count_dictionary["ほのお"] = fire_count

water_count = pokemon_type_list.count("みず")
pokemon_type_count_dictionary["みず"] = water_count

electric_count = pokemon_type_list.count("でんき")
pokemon_type_count_dictionary["でんき"] = electric_count

grass_count = pokemon_type_list.count("くさ")
pokemon_type_count_dictionary["くさ"] = grass_count

ice_count = pokemon_type_list.count("こおり")
pokemon_type_count_dictionary["こおり"] = ice_count

fighting_count = pokemon_type_list.count("かくとう")
pokemon_type_count_dictionary["かくとう"] = fighting_count

poison_count = pokemon_type_list.count("どく")
pokemon_type_count_dictionary["どく"] = poison_count

ground_count = pokemon_type_list.count("じめん")
pokemon_type_count_dictionary["じめん"] = ground_count

flying_count = pokemon_type_list.count("ひこう")
pokemon_type_count_dictionary["ひこう"] = flying_count

Psychic_count = pokemon_type_list.count("エスパー")
pokemon_type_count_dictionary["エスパー"] = Psychic_count

Bug_count = pokemon_type_list.count("むし")
pokemon_type_count_dictionary["むし"] = Bug_count

Rock_count = pokemon_type_list.count("いわ")
pokemon_type_count_dictionary["いわ"] = Rock_count

ghost_count = pokemon_type_list.count("ゴースト")
pokemon_type_count_dictionary["ゴースト"] = ghost_count

dragon_count = pokemon_type_list.count("ドラゴン")
pokemon_type_count_dictionary["ドラゴン"] = dragon_count

dark_count = pokemon_type_list.count("あく")
pokemon_type_count_dictionary["あく"] = dark_count

steel_count = pokemon_type_list.count("はがね")
pokemon_type_count_dictionary["はがね"] = steel_count

fairy_count = pokemon_type_list.count("フェアリー")
pokemon_type_count_dictionary["フェアリー"] = fairy_count

horizontal_axis_index_list = []
for index in range(pokemon_type_count_dictionary.keys().__len__()):
    horizontal_axis_index_list.append(index)

left = horizontal_axis_index_list
height = pokemon_type_count_dictionary.values()
plt.bar(left, height)
plt.show()