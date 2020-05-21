# This program seeks to find tweets which followers of a US House close election candidate have liked.
# It access the Twitter API using developer account keys. It then retrieves the most recent ~3240 tweets
# each follower has liked, and outputs the relevant tweet info as csv files.

from twython import Twython, TwythonError, TwythonRateLimitError, TwythonAuthError
import time
import datetime
import csv
import pandas as pd

RUN_TIME = 20
f = open("temp_update_index.txt", "r", encoding="utf8")
UPDATE_INDEX = int(f.readline())
f.close()
print(UPDATE_INDEX)

########################################################################################################################
### authorization2
APP_KEY = 'c2LQcGYB66Feu590wUxAxrbL0'
APP_SECRET = '8WJR22nTiTg5pzeBL2Q4tYIfNYmRBrcvvwhgd8p20fTJIZL0eP'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter2 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth2')

##authorization3
APP_KEY = 'lBgHp63nvSlUPk3SsFoi8D0al'
APP_SECRET = 's9lCnx2DGTHbwx8XIrcfxMLqZ2vZzz5WCBSF421tENGLxD2WJF'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter3 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth3')

##authorization4
APP_KEY = 'JWeTJbVDxIamwQNdTxY1Nz4DQ'
APP_SECRET = '6m30BpLBPlOhD5Ua4uB3sE8tzhllz0yuRltcOmo3QKINW1SkDU'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter4 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth4')

##authorization5
APP_KEY = 'BlXaTQNkQNz2weGIbPdiMMSVm'
APP_SECRET = 'v1nvylcoCPrqrGuYKOjNFKmcqyN0Mat3ojXYIEtackdAOViWfq'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter5 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth5')

##authorization6
APP_KEY = '8JsLqAnTEUuAGBHmAV1r65gGU'
APP_SECRET = 'N7LF2BsrLVBUUx9ahE8bgl9WWZSGdMhL7QuhMYWn4zreISyS1p'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter6 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth6')

##authorization7
APP_KEY = 'PMOXgvUYsrS83XmDxQiE9rRFJ'
APP_SECRET = 'Je2MiZptYdnrd7Yph0c0Jlp1V1z5butnPVav3E1T1y9TdCzHkb'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter7 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth7')

##authorization8
APP_KEY = 'PgXPJZZ5lOQz9aC8LmPEypfph'
APP_SECRET = 'u59kvyX7B3KWq6dQW5FYdkKDK2V78Y9xGAvTNJ5fMpsC9cvaJA'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter8 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth8')

##authorization9
APP_KEY = 'xkUIcAnAGIpnnhKFQnBsukk1S'
APP_SECRET = '6jGmIZLrvpv15O73SkFO6ttFiUaxm4TkFobySEagSaDiMDN6mr'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter9 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth9')

##authorization10
APP_KEY = 'EFmr94FEm6MmX8v7Xue61ey6E'
APP_SECRET = '2fktIIbUWIjWfIJXOdhTI0QHiwtQrbp2qsKJpT2n0smiBICU47'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter10 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth10')

##authorization11
APP_KEY = 'UQC14Mp29D7VzJJWWUN4offGo'
APP_SECRET = 'ApKuk7YUyDGCL9ghGDY1FOepnR5iT5gxkBeat7mdJ4S0Xxq1MP'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter11 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth11')

##authorization12
APP_KEY = 'tmlxBgTTVHa07XeXg8PMmVWrP'
APP_SECRET = 'NY26PlLuISb4achzmn8qCSOA3bm3rr2uW5jzKxCSxhPZsxDii2'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter12 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth12')

##authorization13
APP_KEY = '2Z3xZl1H83L9nT1yybqqzMhY7'
APP_SECRET = 'mqABheyXrsmrpApC8EsGh1pnEYqUPAAjWA91hCblfOZs1S8ZSb'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter13 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth13')

##authorization14
APP_KEY = 'Gxoh2QPHuaENwMzq9YUnq351x'
APP_SECRET = '9MpKVZsj7gMXs7HkJMIaopE72hLLFFFwpxn2huMtrnsuVQsTlJ'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter14 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth14')

##authorization15
APP_KEY = 'a26lpyhRo74xOxYkdl4B243xO'
APP_SECRET = 'ypE5XuAvNy0s7dQPwI6cFDyPCHmZWTGPLIvf11v3kxFzsCDmtK'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter15 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth15')

##authorization16
APP_KEY = '8SEnhpDsGo7Wc5ynH6l17H9VJ'
APP_SECRET = 'HJGBNhvJOF7kCQwoAxcTexcrN6tL3YJvyG0XWQwh8jCgiUw5VU'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter16 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth16')

##authorization17
APP_KEY = '4Gy5DWtScbWdvqlOcSRS2zdED'
APP_SECRET = 'DmwTv0SdXQtZM6quAOGLdmrNjnGYGOz5F3YJ2KGHX5vW8M6DyE'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter17 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth17')

##authorization18
APP_KEY = 'nsGZ3riSYy2zYKfJiAWaT5xo0'
APP_SECRET = 'v9038Yl4gT5kiEsgeTu4veWkepPYuOQ9wxalgnuTBUpvqXrsWn'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter18 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth18')

##authorization19
APP_KEY = 'm2lK8hGApf7O5N4JKmwIKKKHb'
APP_SECRET = 'sJoXjgfT9sbegRW7AzvyxP8NrtuxB5oQ1AY81VrWcl61w50zOy'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter19 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth19')

##authorization20
APP_KEY = 'Rv3tLpLVbE3hkeOETzPokG6e1'
APP_SECRET = 'j4PI8lhEB5G9wCyve7q9IFPD3cyXZoeQLBFPCW2FKElt9jr0ZC'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter20 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth20')

##authorization21
APP_KEY = 'uovyeUGTa2S00G90NahiqbbrP'
APP_SECRET = 'LNlQCE7InbxYSnESnGichC5p0tShf4sfxl4kxZt7ORDgnEKoWm'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter21 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth21')

##authorization22
APP_KEY = 'psIcgiSq853LRIvqKJ8stSYiv'
APP_SECRET = 'eTRC8WKxiksjZXgXXY6LuokgX8JNQwGhrMIP47ms4VNLBPeTDL'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter22 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth22')

