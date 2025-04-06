{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# 감성 분석 클래스 직접 만들기\n",
    "class Aurora3:\n",
    "    def get_df(self, df):\n",
    "        # 감성 점수와 비율을 랜덤하게 생성 \n",
    "        import random\n",
    "        df['score'] = [round(random.uniform(-1, 1), 2) for _ in range(len(df))]\n",
    "        df['ratio'] = [round(random.uniform(0.1, 0.3), 2) for _ in range(len(df))]\n",
    "        return df\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                                    sentence  score  ratio\n",
      "0                 생각나니 처음 우리 너무 멋쩍게 말놓자던 그 날   1.00   0.15\n",
      "1                   손톱만 깨물었던 니 표정 지금도 눈앞에 선해   0.77   0.22\n",
      "2                참 아꼈어 늘 좋았어 보기 아까워 눈 감기도 했지   0.80   0.18\n",
      "3                    함께라면 먼 길도 잠시야 마음만 달렸었나봐   0.79   0.10\n",
      "4                   밤마다 팔베개를 연습해 꿈에 너를 만나기위해  -0.56   0.20\n",
      "5                    지난날 못 해준게 많아서 혼자 되돌리곤 해   0.97   0.13\n",
      "6      I never think you go away in my life.  -0.64   0.17\n",
      "7                             어디있든 나 먼저 걱정마.  -0.68   0.24\n",
      "8                 넘치게 받은 사랑 남아서 아직 가슴은 부자니까.  -0.88   0.13\n",
      "9   I'll never forget all your love forever.  -0.11   0.18\n",
      "10                         혼자 온 세상 내 은인은 너야.  -0.97   0.20\n",
      "11                             아파할 때도 눈물날 때도   0.05   0.16\n",
      "12                              추억의 힘으로 사니까.   0.64   0.19\n",
      "13               운도 좋아 복도 많아 친구들 모두 날 부러워했지.  -0.03   0.24\n",
      "14                 너를 빼면 가진게 없어도 은근히 용기가 났어.  -0.27   0.28\n",
      "15                  가끔은 같은 모잘 쓰자고 생각마저 같아진다고  -0.77   0.22\n",
      "16               여전히 그 약속을 난 믿어. 쉽게 버릴 수 없어.   0.21   0.20\n",
      "17     I never think you go away in my life.  -0.58   0.13\n",
      "18                            어디있든 나 먼저 걱정마.   0.36   0.14\n",
      "19                넘치게 받은 사랑 남아서 아직 가슴은 부자니까.  -0.04   0.10\n",
      "20  I'll never forget all your love forever.  -0.38   0.27\n",
      "21                         혼자 온 세상 내 은인은 너야.   0.03   0.17\n",
      "22                     아파할 때도 눈물날 때도 추억에 사니까  -0.92   0.22\n",
      "23                               고마웠어 난 행복했어   0.47   0.17\n",
      "24                           사랑으로 넓은 가슴 생겼어.  -0.47   0.20\n",
      "25                            널 만나면 꼭 안아줄텐데.  -0.20   0.12\n",
      "26     I never think you go away in my life.   0.27   0.18\n",
      "27                             멀리 숨어 미안해하지마.  -0.63   0.13\n",
      "28                              세상이 슬픈 장난친대도   0.86   0.21\n",
      "29                              우리 마음은 갖지못해.   0.91   0.26\n",
      "30  I'll never forget all your love forever.   0.17   0.10\n",
      "31                          또 태어나도 내 은인은 너야.   0.25   0.24\n",
      "32                               그리워할게 간직해둘게   0.42   0.22\n",
      "33                              이젠 니 몫까지 사랑해  -0.45   0.11\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import random\n",
    "\n",
    "# 가짜 감성 분석기 (임시용)\n",
    "class Aurora3:\n",
    "    def get_df(self, df):\n",
    "        df['score'] = [round(random.uniform(-1, 1), 2) for _ in range(len(df))]\n",
    "        df['ratio'] = [round(random.uniform(0.1, 0.3), 2) for _ in range(len(df))]\n",
    "        return df\n",
    "\n",
    "# 저장한 파일 이름이 'test.data'일 경우\n",
    "df = pd.read_csv('test.data.txt', header=None, names=['sentence'])\n",
    "\n",
    "# 감성 분석 실행\n",
    "aurora = Aurora3()\n",
    "df = aurora.get_df(df)\n",
    "\n",
    "# 결과 출력\n",
    "print(df)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                                    sentence  score label\n",
      "0                 생각나니 처음 우리 너무 멋쩍게 말놓자던 그 날   1.00    긍정\n",
      "1                   손톱만 깨물었던 니 표정 지금도 눈앞에 선해   0.77    긍정\n",
      "2                참 아꼈어 늘 좋았어 보기 아까워 눈 감기도 했지   0.80    긍정\n",
      "3                    함께라면 먼 길도 잠시야 마음만 달렸었나봐   0.79    긍정\n",
      "4                   밤마다 팔베개를 연습해 꿈에 너를 만나기위해  -0.56    부정\n",
      "5                    지난날 못 해준게 많아서 혼자 되돌리곤 해   0.97    긍정\n",
      "6      I never think you go away in my life.  -0.64    부정\n",
      "7                             어디있든 나 먼저 걱정마.  -0.68    부정\n",
      "8                 넘치게 받은 사랑 남아서 아직 가슴은 부자니까.  -0.88    부정\n",
      "9   I'll never forget all your love forever.  -0.11    중립\n",
      "10                         혼자 온 세상 내 은인은 너야.  -0.97    부정\n",
      "11                             아파할 때도 눈물날 때도   0.05    중립\n",
      "12                              추억의 힘으로 사니까.   0.64    긍정\n",
      "13               운도 좋아 복도 많아 친구들 모두 날 부러워했지.  -0.03    중립\n",
      "14                 너를 빼면 가진게 없어도 은근히 용기가 났어.  -0.27    중립\n",
      "15                  가끔은 같은 모잘 쓰자고 생각마저 같아진다고  -0.77    부정\n",
      "16               여전히 그 약속을 난 믿어. 쉽게 버릴 수 없어.   0.21    중립\n",
      "17     I never think you go away in my life.  -0.58    부정\n",
      "18                            어디있든 나 먼저 걱정마.   0.36    긍정\n",
      "19                넘치게 받은 사랑 남아서 아직 가슴은 부자니까.  -0.04    중립\n",
      "20  I'll never forget all your love forever.  -0.38    부정\n",
      "21                         혼자 온 세상 내 은인은 너야.   0.03    중립\n",
      "22                     아파할 때도 눈물날 때도 추억에 사니까  -0.92    부정\n",
      "23                               고마웠어 난 행복했어   0.47    긍정\n",
      "24                           사랑으로 넓은 가슴 생겼어.  -0.47    부정\n",
      "25                            널 만나면 꼭 안아줄텐데.  -0.20    중립\n",
      "26     I never think you go away in my life.   0.27    중립\n",
      "27                             멀리 숨어 미안해하지마.  -0.63    부정\n",
      "28                              세상이 슬픈 장난친대도   0.86    긍정\n",
      "29                              우리 마음은 갖지못해.   0.91    긍정\n",
      "30  I'll never forget all your love forever.   0.17    중립\n",
      "31                          또 태어나도 내 은인은 너야.   0.25    중립\n",
      "32                               그리워할게 간직해둘게   0.42    긍정\n",
      "33                              이젠 니 몫까지 사랑해  -0.45    부정\n"
     ]
    }
   ],
   "source": [
    "def label_sentiment(score):\n",
    "    if score > 0.3:\n",
    "        return '긍정'\n",
    "    elif score < -0.3:\n",
    "        return '부정'\n",
    "    else:\n",
    "        return '중립'\n",
    "\n",
    "df['label'] = df['score'].apply(label_sentiment)\n",
    "print(df[['sentence', 'score', 'label']])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
