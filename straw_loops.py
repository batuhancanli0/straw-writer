
glass_size = int(input())
straw_pos = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
kac_dolu=glass_size
for p in range((2*glass_size-straw_pos)//2+2):
    for i in range(straw_pos):
        for j in range(i):
            print(' ', end='')
        print('o', end='')
        print()
    # then the main part of the glass
    for o in range(glass_size-kac_dolu):
        for k in range(o):
            print(' ',end='')
        print('\\',end='')
        for n in range(straw_pos-1):
            print(' ', end='')



        print('o',end='')
        for c in range(2*(glass_size-o)-straw_pos):print(' ',end='')




        print('/',end='')

        print()
    for a in range(kac_dolu, 0, -1):
        bosluk_sayisi = glass_size - a
        yildiz_sayisi = a * 2
        for g in range(bosluk_sayisi):
            print(' ', end='')
        print('\\', end='')
        for h in range(yildiz_sayisi):
            print('*', end='')
        print('/', end='')
        print()

    # for the middle of glass
    for z in range(glass_size):
        print(' ', end='')
    print('--')
    # now, we need to print glass handle
    for k in range(glass_size):
        for o in range(glass_size):
            print(' ', end='')
        print('||', end='')
        print()
    kac_dolu=kac_dolu-1





# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE


