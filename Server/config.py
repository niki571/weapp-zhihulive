'''
Author: wuqianying
Date: 2022-10-29 11:21:47
LastEditors: wuqianying
LastEditTime: 2022-11-05 00:09:14
'''
API_VERSION = '3.0.93'
APP_VERSION = '8.38.0'
APP_BUILD = 'release'
UUID = 'AGARYZtHlBRLBeaIVNTkJUbKheBajpwFGo4='
UA = 'osee2unifiedRelease/11518 osee2unifiedReleaseVersion/8.38.0 Mozilla/5.0 (iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'
APP_ZA = 'OS=iOS&Release=15.4&Model=iPhone13,2&VersionName=8.38.0&VersionCode=11518&Width=1170&Height=2532&DeviceType=Phone&Brand=Apple&OperatorType=46011'
CLIENT_ID = 'c3cef7c66a1843f8b3a9e6a1e3160e20'
APP_SECRET = b'd1b964811afb40118a12068ff74a12f4'

TOKEN_FILE = 'token.json'

ZHIHU_API_ROOT = 'https://api.zhihu.com'
PEOPLE_URL = 'https://www.zhihu.com/people/{}'
LIVE_URL = 'https://www.zhihu.com/lives/{}'
LIVE_USER_URL = 'https://www.zhihu.com/lives/users/{}'
ZHUANLAN_URL = 'https://zhuanlan.zhihu.com/p/{}'
TOPIC_URL = 'https://www.zhihu.com/topic{}/'
LOGIN_URL = ZHIHU_API_ROOT + '/api/account/prod/sign_in'
CAPTCHA_URL = ZHIHU_API_ROOT + '/captcha'

DB_URI = 'mysql+pymysql://root:paopaotang@localhost:3306/zhihu?charset=utf8mb4'

SPEAKER_KEYS = ['name', 'gender', 'headline', 'avatar_url', 'bio',
                'description']
LIVE_KEYS = ['id', 'feedback_score', 'seats', 'subject', 'fee',
             'description', 'status', 'starts_at', 'outline',
             'speaker_message_count', 'liked_num', 'tags', 'topics']
TOPIC_KEYS = ['id', 'avatar_url', 'best_answerers_count', 'best_answers_count',
              'name', 'questions_count', 'followers_count']
SEARCH_FIELDS = ['subject^5', 'outline^2', 'description', 'topic_names^10',
                 'tag_names^5']
SUGGEST_USER_LIMIT = 2
SUGGEST_LIMIT = 6
DOMAIN = 'http://localhost:8300'
