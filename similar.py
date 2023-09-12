# Import necessary modules
import pandas as pd
import math
import sys
import numpy as np
from scipy.spatial import distance
import pickle
from sklearn import preprocessing


def find_top_similar_entitties(max, nba, distance_frame, primary_column, sec_col):
    
    similar_list = []

    for i in range(max):
    
        current_farthest = distance_frame.iloc[i]["idx"]
        close_to_the_top_founder = nba.loc[int(current_farthest)][primary_column]
        mail = nba.loc[int(current_farthest)][sec_col]

        current_distance = distance_frame.iloc[i]["dist"]
        percentile = 100 - (100 / 18.9714833602) * current_distance
        
        current_distance = round(current_distance, 2)
    
        if percentile <0:
            percentile = 0 
            
        percentile = round(percentile, 2)    

        print('similar '+str(i)+' : '+str(close_to_the_top_founder) + ', email : ' +str(mail) + ", Similarity Percentile : "+ (str(percentile)))

        current_user = {
            "Name" : str(close_to_the_top_founder), 
            "Email" : str(mail),
            "Similarity percentile" : percentile
        }

        similar_list.append(current_user)

    return similar_list   

def find_similar_learner(info, columns, primary_column,sec_col):
    
    df = pd.read_csv("learning_partner.csv")

    df.fillna(round(df.mean()), inplace=True)

    df = df.append(info, ignore_index=True)

    selected_student = df[df["name"] == info['name']].iloc[0]

    le = preprocessing.LabelEncoder()
    le.fit(df["gender"])
    df["gender"] = le.transform(df["gender"])
    le.fit(df["language"])
    df["language"] = le.transform(df["language"])
    le.fit(df["interest"])
    df["interest"] = le.transform(df["interest"])
 
    nba_numeric     = df[columns]
    nba_normalized  = (nba_numeric - nba_numeric.mean()) / nba_numeric.std()

    nba_normalized.fillna(round(nba_normalized.mean()), inplace=True)

    top_founder_normalized  = nba_normalized[df[primary_column] == info['name']]
    distances = nba_normalized.apply(lambda row: distance.braycurtis(row, top_founder_normalized.iloc[0]), axis=1)
    distance_frame          = pd.DataFrame(data={"dist": distances, "idx": distances.index})

    distance_frame = pd.DataFrame(data={"dist": distances, "idx": distances.index})
    distance_frame.sort_values(by=["dist"], inplace=True)

    second_smallest     = distance_frame.iloc[1]["idx"]
    most_nearer_entity  = df.loc[int(second_smallest)][primary_column]

    print('Direct similarity : '+most_nearer_entity)

    print('\nTop 4 similar learner Sorted')
    similar_5_list = find_top_similar_entitties(5, df, distance_frame, primary_column, sec_col)

    return similar_5_list

def find_similar_student(info):

    columns = ['age', 'linkedin_act', 'github_act', 'paper_published', 'gender', 'language', 'interest']

    primary_column = "name"
    sec_col = "email"

    return find_similar_learner( info, columns, primary_column,sec_col)

def startpy():

    find_similar_student({id:"1001","name":"Coleen","age":"17","gender":"female","email":"coleen@yahoo.com","language":"english","linkedin_act":"8","github_act":"9","paper_published":"4", "interest":"Machine Learning"})
    
    pickle_out = open("similarity.pkl", "wb")

    pickle.dump(find_similar_student ,pickle_out)

    pickle_out.close()

# if __name__ == '__main__':
#     startpy()