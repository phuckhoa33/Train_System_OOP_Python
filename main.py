from GasStation.Train.Train import Train
from GasStation.PersonObject.User import User
from GasStation.PersonObject.Admin import Admin
from Enum.GenderEnum import GenderState
if __name__ == '__main__':
    # abc = HardChair("afa")
    # user = User("phuckhoa81@gmail.com", "nguyen khoa minh phuc", "sfafa", "0939672575", GenderState.MALE)
    # abc.set_ownership(user)
    # print(abc.displayInformation())
    # a = FirstHead("afaf", 3, 32, 32)
    # print(a.display())
    # a = HeadHeadManagementSystem(1)
    # user = User("phuckhoa81@gmail.com", "nguyen khoa minh phuc", 1, "0972495038", 0)
    # a.buy_ticket(user)
    # a.create_new_chair_or_room_or_insert_goods("soft")
    train = Train("afa", 1)
    user = User("phuckhoa81@gmail.com", "nguyen khoa minh phuc", 1, "0972495038", 0)
    train.display(user)