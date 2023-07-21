from django.db import models
from main.models import User
from django.utils import timezone
import requests
from bs4 import BeautifulSoup
import  random
from colour import Color
from django import forms

class Stogit(models.Model):
    name = models.CharField(max_length=12,default='Stogit')
    online_players = models.IntegerField()
    online_lobbys = models.IntegerField()
    image = models.ImageField(upload_to='games_pics', default='stogit-cover.jpg')
    likes = models.IntegerField()
    available = models.BooleanField(default=True)
    
    def __str__(self):
        return 'Stogit'

class StogitStats(models.Model):
    player = models.OneToOneField(User,on_delete=models.CASCADE)
    total_points = models.IntegerField(default=0)
    rank_role = models.CharField(max_length=12,default='Novice')
    games_played = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    wins_streak = models.IntegerField(default=0)
    most_streak = models.IntegerField(default=0)
    first_match  = models.TimeField(default=timezone.now)
    def __str__(self):
        return self.player.username

class StogitGame(models.Model):
    modes = [('private','Private'),('public','Public')]
    lobbyName = models.CharField(max_length=16, unique=True)
    points = models.IntegerField(default=30)
    count = models.IntegerField(default=4)
    mode = models.CharField(max_length=12, choices=modes ,default='public')
    cardsUsed = models.CharField(max_length=1000000, default='')
    
    @property
    def creator(self):
        players = self.stogitplayer_set.all()
        for player in players:
            if player.role == 'ST':
                return player
        
    @property
    def players(self,):
        return self.stogitplayer_set.all()
  
    @property 
    def colorused(self):
        players = self.stogitplayer_set.all()
        color_used = []
        for i in players:
            color_used.append(i.color)
        return color_used

    @property 
    def playersin(self):
        return self.stogitplayer_set.all().count()
    
    @property
    def rounds(self):
        return StogitRound.objects.all().filter(gameRound=self)
            
    def Initiate(self):
        plo = self.players
        self.nextStoryTeller()
        used = []
        used_str = ''
        totalplayerscards = []
        ploc = plo.count()
        for i in range(ploc):
            lists = []
            lists_str = ''
            for i in range(6):
                number = random.randint(1,192)
                while number in used:
                    number = random.randint(1,192)
                lists.append(number)
                used.append(number)
                used_str += (','+str(number))
                lists_str += (','+str(number))
            lists_str= lists_str[1:]
            totalplayerscards.append(lists_str)
        
            
        used_str = used_str[1:]
        self.cardsUsed =  used_str
        self.save()
        for  index, player in enumerate(plo):
            print(player.userRelated.username+'alan ine: ' + player.role +'/ Initiate-forloop')
            if player.role == 'ST':
                StogitStatus.objects.create(player = player, cards = totalplayerscards[index], status = 'Telling story')
            else:
                StogitStatus.objects.create(player = player, cards = totalplayerscards[index], status  = 'Thinking on cards')
    def nextRound(self,cards):
        def newCard():
            attemp = 0
            card = str(random.randint(1,192))
            used_ones = self.cardsUsed.split(',')
            while card in used_ones:
                print(card +', denied attemp: ' + str(attemp))
                attemp += 1
                card = str(random.randint(1,192))
                if attemp > 192:
                    card= used_ones[random.randint(0,len(used_ones))]
                    attemp = 'YES'
            if attemp != 'YES':
                self.cardsUsed= self.cardsUsed+','+card
            self.save()
            return card
        self.nextStoryTeller()
        players = self.players
        for player in players:
            sStatus = player.status
            player_used =sStatus.cards.split(',') 
            for card in cards:
                if card in player_used:
                    player_used.pop(player_used.index(card))
                    ncard = newCard()
                    player_used.append(ncard)
                    break
            scard = ''
            for card in player_used:
                scard += card+','
            scard = scard[:-1]
            sStatus.cards = scard
            sStatus.save()
            if player.role =='ST':
                sStatus.status = 'Telling story'
            else:
                sStatus.status = 'Thinking on cards'
            sStatus.save()
    def nextStoryTeller(self):
        players = self.players
        for index, player in enumerate(players):
            if player.role =='ST':
                inde = index
                player.role = 'PL'
                player.save()
                if inde +1 == self.playersin:
                    inde = -1
                inde += 1
                pls = players[inde]
                pls.role = 'ST'
                pls.save()
                break
    def __str__(self):
        return self.lobbyName
