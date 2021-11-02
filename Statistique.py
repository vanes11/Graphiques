#from genericpath import isdir
import matplotlib.pyplot as plt
import os
import sys
#import glob
#import csv
from matplotlib import pyplot as plt
import pandas as pd
from mpl_toolkits.axes_grid1 import ImageGrid
from PIL import Image
import seaborn as sns
import numpy as np



def FlashFillInformation():

    currentDirectory = os.getcwd()
    chemin1 = currentDirectory+'/FlashFillResults/'+'statResults.txt'
    with open(currentDirectory+'/FlashFillResults/' + "statResults.txt", "w") as a_file:
        a_file.truncate()

    P = []
    BonP = []
    FauxP = []
    tauxFaux = []
    tauxBon = []
    B = []

    for i in range(1,5):

        chemin = currentDirectory+'/FlashFillResults/stat'+str(i)+'.txt'
        
        #print(chemin)
        Benchmarks = []
        nbreP = []
        nbreBonP = []
        nbreFauxP = []
        tauxBonP = []
        tauxFauxP = []

        with open(chemin,"r", newline=None) as f:
            line_count = 0               
            for line in f:
                if line.replace('\n','') != '***':                      
                    if line_count == 0:
                        line = line.replace('\n','')
                        line = list(line)
                        line = ''.join(line[1:])

                        Benchmarks.append(int(line))
                        line_count +=1

                    elif line_count == 1 :                          
                        line = line.replace('\n','')
                        
                        if line == '': 
                                                        
                            nbreP.append(0)
                            nbreFauxP.append(0)
                            nbreBonP.append(0)
                            tauxFauxP.append(0.0)
                            tauxBonP.append(0.0)
                            line_count +=1
                        else:
                            line = line.split(':')
                            line = line[-1]
                            line = line.replace(' ','')
                            nbreP.append(int(line))
                            line_count +=1


                    elif line_count == 2 :
                        line = line.replace('\n','')
                        
                        if line == '':
                            
                            nbreP.append(0)
                            nbreFauxP.append(0)
                            nbreBonP.append(0)
                            tauxFauxP.append(0.0)
                            tauxBonP.append(0.0)
                            line_count +=1
                        else:
                            line = line.split(':')
                            line = line[-1]
                            line = line.replace(' ','')
                            nbreFauxP.append(int(line))
                            line_count +=1
                    
                    elif line_count == 3 :
                        line = line.replace('\n','')    

                        if line == '':
                            
                            nbreP.append(0)
                            nbreFauxP.append(0)
                            nbreBonP.append(0)
                            tauxFauxP.append(0.0)
                            tauxBonP.append(0.0)
                            line_count +=1
                        else:
                            line = line.split(':')
                            line = line[-1]
                            line = line.replace(' ','')
                            nbreBonP.append(int(line))
                            line_count +=1
                    
                    
                    elif line_count == 4 :
                        line = line.replace('\n','')
                        
                        if line == '':
                            
                            nbreP.append(0)
                            nbreFauxP.append(0)
                            nbreBonP.append(0)
                            tauxFauxP.append(0.0)
                            tauxBonP.append(0.0)
                            line_count +=1
                        else:
                            line = line.split(':')
                            line = line[-1]
                            line = line.replace(' ','')
                            tauxFauxP.append(float(line))
                            line_count +=1

                    elif line_count == 5 :
                        line = line.replace('\n','')                           

                        if line == '':
                    
                            nbreP.append(0)
                            nbreFauxP.append(0)
                            nbreBonP.append(0)
                            tauxFauxP.append(0.0)
                            tauxBonP.append(0.0)
                            line_count +=1
                        else:
                            line = line.split(':')
                            line = line[-1]
                            line = line.replace(' ','')
                            tauxBonP.append(float(line))
                            line_count +=1

                else:                        
                    line_count = 0
                                                    
        B.append(Benchmarks)
        P.append(nbreP)
        BonP.append(nbreBonP)
        #FauxP.append(nbreBonP)
        #tauxFaux.append(tauxFauxP)
        tauxBon.append(tauxBonP)
        """ print(Benchmarks,"***********\n")
        print(nbreP,"***********\n")
        print(nbreBonP,"***********\n")
        print(tauxBonP,"***********\n") """
        
        
        with open(chemin1, 'a') as f:
            f.write('Cas de '+str(i)+'exemple(s)\n')
            f.write('Benchmarks : '+str(Benchmarks)+'\n')
            f.write('Nombre de Programmes, : '+str(nbreP)+'\n')
            f.write('Nombre de faux programmes'+str(nbreFauxP)+'\n')
            f.write('Nombre de bons Programmes : '+str(nbreBonP)+'\n')
            f.write('Taux de faux programmes'+str(tauxFauxP)+'\n')
            f.write('Taux de faux programmes'+str(tauxBonP)+'\n')
            f.write('***\n')


    Bx = []; Px=[]; BonPx = []; tauxBonx = []
   
    for i in range(4):
        x = []; y = []; z = []; t = []
        position = []
        for valeur in B[i]:
            position.append((valeur,B[i].index(valeur)))
        
        position.sort(key = lambda x:x[0])
        
        
        for elt in position:
            
            x.append(B[i][elt[1]])    
            y.append(P[i][elt[1]])
            z.append(BonP[i][elt[1]])
            t.append(tauxBon[i][elt[1]])
        
        #print(len(x),len(y),len(z),len(t),i)

        Bx.append(x)
        Px.append(y)
        BonPx.append(z)
        tauxBonx.append(t)
    #print(len(Bx),len(Px),len(BonPx),len(tauxBonx),i)
    #Bx,Px,BonPx,tauxBonx

    return Bx,Px,BonPx,tauxBonx


   


