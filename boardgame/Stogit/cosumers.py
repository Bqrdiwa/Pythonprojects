from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.db import database_sync_to_async
from .models import StogitPlayer, StogitGame, StogitStatus, StogitRound, StogitStats
from main.models import User
from channels.exceptions import StopConsumer

class StogitLobbyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.lobbyname = self.scope['url_route']['kwargs']['lobbyName']
        self.group_name = self.scope['url_route']['kwargs']['lobbyName'].replace(' ', '')

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
            
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        await self.command_handler('player-disconnect' ,data={'username':self.user.username})
        raise StopConsumer()

    async def receive(self, text_data):
        TEXT_DATA = json.loads(text_data)
        command = TEXT_DATA['command']
        
        if command == 'ping':
            await self.channel_layer.group_send(
                self.group_name,
                {
                    "type": "group_handler",
                    'command':'ping',
                    'start-time':TEXT_DATA['start-time'],
                    'username' :TEXT_DATA['username']
                }
            )
        elif command == 'join-player':
            await self.command_handler('player-join', data={'username' : TEXT_DATA['username']})
            print(self.scope['user'])
        
        elif command == 'change-profile':
            color = TEXT_DATA['color']
            await self.command_handler('player-change-profile',data={'color':color})
        
        elif command == 'disband':
            await self.command_handler('disband')
        elif command == 'start':
            await self.command_handler('start')
        elif command =='kick':
            await self.command_handler('kick',data={'username':TEXT_DATA['username']})
        elif command == 'leave':
            await self.command_handler('leave',data={'username':TEXT_DATA['username']})
            


    async def group_handler(self, data):
        command = data['command']
        if command == 'ping':
            await self.send(text_data=json.dumps({
                'command':'pong',
                'start-time':data['start-time'],
                'username':data['username']
            }))
            
        elif command == 'join-player':

            await self.send(text_data=json.dumps(
                {
                'command':'player-connect',
                'player_data':data['player-data']
                }))
            
        elif command == 'leave-player':
            await self.send(text_data=json.dumps(
                {
                'command':'player-disconnect',
                'username':data['username']
                }))
        elif command == 'remove-player':
            await self.send(text_data=json.dumps(
                {
                'command':'remove-player',
                'username':data['username']
                }
            ))
        elif command == 'change-profile-player':
            await self.send(text_data=json.dumps(
                {
                    'command':'change-profile',
                    'profile':data['profile'],
                    'color':data['color'],
                    'username':data['username']
                }
            ))
        elif command == 'disband':
            await self.send(text_data=json.dumps({
                'command':'disband'
            }))
        elif command == 'start':
            await self.send(text_data=json.dumps({
                'command':'start'
            }))
        
            
        


    @database_sync_to_async
    def create_player(self, username):
        self.user = User.objects.get(username = username)
        self.lobby = StogitGame.objects.get(lobbyName = self.lobbyname)
        self.player= StogitPlayer.objects.get(userRelated = self.user, gameRelated = self.lobby)
        self.player.connected = 'True'
        self.player.save()

    @database_sync_to_async
    def change_profile(self, color):
        self.player.random_color(color) 
        self.player.save()

    @database_sync_to_async
    def delete_room(self):
        self.lobby.delete()
    @database_sync_to_async
    def remove_player(self):
        self.player.connected = 'False'
        self.player.save()
        # players_Online = self.lobby.players
        # on_count = 0
        # for player in players_Online:
        #     if player.connected == 'True':
        #         on_count += 1
        # if on_count == 0:
        #     self.lobby.delete()
    @database_sync_to_async 
    def delete_player(self,username=False):
        if username == False:
            self.player.delete()
        else:
            user = User.objects.get(username = username)
            player = StogitPlayer.objects.get(userRelated = user) 
            player.delete()
        
    async def command_handler(self, command, data = None):
        if command == 'player-join':
            await self.create_player(data['username'])
            await self.channel_layer.group_send(
                self.group_name,
                {
                    "type": "group_handler",
                    'command':'join-player',
                    'player-data':{
                    'username': self.user.username,
                    'role':self.player.role,
                    'profile':self.player.profile,
                    'color':self.player.color}
                    
                }
            )
        elif command == 'player-disconnect':
            await self.remove_player()
            await self.channel_layer.group_send(
                self.group_name,
                {
                    "type": "group_handler",
                    'command':'leave-player',
                    'username':data['username']
                    
                }
            )
        elif command == 'player-change-profile':
            await self.change_profile(data['color'])
            username= self.user.username
            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type':'group_handler',
                    'command':'change-profile-player',
                    'color':data['color'],
                    'profile':self.player.profile,
                    'username': username
                }
                )
        elif command == 'disband':
            await self.delete_room()
            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type':'group_handler',
                    'command':'disband',
                    
                }
            )
        elif command == 'start':
            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type':'group_handler',
                    'command':'start'
                }
            )
        elif command == 'leave':
            await self.delete_player()
            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type':'group_handler',
                    'command':'remove-player',
                    'username': data['username']
                }
            )
        elif command == 'kick':
            await self.delete_player(username = data['username'])
            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type':'group_handler',
                    'command':'remove-player',
                    'username': data['username']
                }
            )
class StogitGameConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.gameName = self.scope['url_route']['kwargs']['lobbyName']
        self.group_name = 'Game-'+(self.scope['url_route']['kwargs']['lobbyName'].replace(' ', ''))

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

        
    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        raise StopConsumer()
    
    async def receive(self, text_data=None):
        TEXT_DATA = json.loads(text_data)
        command = TEXT_DATA['command']
        if command == 'ping':
            await self.send(json.dumps({
                'command':'pong',
                'latency':TEXT_DATA['ping']
            }))
        elif command == 'connect':
            await self.command_handeler('connect', data={'username':TEXT_DATA['username']})
        elif command == 'narrate':
            await self.command_handeler('st-narrate',data={'story':TEXT_DATA['story'],'card':TEXT_DATA['card']})
        elif command =='pl-pick':
            await self.command_handeler('pl-pick',data={'card':TEXT_DATA['card']})
        elif command =='get-status':
            await self.command_handeler('get-status',data={'username':TEXT_DATA['username']})
        elif command =='pl-vote':
            await self.command_handeler('pl-vote',data={'card':TEXT_DATA['card'],'username':TEXT_DATA['username']})
        elif command =='initiate-nextround':
            await self.command_handeler('initiate')
        elif command == 'get_data':
            await self.command_handeler('get_data',data={'type':TEXT_DATA['type']})
    async def group_handeler(self,data):
        command = data['command']
        if command == 'st-narrate':
            print(data['story'])
            await self.send(json.dumps({
                'command':'st-narrate',
                'story':data['story'],
                'card':data['card']
                
            }))
        elif command =='pl-pick':
            await self.send(json.dumps({
                'command':'pl-pick',
                'username':data['username'],
                'card':data['card'],
                'rounds':data['rounds']
            }))
        elif command =='initiate-vote':
            await self.send(json.dumps({
                'command':'initiate-vote',
                'cards':data['cards'],
                'story':data['story']
            }))
        elif command == 'pl-vote':
            await self.send(json.dumps({
                'command':'pl-vote',
                'card':data['card'],
                'rounds':data['rounds'],
                'username':data['username'],
                'correct':data['correct']
            }))
        elif command =='result':
            result = data['result']
            if data['win'] == 'T':
                winnerDATA = data['WD']
                await self.send(json.dumps({
                    'command':'result',
                    'win':'T',
                    'WD':winnerDATA,
                    'TC':data['truecard'],
                    'RD':result
                }))
            else:
                await self.send(json.dumps({
                    'command':'result',
                    'win':'F',
                    'RD':result,
                    'TC':data['truecard']
                }))
        elif command == 'initiate':
            await self.get_player(self.user.username)
            newcards = self.status.cards
            newrole = self.player.role
            await self.send(json.dumps({
                'command':'change',
                'role':newrole,
                'cards':newcards
            }))
    @database_sync_to_async
    def get_player(self,username):
        self.user = User.objects.get(username=username)
        self.game = StogitGame.objects.get(lobbyName=self.gameName)
        self.player = StogitPlayer.objects.get(userRelated = self.user,gameRelated=self.game)
        self.status = StogitStatus.objects.get(player= self.player)
        self.stats = StogitStats.objects.get(player=self.user)
    @database_sync_to_async
    def st_narrate(self,card,story):
        players = self.game.players
        for pl in players:
            Sstatus= pl.stogitstatus
            Sstatus.status = 'Picking cards'
            Sstatus.save()
        self.status.status = 'Waiting for players to pick cards'
        self.status.save()
        self.round = StogitRound.objects.create(cardOwner= self.player,gameRound=self.game,selectedCard=card,story = story)
    @database_sync_to_async    
    def pl_pick(self,card):
        self.round = StogitRound.objects.create(cardOwner= self.player,gameRound=self.game,selectedCard=card,story='PL')
        rounds = self.game.rounds
        self.status.status = 'Picked, Waiting for others to pick'
        self.status.save()
        
        
        if rounds.count() == self.game.playersin:
            cards = ''
            for round in rounds:
                card = round.selectedCard
                cards += (card+',')
            cards = cards[:-1]
            return True,rounds.count(),cards
        else:
            return False,rounds.count(),None
    @database_sync_to_async
    def initiate_vote(self):
        players = self.game.players
        print(players)
        for pl in players:
            Sstatus= pl.stogitstatus
            if pl.role =='ST':
                Sstatus.status = 'Watching players votes'
                Sstatus.save()
            else:   
                Sstatus.status = 'Voting cards'
                Sstatus.save()
    @database_sync_to_async
    def pl_vote(self,card):
        try :
            self.round
        except:
            self.round = StogitRound.objects.get(cardOwner= self.player,gameRound=self.game)
        self.round.votedCard = card
        self.round.save()
        sts = self.game.players
        correct ='False'
        for st in sts:
            if st.role =='ST' and st.round.selectedCard == card:
                correct ='True'
        self.status.status = 'Waiting for others to vote'
        self.status.save()
        players = self.game.players
        count = 0
        for plo in players:
            if plo.status.status == 'Waiting for others to vote':
                count += 1
        plc = self.game.playersin - 1
        if plc == count:
            return True,str(count)+'/'+str(plc),correct
        else:
            return False,str(count)+'/'+str(plc),correct
    @database_sync_to_async
    def initiate_result(self):
        players = self.game.players
        players_points = {}
        count = 0
        
        for player in players:
            player.status.status = 'Watching Result'
            player.status.save()
            players_points[player.userRelated.username] = 0
            if player.role =='ST':
                st= player
        for player in players:
            if player.role =='PL':
                round = player.round
                status = player.status
                if round.votedCard == st.round.selectedCard:
                    players_points[player.userRelated.username] += 3
                    count += 1
                    status.point = status.point + 3
                    status.save()
                else:
                    plwinner = StogitRound.objects.get(selectedCard=round.votedCard).cardOwner
                    players_points[plwinner.userRelated.username] += 1
                    status = plwinner.status
                    status.point = status.point + 1
                    status.save()
        if count != self.game.rounds.count()-1 and count > 0:
            players_points[st.userRelated.username] += 3
            status = st.status
            status.point = status.point + 3
            status.save()
        truecard = st.round.selectedCard
        for player in self.game.players:
            if player.status.point >= self.game.points:
                return players_points, player.userRelated.username,truecard
        return players_points,False,truecard
    @database_sync_to_async
    def initiate(self):
        cards_used = []
        for round in self.game.rounds:
            cards_used.append(round.selectedCard)
        self.round.reset()
        self.game.nextRound(cards_used)

    @database_sync_to_async
    def deleteRoom(self):
        self.game.delete()

    @database_sync_to_async
    def get_data(self,type):
        if type == 'voteCards':
            cards = ''
            usernames = ''
            rounds = self.game.rounds
            for round in rounds:
                card = round.selectedCard
                usernames += (round.cardOwner.userRelated.username+',')
                cards += (card+',')
            cards = cards[:-1]
            usernames = usernames[:-1]
            return cards, usernames
        elif type =='pickCards':
            rounds = self.game.rounds
            for round in rounds:
                print(round.story)
                if round.story != 'PL':
                    story = round.story
            return story
                    
    @database_sync_to_async
    def get_status(self,username):
        status = User.objects.get(username=username).stogitplayer_set.get().status.status
        return status
    @database_sync_to_async
    def get_round(self):
        self.round = StogitRound.objects.get(cardOwner= self.player,gameRound=self.game)
    @database_sync_to_async
    def save_informations(self):
        for player in self.game.players:
            stats = player.stats
            if player.status.point >= self.game.points:
                stats.total_points = player.stats.total_points + player.status.point
                stats.games_played = stats.games_played + 1
                stats.wins = stats.wins +1
                stats.wins_streak = stats.wins_streak +1
                if stats.wins_streak > stats.most_streak:
                    stats.most_streak = stats.wins_streak
            else:
                stats.total_points = player.stats.total_points - (self.game.points - player.status.point)
                stats.games_played = stats.games_played + 1
                stats.losses = stats.losses + 1
            stats.save()
    @database_sync_to_async
    def get_stats(self,username):
        statsData = {}
        player = User.objects.get(username=username).stogitplayer_set.get()
        stats = player.stats
        statsData['U'] = username
        statsData['P'] = player.profile
        statsData['TP'] = stats.total_points
        statsData['RR'] = stats.rank_role
        statsData['GP'] = stats.games_played
        statsData['W'] = stats.wins
        statsData['L'] = stats.losses
        statsData['WS'] = stats.wins_streak
        statsData['MS'] = stats.most_streak
        statsData['FM'] = stats.first_match.strftime('%Y-%m-%d')
        return statsData
                
        
    async def command_handeler(self,command,data=None):

        if command == 'connect':
            await self.get_player(data['username'])
            status = self.status.status
            await self.send(json.dumps({
                    'command':'reconnect-data',
                    'phase':'baseView',
                    'status':status
                }))

        elif command == 'st-narrate':
            await self.st_narrate(data['card'],data['story'])
            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type':'group_handeler',
                    'command':'st-narrate',
                    'story':data['story'],
                    'card':data['card']
                }
            )
        elif command == 'pl-pick':
            HA,rounds,cards = await self.pl_pick(data['card'])
            await self.channel_layer.group_send(
                self.group_name,
                {
                    'type':'group_handeler',
                    'command':'pl-pick',
                    'card':data['card'],
                    'username':self.user.username,
                    'rounds':rounds
                }
            )
            
            if HA == True:
                await self.initiate_vote()
                story = await self.get_data('pickCards')
                await self.channel_layer.group_send(
                    self.group_name,
                    {
                        'type':'group_handeler',
                        'command':'initiate-vote',
                        'cards':cards,
                        'story':story
                    }
                )
        elif command == 'get-status':
            status = await self.get_status(data['username'])
            await self.send(json.dumps({
                'command':'pong-status',
                'status':status,
                'username':data['username']
            }))
        elif command == 'pl-vote':
            try :
                self.round.selectedCard
            except:
                await self.get_round()
            if data['card'] == self.round.selectedCard:
                await self.send(json.dumps({
                    'command':'error',
                    'msg':'You can\'t vote for your own card'
                }))
            else:
                gonext,whodo,correct = await self.pl_vote(data['card'])
                await self.channel_layer.group_send(
                    self.group_name,
                    {
                        'type':'group_handeler',
                        'command':'pl-vote',
                        'card':data['card'],
                        'rounds':whodo,
                        'username':data['username'],
                        'correct':correct
                    }
                )

                if gonext:
                    points_earned,win_or_not,truecard = await self.initiate_result()
                    if win_or_not:
                        await self.save_informations()
                        winner_data = await self.get_stats(win_or_not)
                        await self.channel_layer.group_send(
                            self.group_name,
                            {
                                'type':'group_handeler',
                                'command':'result',
                                'result':points_earned,
                                'WD':winner_data,
                                'truecard':truecard,
                                'win':'T'
                            }
                        )
                        await self.deleteRoom()
                    else:
                        await self.channel_layer.group_send(
                            self.group_name,
                            {
                                'type':'group_handeler',
                                'command':'result',
                                'result':points_earned,
                                'truecard':truecard,
                                'win':'F'
                            }
                        )
        elif command == 'initiate':
            try: 
                self.round.selectedCard
            except:
                await self.get_round()
            if self.player.role == 'ST':
                await self.initiate()
                await self.channel_layer.group_send(
                    self.group_name,
                    {
                        'type':'group_handeler',
                        'command':'initiate'
                    }
                )
        elif command == 'get_data':
            dataType = data['type']
            if dataType == 'pickCards':
                story = await self.get_data('pickCards')
                await self.send(json.dumps({
                    'command':'reconnect-data',
                    'phase':'pickCards',
                    'story':story
                }))
            elif dataType == 'voteCards':
                story = await self.get_data('pickCards')
                cards, usernames = await self.get_data('voteCards')
                await self.send(json.dumps({
                    'command':'reconnect-data',
                    'phase':'voteCards',
                    'story':story,
                    'cards':cards,
                    'usernames':usernames
                }))
