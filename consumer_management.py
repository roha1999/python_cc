import consumer as cm
 
class ConsumerManagement:
    def __init__(self):
        self.__consumer_list=[]
 
 
    def add_consumer_details(self,consumer_id,consumer_name,units_consumed):
 #Fill your code here
        p_obj=cm.Consumer(consumer_id,consumer_name,units_consumed)
        p_obj.calculate_total_charges()
        self.__consumer_list.append(p_obj)
        return
  
    def view_consumer_details(self, units_consumed):
#Fill your code here
        con_dict={}
        for i in self.__consumer_list:
            if i.get_units_consumed()>units_consumed:
                con_dict[i.get_consumer_id()]=i.get_total_charges()
        return con_dict 