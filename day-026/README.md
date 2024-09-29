# Goals: List & Dictionary Comprehension

리스트와 딕셔너리를 써서 작업할 때 많은 양의 코드를 중려서 쓸 수 있게 해줌

## List Comprehension

> 이전 리스트에서 새로운 리스트를 만드는 경우

```python
new_list = [new_item for item in list]

# Conditional List Comprehension
new_list = [new_item for item in list if test]
```

## Dictionary Comprehension

```python
new_dict = [new_key:new_value for item in list]

# Conditional Dictionary Comprehension
new_dict = {new_key:new_value for (key, value) in dict.items() if test}
```
