from building_profiles import *

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print_profile(user_profile)

user_profile2 = build_profile('trish', 'roush', age=54, job='java software engineer',
                                                location='aurora')
print_profile(user_profile2)