def QuickFillInformation():

    currentDirectory = os.getcwd()
    chemin1 = currentDirectory+'/QuickFillResults/'+'statResults.txt'

    with open(currentDirectory+'/QuickFillResults/' + "statResults.txt", "w") as a_file:
        a_file.truncate()

    P = []
    BonP = []
    FauxP = []
    tauxFaux = []
    tauxBon = []
    B = []

    for i in range(1,5):

        chemin = currentDirectory+'/QuickFillResults/stat'+str(i)+'.txt'
        
        #print(chemin)
        Benchmarks = []
        nbreP = []
        nbreBonP = []
        nbreFauxP = []
        tauxBonP = []
        tauxFauxP = []

        with open(chemin,"r", newline=None) as f:
            line_count = 0               
            for line in f:
                if line.replace('\n','') != '***':                      
                    if line_count == 0:
                        line = line.replace('\n','')
                        line = list(line)
                        line = ''.join(line[1:])

                        Benchmarks.append(int(line))
                        line_count +=1

                    elif line_count == 1 :                          
                        line = line.replace('\n','')
                        
                        if line == '': 
                                                        
                            nbreP.append(0)
                            nbreFauxP.append(0)
                            nbreBonP.append(0)
                            tauxFauxP.append(0.0)
                            tauxBonP.append(0.0)
                            line_count +=1
                        else:
                            line = line.split(':')
                            line = line[-1]
                            line = line.replace(' ','')
                            nbreP.append(int(line))
                            line_count +=1


                    elif line_count == 2 :
                        line = line.replace('\n','')
                        
                        if line == '':
                            
                            nbreP.append(0)
                            nbreFauxP.append(0)
                            nbreBonP.append(0)
                            tauxFauxP.append(0.0)
                            tauxBonP.append(0.0)
                            line_count +=1
                        else:
                            line = line.split(':')
                            line = line[-1]
                            line = line.replace(' ','')
                            nbreFauxP.append(int(line))
                            line_count +=1
                    
                    elif line_count == 3 :
                        line = line.replace('\n','')    

                        if line == '':
                            
                            nbreP.append(0)
                            nbreFauxP.append(0)
                            nbreBonP.append(0)
                            tauxFauxP.append(0.0)
                            tauxBonP.append(0.0)
                            line_count +=1
                        else:
                            line = line.split(':')
                            line = line[-1]
                            line = line.replace(' ','')
                            nbreBonP.append(int(line))
                            line_count +=1
                    
                    
                    elif line_count == 4 :
                        line = line.replace('\n','')
                        
                        if line == '':
                            
                            nbreP.append(0)
                            nbreFauxP.append(0)
                            nbreBonP.append(0)
                            tauxFauxP.append(0.0)
                            tauxBonP.append(0.0)
                            line_count +=1
                        else:
                            line = line.split(':')
                            line = line[-1]
                            line = line.replace(' ','')
                            tauxFauxP.append(float(line))
                            line_count +=1

                    elif line_count == 5 :
                        line = line.replace('\n','')                           

                        if line == '':
                    
                            nbreP.append(0)
                            nbreFauxP.append(0)
                            nbreBonP.append(0)
                            tauxFauxP.append(0.0)
                            tauxBonP.append(0.0)
                            line_count +=1
                        else:
                            line = line.split(':')
                            line = line[-1]
                            line = line.replace(' ','')
                            tauxBonP.append(float(line))
                            line_count +=1

                else:                        
                    line_count = 0
                                                    
        B.append(Benchmarks)
        P.append(nbreP)
        BonP.append(nbreBonP)
        #FauxP.append(nbreBonP)
        #tauxFaux.append(tauxFauxP)
        tauxBon.append(tauxBonP)
        """ print(Benchmarks,"***********\n")
        print(nbreP,"***********\n")
        print(nbreBonP,"***********\n")
        print(tauxBonP,"***********\n") """
        
        
        with open(chemin1, 'a') as f:
            f.write('Cas de '+str(i)+'exemple(s)\n')
            f.write('Benchmarks : '+str(Benchmarks)+'\n')
            f.write('Nombre de Programmes, : '+str(nbreP)+'\n')
            f.write('Nombre de faux programmes'+str(nbreFauxP)+'\n')
            f.write('Nombre de bons Programmes : '+str(nbreBonP)+'\n')
            f.write('Taux de faux programmes'+str(tauxFauxP)+'\n')
            f.write('Taux de faux programmes'+str(tauxBonP)+'\n')
            f.write('***\n')
    
    
    Bx = []; Px=[]; BonPx = []; tauxBonx = []
    

    for i in range(4):
        x = []; y = []; z = []; t = []
        position = []
        for valeur in B[i]:
            position.append((valeur,B[i].index(valeur)))
        
        position.sort(key = lambda x:x[0])
        
        
        for elt in position:
            
            x.append(B[i][elt[1]])    
            y.append(P[i][elt[1]])
            z.append(BonP[i][elt[1]])
            t.append(tauxBon[i][elt[1]])
        
        #print(len(x),len(y),len(z),len(t),i)

        Bx.append(x)
        Px.append(y)
        BonPx.append(z)
        tauxBonx.append(t)
    #print(len(Bx),len(Px),len(BonPx),len(tauxBonx),i)
    #Bx,Px,BonPx,tauxBonx

    return Bx,Px,BonPx,tauxBonx


  



