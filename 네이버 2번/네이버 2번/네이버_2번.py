blocks=[[0, 50], [0, 22], [2, 10], [1, 4], [4, -13]]
def sol(blocks):

    oneChecked = False
    twoChecked = False
    for i in range(len(blocks)):
        blocks[i].append(i)

    while True:
        for i in range(len(blocks)):
            # 루트 블록
            for j in range(len(blocks)):
                #하위 블록 중 하나
                if blocks[i][2] +1 == blocks[j][2]:
                    # 바로 한 칸 하위에 있는 블록 이란것
                    if blocks[i][0] == blocks[j][0]: 
                        #왼쪽
                        oneChecked = True

                    if blocks[i][0] == blocks[j][0]+1:
                        #오른쪽
                        twoChecked = True

                if oneChecked == True and twoChecked == True:
                    continue
                elif oneChecked == True and twoChecked==False:
                    blocks.append([blocks[j][0]+1, blocks[i][1]-blocks[j][1], blocks[j][2]])
                    oneChecked = False
                    break
                elif oneChecked == False and twoChecked == True:
                    blocks.append([blocks[j][0], blocks[i][1]-blocks[j][1], blocks[j][2]])
                    twoChecked = False
                    break

                else:
                    continue


    print(blocks)
            

sol(blocks)