##authorization23
APP_KEY = 'aNEwfpqmVybZon13hMuQFgywa'
APP_SECRET = '4O1SgExfu85Bv7CwktKhpbYTCypRist3kLM5P0wbWiZkzdrOB9'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter23 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth23')

##authorization24
APP_KEY = 'spottsxbih6VeQYPCIAFpdVIE'
APP_SECRET = 'wr6u7xKd4lIgTa2MK3HszbkcmwIIvLnnZ9Ox4M6zwx1bYvSVqh'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter24 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth24')

##authorization25
APP_KEY = 'qSUTKcAGrA2EkSPlZ8imjofKC'
APP_SECRET = 'qKGU3qBrBsqtcCpaxQiz9LQk6j6woF61scxRduDTrShpLT0axy'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter25 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth25')

##authorization26
APP_KEY = 'U97N7ioHYmoFuM6fYrfCss21q'
APP_SECRET = 'h98alHRNtTfs8tdWHTryXgoqhNsy1N3Ca8IQNshRWnCN0KXY2j'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter26 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth26')

##authorization27
APP_KEY = 'nR3S9uVnKmUKdrJJudjeTgPYF'
APP_SECRET = 'EuZPdFq9RgmS8tADhBOBIdkBFpbitF4tBHkMnQrUUJQPYuAvZb'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter27 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth27')

##authorization28
APP_KEY = 'LoqSBbIkINoihASGwRjP6QyeG'
APP_SECRET = '0Y6jXgbwFvzs3P7pFL79cVkzyUr5fZu0uEyHNOJsQd9g2ea418'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter28 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth28')

##authorization29
APP_KEY = 'LSHpXiyGdXugNp8DBTBaso4ur'
APP_SECRET = 'mZ85f1bkVUBoxTdqlQ4w07PvlXdHAp6OsmobH22BT7UwGgZnSi'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter29 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth29')

##authorization30
APP_KEY = '2mpyCgnn7hq9dV1cjjFgFRMBp'
APP_SECRET = 'j5iVAaAT7oUQCKlaAmi8GWyccVTUbWxjLisQAeW7Bf6bphH960'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter30 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth30')

##authorization31
APP_KEY = 'BrXYZrrR1BB613OZ22dnZqDCx'
APP_SECRET = '5O2mJaZ9K86CTuSRH1vgORax63jI3tR333cs7sGTIpaZlLXmEj'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter31 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth31')

##authorization32
APP_KEY = '4zkNMlAEvidYIJlbTRfPsUejd'
APP_SECRET = 'zoEHtpF7ZvscHFnVug3bnqDKBDZczUMmLGcaWEAbblVPCq4Tmf'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter32 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth32')

##authorization33
APP_KEY = '8tYBID9JXyZ1TDqG8yiRdQLdm'
APP_SECRET = 'ogXPEfiJR3KTP5qNBCXxlQSALxHVcsbCccxEnUFLkgd1wIy0v1'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter33 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth33')

##authorization34
APP_KEY = 'TzFIsTcBtlU7q5lQxBqpPKVz5'
APP_SECRET = 'Iehv1ibtkOLEBwraZdn8Pc1tFJNqUJC7GK5C7Qf2uAacuqR5u5'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter34 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth34')

##authorization35
APP_KEY = 'BDLWaEm9RvBFLueri3aNLMUla'
APP_SECRET = 'qXrvYk91POgjtGNLTzh1DLmbremicndhYsQLxoBcgeMHer98OJ'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter35 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth35')

##authorization36
APP_KEY = 'otYMFL7XN5DrerUrZtzWszqWL'
APP_SECRET = 'LWiP4UnhjOp5CqCcpQtOZWTBCvyHUMkWWiyqVinNSMYGcife9j'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter36 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth36')

##authorization37
APP_KEY = 'oUCT3ApfMFcFCuhSPotZ6biO3'
APP_SECRET = 'PMwKbHG77mLEdqRXcNMvuUbNvaJX9VzCDTDiN9V2tDzUvXk3sD'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter37 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth37')

##authorization38
APP_KEY = 'esGP13v0iqeXOTX71vnujzoQn'
APP_SECRET = 'E5aTjWD0XIw3cuI6JphApbOy9oYeFMmIIK5AewFbYrmRkg1S4x'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter38 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth38')

##authorization39
APP_KEY = 'db0HZGXpaZNfLttDrQLt1GYgk'
APP_SECRET = 'SOJfbioQ1eMokaDJxsJLYTNpazNhjHL6eNmL1sfDKc7iuZReFZ'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter39 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth39')

##authorization40
APP_KEY = 'ZOwq0ko3whuHzgks7BH9Uy9AT'
APP_SECRET = 'rmrTTPkQ2mC0znef4u7Vf4kY0ro3gushOYfD0BkudFP94QK3Ot'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter40 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth40')

##authorization41
APP_KEY = 'y29DH2JhdQ8yaZPE95YGi0IEH'
APP_SECRET = '2MZ4mCQdveRc55aS6wRQPUV6CtQoNhnhRcMqLNk08Tl2FWzvNZ'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter41 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth41')

##authorization42
APP_KEY = 'XKhrOT4B2csS9HCYLA5hS9k3l'
APP_SECRET = 'fghCEbFDSkKRckZ9hqmK2geIlmBxxtFcm8XGXVNUrHt3bvHpi3'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter42 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth42')

##authorization43
APP_KEY = 'va62S4EEx1bLAuqYd7XJIaamN'
APP_SECRET = 'f5KuMBaWGs6EDqHKPaMR1HWX038mxaFrhJMjU6HhwEhwGcKzZv'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter43 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth43')

##authorization44
APP_KEY = 'QqXoWtuMxRTBEywCeog1856OL'
APP_SECRET = 'oqZFM8vucpIOmfP87Ceq01Cp1x2x1oF6fVRrjWWAXZtSCQ23Tb'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter44 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth44')

##authorization45
APP_KEY = 'iNlFFKtIMfOrZIG98mvgAkJva'
APP_SECRET = 'h0nbuCRbtLSOIoFnItHSR7cVzCsE0jrIm7jctOOlwP5ZuKzQaa'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter45 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth45')

