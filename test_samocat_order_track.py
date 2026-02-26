
# Захарова Анастасия_финальный_проект_часть_2_38_кагорта_Инженер по тестированию расширенный.
import data
import sender_stand_request

def creat_order(): 
    response_order = sender_stand_request.create_order(data.order_body)
    track = response_order.json()["track"] 
    return track

def test_get_order():
    track =creat_order()
    response_get = sender_stand_request.get_order(track)
    assert response_get.status_code == 200
 

    




     
  
    
    
 







    