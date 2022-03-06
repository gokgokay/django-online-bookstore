def test_category_str(db, category_factory, check):
    category = category_factory.create()
    check.is_(category.__str__(), f"{category.name}")