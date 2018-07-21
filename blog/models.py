# 다른 파일에 있는 것을 추가
from django.db import models
from django.utils import timezone

# 모델을 정의하는 코드(모델은 객체(object))
class Post(models.Model): 
  # 송성을 정의하기 위해, 필드마다 어떤 종류의 데이터 타입을 가지는지를 정해야 함
  # CharField - 글자 수 제한
  # TextField - 글자 수 제한 없음
  # DateTimeField - 날짜와 시간
  # ForeignKey - 다른 모델에 대한 링크
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  # publish 메서드 - 메서드 이름은 소문자와 언더스코어 사용
  def publish(self):
    self.published_date = timezone.now()
    self.save()

  # __던더 붙은 것은 매직 메소드
  def __str__(self):
    return self.title