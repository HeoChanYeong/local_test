#60181958 허찬영
''' 3. 영한사전과 같이 한글과 영어에 대응되는 리스트 korean과 english를 만든 후, 표준입력
으로 한글을 입력 받아 영어를 출력하는 프로그램을 작성하시오. - 단어가 사전에 없으면 적절한 메시지를 출력
korean = [‘정렬’, ‘초보자’, ‘내포’, ‘사전’]
english = [‘sorting’, ‘novice’, ‘comprehension’, ‘dictionary’]
예)
찾을 단어 입력? 초보자
novice
'''
korean = ['정렬', '초보자', '내포', '사전']
english = ['sorting', 'novice', 'comprehension', 'dictionary']
word = input('찾을 단어 입력 ? ')
for i in range(len(korean)):
 if (word == korean[i]):
  print(english[i])
  break
 else:
  if(i==3):
   print('찾는 단어가 없습니다')
  else:
   continue
