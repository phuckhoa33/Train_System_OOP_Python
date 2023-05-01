from GasStation.Train.Wagon.Chair import HardChair
from GasStation.User.User import User 
from Enum.GenderEnum import GenderState
from GasStation.Train.Wagon.Wagon import FirstHead

if __name__ == '__main__':
    # abc = HardChair("afa")
    # user = User("phuckhoa81@gmail.com", "nguyen khoa minh phuc", "sfafa", "0939672575", GenderState.MALE)
    # abc.set_ownership(user)
    # print(abc.displayInformation())
    a = FirstHead("afaf", 3, 32, 32)
    print(a.display())