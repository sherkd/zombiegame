"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

import django
from django.test import TestCase
from game.classes.player import Player
from game.classes.moneybank import Bank
from game.classes.enemy import Enemy

# TODO: Configure your database in settings.py and sync before running tests.

class ViewTest(TestCase):
    """Tests for the application views."""
    
    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(ViewTest, cls).setUpClass()
            django.setup()

    def test_home(self):
        """Tests the home page."""
        response = self.client.get('/')
        self.assertContains(response, 'Home Page', 1, 200)      

    def test_survival(self):
        """Tests the survival page."""
        response = self.client.get('/survival')
        self.assertContains(response, 'Survival', 3, 200)

    def test_tournament(self):
        """Tests the tournament page."""
        response = self.client.get('/tournament')
        self.assertContains(response, 'Tournament', 3, 200)
        
    def test_groupfight(self):
        """Tests the recovery page."""
        response = self.client.get('/groupfight')
        self.assertContains(response, 'Groupfight', 1, 200)

    def test_fight(self):
        """Tests the fight page."""
        response = self.client.get('/fight')
        self.assertContains(response, 'Fight', 3, 200)

    def test_quest(self):
        """Tests the quest page."""
        response = self.client.get('/quest')
        self.assertContains(response, 'Quest', 3, 200)

    def testBank(self):
        bank = Bank(Player("name", 100, 10, ["cl"], 50, ["items"], 1, 20, 0, 0, 1))      
        self.assertEquals(0, bank.player.getBalance())
        bank.depositMoney(10)
        self.assertEquals(40, bank.player.getMoney())
        self.assertEquals(10, bank.player.getBalance())
        
    def testEnemy(self):
        en = Enemy("Henk", 3, 100, Weapon("Henk weapon", 5, 100), None)
        self.assertEquals("Henk", en.getName())
        self.assertEquals(3, en.getLevel())
        self.assertEquals(100, en.getHealth())
        self.assertEquals(None, en.getRewardItem())
        self.assertEquals(en.getLevel() * 2.2, en.getRewardMoney())
        self.assertEquals(en.getLevel() * 4.3, en.getRewardExp())

    def testPostgres(self):
        database = Postgres()
        print(database.getConnection())
        database.createDatabase()
        database.insertAccount()
        database.getAccount(12)
        #database.insertWeapon(Weapon("wep", 12, 200, 4, "sniper"))

    def testSearch(self):
        search = SearchLevel(Player("name", 100, 10, ["cl"], 50, ["items"], 1, 20, 0, 0, 1), 2)
        self.assertEquals("name", search.getPlayer().getUserName())
        search.startScouting()
        self.assertEquals(["cl", "scouting"], search.getPlayer().getCooldowns())
        self.assertEquals(1, search.getSeconds())

    def testSurvival(self):
        #Player(username, health, attack, cooldowns, money, items, weapons, level, experience, balance)
        surv = Survival(Player("name", 100, 10, ["cl"], 50, ["items"], 1, 20, 0, 0, 1), 1, 10)

        #Enemy(name, level, health, weapon, rewardItem)
        #en = Enemy("Henk", 3, 100, Weapon("Henk weapon", 5, 100), None)

        self.assertEquals(100, surv.player.getHealth())

        self.assertEquals(1, surv.getWaveCounter())

        surv.startOneWave()

        self.assertEquals(2, surv.getWaveCounter())
        self.assertEquals(90, surv.player.getHealth())

        surv.startOneWave()

        self.assertEquals(3, surv.getWaveCounter())
        self.assertEquals(70, surv.player.getHealth())

        surv.startOneWave()

        self.assertEquals(4, surv.getWaveCounter())
        self.assertEquals(40, surv.player.getHealth())

        surv.startOneWave()

        self.assertEquals(5, surv.getWaveCounter())
        self.assertEquals(0, surv.player.getHealth())

    def testTournament(self):
        enemy1 = Enemy("drakenslachter010", 13, 240, Weapon("waterpistool", 20, 300), None)
        enemy2 = Enemy("oreobakker12", 5, 160, Weapon("botermes", 10, 70), None)
        enemy3 = Enemy("swaggerboy111", 7, 180, Weapon("minigun", 30, 400), None)
        player1 = Player("bamboeknul69", 300, 70, [], 100, ["legendarische steekmes"], 10, 9000, 0, 0, 1)

        tournament = Tournament(player1, enemy3, 3)
        self.assertEquals(3, tournament.counter)   #ivm recursieve functie is vanaf hier ***
        tournament.startTournament()
       
        self.assertEquals("swaggerboy111", tournament.enemy.getName())
        self.assertEquals(270, tournament.player.getHealth())
        self.assertEquals(tournament.enemy.health, 110)
       
        tournament.attack()
       
        self.assertEquals(tournament.enemy.health, 40)
        self.assertEquals(tournament.player.getHealth(), 240) 
        self.assertEquals(player1.getCooldowns(), ["Tournament", "Tournament", "Tournament"]) 
        self.assertEquals(tournament.counter, 3) 
        tournament.attack()  
        self.assertEquals(tournament.enemy.health, -30)   #t/m hier voor counter == 3

       # self.assertEquals(3, tournament.counter)   #ivm recursieve functie is vanaf hier ***
       # tournament.startTournament()
       #
       # self.assertEquals("drakenslachter010", tournament.enemy.getName())
       # self.assertEquals(210, tournament.player.getHealth())
       # self.assertEquals(tournament.enemy.health, 240)
       #
       # tournament.attack()
       #
       # self.assertEquals(tournament.enemy.health, 170)
       # self.assertEquals(tournament.player.getHealth(), 190) # laatste attack van enemy1 voor zijn dood + eerste attack van enemy2 = 20+30
       # self.assertEquals(player1.getCooldowns(), ["Tournament"]) 
       # self.assertEquals(tournament.counter, 2) 
       # tournament.attack()  
       # tournament.attack()
       # tournament.attack()
       # self.assertEquals(tournament.enemy.health, -40)  
       # self.assertEquals(tournament.player.health, 130) #t/m hier voor counter == 2 

    def testWeapon(self):
        wep = Weapon("Wep", 10, 100)
        self.assertEquals("Wep", wep.getName())
        self.assertEquals(10, wep.getDamage())
        self.assertEquals(100, wep.getValue())
        self.assertEquals("", wep.getDescription())
        for x in range(20):
            print(random.randint(0, 4))

    def testPlayer(self):      
        player = Player("P", 100, 10, ["cooldown1", "cooldown2"], 100, ["item1", "item2"], [Weapon("SMG", 12, 120), Weapon("RPG", 12, 120)], 10, 0, 0, Weapon("Sniper", 12, 120))
        self.assertEquals("P", player.getUserName())
        """"
        self.assertEquals(100, player.getHealth())
        player.setHealth(50)
        self.assertEquals(50, player.getHealth())       

        self.assertEquals(10, player.getAttackDamage())
        player.setAttackDamage(12)
        self.assertEquals(12, player.getAttackDamage())

        self.assertEquals(["cooldown1", "cooldown2"], player.getCooldowns())
        player.addCooldown("cooldown3")
        self.assertEquals(["cooldown1", "cooldown2", "cooldown3"], player.getCooldowns())
        player.removeCooldown("cooldown2")
        self.assertEquals(["cooldown1", "cooldown3"],  player.getCooldowns())

        self.assertEquals(100, player.getMoney()) 
        player.setMoney(50)
        self.assertEquals(50, player.getMoney()) 

        self.assertEquals(["item1", "item2"], player.getItems())
        player.addItem("item3")
        self.assertEquals(["item1", "item2", "item3"], player.getItems())
        player.removeItem("item3") 
        self.assertEquals(["item1", "item2"], player.getItems())

        self.assertEquals(10, player.getLevel())
        player.increaseLevel()
        self.assertEquals(11, player.getLevel())

        self.assertEquals(0, player.getExperience())
        self.assertEquals(player.getLevel() * 140, player.getRequiredExp())
        player.setExperience(player.getRequiredExp() + 10)
        self.assertEquals((player.getLevel() * 140) + 10, player.getExperience())
        self.assertEquals(True, player.checkLevelUp())
        self.assertEquals(12, player.getLevel())
        self.assertEquals(130, player.getExperience())

        self.assertEquals(0, player.getBalance())
        player.setBalance(10)
        self.assertEquals(10, player.getBalance())

        print(player.getWeapons())
        player.removeWeapon(Weapon("SMG", 12, 120))
        print(player.getWeapons())

        self.assertEquals(player.getEquipedWeapon().getName(), "Sniper")
        player.setEquipedWeapon(player.getWeapons()[0])
        self.assertEquals(player.getEquipedWeapon().getName(), "RPG")
        self.assertEquals(player.getWeapons()[0].getName(), "Sniper
        """

    
