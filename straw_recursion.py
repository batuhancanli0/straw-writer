
glass_size = int(input())
straw_pos = int(input())

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
#for outer loop
def counter(n,i,f):
    if n == 0:
        return
    #straw
    def boslukbasici(straw_pos):
        if straw_pos == 0:
            return

        print(' ', end='')
        boslukbasici(straw_pos - 1)

    def straw_basici(straw_pos, b):
        if straw_pos == 0:
            return

        boslukbasici(b - 1)
        print('o')

        straw_basici(straw_pos - 1, b + 1)

    # glass part
    #empty part
    def bosbardak(i,h):
        if i==0:
            return
        boslukbasici(h)
        print('\\', end='')
        boslukbasici(straw_pos - 1)
        print('o', end='')
        boslukbasici(2 * (glass_size - h) - straw_pos)
        print('/')
        bosbardak(i - 1, h + 1)
    # filled part


    def yildizlar(glass_size):
        if glass_size == 0:
            return
        print('*', end='')
        yildizlar(glass_size - 1)

    def bardakbasici(f, y, d):
        if f == 0:
            return

        boslukbasici(y - d+i)
        print('\\', end='')
        yildizlar(2 * f)
        print('/')

        bardakbasici(f - 1, y + 1, d)

    # bottom part of the glass
    def middleglass(p):
        if p == 0:
            return
        boslukbasici(glass_size)
        print('--')

    def bardaksapi(glass_size, o):
        if glass_size == 0:
            return

        boslukbasici(o)
        print('||')
        bardaksapi(glass_size - 1, o)

    straw_basici(straw_pos, 1)
    bosbardak(i,0)
    bardakbasici(f, glass_size, glass_size)
    middleglass(1)
    bardaksapi(glass_size, glass_size)
    counter(n - 1,i+1,f-1)


counter((2 * glass_size - straw_pos) // 2 + 2,0,glass_size)










# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