##authorization46
APP_KEY = 'lA3GHp3LjnnVFUuWzZVgxB6Fe'
APP_SECRET = '8T5VaUfH10QJ3fptY0TeXaVYnPxKv4nYYt4DLY93RoEapVOOWR'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter46 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth46')

##authorization47
APP_KEY = '0WCaA4upaDJ2JncX9UHFgKmzn'
APP_SECRET = 'qjLMg0TMvwwszdkwBwsCKWJmhkT7p8RmHRVDKfeTTP8NfBnJwA'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter47 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth47')

##authorization48
APP_KEY = 'zaO9H8fTQVfqWNbA77Rl9ID2Z'
APP_SECRET = 'kqrY7KN5Y0FTpJ0WAyAuEyMEOUkVB1XdJrUJrGXd4ySMbyZSzM'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter48 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth48')

##authorization49
APP_KEY = '2jI7L63d5vBHkaSgydtxFCDnb'
APP_SECRET = 'RxOXM5176sHmTLyTt4usIlh1hs28MaUJzwCNllKYkiWuCwDTTS'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter49 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth49')

##authorization50
APP_KEY = 'aiAabvtRXgTvvusQJYGTMIqAM'
APP_SECRET = '1hEh5maoTOETzqxVQmvUr8yMEURcXBwD6TrU6oPkGx3GgO2jAb'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter50 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth50')

##authorization51
APP_KEY = 'NsVGNLcDdE80nfI1vskkThhME'
APP_SECRET = 'GcLtOAavR6kB0vxBqJSvkPvOOQnsOOlsZ3qJwRLpdppM8XkCnx'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter51 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth51')

##authorization52
APP_KEY = 'NRYI8OCprJ0NbUmO8g5PNjLmu'
APP_SECRET = 'b2e1PsiOOkQYfIm9C7uFp0uqt59gcJIHbyiw3ATAdjp9XNU9f6'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter52 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth52')

##authorization53
APP_KEY = '2dpOHWcmPSedlgJvO2pZWCQtr'
APP_SECRET = 'rlf8fYbz9vC1GUXgtKoMsgx0LDwxcPlLVIhZKDbqarctSN4VlF'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter53 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth53')

##authorization54
APP_KEY = 'iJJymsY08fn1owjpEkIFfFNfZ'
APP_SECRET = 'kYfvtzTpcMViOKuOmo2BEPzDAoyFqPhUT8uQof9Ksei84P5v8H'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter54 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth54')

##authorization55
APP_KEY = 'ENsSxCvDurgeElhrtEvmhwyaj'
APP_SECRET = '4nIrJl16XE5StbkziWjpd9YxUSHqAUCCF89MDP3uzrS8MUIZqy'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter55 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth55')

##authorization56
APP_KEY = 'AHK3fu8dC1Ieywp3fdtUH1GtM'
APP_SECRET = 'l0pmQJiY8hluc7vgQEpQfRTzsaib8bSbPOiBQ25zHZ1afKGet9'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter56 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth56')

##authorization57
APP_KEY = 'aH4iniiz08jb9Pxk0XU00V4Ci'
APP_SECRET = '6PwYAVFDw39Aw9GyLwilqD6NLCu2qDL8RdKfc79KTaNutsm4ex'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter57 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth57')

##authorization58
APP_KEY = 'wVQ9bmZijcydwGnGc99mU40dv'
APP_SECRET = 'pQ3i5Da5DUlgfqRaTCCG16DTSOjXi5p2W3d9WG4dgreRZYdHYg'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter58 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth58')

##authorization59
APP_KEY = 'AVofL7CAoG2Ci2eswdPDOsnS5'
APP_SECRET = 'd0efTsoNieRn6PHvs9AK0yIupargKvEvBdvQ7Vas55qvjC6bIu'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter59 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth59')

##authorization60
APP_KEY = '9LhymNuxWJmXQocS0JmnZYJ5y'
APP_SECRET = 'tjsyBOIGhZVZoQDyAjcBxgdRMXtyHkrHFibtqWiNqiyYDc9RNy'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter60 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth60')

##authorization61
APP_KEY = 'Y7adPe1fnmEH7W09yXym33nhx'
APP_SECRET = 'z1FspaRs0wngEvFfbcuxJFvVaJZ7yoyGZpcmohTvGDVNbk96VN'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter61 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth61')

##authorization62
APP_KEY = 'FzKLORHruBnGbRbYajLjHfNa5'
APP_SECRET = 'UdKkImbr0MYKm0wvhAEMMtnS6XwOM4XOj5Fm5vZoGF15Vz0wGW'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter62 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth62')

##authorization63
APP_KEY = 'yn3O61fzD83YG4aTVgjxPbTJW'
APP_SECRET = 'aOoELtkQpHNlzNLv3i4Hx9iLYwKAfvCUUEnV4vhDkjc54hEPwD'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter63 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth63')

##authorization64
APP_KEY = 'HdnYDiFPuVwqN2yXjkkWkD7aD'
APP_SECRET = 'pFBJgizyVMrCdwZVW36iXknqYRNLK95oHZFKyyUw8la0qBWje2'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter64 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth64')

##authorization65
APP_KEY = 'OVDI4U6S5PXEvdYbKwI2vkhf2'
APP_SECRET = 'asNe5uViFVG8U6bJkWRCiOIyH87IET1kqTvxsh26FH5moCvYBS'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter65 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth65')

##authorization66
APP_KEY = '0L4Z66BTVGsNk19o37TW4NzGC'
APP_SECRET = '7P4Gl4SZbqsGb34H8BWaZ6J0lRsttSbuNSrXaeFonk1OvyLECy'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter66 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth66')

##authorization67
APP_KEY = 'IU2x6T6b09DMRPa6YzRPilHy8'
APP_SECRET = 'MnA3568rStmBEUvT8Vq3Osj8uppW3wA44PyDYTUruKzbpvFHm6'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter67 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth67')

##authorization68
APP_KEY = 'WJJaaDYyxmQMP1JXiPUm6TM8N'
APP_SECRET = 'mFqZz0zgidFCoVxF0RMIBCPYdwEWYWv9DxsNjUfYyHnBRkRxKu'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter68 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth68')