def GraphProduction(Benchmarks,Programs,BonP,tauxBon):
    """ prends les statistiques que retourne la focntion execution pour en faire des graphiques.
    Ces statistiques sont obtenue par lecture de fichier , l1,l2,l3,l4 representent les donnees recoltees dans
   les fichiers stat.txt"""

    arg = sys.argv 
   
    if arg[1] == 'F':
        
        for i in range(4):
            couleur = []
            yLabels = []
            #label de l'ordonnee
            for taux in tauxBon[i]:
               
                if taux < 20.0:
                    couleur.append('red')
                elif taux < 50.0:
                    couleur.append('black')
                elif taux < 75.0:
                    couleur.append('orange')
                elif taux < 95.0:
                    couleur.append('blue')
                else:
                    couleur.append('green')

            for j in range(len(tauxBon[i])):

                yLabels.append('B'+str(Benchmarks[i][j])+'('+str(Programs[i][j])+')')
            #print(yLabels)


            y = tauxBon[i]
            x = Benchmarks[i]
            
            titre= 'Taux de reussite des Programmes sur'+str(i+1)+'exemple (s)'
            nom_graphe = 'TauxF'+str(i+1)+'exemples.svg'
            fig, ax = plt.subplots(figsize=(10, 7))
            bars = ax.barh(x,y,0.7,color=couleur,label="FlashFill")

            for bar in bars:
                width = bar.get_width() 
                width = round(width,2)
                label_y_pos = bar.get_y() + bar.get_height() / 2
                ax.text(width, label_y_pos, s=f'{width}'+'%', va='center')

            for tick in ax.yaxis.get_major_ticks():
                tick.label.set_fontsize(14)
            
            for tick in ax.xaxis.get_major_ticks():
                tick.label.set_fontsize(14)

            
            #ax.set_yticklabels(yLabels)
            plt.title(titre)
            plt.xlabel('Taux de reussite')
            plt.ylabel('Benchmarks & nombre des programmes')    
            plt.grid()
            ax.legend()
            plt.savefig(nom_graphe)
            #plt.show()


    elif arg[1] == 'Q':
        for i in range(4):
            couleur = []
            yLabels = []#label de l'ordonnee
            
            for taux in tauxBon[i]:

                if taux < 30.0:
                    couleur.append('red')
                elif taux < 50.0:
                    couleur.append('black')
                elif taux < 75.0:
                    couleur.append('orange')
                elif taux < 95.0:
                    couleur.append('blue')
                else:
                    couleur.append('green')

            for j in range(len(tauxBon[i])):

                yLabels.append('B'+str(Benchmarks[i][j])+'('+str(Programs[i][j])+')')

            y = tauxBon[i]
            x = Benchmarks[i]
            titre= 'Taux de reussite des Programmes sur'+str(i+1)+'exemple (s)'
            nom_graphe = 'TauxQ'+str(i+1)+'exemples.svg'
            fig, ax = plt.subplots(figsize=(10, 7))
            bars = ax.barh(x,y,0.7,color=couleur,label="QuickFill")

            for bar in bars:
                width = bar.get_width() 
                width = round(width,2)
                label_y_pos = bar.get_y() + bar.get_height() / 2
                ax.text(width, label_y_pos, s=f'{width}'+'%', va='center')

            """ for tick in ax.yaxis.get_major_ticks():
                tick.label.set_fontsize(14)
            
            for tick in ax.xaxis.get_major_ticks():
                tick.label.set_fontsize(14)"""
 
            
            ax.set_yticklabels(yLabels)
            plt.title(titre)
            plt.xlabel('Taux de reussite')
            plt.ylabel('Benchmarks & nombre des programmes')    
            plt.grid()
            ax.legend()
            plt.savefig(nom_graphe)
            #plt.show()



