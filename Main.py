from OnePieceCharacters import Characters
from Pirates import Pirate
from Navy import Marine

Luffy = Pirate('Monkey D. Luffy', 19, 'Gum-Gum', 'Mayumi Tanaka', 'Straw Hats', '1,500,000,000')
Smoker = Marine('Smoker', 36, 'Plume-Plume', 'Mahito Ohba', 'Captain')
Sanji = Pirate('Sanji Vinsmoke', 21, None, 'Hiroaki Hirata', '330,000,000', 'Straw Hats')
Camie = Characters('Camie', 18, None, 'Haruna Ikezawa')

GoodGuys = [Luffy, Smoker, Sanji, Camie]

for i in range(len(GoodGuys)):
    print(GoodGuys[i].show_va())


print(Luffy.show_bounty())
print(Sanji.show_bounty())
print(Sanji.show_fruit())
print(Smoker.show_rank())
print(Smoker.show_fruit())
print(Luffy.show_va())
print(Sanji.show_crew())