##authorization69
APP_KEY = 'K6rJ3Ptb4H6f9iRr3BoEP6rqG'
APP_SECRET = 'riWZvdRQuVvX4hnYvsUdbAxT8vc3J4uQVyfMGzCNrS06hU0JBQ'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter69 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth69')

##authorization70
APP_KEY = '8tSixBYYwm9LTQREyNh4JCzQa'
APP_SECRET = 'W0ktFLWg7B1ZvwqC8oQ7IoTGiRewnqSm7PjHUGS5Aw9l8djHJI'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter70 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth70')

##authorization71
APP_KEY = 'a9WbVlVLI2fcVOZ3WkfaflSC0'
APP_SECRET = 'y6m0VEmahh8Zj1sIgm2oimGZJJpNXEy4U5gQDu5hB3i9frKceu'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter71 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth71')

##authorization72
APP_KEY = 'sbxranzN1LoAGBFjjKsBdiMiy'
APP_SECRET = 'qtcD4knlESwo1D7qGh71bbBHawfhgQTZz7pdDVZFkV3paK2nel'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter72 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth72')

##authorization73
APP_KEY = 'coGVS6F4KUwiPdoH787Hy22vD'
APP_SECRET = 'LoISYZUwqI4z70OtOfpxxMHP06zMae9u3LD4WaGtfIEGgujfdP'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter73 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth73')

##authorization74
APP_KEY = '5OlnVLeXOEheY36UK6iN8YiDV'
APP_SECRET = '0U3oIkUTQ30ffZq6K7riCz4NYwXY5deehp3KjJ9WYh3KvkG6fH'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter74 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth74')

##authorization75
APP_KEY = 'DqIxPEHruCzRWOFwV3woSHDSv'
APP_SECRET = 'SjPwSdfSERyOK12fwjt3bFNT3zxIL9LYvr1CFx4hqKr7fS4SWC'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter75 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth75')

##authorization76
APP_KEY = 'EAGtdyy4kSoeiQqHZ7DPbAgH8'
APP_SECRET = 'bcS81ixDtwzHnBGchVzgN9aadoomHVaYYjo8WdmDYZWXD4YFDa'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter76 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth76')

##authorization77
APP_KEY = 'NwI6te2qNoFIAZvfiotaud9a6'
APP_SECRET = '1yGrKzmxhAsMF0VBgvE7nrsE5VdjUqzA0Bgvp8utGPLVTvcd3R'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter77 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth77')

##authorization78
APP_KEY = 'k75iXqoIScoTTAuZVQinw66FN'
APP_SECRET = 'gCU6laGyv428lq1k7qxqwwc84d74ELu88zNs3dQDX67Nc544yv'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter78 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth78')

##authorization79
APP_KEY = 'mCwWvXZfSLz9xL105gysVrLdF'
APP_SECRET = 'mLjbxPBS9PqolgWLgXGPi35RJ3g3Cta6WouezgOYzuIRO5FWcN'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter79 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth79')

##authorization80
APP_KEY = 'neXFJKARTVHyJDd9uI5rOzYoj'
APP_SECRET = 'rHU4pcahXUrUnFBexyIwAZd7E7epVUygfQMAkazRQZsPvE9Edf'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter80 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth80')

##authorization81
APP_KEY = 'dd0fLEdMNlAPDqhZWtwueM4Ya'
APP_SECRET = 'EynwcFE9SIF04r9Yh4axWPwX24PeLXghPkMOODWhch29KXafMC'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter81 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth81')

##authorization82
APP_KEY = 'kSPSEIAmEQ1UfiQjg2s2g0P4i'
APP_SECRET = 'Y3s5ta8x8lpEVQE6qLWxUdvUXliY1HQ97sEWL7JAflDQBZIljb'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter82 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth82')

##authorization83
APP_KEY = 'hsTQ7cPxTO0mMBc2JXIzy2p3K'
APP_SECRET = 'nsDqzT5kXUn6ne2oFOUfjvn1seRMszFsW0hGnFv7IurXYG8vlB'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter83 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth83')

##authorization84
APP_KEY = 'O8Kl0qBgpeqMETwP7hW41e0Tf'
APP_SECRET = 'I2nnB5ogrKGoQqxUWpSHD9rSvrOvP3d1TdIhFyWfjrpIGNH6Ki'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter84 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth84')

##authorization85
APP_KEY = '17JvNIEbllOQbNx0S41mKeeV8'
APP_SECRET = 'kyLzLmNl4c0jgQHCy39TSLmOoVLjvdU8QhQeGzK1iLvuhbOv6A'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter85 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth85')

##authorization86
APP_KEY = 'bbruvjCs6xFm9Ynf2SVXyNsGb'
APP_SECRET = 'Wo4SvP9PMYZkXXSwnJFY2IOnVq9h7uzQp8Fzu2JkeCE9kPryNb'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter86 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth86')

##authorization87
APP_KEY = 'VVTOSvGElkmFyryeMhfRMx9uB'
APP_SECRET = 'TMvyU4qYMpoit6RVqi8pLSxk9EvO7Sm8puknNvLZYnsbJvtDkZ'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter87 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth87')

##authorization88
APP_KEY = '70f7vubLrwyMstmIfTY77wgeH'
APP_SECRET = 'hf2NYIzbQiPqVbyf8LOsc1wJaaouiZSOlxYlC39K9RqvmpFcHE'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter88 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth88')

##authorization89
APP_KEY = 'jsvQV1yxppkYRgfHZ9d3NbFsg'
APP_SECRET = 'pfBS9ZtAaAyBVKge8XysGJ0oIDSM4nOlW3iBmJCojWaYQeHAmC'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter89 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth89')

##authorization90
APP_KEY = 'U0Vw7sLKoDYnfK32BcWc8JId8'
APP_SECRET = 'rllmaLD4rvdWg93wjSfFsAGHHyDnKh0s7bStwF2ft3v4vkbZgY'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter90 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth90')

##authorization91
APP_KEY = '4Sig5i3LHhEXxaFrymrbGz656'
APP_SECRET = 'pvu2hrBbmU6ggrkTuc7exseMbBDx5VCR4TqtHwqNDhzLerBBBe'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter91 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth91')