def grap1(BQ,tauxBonF,tauxBonQ):

    exemple = [1,2,3,4]
    list1 = []
    

    for j in range(len(BQ[0])):


        yF = [] ; yQ = []

        for i in range(4):
            yF.append(tauxBonF[i][j])
            yQ.append(tauxBonQ[i][j])
        list1.append((yF,yQ))
       
    for i in range(len(list1)):
        plt.clf()
        plt.plot(exemple,list1[i][1],marker='o',label="QuickFill",c='r',lw=1)
        plt.plot(exemple,list1[i][0],marker='o',label="FlashFill",c='b',lw=1)
        plt.ylim(0.0,105.0)
        #plt.xlim(0.5,4)
        plt.title('Statistiques de B'+str(i+1))
        plt.xlabel("Nombre d'exemples")
        plt.ylabel('Taux de bons programmes dans B'+str(i+1))    
        plt.grid(linewidth=0.2)
        plt.legend()
        plt.savefig('b'+str(i+1))


    list1 = []
    for j in range(len(BQ[0])):

        yF = [] ; yQ = []

        for i in range(4):
            yF.append(tauxBonF[i][j])
            yQ.append(tauxBonQ[i][j])

        list1.append((yF,yQ))
       
    for i in range(len(list1)):
        if i == 0 :
            plt.clf()
            plt.plot(exemple,list1[i][1],marker='o',label="QuickFill",c='r',lw=1)
            plt.plot(exemple,list1[i][0],marker='o',label="FlashFill",c='b',lw=1)           
        else:
            plt.plot(exemple,list1[i][1],marker='o',c='r',lw=1)
            plt.plot(exemple,list1[i][0],marker='o',c='b',lw=1)
            
    plt.title('Statistiques de tous les benchmarks')
    plt.xlabel("Nombre d'exemples")
    #plt.xscale('linear')
    plt.ylabel('Benchmarks')    
    plt.grid(linewidth=0.2)
    plt.legend()
    plt.savefig('benchmarks.svg')   


def graph2(BQ,PQ,PF,BonPF,BonPQ):
    
    for i in range(len(PQ[0])):

        if i == 2 or i==5:

            Test1 = [PQ[0][i],PQ[1][i],PQ[2][i],PQ[3][i]]
            Test2 = [BonPQ[0][i],BonPQ[1][i],BonPQ[2][i],BonPQ[3][i]]

            Test3 = [PF[0][i],PF[1][i],PF[2][i],PF[3][i]]
            Test4 = [BonPF[0][i],BonPF[1][i],BonPF[2][i],BonPF[3][i]]

            """ print(Test1 , "\n" , Test2 , "\n\n")
            print(Test3 , "\n" , Test3 , "\n\n") """

            pos_mut_pcts = np.array(Test1)
            pos_cna_pcts = np.array(Test2)

            neg_mut_pcts = np.array(Test3)
            neg_cna_pcts = np.array(Test4)
            genes = ['1', '2', '3', '4']

            with sns.axes_style("white"):
                sns.set_style("ticks")
                sns.set_context("talk")
                
                # plot details
                bar_width = 0.25
                epsilon = .015
                line_width = 1
                opacity = 0.7
                pos_bar_positions = np.arange(len(pos_mut_pcts))
                neg_bar_positions = pos_bar_positions + bar_width

                # make bar plots
                hpv_pos_mut_bar = plt.bar(pos_bar_positions, pos_mut_pcts, bar_width,
                                          color='#000000',
                                          label='QW')

                hpv_pos_cna_bar = plt.bar(pos_bar_positions, pos_cna_pcts, bar_width,
                                          color='#ED0020',
                                          linewidth=line_width,
                                          label='QC')




                hpv_neg_mut_bar = plt.bar(neg_bar_positions, neg_mut_pcts, bar_width,
                                          color='#000000',
                                          label='FW')
                hpv_neg_cna_bar = plt.bar(neg_bar_positions, neg_cna_pcts, bar_width,
                                          color="#0000DD",
                                          linewidth=line_width,
                                          label='FC')


                plt.xticks(neg_bar_positions, genes, rotation=45)
                plt.ylabel('Nombre de Programmes')
                plt.legend(loc='best')
                plt.yscale('log')
                sns.despine()
                plt.legend(bbox_to_anchor=(1.1, 1.05))  
                sns.despine()  
                plt.savefig("b"+str(i+1)+"x")
                exit()




