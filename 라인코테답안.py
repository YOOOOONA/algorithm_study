# # # def solution(enter, leave):
# # #     answer = [0 for _ in range(len(enter))]
# # #     #입실순서가 먼전데 퇴실명부에 뒷순서면 무조건 만났음
# # #     for i in range(len(leave)):
# # #         for j in enter:
# # #             if enter.index(j) < enter.index(leave[i]):
# # #                 if j not in leave[:i]:
# # #                     answer[j-1] += 1
# # #                     answer[leave[i] - 1] += 1
# # #     return answer#반드시 만난 사람은 몇 명
# # # print(solution([1,4,2,3],	[2,1,3,4]))


"""단계별 코테문제 테케 전체 통과"""

"""1번"""
# # def solution(program, flag_rules, commands):
# #     answer = [True for _ in range(len(commands))]
# #     dic = {}
# #     for i in range(len(flag_rules)):
# #         f = flag_rules[i].split()
# #         dic[f[0]] = f[1]#d={"-s":"STRING"}
    
# #     for i in range(len(commands)):
# #         cmd = commands[i].split()
# #         #for j in range(len(cmd)):
# #         j=0
# #         while j<len(cmd):
# #             if j == 0:
# #                 if program == cmd[j]:
# #                     j += 1
# #                     continue
# #                 else:
# #                     answer[i] = False
# #                     break
# #             if cmd[j][0] == '-':
# #                 flag = dic[cmd[j]]
# #                 if cmd[j] == 'NULL':
# #                     continue
# #                 elif j<len(cmd)-1:
# #                     j+= 1
# #                     arg = cmd[j]
# #                     if flag == "STRING":
# #                         for c in arg:
# #                             if ord("A")<=ord(c)<=ord("Z") or ord("a")<=ord(c)<=ord("z") :
# #                                 continue
# #                             else:
# #                                 answer[i] = False
# #                                 break
# #                     elif flag == "NUMBER":
# #                         for c in arg:
# #                             if ord("0")<=ord(c)<=ord("9"):
# #                                 continue
# #                             else:
# #                                 answer[i] = False
# #                                 break
# #                 # elif flag == "NULL":
# #                 #     if arg:#인자가 아무것도 없어야됨
# #                 #         answer[i] = False
# #                 #         break
# #             else:
# #                 answer[i] = False
# #                 break
# #             j += 1
# #     return answer
# # print(solution("line",	["-s STRING", "-n NUMBER", "-e NULL"],	["line -n 100 -s hi -e", "lien -s Bye"]))

"""2번"""
# def solution(program, flag_rules, commands):
#     answer = [True for _ in range(len(commands))]
#     dic = {}
#     for i in range(len(flag_rules)):
#         f = flag_rules[i].split()
#         dic[f[0]] = f[1]#d={"-s":"STRING"}
    
#     for i in range(len(commands)):
#         cmd = commands[i].split()
#         #for j in range(len(cmd)):
#         j=0
#         while (j<len(cmd) and answer[i]):
#             if j == 0:
#                 if program == cmd[j]:
#                     j += 1
#                     continue
#                 else:
#                     answer[i] = False
#                     break
#             if cmd[j][0] == '-':
#                 flag = dic[cmd[j]]
#                 cnt = 0
#                 if flag == 'NULL':
#                     j = j
#                 elif j<len(cmd)-1:
#                     while(j+1<len(cmd) and cmd[j+1][0] != '-'):
#                         j+= 1
#                         arg = cmd[j]
#                         cnt += 1
#                         if flag in ["STRING","STRINGS"]:
#                             if flag == "STRING" and cnt != 1:
#                                 answer[i] = False
#                                 break
#                             for c in arg:
#                                 if ord("A")<=ord(c)<=ord("Z") or ord("a")<=ord(c)<=ord("z") :
#                                     continue
#                                 else:
#                                     answer[i] = False
#                                     break
#                         elif flag in ["NUMBERS","NUMBER"]:
#                             if flag == "NUMBER" and cnt != 1:
#                                 answer[i] = False
#                                 break
#                             for c in arg:
#                                 if ord("0")<=ord(c)<=ord("9"):
#                                     continue
#                                 else:
#                                     answer[i] = False
#                                     break
#                 else:
#                     break
#             else:
#                 answer[i] = False
#                 break
#             j += 1
#     return answer
# #print(solution("line"	,["-s STRINGS", "-n NUMBERS", "-e NULL"]	,["line -n 100 102 -s hi -e", "line -n id pwd -n 100"]))
# print(solution(	"trip",	["-days NUMBERS", "-dest STRING"],	["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"]))

"""3번"""
from collections import deque
def solution(program, flag_rules, commands):
    answer = [True for _ in range(len(commands))]
    dic = {}
    q = deque(flag_rules)
    dup = {}
    while(q):
        # for i in range(len(flag_rules)):
        one = q.popleft()
        f = one.split()
        #ALIAS 넣어야됨
        if len(f)==2:
            dic[f[0]] = f[1]#d={"-s":"STRING"}
        elif len(f)==3:#"-a ALIAS -amount"
            if f[1] == 'ALIAS':
                dup[f[0]] = [f[2],0]
                dup[f[2]] = [f[0],0]
                #한쪽이 이미 dic에 flag있을 떄 
                if f[0] in dic:
                    dic[f[2]] = dic[f[0]]
                elif f[2] in dic:
                    dic[f[0]] = dic[f[2]]
                
                #아직 dic에 안들어왔을 때
                else:
                    q.append(one)#다시 넣어줘
    for i in range(len(commands)):
        cmd = commands[i].split()
        #for j in range(len(cmd)):
        j=0
        while (j<len(cmd) and answer[i]):
            if j == 0:
                if program == cmd[j]:
                    j += 1
                    continue
                else:
                    answer[i] = False
                    break
            if cmd[j][0] == '-':
                if cmd[j] in dup:
                    if dup[dup[cmd[j]][0]][1] != 0:
                        answer[i] = False
                        break
                    else:
                        dup[cmd[j]][1] = 1
                flag = dic[cmd[j]]
                cnt = 0
                if flag == 'NULL':
                    j = j
                elif j<len(cmd)-1:
                    while(j+1<len(cmd) and cmd[j+1][0] != '-'):
                        j+= 1
                        arg = cmd[j]
                        cnt += 1
                        if flag in ["STRING","STRINGS"]:
                            if flag == "STRING" and cnt != 1:
                                answer[i] = False
                                break
                            for c in arg:
                                if ord("A")<=ord(c)<=ord("Z") or ord("a")<=ord(c)<=ord("z") :
                                    continue
                                else:
                                    answer[i] = False
                                    break
                        elif flag in ["NUMBERS","NUMBER"]:
                            if flag == "NUMBER" and cnt != 1:
                                answer[i] = False
                                break
                            for c in arg:
                                if ord("0")<=ord(c)<=ord("9"):
                                    continue
                                else:
                                    answer[i] = False
                                    break
                else:
                    break
            else:
                answer[i] = False
                break
            j += 1
    return answer
print(solution("line",	["-s STRING", "-num NUMBER", "-e NULL", "-n ALIAS -num"],	["line -n 100 -s hi -e", "line -n 100 -e -num 150"]))
print(solution("bank",	["-send STRING", "-a ALIAS -amount", "-amount NUMBERS"]	,["bank -send abc -amount 500 200 -a 400", "bank -send abc -a hey"]))
