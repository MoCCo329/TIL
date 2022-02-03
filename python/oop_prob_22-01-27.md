## 객체지향 프로그래밍 문제

### 1. 딕셔너리 뒤집기

내 답

```python
def dict_invert(my_dict):
    invert_datas = list(zip(my_dict.values(), my_dict.keys()))
    dict_temp = dict()
    
    for data_1 in invert_datas:
        temp = []
        for data_2 in invert_datas:
            if data_1[0] == data_2[0]:
                temp.append(data_2[1])
                        
        dict_temp[data_1[0]] = temp
    
    return dict_temp
```

우수 답

```python
def dict_invert(my_dict):
    result = {}
    for key, value in my_dict.items():
        result[value] = result.get(value, []) + [key]
    return result
```

get으로 기존에 같은 값이 있는지 찾고, + 연산으로 리스트에 더할 수 있었다.



### 2. Doggy 클래스 만들기

```python
class Doggy:
    global birth_of_dogs
    global num_of_dogs
    birth_of_dogs = 0
    num_of_dogs = 0
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        global birth_of_dogs
        global num_of_dogs
        
        birth_of_dogs += 1
        num_of_dogs += 1
        
    def __del__(self):
        global num_of_dogs
        
        num_of_dogs -= 1
    
    def bark(self):
        print("왈왈!")
    
    @classmethod
    def get_status(cls):
        global birth_of_dogs
        global num_of_dogs
        
        print(f"Birth: {birth_of_dogs}, Current: {num_of_dogs}")
```

클래스 변수를 활용할 줄 몰라 global을 사용하였다. 아래처럼 클래스 변수를 사용하면 됐다.

```python
class Doggy:
    birth_of_dogs = 0
    num_of_dogs = 0
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
        Doggy.birth_of_dogs += 1
        Doggy.num_of_dogs += 1
        
    def __del__(self):
        Doggy.num_of_dogs -= 1
    
    def bark(self):
        print("왈왈!")
        
    def get_status():
        print(f"Birth: {Doggy.birth_of_dogs}, Current: {Doggy.num_of_dogs}")
```

그리고 메소드 정의시 ()안에 아무것도 안적었더니 @classmethod 처럼 작동하는것을 볼 수 있었다.(?)