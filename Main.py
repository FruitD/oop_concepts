from Pirates import Pirate
from Navy import Marine

Luffy = Pirate('Straw Hats', 'Monkey D. Luffy', 19, 'Gum-Gum', '1,500,000,000', 'Mayumi Tanaka')
Smoker = Marine('Captain', 'Smoker', 36, 'Plume-Plume', 'Mahito Ohba')
Sanji = Pirate('Straw Hats', 'Sanji Vinsmoke', 21, None, '330,000,000', 'Hiroaki Hirata')

print(Luffy.show_bounty())
print(Sanji.show_bounty())
print(Sanji.show_fruit())
print(Smoker.show_rank())
print(Smoker.show_fruit())
print(Luffy.show_va())
print(Sanji.show_crew())
