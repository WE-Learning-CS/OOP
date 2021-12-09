# 1. SRP 단일 책임 원칙
from enum import Enum

class UserRole(Enum):
	User  = 1
	Admin = 2

class User:
    def __init__(self, user_id, name, role):
        self.user_id = user_id
        self.name    = name
        self.role    = role
    
    def is_admin(self):
        return self.role == UserRole.Admin.name
    
    def greet(self):
        print(f"Hello, {self.name}")
    
    def create_order(self):
        pass

# create_order 함수는 SRP 규칙에 따라 다른 클래스에 속해 있어야 한다.

class User:
    def __init__(self, user_id, name, role):
        self.user_id = user_id
        self.name    = name
        self.role    = role
    
    def is_admin(self):
        return self.role == UserRole.Admin.name
    
    def greet(self):
        print(f"Hello, {self.name}")

class Order:
    def __init__(self):
        pass
    
    def create_order(self):
        pass

# create_order 메소드는 Order 클래스로 옴겨지므로서 User 클래스가 주문을 생성하는 책임까지 지지 않도록 되었다.



# 2. OCP(Open-Closed Principle) 개방-폐쇄 원칙

from abc import *

class Coupon(metaclass = ABCMeta):
    # Coupon 추상 클래스
    price = '쿠폰액'

    @abstractmethod
    def show_coupon(self):
        pass
 
class FirstuseCoupon(Coupon):
    price = 5000
    
    @classmethod
    def show_coupon(cls):
        return cls.price

class ChristmasCoupon(Coupon):
    price = 3000

    @classmethod
    def show_coupon(cls):
        return cls.price

class CouponCalculation:
    def caculate(self):
        price   = 0
        coupons = [FirstuseCoupon(), ChristmasCoupon()]

        for coupon in coupons:
            price += coupon.show_coupon()
        
        return price

a = CouponCalculation()
print(a.caculate())
# 8000

# 동작에는 문제가 없지만 만약 새로운 쿠폰이 추가되었다고 했을 때 기존에 있던 CouponCalculation 클래스 coupons 리스트에 새로운 쿠폰의 인스턴스를 넣어주는 수정을 해주어야 한다. 
# 낮은 결합도란, 하나의 변경이 발생할 때 다른 모듈과 객체로 변경에 대한 요구가 전파되지 않는 상태라고 할 수 있다. 새로운 쿠폰이 생길 때마다 수정이 일어나는 CouponCalculation 클래스는 쿠폰 클래스들과 결합도가 높다고 볼 수 있다.

class NewCouponCalculation:
    def caculate(self):
        price = 0
        for coupon in Coupon.__subclasses__():
            price += coupon.show_coupon()
        
        return price

b = NewCouponCalculation()
print(b.caculate())
# 8000

# 위와 같이 CouponCalculation를 변경하면 새로운 쿠폰의 클래스가 생겨도 CouponCalculation에 수정을 할 필요가 없어진다.



# 3. LSP(Liskov Substitution Principle) 리스코프 치환 원칙
class People:
    def __init__(self, name, gender, age):
        self.name   = name
        self.gender = gender
        self.age    = age

    def get_toilet(self):
        if self.gender == 'male':
            return "남자 화장실"
        
        elif self.gender == 'female':
            return "여자 화장실"

class Child(People):
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age)
    
    def get_toilet(self):
        if self.gender == 'male':
            if self.age <= 5:
                return '엄마 따라서 여자 화장실'
            return "남자 화장실"
        
        elif self.gender == 'female':
            return "여자 화장실"

yeongrok = People('송영록', 'male', 30)
print(yeongrok.get_toilet())
# 남자 화장실
minho    = Child('김민호', 'male', 5)
print(minho.get_toilet())
# 엄마 따라서 여자 화장실

# 상위 타입의 객체를 하위 타입의 객체로 치환해도 상위 타입을 사용하는 프로그램은 정상적으로 동작해야 한다. 
# 부모 클래스의 인스턴스인 영록이는 남자 화장실을 가지만 자식 클래스인 민호로 치환하면 여자 화장실을 간다. LSP 위반

class Rectangle:
    def __init__(self, width, height):
        self.width  = width
        self.height = height
    
    def set_width(self, value):
        self.width = value
    
    def set_height(self, value):
        self.height = value
    
    def get_area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, value):
        self.width  = value
        self.height = value
    
    def set_width(self, value):
        self.width  = value
        self.height = value
    
    def set_height(self, value):
        self.height = value
        self.width  = value

rectangle1 = Rectangle(2, 5)
rectangle2 = Square(5)

rectangle1.set_width(3)
rectangle1.set_height(10)
print(rectangle1.get_area())
# 30

rectangle2.set_width(3)
rectangle2.set_height(10)
print(rectangle2.get_area())
# 100


# 1. 하위 클래스는 부모 클래스에 정의된 것보다 사전조건을 엄격하게 만들면 안 된다.
# 2. 하위 클래스는 부모 클래스에 정의된 것보다 약한 사후조건을 만들면 안된다



# 4. ISP(Interface Segregation Principle) 인터페이스 분리 원칙

class People(metaclass = ABCMeta):
    # 인터페이스 (추상 클래스)
    @abstractmethod
    def sleep(self):
        pass
    
    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def enjoy_adult_video(self):
        pass

