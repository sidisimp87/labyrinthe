import os
def afficher(ms: object) -> object:
    '''
    :param ms: Massage à afficher
    :return: les message simple

    '''

    print('\n','Type = '.upper(),type(ms))
    print('\n', 'Resultat = '.upper(), (ms))
    # print('Help = '.upper(),help(adv))
if __name__ == '__main__':
    # arg= 'salut les gars !'
    arg=os.path.join('')
    afficher(arg)
    arg = os.path.join('sidiki')
    afficher(arg)


    # print('help ==='.upper()
    # help(os.path.split(''))



