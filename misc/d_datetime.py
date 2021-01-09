import datetime
now = datetime.datetime.now()#- datetime.timedelta(days=1)
today = '{:%Y-%m-%d}'.format(now)
print(type(today))
submit_dt = '{}'.format(today)#"2019-03-06T17:00:00.000Z"
print(submit_dt)