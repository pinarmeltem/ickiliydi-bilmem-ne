import random
import time
import sys

speech = [
        'Busecim geldi araba',
        '-Bayağı kalabalık kadroyla gelmişsiniz.',
        'Ya, hadi biz-',
        '-ilişkiniz nasıl gidiyor? Onu konuşalım',
        '-Kim o, nerede o?',
        '-Ya siktir git. Ya salak salak so-']

generic_questions = [
        'Kim o, nerede o?',
        'Ne salak salak sorular soruyorsun ya?',
        'Ne kadar salak salak sorular soruyorsun ya?'
        ]

x_questions = [
        'Kaç yaşındasın sen?',
        'Bir dakika kaç yaşındasın sen? Hayır, kaç yaşındasın sen?',
        'Kaç yaşındasın sen? Bana yaşını söyle.',
        'Hayır, yaşını söyle bana! Kaç yaşındasın sen?']

expressions = [
        'Bir dakika abicim, bıraksanıza beni.',
        'Oğlum bak, oğlum bak normali bunun nedir biliyor musun? "Ozan Bey iyi akşamlar ilişkiniz na-"',
        'Ne salak salak sorular soruyorsun ya?']

monologue = [
        'Dalyarrak böyle mi sorulur bu "ilişkiniz nasıl gidiyor?"',
        'Ben sana soruyor muyum "kimi sikiyorsun" diye, soruyor muyum?',
        'Yani, ne kadar aptal aptal-',
        'Bir dakika abicim öyle bir şey yok bir dakika dur ya.',
        'Ya bir dakika, ya Feridun abi, abi ne kadar aptal aptal sorular bunlar ya "ilişkiniz nasıl gidiyor"',
        ]

reply = 'Kötü bir soru sormadım ki size'
nodes = ['feridun', 'timurlenk', 'gazeteci_1', 'gazeteci_2']

for s in speech:
    time.sleep(1)
    print(s)

ozan_has_not_found_node = True
status = 'searching ...'

while ozan_has_not_found_node:
    target = random.choice(nodes)

    # Search for target
    print('Kim dedi onu? Kim dedi onu?! Hanginiz dedi? -> [{0}] -> {1}'.format(target, status))
    time.sleep(1)

    # Target found
    if target =='gazeteci_1':
        ozan_has_not_found_node = False
        status = 'found'

        x_question_count = len(x_questions)
        x_question_index_list = []
        x_question_ask_count = 2

        # Generate X random question from the questions list.
        for i in range(x_question_ask_count):
            x_question_index = random.randint(0,x_question_count)
            x_question_index_list.append(x_question_index)

        # Question loop here
        x_question_index_list_length = len(x_question_index_list)
        for q in range(x_question_index_list_length):
            time.sleep(1)
            print('\t{0}'.format(x_questions[q]))
            time.sleep(1)

        age = input("\t\tBana yasini soyle!: ")
        # debug age
        age = 16
        time.sleep(1)
        print('\t\t... amcık ağızlı sen kimsin lan {0} yasinda bir adamsin!'.format(age))
        time.sleep(1)
        print('\t\t...sen kimsin lan, sen kimsin ağbii? Sen kimsin?')
        time.sleep(2)
    else:
        gen_question_count = len(generic_questions)
        gen_question_index_list = []
        gen_question_ask_count = 2

        # Generate X random question from the questions list.
        for i in range(gen_question_ask_count):
            gen_question_index = random.randint(0, gen_question_count-1)
            # print(gen_question_index)
            gen_question_index_list.append(gen_question_index)

        # Question loop here
        gen_question_index_list_length = len(gen_question_index_list)
        for q in range(gen_question_index_list_length):
            time.sleep(1)
            _index = gen_question_index_list[q]
            print('\t{0}'.format(generic_questions[_index]))
            time.sleep(1)

# Choose random expression
print('{0}'.format(random.choice(expressions)))

for m in monologue:
    time.sleep(1)
    print(m)

time.sleep(2)
print("Sonra yazacaklar 'Ickiliydi bilmem ne!'")
