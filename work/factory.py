from basic_practice.work.police import Police
from basic_practice.work.timo import Timo


class HeroFactory:

    def create_factory(self, name):
        if name == 'timo':
            return Timo()
        elif name == 'police':
            return Police()
        else:
            raise Exception('该英雄不在英雄工厂')


hero_factory = HeroFactory()
hero_timo = hero_factory.create_factory('timo')
hero_police = hero_factory.create_factory('police')
hero_timo.fight(hero_police.hp, hero_police.power)
hero_timo.speak_lines()
hero_police.fight(hero_timo.hp, hero_timo.power)
hero_police.speak_lines()