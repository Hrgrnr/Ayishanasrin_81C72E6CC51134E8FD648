def linearSearchProduct(productList,targetProduct):
  indices=[]

  for index, product in enumerate(productList):
    if product==targetProduct:
      indices.append(index)

  return indices



Product=["Shoes","boot","Loafer","Shoes","Sandal","Shoes"]
target="Shoes"
target2="apple"
result=linearSearchProduct(Product,target)
print(result)