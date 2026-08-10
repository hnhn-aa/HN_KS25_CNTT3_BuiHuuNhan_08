raw_dishes = [
    {"name": "Phở Bò Special", "price": 120000, "status": "available"},
    {"name": " bún chả ", "price": 45000, "status": "available"},
    {"name": "Lẩu Thái Hải Sản", "price": 250000, "status": "out_of_stock"},
    {"name": "Gỏi Cuốn Tôm Thịt", "price": 60000, "status": "discontinued"},
    {"name": "Cơm Tấm Sườn Nướng", "price": 150000, "status": "available"}
]

def clean_and_validate_dishes(dishes):
    cleaned_list = []
    
    for dish in dishes:
        raw_name = dish.get("name", "")
        words = raw_name.strip().split()
        name_trimmed = " ".join(words).title()

        is_valid = True
        if len(name_trimmed) < 2:
            is_valid = False
        else:
            for char in name_trimmed:
                if not (char.isalpha() or char.isspace()):
                    is_valid = False
                    break

        if is_valid:
            dish_copy = dish.copy()
            dish_copy["name"] = name_trimmed
            cleaned_list.append(dish_copy)
            
    return cleaned_list

def search_dishes(dishes, max_price, status=None):
    result = []
    for dish in dishes:
        price_match = dish.get("price", float('inf')) <= max_price
        status_match = (status is None) or (dish.get("status") == status)
        
        if price_match and status_match:
            result.append(dish)
            
    return result

def sort_dishes_by_price_desc(dishes):
    sorted_dishes = list(dishes)
    n = len(sorted_dishes)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if sorted_dishes[j]["price"] < sorted_dishes[j + 1]["price"]:
                sorted_dishes[j], sorted_dishes[j + 1] = sorted_dishes[j + 1], sorted_dishes[j]
                swapped = True
                
        if not swapped:
            break

    return sorted_dishes

if __name__ == "__main__":
    cleaned = clean_and_validate_dishes(raw_dishes)
    print("Cleaned:", cleaned)
    print("Searched:", search_dishes(cleaned, max_price=130000, status="available"))
    print("Sorted:", sort_dishes_by_price_desc(cleaned))