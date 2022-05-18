import datetime
from django.utils import timezone

if __name__ == '__main__':
    a = timezone.now() - datetime.timedelta(days=1)
    print(a)