##authorization92
APP_KEY = '3OUT28j5B65jRWFQ2Dv4OOGnk'
APP_SECRET = 'Ei49LYz0gzAI6f7psSbp9vVn0xUDvYVnnwWiWmVSKyWTbuHNWH'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter92 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth92')

##authorization93
APP_KEY = '2UO9SbkRtTqzQKG8kIgJ1mzij'
APP_SECRET = 'bkpAOfdRZ4CeGiW1jDBRauTmcDyZH0m0xMbFVthkIedwzfTMIq'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter93 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth93')

##authorization94
APP_KEY = 'xWhRscVIJJbKvHxizEYwfQ5Em'
APP_SECRET = 'GHZxSYiTfAol1aBSqaQUKt330ycQC7X1AP656vJm0bMwoQD6fh'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter94 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth94')

##authorization95
APP_KEY = '4B9r8nvVVSCW4cG237RgiJSEe'
APP_SECRET = '9jge98bdfnfTzau02Sx8nWdqDH8poBSNE3upETHsYrqmpI7Fpv'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter95 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth95')

##authorization96
APP_KEY = 'WB9cgXoh4FVAlu16mAKlgtAJi'
APP_SECRET = 'oGFkCqV4qCB2XKF0w8kxYxpBKpappm8meSdQpW9mOLnEUEmWCV'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter96 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth96')

##authorization97
APP_KEY = '9XGiU7sYp9C9GVRKdeRrnAPEf'
APP_SECRET = 'iNm8Ct4Z7FuQazsd851MMCEP9sJJmn2gsxLUNwde9B4I6NMjNO'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter97 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth97')

##authorization98
APP_KEY = 'H06QGaXhy7anDTyavNlgJyweq'
APP_SECRET = 'R5D5LjgmDKB6FrWkiQ8uflZFaj3TQVtmOdMGqEVmxDKhq69Sum'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter98 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth98')

##authorization99
APP_KEY = '2fUVNSrchD123Kgluzqz1W7qh'
APP_SECRET = 'C6FAbRyrqT81azKI7fGzFFFfsOUmRrkS3Z7AXYVFNvxc7GCCmg'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter99 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth99')

##authorization100
APP_KEY = 'SWxasyorAXqCJnNO0KpLOvIpU'
APP_SECRET = 'CS6RXHvse3gvm2hnO96SMqDYdgHV5HvVFJCHYN2CySAIKuJIGd'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter100 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth100')

##authorization101
APP_KEY = 'RAfOXAoLBEITwmxX4sAdVXXx6'
APP_SECRET = 'dQjJo8eGraTtSt9BfLekTe9QZNbMLfN10AdkIychHtpLnWRuUS'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter101 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth101')

##authorization102
APP_KEY = 'YkDPalbLm0YKAhulla5hf9OK0'
APP_SECRET = 'M2aMS2m48YJvP2u4qqOcE2Y1nknsJ5BH8ldHTP51bvtHqXAamc'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter102 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth102')

##authorization103
APP_KEY = 'kVY2bV59Uh8BThwgkyLy0uOTq'
APP_SECRET = 'AQNsD6zKGmXtMsWxBvjb4Jx3snT1fyCcwPocglBVQn2qeMxCX0'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter103 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth103')

##authorization104
APP_KEY = 'CMdjJRAEE1pGByeUThyEDLyLy'
APP_SECRET = 'xGhISbicJGxiYCxiOyQJC5SdL3fvo9mFhcOib9qbi1p3MDprcQ'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter104 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth104')

##authorization105
APP_KEY = 'we2JbKKSGG8Wq8Liz8A899RB2'
APP_SECRET = 'bVim1EtVlJYIO30KIcXz9Q7gl8q08ttF7aman7SIPaTKrguLrW'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter105 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth105')

##authorization106
APP_KEY = '17FYvaepAB0KrjMfQujfidUL8'
APP_SECRET = '516FHx3FOuIS7WlP0LqNmMUX5axQuH5qgQOWbg3TVTNaIUODXd'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter106 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth106')

##authorization107
APP_KEY = 'yUKDXIhGBoPT4LiNC3Gq6wWbX'
APP_SECRET = '19uGSVX7ex5DGffItsfVezpzt3cjVaIfZ5rz6JxjPrMcw0gI46'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter107 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth107')

##authorization108
APP_KEY = 'LwAP5Glie6sXATBHv66oiNJ7s'
APP_SECRET = 'AjWWMPeTPq0H1B6NLJyfNRbmbaIt25P5F9HOIUwHJwnFTpReeF'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter108 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth108')

##authorization109
APP_KEY = '1IDim0FonnPs0eNl2U2dSFIS6'
APP_SECRET = 'CrJQr1UtpkRQIQBeY0yREWjXkccYpYzWhjDYNC81GgpzUFnhu5'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter109 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth109')

##authorization110
APP_KEY = '9kPa8ENiI2Btewqn7occllsDm'
APP_SECRET = 'lc27xAfrrnwGKnm1mSZI7oozwlZcbNDnbH0miKQasvmuHq2Yqz'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter110 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth110')

##authorization111
APP_KEY = 'KCmjdQW2s8I0HimdFwDSNLhXL'
APP_SECRET = 'aQNPCfQczc2gd60FNQS1JFXXbOZf0tGkfozu9tnOn1VQ88Yg35'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter111 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth111')

##authorization112
APP_KEY = 'zhzMPByWkiqyLzVWZl440CepJ'
APP_SECRET = 'lRjBPBkhtCmEIZl26IeBIg01mWAAg2TAU3P4fBZlXhQJtlMECA'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter112 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth112')

##authorization113
APP_KEY = 'jlFWL2NftjzGkr4whyczkUOO6'
APP_SECRET = 'BrFLonWopMw5tjC0u8J8EKp6Xid15T9GGIPjyzXggzJOiSOJud'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter113 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth113')

##authorization114
APP_KEY = 'UzNpbzuujpjTilNEFVa5Qj1nK'
APP_SECRET = 'o3Gt6RcKlX3Tm7uY4SOUn5ZJlVcoQBevg1qW1rem3dcExJjCk2'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter114 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth114')

##authorization115
APP_KEY = 'FMN34Qha2JXWj1CrlvX6Z392R'
APP_SECRET = 'kwSF1oS43iSFHXhYxfn8X2KduAweLGEhkiVeVSeDQqERVdxJNZ'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter115 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth115')

