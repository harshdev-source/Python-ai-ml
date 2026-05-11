class laptop:
    storage_type = "SSD"

    def __init__(self,RAM,storage):
        self.RAM = RAM
        self.storage = storage


# ------------------CLASS METHODS------------------

    @classmethod #----------DECORATOR----------- it changed the behaviour the this class method
    def get_storage_type(cls):
        print(f"Storage type = {cls.storage_type}")



    def get_info(self):  # Instance Methods
        print(self.RAM,self.storage ,"\t", self.storage_type )



#------------------Static Method------------------
    @staticmethod
    def calc_discount(price, discount):
        final_price = price - (discount * price/100)
        print(f"final price = {final_price}")



l1 = laptop("16GB","512GB")
l2 = laptop("32GB","256GB")

l1.get_info()

laptop.get_storage_type()
l1.calc_discount(40_000,10)