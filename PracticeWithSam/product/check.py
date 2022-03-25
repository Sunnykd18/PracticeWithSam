# from product.models import Product
#
# result = []
# for pro in Product.objects.all():
#     cat_1 = pro.categories.all().values('id')
#     if 4 in cat_1:
#         result.append(pro)
# print(result)
products = []
data = {
    "categories": "ca",
    "objects": products,
    "message": "The message"
}
print(data, "Before")
if len(data["objects"]) == 0:
    data["message"] = "NO products"
else:
    data["message"] = "Products with this cat"

print(data, "After")