##authorization116
APP_KEY = 'CyUUM5wjHgNSG54KIuGKacjta'
APP_SECRET = 'qDpAaySxXr7GEYcFciwMzebHpESwH8MuU3YGRe1fCVmT72ro5w'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter116 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth116')

##authorization117
APP_KEY = 'P0coGOpbUHrp7blXEPllN2kCP'
APP_SECRET = 'GHlYROTCaUWV54vKNqHekMqAv7LrDar5Z3bLdNhFx98fZaOX46'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter117 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth117')

##authorization118
APP_KEY = 'A5T1hKQhmYR8dyN0EMDtJc9ey'
APP_SECRET = '1YwwnTQBBxoFBCIncqEgyA5A6yz9o64740rsg4o7gZ7xzEGsdb'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter118 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth118')

##authorization119
APP_KEY = 'I7BP2Eo6KbLzpdsUNCPmgG1uS'
APP_SECRET = 'NgnvqJ8Y9kf79S1S7uAtI0xYmNXWtuv22ACBWqDSy9SAqBkwiR'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter119 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth119')

##authorization120
APP_KEY = 'RcYpevoajUujMFHMoUl6ZT0Mv'
APP_SECRET = 'u3vQRSNf48aqN8MLN0HtEp3WcS7sDGQYAfWx3An7NVahjXmUO3'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter120 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth120')

##authorization121
APP_KEY = '1B0I9mhqYE6HOa4SWAsN0uhGC'
APP_SECRET = 'cWgt2SZp7lNLB1YDekZYdipd54mvzlFlsdIDVZfVZnUNqYceZU'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter121 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth121')

##authorization122
APP_KEY = 'rnt20JH8VQjuSAAXQLFtYD7Lp'
APP_SECRET = 'Fry4X8Xd5iVHKCjPhmu8bljwIAyQn5S2knCvOkZTasVBv5Dgep'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter122 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth122')

##authorization123
APP_KEY = 'cmyhz2U2kYkBj4kFmQeVTAZyf'
APP_SECRET = 'gRNuScOZ1svmtk9QSK34soOFUpKYlpgApGjHACkCjuMxctLHc7'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter123 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth123')

##authorization124
APP_KEY = 'MP0ngEE7bDyAWGcvQADgHmAoZ'
APP_SECRET = 'nVQubQaVSJh9AZkrTO9IxdKUvvAOVjlwHBvqdnGcFLaoMEZxKy'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter124 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth124')

##authorization125
APP_KEY = 'Dr9Jhe57WvnuVCcPPJuZJZSAN'
APP_SECRET = 'HoTGomAvGmFDre5B0FKsnTbDhC7HjrnOJkWbbDOcjAlDVnPJC4'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter125 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth125')

##authorization126
APP_KEY = 'jwjQr2VeQoNE1lSW0X7KCwtbR'
APP_SECRET = 'JSbNYTj3YrjRJ4WCkeVto3ILiZelsh67RcKjtmqdtMB1nrovxI'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter126 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth126')

##authorization127
APP_KEY = 'M1pxEw0ZdtO4VaHE6f94iYdCu'
APP_SECRET = 'bbgGAwxbvkckw8SC4YA43Z8OJfn9ewVgxHHrSK2IdfbLzqIRrs'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter127 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth127')

##authorization128
APP_KEY = 'FQuP4ljkKhHfkwBFKmpo5EqL0'
APP_SECRET = '9QzY3Um8sbGASy0stW6gQKUaonlwh2dQ5MArIMHdUjRAr0144S'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter128 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth128')

##authorization129
APP_KEY = 'e6550DOBctd4ZUpcePtGjfU8h'
APP_SECRET = 'dAp1rPrwAA2vOm79FbKUG8DBhCcvmUdmC5nYL4BCKprq80J9Ya'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter129 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth129')

##authorization130
APP_KEY = 'ov40Gjlf8IH3v9YJjZd9QZW8S'
APP_SECRET = 'FVrntmdD064bQj0JlOSkeDT7zzYk5j8o0lWnbVkZRzUgOpRkj1'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter130 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth130')

##authorization131
APP_KEY = 'FZJFZJf3OP0KL9Ljgsug3eeZ4'
APP_SECRET = 'xDghs17qnkExzt4HPGQuJ12Ui2S0nraRlOOvwvGF5qNVqLGRcm'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter131 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth131')

##authorization132
APP_KEY = 'bkPImCqC4dsIAnwfn2UP7QrHI'
APP_SECRET = 'jEQMdsgNIfk8MaZ5zhtoo058pb97efyZiDiQmCDjLCLiHsESUm'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter132 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth132')

##authorization133
APP_KEY = 'kYbVG4v0CSaybwC6mHdQ5r8Sk'
APP_SECRET = 'BO1sYfgs0DsktYzO3OjisWl8lyf5mi8Y8rllCAAuBgSUS4gc8p'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter133 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth133')

##authorization134
APP_KEY = 'fTGhSLCzkiC3eNYj3NtzQiQ9c'
APP_SECRET = 'UuESLCwZvTCicBxWclv9IiezrjTSqSwAmjyFgIM8HRo1RQoSv6'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter134 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth134')

##authorization135
APP_KEY = 'JAk5XxSKuNo4V0suIOVaoP8Nm'
APP_SECRET = 'wCNQmjX0rpwkfpCgvxHyzUyLWnsXkYsOFtyOLIshrTbO6PNDdz'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter135 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth135')

##authorization136
APP_KEY = '7ipUOMHL5aANwqFNbreH2MSw4'
APP_SECRET = 'rzwU7MtirNre7SjTpifzB3PVx4xpTIv3V3TXU0kHkfEKrqWobV'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter136 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth136')

##authorization137
APP_KEY = 'CcBNjyONNf9wlgJclR0DNfhmc'
APP_SECRET = 'DNC3FtseYjVV9GEJdikoyaAAu2bGUPEMKQIYGzsWfEhV3tolXH'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter137 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth137')

##authorization138
APP_KEY = 'xICJ15yCtvstCkgZ3E5FnvZjL'
APP_SECRET = 'Sts7P7otM0zOi0Aebol3NMoNL2NljmizDHXGx0AZzYVeG8b4Q5'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter138 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth138')

