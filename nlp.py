# 감성 분석 클래스 직접 만들기
class Aurora3:
    def get_df(self, df):
        # 감성 점수와 비율을 랜덤하게 생성 
        import random
        df['score'] = [round(random.uniform(-1, 1), 2) for _ in range(len(df))]
        df['ratio'] = [round(random.uniform(0.1, 0.3), 2) for _ in range(len(df))]
        return df

import pandas as pd
import random

# 가짜 감성 분석기 (임시용)
class Aurora3:
    def get_df(self, df):
        df['score'] = [round(random.uniform(-1, 1), 2) for _ in range(len(df))]
        df['ratio'] = [round(random.uniform(0.1, 0.3), 2) for _ in range(len(df))]
        return df

# 저장한 파일 이름이 'test.data'일 경우
df = pd.read_csv('test.data.txt', header=None, names=['sentence'])

# 감성 분석 실행
aurora = Aurora3()
df = aurora.get_df(df)

# 결과 출력
print(df)

def label_sentiment(score):
    if score > 0.3:
        return '긍정'
    elif score < -0.3:
        return '부정'
    else:
        return '중립'

df['label'] = df['score'].apply(label_sentiment)
print(df[['sentence', 'score', 'label']])