def graph3(BQ,tauxBonF,tauxBonQ):
    x = BQ[0];x1 = []; x2 = []; x4 = [];Labels = []
    y1 = tauxBonQ[0]
    y2 = tauxBonQ[1]
    y3 = tauxBonQ[2]
    y4 = tauxBonQ[3]

    for i in range(16):
            x1.append(x[i]-0.2)
            x2.append(x[i]+0.2)
            x4.append(x[i]+0.4)
    #print(len(y1),len(y2),len(y3),len(y4),len(x1),len(x2),len(x4))
    
    plt.bar(x1[0:8],y1[0:8],color = 'red',width = 0.3)
    plt.bar(x2[0:8],y2[0:8],color = 'red',width = 0.3)
    plt.bar(x[0:8],y3[0:8],color = 'red',width = 0.3)
    plt.bar(x4[0:8],y4[0:8],color = 'red',width = 0.3) 

    for i in range(len(x)):
        Labels.append('B'+str(i+1))

    plt.xticks(x[0:8], Labels[0:8])
    plt.title('QuickFill : B1 - B8')
    plt.xlabel("Nombre d'exemples")
    plt.ylabel('Taux de bons programmes')    
    plt.grid(linewidth=0.2)
    plt.legend()    
    plt.savefig('bqRed1')


    plt.bar(x1[8:],y1[8:],color = 'red',width = 0.3)
    plt.bar(x2[8:],y2[8:],color = 'red',width = 0.3)
    plt.bar(x[8:],y3[8:],color = 'red',width = 0.3)
    plt.bar(x4[8:],y4[8:],color = 'red',width = 0.3) 

    plt.xticks(x[8:], Labels[8:])
    plt.title('QuickFill : B8...')
    plt.xlabel("Nombre d'exemples")
    plt.ylabel('Taux de bons programmes')    
    plt.grid(linewidth=0.2)
    plt.legend()    
    plt.savefig('bqRed2')


    x = BQ[0];x1 = []; x2 = []; x4 = [];Labels = []
    y1 = tauxBonF[0]
    y2 = tauxBonF[1]
    y3 = tauxBonF[2]
    y4 = tauxBonF[3]

    for i in range(16):
            x1.append(x[i]-0.2)
            x2.append(x[i]+0.2)
            x4.append(x[i]+0.4)
    #print(len(y1),len(y2),len(y3),len(y4),len(x1),len(x2),len(x4))
    plt.clf()
    plt.bar(x1[0:8],y1[0:8],color = 'blue',width = 0.3)
    plt.bar(x2[0:8],y2[0:8],color = 'blue',width = 0.3)
    plt.bar(x[0:8],y3[0:8],color = 'blue',width = 0.3)
    plt.bar(x4[0:8],y4[0:8],color = 'blue',width = 0.3) 

    for i in range(len(x)):
        Labels.append('B'+str(i+1))

    plt.xticks(x[0:8], Labels[0:8])
    plt.title('FlashFill : B1 - B8')
    plt.xlabel("Nombre d'exemples")
    plt.ylabel('Taux de bons programmes')    
    plt.grid(linewidth=0.2)
    plt.legend()    
    plt.savefig('bfRed1')

    plt.clf()
    plt.bar(x1[8:],y1[8:],color = 'blue',width = 0.3)
    plt.bar(x2[8:],y2[8:],color = 'blue',width = 0.3)
    plt.bar(x[8:],y3[8:],color = 'blue',width = 0.3)
    plt.bar(x4[8:],y4[8:],color = 'blue',width = 0.3) 

    plt.xticks(x[8:], Labels[8:])
    plt.title('FlashFill :B8...')
    plt.xlabel("Nombre d'exemples")
    plt.ylabel('Taux de bons programmes')    
    plt.grid(linewidth=0.2)
    plt.legend()    
    plt.savefig('bfRed2')




    """ exemple = [1,2,3,4]
    list1 = []
    list2 = []
    

    for j in range(len(BQ[0])):


        yF = [] ; yQ = []
        yF.append('B'+str(j+1))
        yQ.append('B'+str(j+1))
        for i in range(4):
            yF.append(tauxBonF[i][j])
            yQ.append(tauxBonQ[i][j])
        list1.append(yF)
        list2.append(yQ) """
          
    # create data
