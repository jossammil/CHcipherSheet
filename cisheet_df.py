
"""
@author: jossammil
"""

import pandas as pd

#%%

# old way
#ci_df = pd.DataFrame({'datum':day_numbers,
#                     'ring':ring_col, 
#                     'rotor': rotors_month,
#                     'pluglist': pluglist_month,
#                     'kengruppen': msg_col
#                     })


ci_df = pd.DataFrame()

#%%

ci_df['datum'] = day_numbers

#%%

# Clean up the list brackets in the df

ci_df['rotor'] = ['  '.join(str(i) for i in sublist) for sublist in rotors_month]

ci_df['ring'] = ['  '.join(map("{:02d}".format, l)) for l in ring_col]

# Can use two variations of formatting to add leading zeroes
# print("{:02d}".format(1))
# print(f"{1:02d}")

# Variation without the leading zero for 1-9
# ['  '.join(map(str, l)) for l in ring_col]
# ci_df['ring'] = ['  '.join(map(str, l)) for l in ci_df['ring']]

#ci_df['rotor'] = ci_df['rotor'].apply(', '.join)




# This took a few hours; calls the original pluglist list

pluglist_month_A = [["".join(str(i) for i in sublist) for sublist in x] for x in pluglist_month]
ci_df['pluglist'] = ['  '.join(str(i) for i in sublist) for sublist in pluglist_month_A]

# OR the DF variation
# ci_df['pluglist'] = [["".join(str(i) for i in sublist) for sublist in x] for x in pluglist_month]
# ci_df['pluglist'] = ci_df['pluglist'].apply(', '.join)


msg_col_A = [["".join(str(i) for i in sublist) for sublist in x] for x in msg_col]
ci_df['kengruppen'] = ['  '.join(str(i) for i in sublist) for sublist in msg_col_A]

# ci_df['kengruppen'] = [["".join(str(i) for i in sublist) for sublist in x] for x in msg_col]
# ci_df['kengruppen'] = ci_df['kengruppen'].apply(', '.join)

# Still need to futher clean brackets
# Clean some names up -- convert to German

#%%

# check the df 
ci_df

