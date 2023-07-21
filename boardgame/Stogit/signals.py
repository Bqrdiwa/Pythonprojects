from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import StogitStats

@receiver(post_save,sender = StogitStats)
def updateStogitRankRole(sender, instance, **kwargs):
    rankPoints = instance.total_points
    if rankPoints < 0 < 400:
        instance.rank_role = 'Novice'
    elif 400 < rankPoints < 600:
        instance.rank_role = 'Beginner'
    elif 600 < rankPoints < 750:
        instance.rank_role = 'Apprentice'
    elif 750 < rankPoints < 1000:
        instance.rank_role = 'Journeyman'
    elif 1000 < rankPoints < 1300:
        instance.rank_role = 'Adept'
    elif 1300 < rankPoints < 1600:
        instance.rank_role = 'Skilled'
    elif 1600 < rankPoints < 2000:
        instance.rank_role = 'Expert'
    elif 2000 < rankPoints < 2300:
        instance.rank_role = 'Master'
    elif 2300 < rankPoints < 2600:
        instance.rank_role = 'Grandmaster'
    elif 2600 < rankPoints < 3000:
        instance.rank_role = 'Legend'
    elif rankPoints > 3000:
        rankPoints = rankPoints - 3000
        rankPoints = (rankPoints // 300)+1
        instance.rank_role = f'Legend <{rankPoints}>'
    instance.save()