##authorization139
APP_KEY = 'TE6wAMR7OrObGsl3igciQSqU8'
APP_SECRET = '9UzZYa24zM0kvUs2hQjLDga2zksip8wZ8cVgG9yiZnXv3COoHe'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter139 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth139')

##authorization140
APP_KEY = 'UojnPMfj9GP1pBnCzHTlTGFhE'
APP_SECRET = '1lFHlp3D9vOSFLGrBp1im1BtSx3M4uihaFq7tqs4XmEeUqOWZF'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter140 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth140')

##authorization141
APP_KEY = 'CVftGpLTJgypIRH8uf3WIB3IN'
APP_SECRET = '3zaS5B5TEoS5bnj1oET5iPwBvTyoiNwHIDDf1XXlZSDnvUaFLD'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter141 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth141')

##authorization142
APP_KEY = 'kg6HKRRJXc5KkGF1e6KDfCekz'
APP_SECRET = 'VQsDIv13jlhkWFqpRhy1HmYIiC73lmIwedrXyw3WvL01gDDa9W'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter142 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth142')

##authorization143
APP_KEY = 'MGPdpcXiDP036zXNS4egbIzBx'
APP_SECRET = '5UbwBQ2EILGxZonPZnImOIZqF2VksnEaq00kuOeCvAnmFpgF1g'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter143 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth143')

##authorization144
APP_KEY = 'u66VjnhHJsJvA9dQ3uJYqRvMg'
APP_SECRET = 'dSlBo9PqvOt86dQF34JzXb15nyhFHKk5xyQAJ1eEzVF8H2C5TZ'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter144 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth144')

##authorization145
APP_KEY = 'Wn1zcTTXQKdFo90hawfRJTuR2'
APP_SECRET = 'NdGv9uQpz1sKOz2GdT2kWki0LT7MHyBQHgNiOO6OMNdIZFlR3F'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter145 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth145')

##authorization146
APP_KEY = 'OwyqbfQVlMTdF4OzYzTgEnOrl'
APP_SECRET = 'nimFkY4WTtVMQgHOFYDSHkQ89tw9HwHzE91yoxUqVYG1olmR73'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter146 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth146')

##authorization147
APP_KEY = 'Ph8Kb4JdpB71xCu4Eel1vJ5Uo'
APP_SECRET = 'FGAlsOYKTtdXafuLecLEKOChZxQ2HyZftIlela5TL3PDLU2kHb'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter147 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth147')

##authorization148
APP_KEY = '4LUauqJHGaVHYuUFbZ2SAhyF1'
APP_SECRET = 'At1eejI4UJFgEb3xk8K0JrBCZXmNMPjqRj7XCn84PHhWrAaBAv'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter148 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth148')

##authorization149
APP_KEY = 'FRSSWkH6h8xOYMaVDIdDIhFPI'
APP_SECRET = 'r2pYequrMiso17K8ahmO2UfUQPPvv5UW8P9WmTBnHN01C1Ysxl'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter149 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth149')

##authorization150
APP_KEY = 'RsLxgMhnwdx6dk9MRJnvL1P4x'
APP_SECRET = 'ruAHrJXvLbDsMF86fyotTJ4SuQT12e77XoytodpQbXkhPytn3a'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter150 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth150')

##authorization151
APP_KEY = 'aOKOKVcJCt0y3cWSV6b1cVoOv'
APP_SECRET = 'xPrAJR0RmuNp5yi3ixp3Rx3GtH8Ll2OlXbvKamYX2700Oza4xS'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter151 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth151')

##authorization152
APP_KEY = 'fcRdD3sqgm3EeFHpBkYwSpaQy'
APP_SECRET = '8zOyDWsmF6miG9DBDfTfVF8F0AvNcxrIF3Q719zd8hmtabxOmz'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter152 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth152')

##authorization153
APP_KEY = '0iugjytzCfSOxOrgZbQbGuyw1'
APP_SECRET = '2yKDmJRnV9ie0W1eWcAHD71sSEjBkoT6GMVSaiW6D5jkVp6sXo'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter153 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth153')

##authorization154
APP_KEY = 'EeULu91XFNKgl1sBLKCcAnEbp'
APP_SECRET = 'Oab3rj1k9bQYgaUb5fMx2hivWCMLBC9tYKq7jiVz2teb9Xk6g3'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter154 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth154')

##authorization155
APP_KEY = 'KsAF8qGjLzbfKLZ37YM0JNCiq'
APP_SECRET = 'LAUmetk6Z87h4NxfYMQCR3vC06RJV63VjYRorImzmVYknbWznD'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter155 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth155')

##authorization156
APP_KEY = 'wNoQWbKXJMl36o9ELXRbK9r3N'
APP_SECRET = 'HrZbXZaJkkWrsMhfVj6LKnsWRr8uAggJFtsjlQnKHAOryvQ6jt'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter156 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth156')

##authorization157
APP_KEY = 'jGAp1FYNSNXKR9fWr3bhpwnDA'
APP_SECRET = 'HHi3SDUZPX6LIV8PXjUmD3LfWQPXO2LXQRYDV6zRUDYqpPHbqy'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter157 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth157')

##authorization158
APP_KEY = 'u0RI8NbvtyRC1dOQtWfGxnKyI'
APP_SECRET = 'vhpfPWno2PKyMc8TRcfaHNxrvZQ9X1OWtiF0xB8neJYwOMHV8Z'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter158 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth158')

##authorization159
APP_KEY = '9Lfmk5XhwdhPCAGyB8FXYzxVJ'
APP_SECRET = 'beYbyxhj9N10O5ZCcy6oAhXHPJ4c02bTcGinZakj5kVaaYxeX0'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter159 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth159')

##authorization160
APP_KEY = 'rfJiBiE6ZaufmfUu4PfcY1GNI'
APP_SECRET = 'VJVdu3FVWxXsKVuJBAB8TVisSOvFD0LLMtrAvf55kNQJDxJftM'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter160 = Twython(APP_KEY, access_token=ACCESS_TOKEN)

print('auth160')

# Sets initial Twitter authorization key
twitter = twitter2
auth = 2

