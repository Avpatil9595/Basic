skill=open('skill.txt','r')

skill_list=skill.read()
list=[]
list=skill_list.split('\n')

print(len(list))