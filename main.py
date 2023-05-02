
from Enum.GenderEnum import GenderState
from configuration.Database import MysqlDatabaseConnection
from GasStation.Train.Wagon.WagonManagmentSystem import HeadHeadManagementSystem
from Enum.WagonEnum import WagonType
if __name__ == '__main__':
    # abc = HardChair("afa")
    # user = User("phuckhoa81@gmail.com", "nguyen khoa minh phuc", "sfafa", "0939672575", GenderState.MALE)
    # abc.set_ownership(user)
    # print(abc.displayInformation())
    # a = FirstHead("afaf", 3, 32, 32)
    # print(a.display())
    a = HeadHeadManagementSystem(1)