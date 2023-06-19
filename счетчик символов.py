
def bencmark(func):
    import time
    def wrapper(*args, **kwargs):
        start=time.time()
        character_counter_v2("Hello, world")
        return_value=func(*args,**kwargs)
        end = time.time()
        print(f'Время выполнения {end-start}')
        return return_value
    return wrapper






def character_counter(s): #строка символов
    for sym in set(s):
        counter=0
        for sub_sym in s:
            if sub_sym==sym:
                counter+=1
        print(f'количество "{sym}"={counter}')

@bencmark

def character_counter_v2(s): #строка символов
    syns_counter={}
    for syn in s:
        syns_counter[syn]=syns_counter.get(syn,0)+1
    return syns_counter

def print_symbs(d):
    for syn,count in d.items():
        print(f'количество "{syn}"={count}')

s="8fg45u3v4jtu7bs4dr783uv2ui4tedujd48r8wi3ujr4w"
character_counter_v2('Hello,world')
print_symbs(d)