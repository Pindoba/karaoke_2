# import datetime
import time



# def hora_atualiza():
#     hora = datetime.datetime.now()
#     hora_str = hora.strftime("%H:%M")
#     forme.label_4.setText(hora_str)
#     print(hora_str)



from main import hora_atualiza
def my():

    while 1:
        hora_atualiza()
        time.sleep(2)