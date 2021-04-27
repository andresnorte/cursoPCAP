campo = range(0, 9)
def draw_campo(campo):
    print ("---------------------")

    for i in range(3):
        print ("|", campo[0+i*3], "|", campo[1+i*3], "|", campo[2+i*3], "|")
        print ("--------------------")


print(draw_campo(campo))
