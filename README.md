# 为所欲为生成器
Using a depth-limited bfs to find the shortest 成语接龙 path from a certain idiom to "为所欲为“(or any idioms).

The dictionary for the idioms is stored in idiom_dict.npy. It is pre-calculated using idioms from THUOCL by create_dict_from_file().You can create your own idioms set using that function.

The default limit of depth is 4. The default target is "为所欲为“. These could be modified easily.



run:
pip install -xpinyin

python3 main.py 你的成语

example:

python3 main.py 千方百计

['千方百计', '岌岌可危', '为所欲为']

python3 main.py 赫赫有名

['赫赫有名', '名副其实', '事与愿违', '为所欲为']
