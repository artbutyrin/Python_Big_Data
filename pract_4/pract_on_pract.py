def join_words(*words, sep=', '):
    result = ""
    for i, val in enumerate(words):
        if i == 0:
            result = f"{val}"
        else:
            result = f"{result}{sep}{val}"
    return result


string = join_words("a", "b", "c")

print(string)

list_name = ["Max", "Oleksandr", "Ira", "Nazar"]

list_name_filt = [name for name in list_name if "r" in name]

list_name_filt_1 = filter(lambda name: "r" in name, list_name)

list_name_sorted = sorted(list_name_filt, key=lambda x: len(x))

list_name_sorted


def my_fun(fn):
  def my_dec_fun(*args, **kwargs):
   print("hello")
   return fn(*args, **kwargs)
  return my_dec_fun

@my_fun
def add(a, b):
  return a + b

print(add(1, 2))