class Adult(People):
    # 클라이언트 
    def sleep(self):
        return '잠 쿨쿨'
    
    def eat(self):
        return '먹는다'
    
    def enjoy_adult_video(self):
        return '즐긴다'

class Child(People):
    # 클라이언트
    def sleep(self):
        return '어린이라서 9시에 잔다'
    
    def eat(self):
        return '먹는다'
    
    def enjoy_adult_video(self):
        pass
    
    # 어린이는 enjoy_adult_video 메서드를 이용할 수 없다.

# People 인터페이스는 자신을 사용하는 클라이언트 기준으로 분리해야 한다. Child 클라이언트가 사용하지 않을 메서드에 의존할 것을 강요하면 안 된다.



# 5. DIP(Dependency Inversion Principle) 의존 역전 원칙

# 클래스가 있을 때 어떤 클래스가 다른 클래스를 사용하는 관계에 있으면 사용하는 클래스를 상위 모듈, 사용 당하는 클래스를 하위 모듈이라고 한다.
# 클래스는 가능한 추상적으로 의존해야 하며 구체적으로 의존하면 안 된다.
class Sword:
    def __init__(self, damage):
        self.damage = damage

    def slash(self, other_character):
        other_character.get_damage(self.damage)

class Character:
    def __init__(self, name, hp, sword: Sword):
        self.name  = name
        self.hp    = hp
        self.sword = sword

    def attack(self, other_character):
        """다른 유저를 공격하는 메소드"""
        if self.hp > 0:
            self.sword.slash(other_character)
        else:
            print(self.name + "님은 쓰러져서 공격할 수 없습니다.")

    def change_sword(self, new_sword):
        """검을 바꾸는 메소드"""
        self.sword = new_sword

    def get_damage(self, damage):
        """캐릭터가 공격받았을 때 자신의 체력을 깎는 메소드"""
        if self.hp <= damage:
            self.hp = 0
            print(self.name + "님은 쓰러졌습니다.")
        else:
            self.hp -= damage

    def __str__(self):
        return f"{self.name}님은 hp: {self.hp}이(가) 남았습니다."

bad_sword  = Sword(100)
good_sword = Sword(200)

character_1 = Character("구본욱", 200, bad_sword)
character_2 = Character("김민호", 500, good_sword)

character_1.attack(character_2)
character_2.attack(character_1)

print(character_1)
print(character_2)

# 구본욱님은 쓰러졌습니다.
# 구본욱님은 hp: 0이(가) 남았습니다.
# 김민호님은 hp: 400이(가) 남았습니다.

# 상위 모듈인 Character가 하위 모듈인 Sword를 의존하고 있다. Sword의 메서드가 수정되거나 삭제되면 Character가 동작할 수 없게 된다.

class IWeapon(ABC):
    """무기 클래스"""
    @abstractmethod
    def use_on(self, other_character):
        pass

class Sword(IWeapon):
    """검 클래스"""
    def __init__(self, damage):
        self.damage = damage
        
    def use_on(self, other_character):
        other_character.get_damage(self.damage)

class Gun(IWeapon):
    """총 클래스"""
    def __init__(self, damage, num_rounds):
        self.damage = damage
        self.num_rounds = num_rounds
        
    def use_on(self, other_character):
        """총 사용 메소드"""
        if self.num_rounds > 0:
            other_character.get_damage(self.damage)
            self.num_rounds -= 1
        else:
            print("총알이 없어 공격할 수 없습니다")

class NewCharacter:
    def __init__(self, name, hp, weapon: IWeapon):
        self.name   = name
        self.hp     = hp
        self.weapon = weapon

    def attack(self, other_character):
        """다른 유저를 공격하는 메소드"""
        if self.hp > 0:
            self.weapon.use_on(other_character)
        else:
            print(self.name + "님은 쓰러져서 공격할 수 없습니다.")

    def change_sword(self, new_sword):
        """검을 바꾸는 메소드"""
        self.sword = new_sword

    def get_damage(self, damage):
        """캐릭터가 공격받았을 때 자신의 체력을 깎는 메소드"""
        if self.hp <= damage:
            self.hp = 0
            print(self.name + "님은 쓰러졌습니다.")
        else:
            self.hp -= damage

    def __str__(self):
        return f"{self.name}님은 hp: {self.hp}이(가) 남았습니다."

sword = Sword(5)
gun   = Gun(200, 10)

game_character_1 = NewCharacter("구본욱", 200, sword)
game_character_2 = NewCharacter("김민호", 500, gun)

game_character_1.attack(game_character_2)
game_character_2.attack(game_character_1)

print(game_character_1)
print(game_character_2)

# 구본욱님은 쓰러졌습니다.
# 구본욱님은 hp: 0이(가) 남았습니다.
# 김민호님은 hp: 495이(가) 남았습니다.

# 상위 모듈이 하위 모듈을 사용할 때 직접 인스턴스를 가져다 쓰지 말아야 한다. 
# 하위 모듈의 구체적인 내용에 상위 모듈이 의존하게 되어 하위 모듈에 변화가 있을 때마다 상위 모듈의 코드를 자주 수정해야 되기 때문이다.
