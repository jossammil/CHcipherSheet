
"""
@author: jossammil
"""

import pandas as pd

#%%

ci_df = pd.DataFrame({'ring':ring_col, 
                      'rotor': rotors_month,
                      'pluglist': pluglist_month,
                      'kengruppen': msg_col
                      })

#%%

# Clean up the list brackets in the df

ci_df['ring'] = [','.join(map(str, l)) for l in newpd['ring']]

ci_df['rotor'] = ci_df['rotor'].apply(', '.join)

# This took a few hours; calls the original pluglist list
ci_df['pluglist'] = [["".join(str(i) for i in sublist) for sublist in x] for x in pluglist_month]

ci_df['kengruppen'] = [["".join(str(i) for i in sublist) for sublist in x] for x in msg_col]


# Still need to futher clean brackets
# Clean some names up -- convert to German
