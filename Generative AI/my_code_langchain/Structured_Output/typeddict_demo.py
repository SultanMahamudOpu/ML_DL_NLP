from typing import TypedDict

class ProductReview(TypedDict):
    product_name : str
    rating : int
    review : str

new_review : ProductReview = {
    'product_name' : 'Wireless Headphones',
    # 'rating' : 5,
    'rating' : '5', # TypedDict এর সমস্যা টা দেখ, এখানে হওয়া উচিত ছিল int, কিন্তু str দিলেও কোন error দিচ্ছে না। মানে কোন strong validation নাই, যেটা pydantic এ আছে
    'review' : 'Excellent product'
}

print(new_review)
print(new_review['product_name'])