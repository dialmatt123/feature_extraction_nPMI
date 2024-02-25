import pandas as pd
import numpy as np

# import data
df = pd.read_csv([INSERT DIRECTORY OF DATA FILE], delimiter = ',', index_col=0)

# convert dialect classification column as list
# users have to refer to the name(s) of the dialect group column in their data
classification = input('Enter classification:')
g = df[str(classification)].values.tolist()

# calculation of PMI for all features
###### need to set the number of classification columns in the data ######
class_col = 1

# the empty lists below are created to store outputs in the PMI fuction
var_list = []
grp_list = []
PMI_list = []
nPMI_list = []
prop_list = []
excl_list = []
feat_list = []

# PMI function
def PMI(feat, group):
    # sum of feature tokens for probability calculation
    feat_tokens = sum(feat.values())
    # for loop for the dialect groups
    for i in range(len(df_co.columns)):
        # for loop for the variants
        for j in range(len(df_co.index)):
            # occurence of a variance within a dialect group
            xy = int(df_co.iloc[j,i])
            # total occurence of a variant
            x = feat[df_co.index[j]]
            # total number of tokens found in one dialect group
            y = group[df_co.columns[i]]
            # probability calculation
            calc = (xy/feat_tokens)/((x/feat_tokens)*(y/feat_tokens))
            # filter out 0 so that the log function will not return an error
            if calc != 0:
                # add log function to calculate PMI score
                PMI_score = round(np.log2(calc), 3)
                # representativeness of dialects within the group which has the feature; with_feat_in_group/total_in_group
                prop = round(int(df_co.iloc[j,i])/grp[df_co.columns[i]], 3)
                # exclusivity of the feature; no_dialects_with_feature/all_dialects_with_feature_in_data
                excl = round(int(df_co.iloc[j,i])/feat[df_co.index[j]],3)

                # normalised PMI
                nPMI = round(PMI_score/-np.log2((xy/feat_tokens)), 3)
                # append values to the empty lists in order to create df
                var_list.append(df_co.index[j])
                grp_list.append(df_co.columns[i])
                PMI_list.append(PMI_score)
                nPMI_list.append(nPMI)
                prop_list.append(prop)
                excl_list.append(excl)
                feat_list.append(df_co.index.names)
    # create dataframe based on the feature extraction values
    new_df = pd.DataFrame(
        {'Feature':feat_list, 'Variant':var_list, 'Dialect Group':grp_list, 'PMI': PMI_list, 'nPMI': nPMI_list,'Exclusivity': excl_list, 'Representativeness': prop_list})
    return new_df

# for loop to measure PMI for all the variants in the dataset
for i in range(len(df.columns)-class_col):
    # convert feature column to a list
    f = df[df.columns[i]].values.tolist()    
    # zip feature list and group list into a dataframe
    temp_df = pd.DataFrame(zip(f,g))
    # remove all empty row in the pair
    temp_df = temp_df.dropna()    
    # create dictionary for each variant and the number of tokens for the calculation in the PMI function (see Line 26)
    feat = pd.Series(temp_df[0]).value_counts().to_dict()
    # create dictionary for each dialect group and the number of tokens for the calculation in the PMI function (see Line 44)
    grp = pd.Series(temp_df[1]).value_counts().to_dict()
    # create co-occurence matrix for the for loop in the PMI calculation (provides numbers for the probability calculation)
    df_co = pd.crosstab(df[df.columns[i]], df[str(classification)])
    # export results to a .csv file
    PMI(feat, grp).to_csv([INSERT DIRECTORY HERE] + '_' + str(classification) + '.csv')
print('file exported')