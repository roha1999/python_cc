class Consumer:
    def __init__(self,consumer_id,consumer_name,units_consumed):
        self.__consumer_id=consumer_id
        self.__consumer_name=consumer_name
        self.__units_consumed=units_consumed
        self.__total_charges=0.0
        return
    def get_consumer_id(self):
        return self.__consumer_id
 
    def set_consumer_id(self,consumer_id):
        self.__consumer_id=consumer_id
 
    def get_consumer_name(self):
        return self.__consumer_name

    def set_consumer_name(self,consumer_name):
        self.__consumer_name=consumer_name

    def get_units_consumed(self):
        return self.__units_consumed

    def set_units_consumed(self,units_consumed):
        self.__units_consumed=units_consumed

    def get_total_charges(self):
        return self.__total_charges

    def set_total_charges(self,total_charges):
        self.__total_charges=total_charges 

    def calculate_total_charges(self):
    # Fill your code here 
        if(self.__units_consumed>300):
            self.__total_charges=500+((self.__units_consumed-300)*3)
        elif(self.__units_consumed>100):
            self.__total_charges=100+((self.__units_consumed-100)*2)
        else:
            if(self.__units_consumed>=50):
                self.__total_charges=self.__units_consumed
            else:
                self.__total_charges=50
        return