#Write a function called linear_search_product that takes the list of products and a target product name as input. The function should perform a linear search to find the target product in the list and return a list of indices of all occurrences of the product if found, or an empty list if the product is not found￼




def linear_search_product(products, target_product_name):
  product_indices = []
  for i in range(len(products)):
    product = products[i]
    if product == target_product_name:
      product_indices.append(i)
  return product_indices


products = ["Apple","Banana","Orange","Apple","MANGO","Apple","MANGO"]


target_product_name = "Apple"


product_indices = linear_search_product(products, target_product_name)


print(product_indices)

