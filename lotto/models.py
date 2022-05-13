from django.db import models
from django.utils import timezone
import random

# Create your models here.
# DB's object : Row (DB record)
class GuessNumbers(models.Model):
    name = models.CharField(max_length=24) # 로또 번호 리스트의 이름
    text = models.CharField(max_length=255) # 로또 번호 리스트에 대한 설명
    lottos = models.CharField(max_length=255, default='[1, 2, 3, 4, 5, 6]') # 로또 번호들이 담길 STATIC_ROOT
    num_lotto = models.IntegerField(default=5) # 6개 번호 set의 개수
    update_data = models.DateTimeField()

    def generate(self): # 로또 번호를 자동으로 생성
        self.lottos = ""
        origin = list(range(1,46))
        # 6개 번호 set 개수만큼 1~46 뒤섞은 후 앞의 6개 골라내어 sorting
        for _ in range(0, self.num_lotto):
            random.shuffle(origin)
            guess = origin[:6]
            guess.sort()
            self.lottos += str(guess) + '\n' # 로또 번호 str에 6개 번호 set 추가
        self.update_data = timezone.now()
        self.save() # GuessNumbers object를 DB에 저장

    def __str__(self): # Admin page에서 display되는 텍스트에 대한 변경
        return "pk {} : {} - {}".format(self.pk, self.name, self.text) # pl 자동생성
