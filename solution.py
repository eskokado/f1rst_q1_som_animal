from animal_sound_singleton import AnimalSoundSingleton, Cat, Dog

animal_sound = AnimalSoundSingleton()

while True:
    t_input = input("Digite ['1'-Gato | '2'-Cachorro | 'histórico'] (ou 'q' para finalizar): ")

    if t_input.lower() == 'q':
        print("Finalizando o programa.")
        break

    if t_input == '1':
        result = animal_sound.record_sound(Cat())
        print(result)
    elif t_input == '2':
        result = animal_sound.record_sound(Dog())
        print(result)
    elif t_input == 'histórico':
        for history in animal_sound.get_history().split('\n'):
            print(history)
