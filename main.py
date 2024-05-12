import random

SUIT_TUPLE = ('Крести','Черви','Пики','Буби')
RANK_TUPLE = ('ТУЗ','2','3','4','5','6','7','8','9','10','Валет','Дама','Король','Джокер')

NCARDS = 8

def getCard (descListIn):
    thisCard = descListIn.pop()

    return thisCard

def shuffle (descListIn):
    deckListOut = descListIn.copy()
    random.shuffle(deckListOut)
    return deckListOut

print('Добро пожаловать в игру больше или меньше')
print('Тебе надо выбрать будет ли следующая карта больше или меньше')
print('За каждую правильную карту ты получаешь 20 очков')
print('За каждую неправильную с тебя снимают 15 очков')
print('Для начала у тебя есть 50 очков')
print()

startingDeckList = []

for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank':rank, 'suit':suit, 'value':thisValue+1}
        startingDeckList.append(cardDict)

point = 50

while True:
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print('Начальная карта это: ', currentCardRank + ' масти ' + currentCardSuit)
    print()

    for cardNumber in range(0,NCARDS):

        answer = input('Следующая карта будет больше или меньше: ' + currentCardRank + ' ' + currentCardSuit + '?' + '\nВведите "h" если считайте что больше "l" если считайте меньше\n>>')

        answer = answer.casefold()
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']

        print('Следующая карта это: ' + nextCardRank + ' масти ' + nextCardSuit)

        if answer == 'h':
            if nextCardValue > currentCardValue:
                print('Ты угадал!')
                point += 20
            else:
                print('Ты не угадал!')
                point -= 15

        elif answer == 'l':
            if nextCardValue < currentCardValue:
                point += 20
                print('Ты прав!')

            else:
                point -= 15
                print('Ты не прав!')

        print('У тебя ' + str(point) + ' очков')
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue

        goAgain = input('Чтобы сыграть снова нажми ENTER, или напиши "выйти" чтобы игра закончилась \n>>')
        if goAgain == 'выйти':
            break

print('Пока')