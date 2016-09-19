from django.db import models


class Recipe(models.Model):
    """A preparation of food."""

    name = models.CharField(max_length=255)

    desc = models.TextField(null=True, blank=True)

    ingredients = models.ManyToManyField(
        'cookbook.Food',
        through='cookbook.Ingredient',
        through_fields=('recipe', 'food')
    )

    instructions = models.TextField(null=True, blank=True)

    class Meta(object):
        app_label = 'cookbook'
        default_related_name = 'recipes'

    def __unicode__(self):
        return self.name


class Food(models.Model):
    """An edible item."""

    name = models.CharField(max_length=255)

    class Meta(object):
        app_label = 'cookbook'
        default_related_name = 'foods'

    def __unicode__(self):
        return self.name


class Ingredient(models.Model):
    """A food that is used in a recipe."""

    recipe = models.ForeignKey(Recipe)

    food = models.ForeignKey(Food)

    # ex. 1/8 = 0.125, 1/4 = 0.250
    amount = models.DecimalField(max_digits=6, decimal_places=3,
                                 null=True, blank=True)

    # ex. tsp, tbsp, cup
    unit_of_measure = models.CharField(max_length=255)

    # ex. 2 cloves of garlic, minced
    desc = models.TextField()

    class Meta(object):
        app_label = 'cookbook'

    def __unicode__(self):
        return '{recipe}: {amount} {unit_of_measure} {food}'.format(
            recipe=self.recipe,
            amount=self.amount,
            unit_of_measure=self.unit_of_measure,
            food=self.food
        )
