from datetime import datetime, timedelta

# 時間を設定
time1 = datetime.strptime('08:30:00', '%H:%M:%S')
time2 = datetime.strptime('17:30:00', '%H:%M:%S')

# 時間の差分を計算
time_difference = time2 - time1

# 結果を表示
print(time_difference)
hours, minutes, seconds = str(time_difference).split(":")

# 時間が8時間以上なら8時間を返す
if int(hours) >= 8:
    return_time = timedelta(hours=8)  # 8時間のtimedeltaオブジェクトを作成
else:
    return_time = time_difference  # 差分が8時間未満ならそのまま使用

# 返す時間を "HH:MM:SS" 形式で出力
return_time_str = str(return_time)
print(return_time_str)

