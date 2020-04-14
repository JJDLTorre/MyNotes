### Find and replace two items. For example academic years from 2018-2019 to 2019-2020. 
'''
:%s/\v(2018|2019)/\={"2018":"2019","2019":"2020"}[submatch(1)]/gc 
'''