class StogitPlayer(models.Model):
    roles = [('ST','گرداننده'),('PL','بازیکن')]
    def combination_color(self,color):
        def get_random_color_combination(hex_color):
            # Parse the input hex color into a `Color` object
            c = Color(hex_color)

            # Get the HSL values of the color
            h, s, l = c.get_hsl()

            # Determine whether to use a lighter or darker shade based on the lightness value
            if l < 0.5:
                l += random.uniform(0.2, 0.4)
            else:
                l -= random.uniform(0.1, 0.2)

            # Create a new `Color` object with the same hue and saturation, but a different lightness value
            contrast_color = Color(hsl=(h, s, l))

            # Return a tuple containing the input color and its contrasting color
            return (contrast_color.hex_l)
        colors = [color]
        for i in range(4):
            colors.append(get_random_color_combination(colors[i]))
        colors =  str(colors).replace('[', '').replace(']', '').replace(' ', '').replace('\'', '').replace('#', '')
        return colors
    def random_color(self,auto = 'True'):
        if auto == 'True':
            allowed_colors = ['red','green','blue','yellow','purple','pink','brown','grey']
            usedones  = self.gameRelated.colorused
            color  = allowed_colors[random.randint(0,7)]
            while color in usedones:
                color  = allowed_colors[random.randint(0,7)]
            self.color = color
        else:
            color = auto
            self.color = color
        
        combinationcolors = self.combination_color(color)
        self.profile =  '<svg viewBox="0 0 36 36" fill="none" role="img" xmlns="http://www.w3.org/2000/svg" width="80" height="80"><mask id=":r13:" maskUnits="userSpaceOnUse" x="0" y="0" width="36" height="36"><rect width="36" height="36" rx="72" fill="#FFFFFF"></rect></mask><g mask="url(#:r13:)"><rect width="36" height="36" fill="#0e2430"></rect><rect x="0" y="0" width="36" height="36" transform="translate(-4 -4) rotate(188 18 18) scale(1.2)" fill="#f5b349" rx="36"></rect><g transform="translate(-4 -4) rotate(8 18 18)"><path d="M15 21c2 1 4 1 6 0" stroke="#000000" fill="none" stroke-linecap="round"></path><rect x="11" y="14" width="1.5" height="2" rx="1" stroke="none" fill="#000000"></rect><rect x="23" y="14" width="1.5" height="2" rx="1" stroke="none" fill="#000000"></rect></g></g></svg>'
        self.save()
    
    @property
    def stats(self):
        return StogitStats.objects.get(player=self.userRelated)
        
    @property
    def status(self):
        return StogitStatus.objects.get(player= self)
    @property
    def round(self):
        return self.stogitround
    gameRelated = models.ForeignKey(StogitGame, on_delete=models.CASCADE)
    userRelated  = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.CharField(max_length=1200000, default ='')
    color = models.CharField(max_length=12, default='')
    role = models.CharField(max_length=2, choices=roles, default = 'PL')
    connected = models.CharField(max_length=12,default='False')
    
    def __str__(self):
        return self.userRelated.username

class StogitStatus(models.Model):
    player = models.OneToOneField(StogitPlayer, on_delete=models.CASCADE)
    cards = models.CharField(max_length=120000)
    status = models.CharField(max_length=48)
    point = models.IntegerField(default=0)

    def __str__(self):
        return self.player.userRelated.username
    
class StogitRound(models.Model):
    cardOwner = models.OneToOneField(StogitPlayer, on_delete=models.CASCADE)
    gameRound = models.ForeignKey(StogitGame, on_delete=models.CASCADE)
    selectedCard = models.CharField(max_length=4)
    votedCard = models.CharField(max_length=4,default='')
    story = models.CharField(max_length=3)
    

    def reset(self):
        rounds = StogitRound.objects.all().filter(gameRound= self.gameRound)
        for roun in rounds:
            roun.delete()


class HostForm(forms.Form):
    modes = [('private','Private'),('public','Public')]
    counts = [('4','4'),('5','5'),('5','5'),('6','6'),('7','7'),('8','8')]
    lobbyName = forms.CharField(max_length=12, widget=forms.TextInput(attrs={
        'class':'form',
        'id':'lobbyName',
        'placeholder':'Lobby name'
    }))
    mode = forms.ChoiceField(choices=modes, widget=forms.Select(attrs={
        'class':'form',
        'id':'mode',
        'placeholder': 'mode'
    }))
    points = forms.CharField(max_length=3,widget=forms.TextInput(attrs={
        'class':'form',
        'id':'points',
        'placeholder':'Points to win'
    }))
    count = forms.ChoiceField(choices=counts,widget=forms.Select(attrs={
        'class':'form',
        'id':'count',
    }))

    class Meta():
        model = StogitGame
        fields = ['lobbyName','mode','points','count']
        
    def clean_lobbyName(self):
        lobbyname= self.cleaned_data.get('lobbyName')
        try:
            StogitGame.objects.get(lobbyName=lobbyname)
            raise forms.ValidationError('Lobbyname already exists!')
        except:
            return lobbyname
    def clean_points(self):
        points = self.cleaned_data.get('points')
        try:
            points = int(points)
        except:
            raise forms.ValidationError('Points to win must be a digit')
        if   points > 100 or 10 > points :
            raise forms.ValidationError('Points must be between 10 and 100')
        return points
