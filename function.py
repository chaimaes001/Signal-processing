# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 08:01:52 2021
@author: Chaimae
""" 
import numpy as np
from python_speech_features import mfcc
import scipy.io.wavfile as wav
from dtw import dtw

# cette fonction permet de comparer le signal de deux mots 
def detecter_mot(mot, mot1):
   
    #ici la paramétrisation du premier audio/mot 
    (rate, sig) = wav.read("audios/"+mot+".wav")
    mfcc_feat = mfcc(sig, rate)
    #fbank_feat = logfbank(sig,rate)   
    print("longeur du aud1 = "+str(len(sig)))
    
    #ici la paramétrisation du deuxième mot/audio
    (rate1, sig1) = wav.read("audios/"+mot1+".wav")
    mfcc_feat1 = mfcc(sig1, rate1)
    #fbank_feat1 = logfbank(sig1,rate1)   
    print("longeur du aud2 = "+str(len(sig1))) 

    x = np.array(mfcc_feat).reshape(-1, 1)
    w = np.array(mfcc_feat1).reshape(-1, 1)

    #test ici avec la fontion de python
    #d, path = fastdtw(x, w, dist=euclidean)
    #print("la distance de fastdtw est = "+str(d))
    
    #calcul de la dtw avec la fonction implémentée
    d=dtw(x,w)   
    print("la fonction de la dtw donne = "+str(d))
    
    if(d>0):
        resultat="les mots ne sont pas identiques"
    else:
            resultat="Les mots sont identiques"
    print(resultat)
    return resultat

#detecter_mot("Bonjour")





