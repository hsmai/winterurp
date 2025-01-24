import numpy as np

from moabb.datasets import Cho2017
from moabb.paradigms import LeftRightImagery
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

lr = LogisticRegression(max_iter = 1000)


# Load MOABB dataset
dataset = Cho2017()
paradigm = LeftRightImagery(resample=128)

# Get data from the first subject and the first session
X, y, metadata = paradigm.get_data(dataset=dataset, subjects=[1])




print("X shape:", X.shape)
print("y shape:", y.shape)
print("Metadata shape:", metadata.shape)

print("X data sample:", X[:1])  # 첫 5개 샘플 출력

# y 데이터 확인 (레이블)
print("y data sample:", y[:10])  # 첫 10개 레이블 출력

# metadata 데이터프레임 확인
print("Metadata sample:")
print(metadata.head())  # metadata는 pandas DataFrame이므로 head로 확인



C3 = X[ : ,12, : ]
C4 = X[ : ,53, : ]



#C3 채널 평균(64개)
C3_channel_mean = C3.mean(axis=1)


#C4 채널 평균(64개)
C4_channel_mean = C4.mean(axis=1)


#C3 채널 표준편차(64개)
C3_channel_std = C3.std(axis=1)


#C4 채널 표준편차(64개)
C4_channel_std = C4.std(axis=1)


#C3 채널과 C4 채널의 차이
channel_difference = C4-C3
print(channel_difference.shape)


#5개 데이터 합치기
input_data = np.column_stack((C3_channel_mean, C4_channel_mean, C3_channel_std, C4_channel_std, channel_difference))
print(input_data)

#훈련, 테스트 데이터셋 나누기
train_input, test_input, train_target, test_target = train_test_split(input_data, y, random_state=42)


#모델 훈련 및 평가
lr.fit(train_input, train_target)
print(lr.classes_)

y_pred = lr.predict(test_input)
accuracy = accuracy_score(test_target, y_pred)
print(accuracy)




