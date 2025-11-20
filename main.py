#mashqlar2_2011

# 1 - masala
def remove_duplicates(lst):
    return list(set(lst))


def get_ends(lst):
    if not lst:
        return None, None
    return lst[0], lst[-1]

def count_elements(lst):
    return len(lst)

items = [1, 2, 2, 3, 3, 4, 1]

no_duplicates = remove_duplicates(items)

sorted_items = sorted(no_duplicates)

first, last = get_ends(sorted_items)

count = count_elements(sorted_items)

print("Takrorlarsiz:", no_duplicates)
print("Tartiblangan:", sorted_items)
print("Birinchi:", first)
print("Oxirgi:", last)


# 2 - masala

def merge_lists(lst1, lst2):
    return lst1 + lst2

def sort_merged(lst):
    return sorted(lst)

def get_evens(lst):
    return [x for x in lst if x % 2 == 0]

def sum_evens(lst):
    return sum(x for x in lst if x % 2 == 0)

list1 = [1, 3, 5]
list2 = [2, 4, 6]

merged = merge_lists(list1, list2)
sorted_list = sort_merged(merged)

evens = get_evens(sorted_list)
evens_sum = sum_evens(sorted_list)
print("Birlashtirilgan ro'yxat:", merged)
print("Tartiblangan ro'yxat:", sorted_list)
print("Juft sonlar:", evens)
print("Juft sonlar yig'indisi:", evens_sum)

#3 - masala

def find_min_max(lst):
    return min(lst), max(lst)

def diff_min_max(lst):
    mn, mx = find_min_max(lst)
    return mx - mn

def index_max(lst):
    return lst.index(max(lst))

def remove_min(lst):
    lst_copy = lst.copy()
    lst_copy.remove(min(lst_copy))
    return lst_copy


values = [12, 5, 8, 19, 3, 15]


mn, mx = find_min_max(values)


difference = diff_min_max(values)


idx_max = index_max(values)


removed_min_list = remove_min(values)

print("Eng kichik:", mn)
print("Eng katta:", mx)
print("Farqi:", difference)
print("Eng katta element indeksi:", idx_max)
print("Eng kichik o'chirilgandan keyin:", removed_min_list)
