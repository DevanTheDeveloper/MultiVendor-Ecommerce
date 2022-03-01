from product.models import Category, SubCategory
import regex as re 


def menu_categories(request):

	categories = Category.objects.all()

	return {'menu_categories':categories}

def vendor_categories(request):
	
	pattern = r"\/vendors\/(\d+)"
	result = re.match(pattern, request.path)

	if result:
		print(result, result.group())
		vendor = result.group(1)
		print(vendor)
		vendor_categories = SubCategory.objects.filter(vendor=vendor)
		print(vendor_categories)
		return {'vendor_categories':vendor_categories}
	else:
		return {'vendor_categories':''}
	