"""     df1 = pd.DataFrame(list1[0:8],
                    columns=['Benchmarks', '1', '2', '3', '4'])
    
    df2 = pd.DataFrame(list1[8:],
                    columns=['Benchmarks', '1', '2', '3', '4'])
    

    df3 = pd.DataFrame(list2[0:8],
                    columns=['Benchmarks', '1', '2', '3', '4'])
    
    df4 = pd.DataFrame(list2[8:],
                    columns=['Benchmarks', '1', '2', '3', '4'])
    
    
   
    df1.plot(x='Benchmarks',
            kind='bar',
            stacked=False,
            title='FlasFill : B1 - B8')
     
    plt.savefig('b1F')

    df2.plot(x='Benchmarks',
            kind='bar',
            stacked=False,
            title='FlasFill : B8..')
    plt.savefig('b2F')

    df3.plot(x='Benchmarks',
            kind='bar',
            stacked=False,
            title='QuickFill : B1 - B8')
    plt.savefig('b1Q')

    df4.plot(x='Benchmarks',
            kind='bar',
            stacked=False,
            title='QuickFill : B8..')
    plt.savefig('b2Q') """




def graph4(BQ,tauxBonF,tauxBonQ):
    exemple = [1,2,3,4]
    exemple1 = []
    exemple2 = []
    
       
    for j in range(len(BQ[0])):


        yF = [] ; yQ = []; exemple1 = [];exemple2 = []
       

        for i in range(len(exemple)):
            yF.append(tauxBonF[i][j])
            yQ.append(tauxBonQ[i][j])
        #list1.append(yF)
        #list2.append(yQ)
        #print(yF,yQ)
        for i in range(4):
            exemple1.append(exemple[i]-0.2)
            exemple2.append(exemple[i]+0.1)
        
        #print(len(exemple1),len(exemple2),len(yQ),len(yF))
        
        plt.clf()
        plt.bar(exemple1,yQ,color = 'red',width = 0.3,label='Q')
        plt.bar(exemple2, yF,color = 'blue',width = 0.3,label ='F')
        plt.title('Statistiques de B'+str(j+1))
        plt.xlabel("Nombre d'exemples")
        plt.ylabel('Taux de bons programmes dans B'+str(j+1))    
        plt.grid(linewidth=0.2)
        plt.legend()
        plt.savefig('ba'+str(j+1))

    

""" def graph2(BQ,PQ,PF,BonPF,BonPQ):
    x = []
    exemple = [1,2,3,4]
    #width = 0.40

    for i in range(len(BQ[0])):
        x.append('B'+str(i+1))


    for j in range(len(BQ[0])):    
        yF = [] ; yQ = []; yFF = []; yQQ = []
        for i in range(4):
            yF.append(BonPF[i][j])
            yQ.append(BonPQ[i][j])
            yFF.append(PF[i][j])
            yQQ.append(PQ[i][j])

        #list1.append((yF,yQ))
    plt.bar(exemple, yF, color='b',width = 0.2)
    plt.bar(exemple, yFF, bottom=yF, color='k',width = 0.2)
    plt.bar(exemple, yQ, color='r',width = 0.2)
    plt.bar(exemple, yQQ, bottom=yQ, color='k',width = 0.2)
    plt.show()
    exit()

 
    plt.bar(exemple-0.2, yF, color='b',width = 0.2)
    plt.bar(exemple+0.2, yFF, bottom=yF, color='k',width = 0.2)
    plt.bar(exemple-0.2, yQ, color='r',width = 0.2)
    plt.bar(exemple+0.2, yQQ, bottom=yQ, color='k',width = 0.2)


    
   
   plt.bar(x-0.2, y1, width)
    plt.bar(x+0.2, y2, width) 


 """




