from collections import defaultdict
import numpy as np
from xpinyin import Pinyin
import sys
def backtrack(pathDict,endPoint):
    path=[]
    while endPoint in pathDict:
        prev=pathDict[endPoint]
        path=[prev]+path
        endPoint=prev
    return path

class idom_finder:
    def __init__(self, idiom_dict_file,target_idiom,depth_limit=5):
        self.idiom_dict=read_dictionary = np.load(idiom_dict_file).item()
        self.target=target_idiom
        self.depth_limit=depth_limit
        self.p=Pinyin()

    def find_neighbor(self,node):
        last_pinyin=self.p.get_pinyin(node[-1])
        return self.idiom_dict[last_pinyin]

    def bfs_search(self,current_node):
        visited=set()
        frontier=[]
        depth_queue=[]

        frontier.append(current_node)
        depth_queue.append(1)
        visited.add(current_node)
        pathMap={}
        path=[]
        current_depth=0
        while current_depth<self.depth_limit:
            s=frontier.pop(0)
            current_depth=depth_queue.pop(0)
            if s==self.target:
                path=backtrack(pathMap,self.target)+[s]
                return path
            neighbors=self.find_neighbor(s)
            for neighbor in neighbors:
                if neighbor in visited:
                    continue
                if neighbor not in frontier:
                    frontier.append(neighbor)
                    depth_queue.append(current_depth+1)
                    pathMap[neighbor]=s
            visited.add(s)
        return "无法在"+str(self.depth_limit)+"步内找到"+str(self.target)

def create_dict_from_file(file_name):
    idioms_list=[]
    p=Pinyin()
    with open(file_name) as fp:
        for line in fp:
            idiom = line.split("\t")[0][:-1]
            if len(idiom)==4:
                idioms_list.append(idiom)
    idioms_dict=defaultdict(list)
    for idiom in idioms_list:
        initial_pinyin=p.get_pinyin(idiom[0])
        idioms_dict[initial_pinyin].append(idiom)
    np.save("idioms_dict.npy",idioms_dict)
    

def main():
    finder=idom_finder("idioms_dict.npy","为所欲为")
    print(finder.bfs_search(sys.argv[1]))
main()