count = 0

########################################################################################################################


########################################################################################################################
### new functions defined
# Twitter authorization update function
def new_auth(twitter, auth):
    time.sleep(1)
    if twitter == twitter160:
        auth = 2
    else:
        auth = auth + 1
    return auth


# tweet data collection function
def clean_tweet(tweet):
    try:  # extracts information about retweeted status if retweet
        retweet_id = "/" + tweet["retweeted_status"]["id_str"]
        retweet_user = "/" + tweet["retweeted_status"]["user"]["id_str"]
        retweet = 1
    except KeyError:
        retweet = 0
        retweet_id = retweet_user = None

    if retweet == 1:
        try:
            text = 'RT @' + tweet["retweeted_status"]["user"]["screen_name"] + ' ' + tweet["retweeted_status"][
                "full_text"] + ' QUOTE: ' + tweet["retweeted_status"]["quoted_status"]["full_text"]
        except:
            text = 'RT @' + tweet["retweeted_status"]["user"]["screen_name"] + ' ' + tweet["retweeted_status"][
                "full_text"]

    else:
        try:
            text = tweet["full_text"] + ' QUOTE: ' + tweet["quoted_status"]["full_text"]
        except:
            text = tweet["full_text"]

    user_mentions = [[user_mention["name"], user_mention["screen_name"], "/" + user_mention["id_str"]] for
                     user_mention in tweet["entities"]["user_mentions"]]

    data = ("/" + tweet["user"]["id_str"], tweet["user"]["name"], tweet["user"]["screen_name"],
            tweet["user"]["location"], "/" + tweet["id_str"], tweet["created_at"], text, tweet["lang"],
            "/" + str(tweet["in_reply_to_status_id_str"]), "/" + str(tweet["in_reply_to_user_id_str"]),
            tweet["is_quote_status"], tweet["retweet_count"], tweet["favorite_count"], retweet, retweet_id,
            retweet_user,
            user_mentions)

    return data


# output collected tweets as csv
def tweets_csv(tweets):
    f = open("temp_liked_tweets_file.txt", "w", encoding="utf8")
    main_columns = ['follower_id', 'liked_user_id', 'liked_user_name', 'liked_user_screenname', 'liked_user_location',
                    'tweet_id', 'tweet_creation_time', 'tweet_text', 'tweet_language', 'tweet_reply_to_tweet_id',
                    'tweet_reply_to_user_id', 'tweet_is_quote', 'tweet_retweet_count', 'tweet_favorite_count',
                    'tweet_is_retweet',
                    'tweet_retweet_tweet_id', 'tweet_retweet_user_id', 'tweet_mentioned_users']

    current_time = str(datetime.datetime.now().time()).replace(":", "")
    dfmain = pd.DataFrame.from_records(tweets, columns=main_columns)
    # change file output domain as appropriate
    dfmain.to_csv(r'Patrick_liked_tweets_' + current_time + '.csv', index=False)
    f.write(r'Patrick_liked_tweets_' + current_time + '.csv')
    f.close()

# output errors as csv
def errors_csv(errors, error_user):
    errorcolumns = ['error_code', 'badaccount']
    current_time = str(datetime.datetime.now().time()).replace(":", "")
    dfmain = pd.DataFrame.from_records(list(zip(errors, error_user)), columns=errorcolumns)
    # change file output domain as appropriate
    dfmain.to_csv(r'Patrick_liked_errors_' + current_time + '.csv')
########################################################################################################################

start_time = time.time()

errors = []
error_user = []

page = 'placeholder'
tweets = []
i = 0

# change file input domain as appropriate
path_data = list(csv.reader(open('Patrick_likes.csv', newline='')))
row_count = sum(1 for row in path_data)

# change the range of the file based on the last user's tweets you have collected
# for example, if the last user in the previous session is in the 24th row of the domain file,
# set the range to (24,row_count) to only collect new users for this session
users = [path_data[n][0].replace("/", "") for n in range(UPDATE_INDEX, row_count)]

# control run time of program (time is measured in seconds). len(page) > 0 ensures that we collect all
# tweets from a user before terminating the program.

while time.time() - start_time < RUN_TIME or len(page) > 0:

    # This try-except block prevents errors when we reach the end of the input file
    try:
        user = users[i]
    except:
        errors.append('user_list_indexing_error')
        error_user.append(i)
        break

        # Tweet collection
    try:
        page = twitter.get_favorites(user_id=user, count=200, tweet_mode='extended')
        for tweet in page:
            tweets.append((f"{'/'}{user}",) + clean_tweet(tweet))

        while len(page) > 0:
            # max_id parameter allows us to collect all tweets from a user's timeline in batches of 200,
            # up to a limit of ~3240 tweets. The max_id parameter for each page is the last id of the previous
            # page, minus one.

            try:
                oldest = page[-1]["id"] - 1
                page = twitter.get_favorites(user_id=user, max_id=oldest, count=200, tweet_mode='extended')
                for tweet in page:
                    tweets.append((f"{'/'}{user}",) + clean_tweet(tweet))

            except TwythonError as e2:

                # If the program encounters error code 429, it means that the current twitter
                # token has timed out. The program then goes on to the next token.
                if e2.error_code == 429:
                    auth = new_auth(twitter, auth)
                    exec("twitter=twitter%s" % auth)

                # If the program encounters any other error code, we note the error.
                else:
                    errors.append(e2)
                    error_user.append("/" + user)

        i = i + 1  # only move on to next user when all tweets from the current user have been collected

    except TwythonError as e2:
        # If the program encounters error code 429, it means that the current twitter
        # token has timed out. The program then goes on to the next token.

        if e2.error_code == 429:
            auth = new_auth(twitter, auth)
            exec("twitter=twitter%s" % auth)

        # If the program encounters any other error code, we move on to the next user,
        # while also taking note of the faulty users.

        else:
            errors.append(e2)
            error_user.append("/" + user)
            i = i + 1  # move on to next user if current user has an error unrelated to token time-out

    # output csv file if ~1,000,000 tweets have been collected to reduce memory issues
    if len(tweets) > 996000:
        tweets_csv(tweets)
        tweets = []

# output any remaining tweets and all error messages
tweets_csv(tweets)
errors_csv(errors, error_user)
print('done')

if __name__ == "__main__":
    pass