def graph5(BQ,PQ,PF,BonPF,BonPQ):
    
    x = BQ[0]
    for j in range(4):
        x1 = []; x2 = []; x4 = [];Labels = []
        y1 = []; y2 = []; y3 = []; y4 = []
        y1 = BonPQ[j]
        y2 = PQ[j]
        y3 = BonPF[j]
        y4 = PF[j]

        
        for i in range(16):
                x1.append(x[i]-0.4)
                x2.append(x[i]-0.2)
                x4.append(x[i]+0.2)
        
        
        for i in range(len(x)):
            Labels.append('B'+str(i+1))

        # des Benchmarks 1 -8
        plt.clf()
        plt.bar(x1[0:8],y1[0:8],color = 'red',width = 0.2,label = 'QC')
        plt.bar(x2[0:8],y2[0:8],color = 'green',width = 0.2,label = 'QT')
        plt.bar(x[0:8],y3[0:8],color = 'blue',width = 0.2,label = 'FC')
        plt.bar(x4[0:8],y4[0:8],color = 'black',width = 0.2,label = 'FT')    

        plt.xticks(x[0:8], Labels[0:8])
        plt.title('Nombre de programmes de FlashFill et QuickFill sur' +str(j+1)+ 'exemple (s)')
        plt.xlabel("Benchmarks")
        plt.ylabel('Nombre de Programmes')  
        plt.yscale('log')  
        plt.grid(linewidth=0.2)
        plt.legend()    
        plt.savefig('groupx'+str(j+1))

        # des Benchmarks 9 - 12.   
        plt.clf()    
        plt.bar(x1[8:],y1[8:],color = 'red',width = 0.2,label = 'QC')
        plt.bar(x2[8:],y2[8:],color = 'green',width = 0.2,label = 'QT')
        plt.bar(x[8:],y3[8:],color = 'blue',width = 0.2,label = 'FC')
        plt.bar(x4[8:],y4[8:],color = 'black',width = 0.2,label = 'FT') 

        plt.xticks(x[8:], Labels[8:])
        plt.title('Nombre de programmes de FlashFill et QuickFill sur' +str(j+1)+ 'exemple (s)')
        plt.xlabel("Benchmarks")
        plt.ylabel('Nombre de Programmes')  
        plt.yscale('log')  
        plt.grid(linewidth=0.2)
        plt.legend()    
        plt.savefig('groupy'+str(j+1))




def MakeGrid():

    list1 = []; list2 = []; list3 = []; list4 = []; list5=[]
    for i in range(1,17):
        b = Image.open("b"+str(i)+".svg")
        list1.append(b)
        c = Image.open("ba"+str(i)+".svg")
        list2.append(c)
        d = Image.open("b"+str(i)+"x.svg")
        list3.append(d)
    

    for i in range(1,3):
        e = Image.open("b"+str(i)+"F.svg")
        list4.append(e)
        e = Image.open("bfRed"+str(i)+".svg")
        list4.append(e)

        e1 = Image.open("b"+str(i)+"Q.svg")
        list5.append(e1)
        e1 = Image.open("bqRed"+str(i)+".svg")
        list5.append(e1)

    # mettons en place notre grid d'image
    """ fig = plt.figure(figsize=(20.,20.))
    grid = ImageGrid(fig, 111,
                    nrows_ncols=(2,3),
                    axes_pad = 0.2,)

    for ax, im in zip(grid, list1[0:6]):
    
        ax.imshow(im)
    plt.savefig('linegrid1.svg')



    fig = plt.figure(figsize=(20.,20.))
    grid = ImageGrid(fig, 111,
                    nrows_ncols=(2,3),
                    axes_pad = 0.2,)

    for ax, im in zip(grid, list1[6:12]):       
        
        ax.imshow(im)
    plt.savefig('linegrid2.svg')

    fig = plt.figure(figsize=(20.,20.))
    grid = ImageGrid(fig, 111,
                    nrows_ncols=(2,2),
                    axes_pad = 0.2,)

    for ax, im in zip(grid, list1[12:]):       
        
        ax.imshow(im)
    plt.savefig('linegrid3.svg')
 """


    """ fig = plt.figure(figsize=(20.,20.))
    grid = ImageGrid(fig, 111,
                    nrows_ncols=(2,3),
                    axes_pad = 0.2,)

    for ax, im in zip(grid, list2[0:6]):
    
        ax.imshow(im)
    plt.savefig('bargrid1.svg')



    fig = plt.figure(figsize=(20.,20.))
    grid = ImageGrid(fig, 111,
                    nrows_ncols=(2,3),
                    axes_pad = 0.2,)

    for ax, im in zip(grid, list2[6:12]):       
        
        ax.imshow(im)
    plt.savefig('bargrid2.svg')

    fig = plt.figure(figsize=(20.,20.))
    grid = ImageGrid(fig, 111,
                    nrows_ncols=(2,2),
                    axes_pad = 0.2,)

    for ax, im in zip(grid, list2[12:]):       
        
        ax.imshow(im)
    plt.savefig('bargrid3.svg')
 """

    fig = plt.figure(figsize=(20.,20.))
    grid = ImageGrid(fig, 111,
                    nrows_ncols=(2,3),
                    axes_pad = 0.2,)

    for ax, im in zip(grid, list3[0:6]):
    
        ax.imshow(im)
    plt.savefig('stackgrid1.svg')



    fig = plt.figure(figsize=(20.,20.))
    grid = ImageGrid(fig, 111,
                    nrows_ncols=(2,3),
                    axes_pad = 0.2,)

    for ax, im in zip(grid, list3[6:12]):       
        
        ax.imshow(im)
    plt.savefig('stackgrid2.svg')

    fig = plt.figure(figsize=(20.,20.))
    grid = ImageGrid(fig, 111,
                    nrows_ncols=(2,2),
                    axes_pad = 0.2,)

    for ax, im in zip(grid, list3[12:]):       
        
        ax.imshow(im)
    plt.savefig('stackgrid3.svg') 


    """ fig = plt.figure(figsize=(20.,20.))
    grid = ImageGrid(fig, 111,
                    nrows_ncols=(2,2),
                    axes_pad = 0.2,)

    for ax, im in zip(grid, list4):       
        
        ax.imshow(im)
    plt.savefig('groupgrid1.svg')

    fig = plt.figure(figsize=(20.,20.))
    grid = ImageGrid(fig, 111,
                    nrows_ncols=(2,2),
                    axes_pad = 0.2,)

    for ax, im in zip(grid, list5):       
        
        ax.imshow(im)
    plt.savefig('groupgrid2.svg')"""






