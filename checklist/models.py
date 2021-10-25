from django.db import models


class Card(models.Model):
    DEFAULT = '-'

    IV_JUDGE_CHOICES = [
        ('DEFAULT', '-'),
        ('NO_GOOD', 'No Good'),
        ('DECENT', 'Decent'),
        ('PRETTY_GOOD', 'Pretty Good'),
        ('VERY_GOOD', 'Very Good'),
        ('FANTASTIC', 'Fantastic'),
        ('BEST', 'Best')
    ]

    NATURE_CHOICES = [
        ('DEFAULT', '-'),
        ('HARDY','Hardy'),
        ('LONELY','Lonely'),
        ('BRAVE','Brave'),
        ('ADAMANT','Adamant'),
        ('NAUGHTY','Naughty'),
        ('BOLD','Bold'),
        ('DOCILE','Docile'),
        ('RELAXED','Relaxed'),
        ('IMPISH','Impish'),
        ('LAX','Lax'),
        ('TIMID','Timid'),
        ('HASTY','Hasty'),
        ('SERIOUS','Serious'),
        ('JOLLY','Jolly'),
        ('NAIVE','Naive'),
        ('MODEST','Modest'),
        ('MILD','Mild'),
        ('QUIET','Quiet'),
        ('BASHFUL','Bashful'),
        ('RASH','Rash'),
        ('CALM','Calm'),
        ('GENTLE','Gentle'),
        ('SASSY','Sassy'),
        ('CAREFUL','Careful'),
        ('QUIRKY','Quirky')
    ]

    

    dexid = models.PositiveSmallIntegerField(primary_key=True)
    poke_name = models.CharField(max_length=12, default="pokemon ?")
    image = models.ImageField(default=None)
    poke_sprite = models.ImageField(default=None)
    shiny_sprite = models.ImageField(default=None)
    type1 = models.CharField(max_length=12, default=None, blank=True, null=True)
    type2 = models.CharField(max_length=12, default=None, blank=True, null=True)
    is_default = models.BooleanField(default=False)
    ability1 = models.CharField(max_length=25, default="ability ?", blank=True, null=True)
    ability2 = models.CharField(max_length=25, default="ability ?", blank=True, null=True)
    hidden_ability = models.CharField(max_length=25, default=None, blank=True, null=True)
    generation = models.CharField(max_length=25, default="unknown")
    evolves_from_species = models.CharField(max_length=12, default=None, blank=True, null=True)
    is_legendary = models.BooleanField(default=False)
    is_mythical = models.BooleanField(default=False)
    gender_rate = models.SmallIntegerField(default=4)
    gender_differences = models.BooleanField(default=False)
    hp_iv = models.CharField(max_length=12, choices=IV_JUDGE_CHOICES, default=DEFAULT)
    attack_iv = models.CharField(max_length=12, choices=IV_JUDGE_CHOICES, default=DEFAULT)
    defense_iv = models.CharField(max_length=12, choices=IV_JUDGE_CHOICES, default=DEFAULT)
    sp_attack_iv = models.CharField(max_length=12, choices=IV_JUDGE_CHOICES, default=DEFAULT)
    sp_defense_iv = models.CharField(max_length=12, choices=IV_JUDGE_CHOICES, default=DEFAULT)
    speed_iv = models.CharField(max_length=12, choices=IV_JUDGE_CHOICES, default=DEFAULT)
    hp_iv_shiny = models.CharField(max_length=12, choices=IV_JUDGE_CHOICES, default=DEFAULT)
    attack_iv_shiny = models.CharField(max_length=12, choices=IV_JUDGE_CHOICES, default=DEFAULT)
    defense_iv_shiny = models.CharField(max_length=12, choices=IV_JUDGE_CHOICES, default=DEFAULT)
    sp_attack_iv_shiny = models.CharField(max_length=12, choices=IV_JUDGE_CHOICES, default=DEFAULT)
    sp_defense_iv_shiny = models.CharField(max_length=12, choices=IV_JUDGE_CHOICES, default=DEFAULT)
    speed_iv_shiny = models.CharField(max_length=12, choices=IV_JUDGE_CHOICES, default=DEFAULT)
    hp_ev = models.SmallIntegerField(default=0) # For later implementation
    attack_ev = models.SmallIntegerField(default=0) # For later implementation
    defense_ev = models.SmallIntegerField(default=0) # For later implementation
    sp_attack_ev = models.SmallIntegerField(default=0) # For later implementation
    sp_defense_ev = models.SmallIntegerField(default=0) # For later implementation
    speed_ev = models.SmallIntegerField(default=0) # For later implementation
    caught = models.BooleanField(default=False)
    caught_shiny = models.BooleanField(default=False)
    nature = models.CharField(max_length=12, choices=NATURE_CHOICES, default=DEFAULT)
    nature_shiny = models.CharField(max_length=12, choices=NATURE_CHOICES, default=DEFAULT)
    ability = models.CharField(max_length=25, default="ability", null=True, blank=True)
    ability_shiny = models.CharField(max_length=25, default="ability", null=True, blank=True)
    pokeball = models.BooleanField(default=False)
    pokeball_shiny = models.BooleanField(default=False)
    pokeball_img = models.ImageField(default=1)
    greatball = models.BooleanField(default=False)
    greatball_shiny = models.BooleanField(default=False)
    greatball_img = models.ImageField(default=1)
    ultraball = models.BooleanField(default=False)
    ultraball_shiny = models.BooleanField(default=False)
    ultraball_img = models.ImageField(default=1)
    masterball = models.BooleanField(default=False)
    masterball_shiny = models.BooleanField(default=False)
    masterball_img = models.ImageField(default=1)
    safariball = models.BooleanField(default=False)
    safariball_shiny = models.BooleanField(default=False)
    safariball_img = models.ImageField(default=1)
    levelball = models.BooleanField(default=False)
    levelball_shiny = models.BooleanField(default=False)
    levelball_img = models.ImageField(default=1)
    lureball = models.BooleanField(default=False)
    lureball_shiny = models.BooleanField(default=False)
    lureball_img = models.ImageField(default=1)
    moonball = models.BooleanField(default=False)
    moonball_shiny = models.BooleanField(default=False)
    moonball_img = models.ImageField(default=1)
    friendball = models.BooleanField(default=False)
    friendball_shiny = models.BooleanField(default=False)
    friendball_img = models.ImageField(default=1)
    loveball = models.BooleanField(default=False)
    loveball_shiny = models.BooleanField(default=False)
    loveball_img = models.ImageField(default=1)
    heavyball = models.BooleanField(default=False)
    heavyball_shiny = models.BooleanField(default=False)
    heavyball_img = models.ImageField(default=1)
    fastball = models.BooleanField(default=False)
    fastball_shiny = models.BooleanField(default=False)
    fastball_img = models.ImageField(default=1)
    sportball = models.BooleanField(default=False)
    sportball_shiny = models.BooleanField(default=False)
    sportball_img = models.ImageField(default=1)
    premierball = models.BooleanField(default=False)
    premierball_shiny = models.BooleanField(default=False)
    premierball_img = models.ImageField(default=1)
    repeatball = models.BooleanField(default=False)
    repeatball_shiny = models.BooleanField(default=False)
    repeatball_img = models.ImageField(default=1)
    timerball = models.BooleanField(default=False)
    timerball_shiny = models.BooleanField(default=False)
    timerball_img = models.ImageField(default=1)
    nestball = models.BooleanField(default=False)
    nestball_shiny = models.BooleanField(default=False)
    nestball_img = models.ImageField(default=1)
    netball = models.BooleanField(default=False)
    netball_shiny = models.BooleanField(default=False)
    netball_img = models.ImageField(default=1)
    diveball = models.BooleanField(default=False)
    diveball_shiny = models.BooleanField(default=False)
    diveball_img = models.ImageField(default=1)
    luxuryball = models.BooleanField(default=False)
    luxuryball_shiny = models.BooleanField(default=False)
    luxuryball_img = models.ImageField(default=1)
    healball = models.BooleanField(default=False)
    healball_shiny = models.BooleanField(default=False)
    healball_img = models.ImageField(default=1)
    quickball = models.BooleanField(default=False)
    quickball_shiny = models.BooleanField(default=False)
    quickball_img = models.ImageField(default=1)
    duskball = models.BooleanField(default=False)
    duskball_shiny = models.BooleanField(default=False)
    duskball_img = models.ImageField(default=1)
    cherishball = models.BooleanField(default=False)
    cherishball_shiny = models.BooleanField(default=False)
    cherishball_img = models.ImageField(default=1)
    dreamball = models.BooleanField(default=False)
    dreamball_shiny = models.BooleanField(default=False)
    dreamball_img = models.ImageField(default=1)
    beastball = models.BooleanField(default=False)
    beastball_shiny = models.BooleanField(default=False)
    beastball_img = models.ImageField(default=1)


    
    def __str__(self):
        return self.poke_name