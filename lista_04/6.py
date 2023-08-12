entrada = float(input('Suponha que você foi à loja da Apple e realizou uma compra, qual foi o valor pago pela compra? R$'))

desconto15 = entrada - ( entrada * ( 15 / 100 ) )

desconto5 = entrada - ( entrada * ( 5 / 100 ) )

if entrada >= 6999:
    print(f'Parabéns, você ganhou 15% de desconto na compra! O valor total da sua compra é R${desconto15}')

else: print(f'Parabéns, você ganhou 5% de desconto na compra! O valor total da sua compra é R${desconto5}')