def MakeFinalGrid():

    list1 = []; list2 = []; list3 = []
    for i in range(1,17):
        b = Image.open("b"+str(i)+".png")
        list1.append(b)
        

    for i in range(1,5):
        c = Image.open("groupx"+str(i)+".png")
        list2.append(c)
        
        d = Image.open("groupy"+str(i)+".png")
        list3.append(d)
    
    for i in range(len(list2)):
        plt.clf()
        fig = plt.figure(figsize=(20.,20.))
        grid = ImageGrid(fig, 111,
                        nrows_ncols=(1,2),
                        axes_pad = 0.2,
                        label_mode='1',)

        for ax, im in zip(grid, [list2[i],list3[i]]):
        
            ax.imshow(im)
        plt.savefig('grid'+str(i+1)+'.svg')
        plt.show()
          
    plt.clf()
    fig = plt.figure(figsize=(20.,20.))
    grid = ImageGrid(fig, 111,
                    nrows_ncols=(2,2),
                    axes_pad = 0.2,
                    label_mode='1',)

    for ax, im in zip(grid, list1[0:4]):    
        ax.imshow(im)
    plt.savefig('group1.svg')
    plt.show()
   
    plt.clf()
    fig = plt.figure(figsize=(20.,20.))
    grid = ImageGrid(fig, 111,
                    nrows_ncols=(2,2),
                    axes_pad = 0.2,
                    label_mode='1',)

    for ax, im in zip(grid, list1[4:8]):              
        ax.imshow(im)
    plt.savefig('group2.svg')
    plt.show()

    plt.clf()
    fig = plt.figure(figsize=(20.,20.))
    grid = ImageGrid(fig, 111,
                    nrows_ncols=(2,2),
                    axes_pad = 0.2,
                    label_mode='1',)

    for ax, im in zip(grid, list1[8:12]):              
        ax.imshow(im)
    plt.savefig('group3.svg')
    plt.show()


    plt.clf()
    fig = plt.figure(figsize=(20.,20.))
    grid = ImageGrid(fig, 111,
                    nrows_ncols=(2,2),
                    axes_pad = 0.2,
                    label_mode='1',)

    for ax, im in zip(grid, list1[12:]):              
        ax.imshow(im)
    plt.savefig('group4.svg')
    plt.show()






def main ():

    arg = sys.argv 
    if len(arg)>1:

        if arg[1] == 'F':

            BF,PF,BonPF,tauxBonF = FlashFillInformation()
            """ for i in range(4):

                #print(len(BF[i]),len(PF[i]),len(BonPF[i]),len(tauxBonF[i]))
                print(BF[i],"******************\n",PF[i],"******************\n",BonPF[i],"******************\n",tauxBonF[i])
 """
        elif arg[1]=='Q':
            BQ,PQ,BonPQ,tauxBonQ = QuickFillInformation()

            """ for i in range(4):
                print(BQ[i],"******************\n",PQ[i],"******************\n",BonPQ[i],"******************\n",tauxBonQ[i])
                #print(len(BQ[i]),len(PQ[i]),len(BonPQ[i]),len(tauxBonQ[i]))
 """
    
    #GraphProduction(Benchmarks,Programs,BonP,tauxBon)
    if arg[1] =='D':

        BQ,PQ,BonPQ,tauxBonQ = QuickFillInformation()
        BF,PF,BonPF,tauxBonF = FlashFillInformation()
        grap1(BQ,tauxBonF,tauxBonQ)
        #graph2(BQ,PQ,PF,BonPF,BonPQ)
        #graph3(BQ,tauxBonF,tauxBonQ)
        #graph4(BQ,tauxBonF,tauxBonQ)
        #graph5(BQ,PQ,PF,BonPF,BonPQ)
        #MakeGrid()
        #MakeFinalGrid()
   



if __name__ == "__main__":
    main()

